import io, os, re
BASE = os.path.dirname(os.path.abspath(__file__))
ORIG = os.path.join(BASE, "..", "original", "screens.rpy")
ES = os.path.join(BASE, "..", "game", "tl", "spanish", "screens.rpy")
src = io.open(ORIG, encoding="utf-8").read()
have = set(re.findall(r'^\s*old "(.*)"$', io.open(ES, encoding="utf-8").read(), re.M))
used = set()
for m in re.finditer(r'_\(\s*"((?:\\.|[^"\\])*)"', src):
    used.add(m.group(1).replace('\\"', '"'))
print("usadas:", len(used), "cubiertas:", len(have))
for s in sorted(used):
    if s not in have:
        print("FALTA:", repr(s))
