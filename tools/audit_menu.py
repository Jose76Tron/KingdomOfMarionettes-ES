"""Extrae todas las opciones de menu (choice strings) EN vs ES para auditoria."""
import os, re
BASE = os.path.dirname(os.path.abspath(__file__))
ORIG = os.path.join(BASE, "..", "original")
GAME = os.path.join(BASE, "..", "game")
RE_DQ = re.compile(r'"((?:\\.|[^"\\])*)"')

def choices(path):
    lines = open(path, encoding="utf-8").read().splitlines()
    out = []
    in_menu = False
    for i, ln in enumerate(lines, 1):
        s = ln.strip()
        if re.match(r"menu\s*:", s):
            in_menu = True
            continue
        if in_menu:
            if not s or s.startswith("#"):
                continue
            m = re.match(r'"((?:\\.|[^"\\])*)"\s*(if\s+.+)?\s*:', s)
            if m:
                out.append((i, m.group(1)))
                continue
            # fin del menu: linea con indentacion menor que no es opcion
            # (heuristica simple: si no empieza con " seguimos un poco)
            if re.match(r'^(label|jump|scene|show|hide|play|\$|return|if|elif|else|python|init|define|default|screen|style|translate|old|new)\b', s):
                in_menu = False
    return out

total_un = 0
for f in ["script.rpy", "script day2.rpy", "choice chapter 1.rpy", "day2 choice.rpy"]:
    co = choices(os.path.join(ORIG, f))
    cg = choices(os.path.join(GAME, f))
    print("=" * 20, f, f"orig={len(co)} es={len(cg)}")
    do = {c: i for i, c in co}
    dg = {c: i for i, c in cg}
    for i, c in co:
        if c in dg:
            continue  # sigue en ingles
        # buscar su traduccion: linea i del ES
        es_lines = open(os.path.join(GAME, f), encoding="utf-8").read().splitlines()
        es = es_lines[i - 1].strip() if i - 1 < len(es_lines) else "?"
        print(f"  L{i} EN: {c!r:90} ES: {es[:100]!r}")
        if c == c:
            pass
    print(f"  --- SIN TRADUCIR (iguales en ES):")
    for i, c in cg:
        if c in do:
            print(f"  L{i}: {c!r}")
            total_un += 1
print("TOTAL sin traducir:", total_un)
