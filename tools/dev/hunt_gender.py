import io, os, re
BASE = os.path.dirname(os.path.abspath(__file__))
ORIG = os.path.join(BASE, "../..", "original")
GAME = os.path.join(BASE, "../..", "game")
FILES = ["script.rpy", "script day2.rpy", "choice chapter 1.rpy", "day2 choice.rpy"]
NAMES = ["Jestyn", "Knighter", "Wizzy", "Prieston", "Crownus", "Butley",
         "Maidy", "Maidra", "Maidelyn", "Sweetyn", "Seven", "Ngelus"]
RE_DQ = re.compile(r'"((?:\\.|[^"\\])*)"')

def strings_de(path):
    out = []
    for i, ln in enumerate(io.open(path, encoding="utf-8").read().splitlines(), 1):
        s = ln.strip()
        if not s or s.startswith("#"):
            continue
        for m in RE_DQ.finditer(ln):
            out.append((i, m.group(1)))
    return out

print("== NOMBRES EN ORIGINAL AUSENTES EN TRADUCCION (misma linea) ==")
for f in FILES:
    lo = strings_de(os.path.join(ORIG, f))
    lg = strings_de(os.path.join(GAME, f))
    for (io_, en), (ig, es) in zip(lo, lg):
        for n in NAMES:
            if re.search(r"\b" + n + r"\b", en) and not re.search(r"\b" + n + r"\b", es):
                print(f"{f}:{ig} pierde '{n}': EN={en[:130]!r} || ES={es[:130]!r}")

FEM = ["cansada", "contenta", "sola", "segura", "nerviosa", "preocupada",
       "avergonzada", "emocionada", "sorprendida", "asustada", "dormida",
       "despierta", "sentada", "acostada", "callada", "perdida", "dispuesta",
       "obligada", "acostumbrada", "harta", "orgullosa", "celosa",
       "divertida", "aburrida", "vestida", "herida", "muerta", "seguro"]
print("== CANDIDATAS FEMENINO/MASCULINO EN mc Y NARRACION ==")
for f in FILES:
    lines = io.open(os.path.join(GAME, f), encoding="utf-8").read().splitlines()
    olines = io.open(os.path.join(ORIG, f), encoding="utf-8").read().splitlines()
    for i, ln in enumerate(lines, 1):
        s = ln.strip()
        if not s or s.startswith("#"):
            continue
        es_narr = re.match(r'^"((?:\\.|[^"\\])*)"', s)
        es_mc = re.match(r'^mc "(.*)"\s*$', s)
        if not (es_narr or es_mc):
            continue
        txt = (es_narr or es_mc).group(1)
        low = txt.lower()
        hits = [w for w in FEM if re.search(r"\b" + w + r"\b", low)]
        if hits:
            en = olines[i-1].strip() if i-1 < len(olines) else "?"
            print(f"{f}:{i} [{','.join(hits)}] ES={txt[:140]!r}")
            print(f"   EN={en[:140]!r}")
