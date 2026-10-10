import io, os, re
BASE = os.path.dirname(os.path.abspath(__file__))
ORIG = os.path.join(BASE, "../../original")
GAME = os.path.join(BASE, "../../game")
FILES = ["script.rpy", "script day2.rpy", "choice chapter 1.rpy", "day2 choice.rpy"]
RE_DQ = re.compile(r'"((?:\\.|[^"\\])*)"')
NAMES = ["Jestyn", "Knighter", "Wizzy", "Prieston", "Crownus", "Butley",
         "Maidy", "Maidra", "Maidelyn", "Sweetyn", "Seven"]

def strings_de(path):
    out = []
    lines = io.open(path, encoding="utf-8").read().splitlines()
    for i, ln in enumerate(lines, 1):
        s = ln.strip()
        if not s or s.startswith("#"):
            continue
        is_narr = bool(re.match(r'^"((?:\\.|[^"\\])*)"', s))
        for m in RE_DQ.finditer(ln):
            out.append((i, m.group(1), is_narr, ln))
    return out

for f in FILES:
    lo = strings_de(os.path.join(ORIG, f))
    lg = strings_de(os.path.join(GAME, f))
    for (io_, en, isn, ln), (ig, es, _, _) in zip(lo, lg):
        if not isn:
            continue
        if re.match(r"^(He|She|They|His|Her|Their|Him|It)\b", en):
            es_start = re.match(r"^(\.\.\.|…|\s)*([A-ZÁÉÍÓÚÑ¿¡\[]\w*)", es)
            head = es_start.group(2) if es_start else "?"
            if head not in ("Él", "Ella", "Ellos", "Ellas", "Jestyn", "Knighter",
                            "Wizzy", "Prieston", "Crownus", "Butley", "Maidy",
                            "Maidra", "Maidelyn", "Su", "El", "La", "Los", "Las",
                            "Un", "Una", "Este", "Esta", "Ese", "Esa", "Mi", "Mis",
                            "Al", "Del", "En", "Con", "Sin", "Por", "Para", "Como",
                            "Cuando", "Mientras", "Después", "Antes", "Entonces",
                            "Pero", "Aunque", "Porque", "Pues", "Bien", "Mal",
                            "Aquí", "Allí", "Ahora", "Hoy", "Ayer", "De", "No",
                            "Sí", "Qué", "Quién", "Cuál", "Cuánto", "Dónde", "Cómo"):
                print(f"{f}:{ig} EN=[{en[:100]}]")
                print(f"   ES=[{es[:100]}]")
