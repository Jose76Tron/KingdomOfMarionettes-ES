import io, os
BASE = os.path.dirname(os.path.abspath(__file__))
orig = io.open(os.path.join(BASE, "..", "original", "screens.rpy"), encoding="utf-8").read().splitlines()
ancla = '                        textbutton "Chinese" action Language("chinese")'
assert sum(1 for l in orig if l.strip() == ancla.strip()) == 1, "ancla no unica"
out = []
for ln in orig:
    out.append(ln)
    if ln.strip() == ancla.strip():
        out.append('                        textbutton "Espa\xf1ol" action Language("spanish")')
io.open(os.path.join(BASE, "..", "game", "screens.rpy"), "w", encoding="utf-8").write("\n".join(out) + "\n")
print("screens.rpy generado con boton Espa\u00f1ol")
