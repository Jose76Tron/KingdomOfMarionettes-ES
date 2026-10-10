import io, os, re
BASE = os.path.dirname(os.path.abspath(__file__))
GAME = os.path.join(BASE, "../..", "game")
RX = re.compile(r'^(\s*)"((?:\\.|[^"\\])*)"\s*(if\s+.+?)?\s*:\s*(#.*)?$')
for f in ["script.rpy", "script day2.rpy", "choice chapter 1.rpy", "day2 choice.rpy"]:
    for i, ln in enumerate(io.open(os.path.join(GAME, f), encoding="utf-8").read().splitlines(), 1):
        m = RX.match(ln)
        if m and "textbutton" not in ln and "_(" not in ln:
            c = m.group(2)
            first = re.sub(r"^[¿¡\.\s\"']+", "", c)[:1]
            if first and first != first.upper():
                print(f"{f}:{i}: minuscula -> {c[:100]}")
# restos de roles en ingles
for f in ["script.rpy", "script day2.rpy", "choice chapter 1.rpy", "day2 choice.rpy"]:
    for i, ln in enumerate(io.open(os.path.join(GAME, f), encoding="utf-8").read().splitlines(), 1):
        if re.search(r"rey t\xedtere", ln):
            print(f"{f}:{i}: RESTO rey titere -> {ln.strip()[:120]}")
