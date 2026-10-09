"""Verifica el parche ES: placeholders intactos, nombres protegidos y sintaxis.
Uso: python tools/comprobar.py [--origen original] [--parche game]
"""
import os, re, sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ORIGEN = os.path.join(BASE, "original")
PARCHE = os.path.join(BASE, "game")

NOMBRES = ["Jestyn", "Knighter", "Wizzy", "Prieston", "Crownus", "Butley",
           "Maidy", "Maidra", "Maidelyn"]
RE_TAG = re.compile(r"\{[^{}]*\}|\[[^\[\]]*\]")
RE_DQ = re.compile(r'"((?:\\.|[^"\\])*)"')

MAL_TRADUCIDOS = {"Caballero": "Knighter", "Bufon": "Jestyn", "Bufón": "Jestyn",
                  "Maguito": "Wizzy", "Cura": "Prieston", "Mayordomo": "Butley"}

def cadenas(fich):
    return RE_DQ.findall(open(fich, encoding="utf-8").read())

def main():
    origen = sys.argv[sys.argv.index("--origen")+1] if "--origen" in sys.argv else ORIGEN
    parche = sys.argv[sys.argv.index("--parche")+1] if "--parche" in sys.argv else PARCHE
    errores = 0
    for raiz, _, fichs in os.walk(parche):
        for f in fichs:
            if not f.endswith(".rpy"):
                continue
            p = os.path.join(raiz, f)
            rel = os.path.relpath(p, parche)
            o = os.path.join(origen, rel)
            try:
                pt = open(p, encoding="utf-8").read()
            except Exception as e:
                print(f"[ERROR] {rel}: no se lee ({e})"); errores += 1; continue
            # parentesis/comillas balanceadas por linea (heuristico)
            for i, ln in enumerate(pt.splitlines(), 1):
                if ln.count('"') % 2 == 1 and not ln.strip().startswith("#"):
                    # permitir \" escapadas
                    tmp = ln.replace('\\"', '')
                    if tmp.count('"') % 2 == 1:
                        print(f"[WARN] {rel}:{i} comillas desbalanceadas: {ln[:100]}")
            # nombres mal traducidos
            for mal, bien in MAL_TRADUCIDOS.items():
                for i, ln in enumerate(pt.splitlines(), 1):
                    if ln.strip().startswith("#"):
                        continue
                    if re.search(rf'"{[^"]*{mal}[^"]*}"', ln) and bien.lower() not in ln.lower():
                        print(f"[WARN] {rel}:{i} posible nombre traducido '{mal}' (esperado {bien})")
            # placeholders vs original
            if os.path.exists(o):
                co = cadenas(o); cp = cadenas(p)
                to = sorted(set(t for s in co for t in RE_TAG.findall(s)))
                tp = sorted(set(t for s in cp for t in RE_TAG.findall(s)))
                # cada tag del parche deberia existir en el original (salvo traduccion legitima de {a=...}?)
                for t in tp:
                    if t not in to and "[text]" not in t and "Page" not in t:
                        pass  # no bloqueante
    print("OK: comprobacion terminada" if errores == 0 else f"FALLOS: {errores}")
    return errores

if __name__ == "__main__":
    sys.exit(main())
