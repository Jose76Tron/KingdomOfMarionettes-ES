import os, re, collections
BASE = os.path.dirname(os.path.abspath(__file__))
ORIG = os.path.join(BASE, "../..", "original")
GAME = os.path.join(BASE, "../..", "game")
files = ["script.rpy", "script day2.rpy", "choice chapter 1.rpy", "day2 choice.rpy"]
for f in files:
    o = open(os.path.join(ORIG, f), encoding="utf-8").read()
    g = open(os.path.join(GAME, f), encoding="utf-8").read()
    print("=" * 20, f)
    for name in ["Jestyn", "Knighter", "Wizzy", "Prieston", "Crownus", "Butley", "Maidy", "Maidra", "Maidelyn", "Sweetyn"]:
        print(f"  {name}: orig={o.count(name)} es={g.count(name)}")
    for tag in ["[player_call]", "[title]", "[poss]", "[subj]", "{color=", "{cps=", "{size="]:
        print(f"  {tag}: orig={o.count(tag)} es={g.count(tag)}")
    # posibles restos de traduccion de nombres
    for mal in ["Caballero", "Bufón", "Maguito", "Cura ", "Mayordomo"]:
        c = len(re.findall(r'"[^"]*' + mal + r'[^"]*"', g))
        if c:
            print(f"  AVISO '{mal}': {c}")
    # lineas con [title] con articulo ingles residual
    for pat in ["the [title]", "a [title]", "an [title]"]:
        c = g.count(pat)
        if c:
            print(f"  RESTO EN '{pat}': {c}")
    # comillas desbalanceadas
    bad = 0
    for i, ln in enumerate(g.splitlines(), 1):
        if ln.strip().startswith("#"):
            continue
        tmp = ln.replace('\\"', "")
        if tmp.count('"') % 2 == 1:
            bad += 1
            if bad < 5:
                print(f"  COMILLAS L{i}: {ln[:110]}")
    print(f"  lineas con comillas mal: {bad}")
