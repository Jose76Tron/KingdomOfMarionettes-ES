import io
t = io.open("game/screens.rpy", encoding="utf-8").read()
o = io.open("original/screens.rpy", encoding="utf-8").read()
print("boton ok:", 'textbutton "Espa\xf1ol" action Language("spanish")' in t)
a = o.splitlines()
b = t.splitlines()
print("lineas orig/dest:", len(a), len(b))
import difflib
d = [l for l in difflib.unified_diff(a, b, lineterm="")]
print("diff lineas:", len(d))
for l in d:
    print(l[:100])
