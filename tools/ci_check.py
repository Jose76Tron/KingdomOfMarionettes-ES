"""Checks de CI (autocontenidos, sin carpeta original/): interfaz ES.
Uso: python tools/ci_check.py
"""
import io, os, re, sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = os.path.join(BASE, "game", "tl", "spanish", "screens.rpy")
raw = io.open(P, encoding="utf-8", newline="").read()
olds = re.findall(r'^\s*old "(.*)"\s*$', raw, re.M)
news = re.findall(r'^\s*new "(.*)"\s*$', raw, re.M)
BS = chr(92)

fallos = []
if len(olds) != len(set(olds)):
    dup = sorted({o for o in olds if olds.count(o) > 1})
    fallos.append("old duplicados: %s" % dup)

req_old = [
    "Save", "Load", "Preferences", "Quit", "empty slot",
    "Automatic saves", "{#file_time}%A, %B %d %Y, %H:%M",
    "{#weekday}Monday", "{#month}January",
    "Prefs", "End Replay", "Main Menu", "Language", "Mute All",
    "The dialogue history is empty.",
    "Version [config.version!t]" + BS + "n",
]
falta_old = [r for r in req_old if r not in olds]
if falta_old:
    fallos.append("old que faltan: %s" % falta_old)

req_new = ["Guardar", "hueco vacío", "Idioma", "Menú principal"]
falta_new = [r for r in req_new if r not in news]
if falta_new:
    fallos.append("new que faltan: %s" % falta_new)
if not any(n.startswith("Versión") for n in news):
    fallos.append("falta new Versión")

if fallos:
    print("CI FALLA:")
    for f in fallos:
        print(" -", f)
    sys.exit(1)
print("CI OK: %d cadenas unicas, requeridas presentes" % len(olds))
