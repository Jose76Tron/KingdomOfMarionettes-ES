import io, os
BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
JOBS = [
    ("day2 choice.rpy", "sola en el pasillo, completamente confundida.",
     "en el pasillo, sin entender nada."),
    ("script.rpy", "lanza la pelota al aire y la atrapa con facilidad.",
     "lanza la bola al aire y la atrapa con facilidad."),
    ("script.rpy", "deja que la pelota se le escape de los dedos",
     "deja que la bola se le escape de los dedos"),
    ("choice chapter 1.rpy", "Sólo una pelota. No recuerdo haber visto una bola roja",
     "Sólo una bola. No recuerdo haber visto una bola roja"),
    ("script day2.rpy", "No estoy seguro\":", "No lo sé\":"),
]
for fich, viejo, nuevo in JOBS:
    p = os.path.join(BASE, "game", fich)
    txt = io.open(p, encoding="utf-8").read()
    n = txt.count(viejo)
    print(("OK %dx " % n if n else "FALLO ") + fich + " :: " + viejo[:50])
    if n:
        io.open(p, "w", encoding="utf-8").write(txt.replace(viejo, nuevo))
