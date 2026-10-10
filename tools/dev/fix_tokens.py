"""Repara tokens ZZNOMBREnZZ que el motor tradujo (NAME->NOMBRE) sin restaurar."""
import os, re
BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
GAME = os.path.join(BASE, "game")
NOMBRES = [
    "Kingdom of Marionettes", "Kingdom Of Marionettes", "Jestyn", "Jester",
    "Knighter", "Wizzy", "Prieston", "Crownus", "Butley", "Maidy", "Maidra",
    "Maidelyn", "Sweetyn", "Stubbornelle", "Stubornelle", "Seven", "Ngelus",
    "Jes", "Kni", "Wiz", "Pri",
]
pat = re.compile(r"ZZNOMBRE(\d+)ZZ", re.IGNORECASE)
n = 0
for raiz, _, fichs in os.walk(GAME):
    for f in fichs:
        if not f.endswith(".rpy"):
            continue
        p = os.path.join(raiz, f)
        txt = open(p, encoding="utf-8").read()
        def rep(m):
            global_n = int(m.group(1))
            return NOMBRES[global_n] if global_n < len(NOMBRES) else m.group(0)
        nuevo, k = pat.subn(rep, txt)
        # variantes minusculizadas por el motor
        if k:
            open(p, "w", encoding="utf-8").write(nuevo)
            n += k
            print(f"{os.path.relpath(p, GAME)}: {k} reparados")
print(f"TOTAL: {n}")
