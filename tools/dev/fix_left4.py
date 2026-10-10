import io, os
BASE = os.path.dirname(os.path.abspath(__file__))
GAME = os.path.join(BASE, "../..", "game")
FIXES = [
    ("day2 choice.rpy", '"eso es todo":', '"Eso es todo":'),
    ("script.rpy", "había una habitación etiquetada como 'El Rey'. Entonces el rey títere debe haber existido.",
     "había una habitación etiquetada como «El Rey». Entonces el Rey Marioneta debió de existir."),
    ("script day2.rpy", "no quiere que reemplace al rey títere...?", "no quiere que reemplace al Rey Marioneta...?"),
    ("choice chapter 1.rpy", "nunca hubo un rey títere. ¿O… hace tiempo", "nunca hubo un Rey Marioneta. ¿O… hace tiempo"),
]
for fich, viejo, nuevo in FIXES:
    p = os.path.join(GAME, fich)
    txt = io.open(p, encoding="utf-8").read()
    n = txt.count(viejo)
    print(("OK %dx " % n if n else "FALLO ") + fich + ": " + viejo[:55])
    if n:
        io.open(p, "w", encoding="utf-8").write(txt.replace(viejo, nuevo))
