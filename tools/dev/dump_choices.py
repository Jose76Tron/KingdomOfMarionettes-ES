"""Vuelca TODAS las opciones de menu (linea que empieza por "...": )."""
import os, re
BASE = os.path.dirname(os.path.abspath(__file__))
GAME = os.path.join(BASE, "../..", "game")
RX = re.compile(r'^(\s*)"((?:\\.|[^"\\])*)"\s*(if\s+.+?)?\s*:\s*(#.*)?$')
for f in ["script.rpy", "script day2.rpy", "choice chapter 1.rpy", "day2 choice.rpy"]:
    print("=" * 25, f)
    for i, ln in enumerate(open(os.path.join(GAME, f), encoding="utf-8").read().splitlines(), 1):
        m = RX.match(ln)
        if m and "textbutton" not in ln and "_(" not in ln:
            print(f"  L{i}: {m.group(2)[:110]}")
