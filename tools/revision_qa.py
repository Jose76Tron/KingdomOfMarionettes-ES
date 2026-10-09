"""Barrido local de calidad (sin APIs): restos de ingles, inconsistencias,
anomalias de longitud, duplicados, puntuacion y balance de tags.
Uso: python tools/revision_qa.py > revision_reporte.txt
"""
import os, re, collections

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ORIG = os.path.join(BASE, "original")
GAME = os.path.join(BASE, "game")
FILES = ["script.rpy", "script day2.rpy", "choice chapter 1.rpy", "day2 choice.rpy"]

import sys
sys.stdout = open(os.path.join(BASE, "revision_reporte.txt"), "w", encoding="utf-8")

# Palabras inglesas comunes que JAMAS deberian aparecer en texto ES
# (excluye nombres propios del glosario y terminos validos en ambos idiomas).
EN_STOP = """the and you your that this with from they them their there then than
what when where which while will would could should have has had are was were
been being his her its our out about into over after before between through
yourself herself himself itself thought though although because until against
very just only also even ever never always often still already yet not no nott
but for nor yet so such same own too very can will shall may might must
who whom whose how why because until while though although
one two three first second third much many more most other another every
here there now today tonight morning night day time way thing things
something anything nothing everything someone anyone everyone
man men woman women boy girl kid king queen knight puppet jester master
maid butler mage wizard priest lion rabbit farmer chocolate money gold door
room stage theater corridor storage window mirror phone job boss guard
looked saw seen came went come go get got make made take took put say said
tell told ask asked know knew think thought feel felt seem seemed become
like love hate want wanted need started began keep leave left help killed dead
kill stop""".split()

EN_STOP = [w for w in EN_STOP if w not in
           {"no", "si", "en", "la", "el", "con", "por", "una", "que", "se", "un",
            "fin", "mar", "pie", "red", "bar", "collar"}]  # validas en ES
EN_SET = set(EN_STOP)

RE_DQ = re.compile(r'"((?:\\.|[^"\\])*)"')
RE_WORD = re.compile(r"[A-Za-záéíóúñü]+")

def strings_de(path):
    out = []
    for i, ln in enumerate(open(path, encoding="utf-8").read().splitlines(), 1):
        s = ln.strip()
        if not s or s.startswith("#"):
            continue
        for m in RE_DQ.finditer(ln):
            out.append((i, m.group(1)))
    return out

print("### 1. RESTOS DE INGLES EN TEXTO ES ###")
for f in FILES:
    for i, es in strings_de(os.path.join(GAME, f)):
        low = es.lower()
        # quita tags y nombres
        txt = re.sub(r"\{[^{}]*\}|\[[^\[\]]*\]", " ", low)
        txt = re.sub(r"zznombre\d+zz", " ", txt)
        hall = sorted({w for w in RE_WORD.findall(txt) if w in EN_SET})
        if hall:
            print(f"{f}:{i} [{','.join(hall)}] {es[:160]}")

print("### 2. LINEAS SOSPECHOSAMENTE CORTAS/LARGAS (ratio) ###")
for f in FILES:
    lo = strings_de(os.path.join(ORIG, f))
    lg = strings_de(os.path.join(GAME, f))
    do = collections.defaultdict(list)
    for i, c in lo:
        do[c].append(i)
    for i, es in lg:
        pass
    # alinear por indice de cadena
    for (io, en), (ig, es) in zip(lo, lg):
        a, b = len(en), len(es)
        if a > 30:
            r = b / max(a, 1)
            if r < 0.45 or r > 2.6:
                print(f"{f}:{ig} ratio={r:.2f} EN={en[:110]!r} || ES={es[:110]!r}")

print("### 3. PALABRAS DUPLICADAS Y ESPACIADOS ###")
for f in FILES:
    for i, es in strings_de(os.path.join(GAME, f)):
        low = " " + es.lower() + " "
        for w in [" que que ", " de de ", " la la ", " el el ", " en en ",
                  " y y ", " no no ", " se se ", " lo lo ", " te te ",
                  " a a ", " por por ", " con con ", " su su ", " mi mi "]:
            if w in low and "no, no" not in low:
                print(f"{f}:{i} DUP{w.strip()} :: {es[:150]}")
        if " ," in es or " ." in es or "  " in es or "¿ " in es or "¡ " in es:
            print(f"{f}:{i} ESP :: {es[:150]}")
        if es.count("?") > es.count("¿") or es.count("!") > es.count("¡"):
            print(f"{f}:{i} SIGNOS :: {es[:150]}")

print("### 4. TAGS DESBALANCEADOS VS ORIGINAL ###")
for f in FILES:
    lo = strings_de(os.path.join(ORIG, f))
    lg = strings_de(os.path.join(GAME, f))
    for (io, en), (ig, es) in zip(lo, lg):
        for ch1, ch2 in [("{", "}"), ("[", "]")]:
            if en.count(ch1) != es.count(ch1) or en.count(ch2) != es.count(ch2):
                print(f"{f}:{ig} TAG EN={en[:120]!r} || ES={es[:120]!r}")

print("### 5. MISMAS EN CON DISTINTA ES (inconsistencias) ###")
todo = collections.defaultdict(set)
for f in FILES:
    lo = strings_de(os.path.join(ORIG, f))
    lg = strings_de(os.path.join(GAME, f))
    for (io, en), (ig, es) in zip(lo, lg):
        todo[en].add(es)
n = 0
for en, ess in todo.items():
    if len(ess) > 1 and len(en) > 15:
        n += 1
        if n <= 60:
            print(f"EN: {en[:130]!r}")
            for e in ess:
                print(f"   ES: {e[:130]!r}")
print(f"(total inconsistentes: {n})")
print("FIN")
