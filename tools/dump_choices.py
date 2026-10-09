"""Vuelca todas las opciones de menu de los ficheros ES para revision."""
import os, re
BASE = os.path.dirname(os.path.abspath(__file__))
GAME = os.path.join(BASE, "..", "game")
for f in ["script.rpy", "script day2.rpy", "choice chapter 1.rpy", "day2 choice.rpy", "character.rpy"]:
    print("=" * 25, f)
    lines = open(os.path.join(GAME, f), encoding="utf-8").read().splitlines()
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
                print(f"  L{i}: {m.group(1)[:110]}")
                continue
            if re.match(r"^(label|jump|scene|show|hide|play|queue|voice|\$|return|if|elif|else|python|init|define|default|screen|style|translate|old|new)\b", s):
                in_menu = False
