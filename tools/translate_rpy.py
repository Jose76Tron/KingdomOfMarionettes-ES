"""Traduccion automatica EN->ES de los .rpy con glosario de nombres protegidos.
Motor: Google GTX gratuito (sin clave). Con cache para reanudar.

Uso:
  python tools/translate_rpy.py [--origen original] [--destino game] [--solo script.rpy]

Reglas:
- NO traduce nombres propios (ver NOMBRES).
- NO traduce ficheros de audio/imagen, voces, etiquetas de codigo.
- Protege {tags} y [variables] durante la traduccion.
- Traduce dialogos, narracion, menus y prompts.
"""
import os, re, sys, json, time, urllib.parse, urllib.request

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ORIGEN = os.path.join(BASE, "original")
DESTINO = os.path.join(BASE, "game")
CACHE = os.path.join(BASE, "tools", "mt_cache.json")

# Nombres y terminos que JAMAS se traducen (glosario del proyecto).
NOMBRES = [
    "Kingdom of Marionettes",
    "Kingdom Of Marionettes",
    "Jestyn", "Jester", "Knighter", "Wizzy", "Prieston",
    "Crownus", "Butley", "Maidy", "Maidra", "Maidelyn",
    "Sweetyn", "Stubbornelle", "Stubornelle", "Seven",
    "Ngelus", "Jes", "Kni", "Wiz", "Pri",
]

AUDIO_EXT = (".mp3", ".ogg", ".wav", ".opus")
IMG_EXT = (".png", ".jpg", ".jpeg", ".webp")

RE_DQ = re.compile(r'"((?:\\.|[^"\\])*)"')
RE_SQ = re.compile(r"'((?:\\.|[^'\\])*)'")
RE_TAG = re.compile(r"\{[^{}]*\}|\[[^\[\]]*\]")
RE_EXACT_SKIP = re.compile(r"^[\s\W\d]*$")

def proteger_nombres(s):
    """Sustituye nombres por ZZNAME<n>ZZ para que el motor no los toque.
    Solo palabras completas (evita romper 'Knight' con 'Kni', etc.).
    Orden: terminos largos primero para no fragmentar ('Jestyn' antes que 'Jes').
    """
    mapa = {}
    for i, n in sorted(enumerate(NOMBRES), key=lambda t: -len(t[1])):
        tok = f"ZZNAME{i}ZZ"
        s2, k = re.subn(r"\b" + re.escape(n) + r"\b", tok, s)
        if k:
            s = s2
            mapa[tok] = n
    return s, mapa

def proteger_tags(s):
    mapa = {}
    def repl(m):
        tok = f"ZZTAG{len(mapa)}ZZ"
        mapa[tok] = m.group(0)
        return tok
    return RE_TAG.sub(repl, s), mapa

def restaurar(s, mapa):
    for tok, val in mapa.items():
        s = s.replace(tok, val)
        # el motor a veces minusculiza el token o traduce NAME->NOMBRE dentro
        s = s.replace(tok.lower(), val)
        nombre_tok = tok.replace("ZZNAME", "ZZNOMBRE")
        s = s.replace(nombre_tok, val)
        s = s.replace(nombre_tok.lower(), val)
    return s

def es_traducible(contenido, linea):
    c = contenido.strip()
    if not c or len(c) < 2:
        return False
    if RE_EXACT_SKIP.match(c):
        return False
    low = c.lower()
    if low.endswith(AUDIO_EXT) or low.endswith(IMG_EXT):
        return False
    if "/" in c and " " not in c and ("." in c):
        return False  # ruta de fichero
    # voces y audio: la linea manda
    l = linea.strip()
    if l.startswith("voice ") or l.startswith("play ") or l.startswith("queue "):
        return False
    if c in NOMBRES:
        return False
    # identificadores de codigo sin espacios (bg_office, truecenter...)
    if " " not in c and re.match(r"^[A-Za-z0-9_]+$", c):
        return False
    # define/default/character estructurales de una palabra
    if l.startswith(("default ", "define gui.", "define config.", "style ", "screen ", "image ")):
        if " " not in c:
            return False
    return True

def extraer_cadenas(texto):
    """Devuelve lista ordenada de cadenas unicas traducibles del fichero."""
    cadenas = set()
    for linea in texto.splitlines():
        s = linea.strip()
        if not s or s.startswith("#"):
            continue
        if s.startswith("old "):
            continue  # plantillas de traduccion existentes
        for m in RE_DQ.finditer(linea):
            c = m.group(1)
            # desescapar \" para evaluar
            eval_c = c.replace('\\"', '"')
            if es_traducible(eval_c, linea):
                cadenas.add(c)
    return sorted(cadenas)

SEP = "\n###999###\n"

def _gtx(q_text):
    query = "client=gtx&sl=en&tl=es&dt=t&q=" + urllib.parse.quote(q_text, safe="")
    url = "https://translate.googleapis.com/translate_a/single?" + query
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=30) as r:
        data = json.load(r)
    return "".join(seg[0] for seg in data[0] if isinstance(seg, list) and seg)

def traducir_lote(items):
    """Traduce lista de strings EN->ES via Google GTX (lote con separador)."""
    import re as _re
    big = SEP.join(items)
    for intento in range(5):
        try:
            txt = _gtx(big)
            partes = _re.split(r"###\s*999\s*###", txt)
            if len(partes) != len(items):
                # el motor a veces mete saltos extra: reintentar con lote menor
                raise ValueError(f"lote partido en {len(partes)}, esperado {len(items)}")
            return [p.strip() for p in partes]
        except Exception as e:
            espera = 2 ** intento + 1
            print(f"  reintento {intento+1}/5 tras error: {e} (espera {espera}s)")
            time.sleep(espera)
    raise RuntimeError("fallo MT tras 5 intentos")

def traducir_texto(s, cache):
    if s in cache:
        return cache[s]
    s1, m_nombres = proteger_nombres(s)
    s2, m_tags = proteger_tags(s1)
    if not s2.strip():
        return s
    es = _gtx(s2)
    es = restaurar(es, m_tags)
    es = restaurar(es, m_nombres)
    cache[s] = es
    return es

def traducir_fichero(origen, destino, cache, lote=12):
    texto = open(origen, encoding="utf-8").read()
    cadenas = extraer_cadenas(texto)
    print(f"{os.path.basename(origen)}: {len(cadenas)} cadenas")
    pendientes = [c for c in cadenas if c not in cache]
    print(f"  pendientes (sin cache): {len(pendientes)}")
    # traducir en lotes con pre-proteccion
    for i in range(0, len(pendientes), lote):
        grupo = pendientes[i:i+lote]
        # pre-proteger todo el grupo
        prot = []
        mapas = []
        for c in grupo:
            a, mn = proteger_nombres(c)
            b, mt = proteger_tags(a)
            prot.append(b)
            mapas.append((mn, mt))
        es_grupo = traducir_lote(prot)
        for c, es, (mn, mt) in zip(grupo, es_grupo, mapas):
            es = restaurar(es, mt)
            es = restaurar(es, mn)
            cache[c] = es
        print(f"  {min(i+lote, len(pendientes))}/{len(pendientes)}")
        json.dump(cache, open(CACHE, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        time.sleep(0.6)
    # reconstruir fichero
    def sustituye(linea):
        if linea.strip().startswith("#") or linea.strip().startswith("old "):
            return linea
        # saltar lineas de audio/voz completas (sus strings son ficheros)
        ls = linea.strip()
        if ls.startswith(("voice ", "play ", "queue ")):
            return linea
        def rep(m):
            c = m.group(1)
            eval_c = c
            if not es_traducible(c.replace('\\"', '"'), linea):
                return m.group(0)
            if c not in cache:
                return m.group(0)
            nuevo = cache[c].replace('"', '\\"')
            return '"' + nuevo + '"'
        return RE_DQ.sub(rep, linea)
    out = "\n".join(sustituye(l) for l in texto.splitlines())
    os.makedirs(os.path.dirname(destino), exist_ok=True)
    open(destino, "w", encoding="utf-8").write(out + "\n")
    print(f"  escrito {destino}")

def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--origen", default=ORIGEN)
    ap.add_argument("--destino", default=DESTINO)
    ap.add_argument("--solo", default="")
    ap.add_argument("--lote", type=int, default=12)
    args = ap.parse_args()
    cache = {}
    if os.path.exists(CACHE):
        cache = json.load(open(CACHE, encoding="utf-8"))
    ficheros = ["script.rpy", "script day2.rpy", "choice chapter 1.rpy",
                "day2 choice.rpy", "character.rpy", "Animation.rpy",
                "screens.rpy", "options.rpy", "gui.rpy"]
    if args.solo:
        ficheros = [args.solo]
    for f in ficheros:
        o = os.path.join(args.origen, f)
        d = os.path.join(args.destino, f)
        if not os.path.exists(o):
            print(f"falta {o}, se omite")
            continue
        traducir_fichero(o, d, cache, lote=args.lote)
    json.dump(cache, open(CACHE, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"Cache: {len(cache)} entradas en {CACHE}")

if __name__ == "__main__":
    main()
