import io, os
BASE = os.path.dirname(os.path.abspath(__file__))
GAME = os.path.join(BASE, "..", "game")
FIXES = [
    ("script.rpy", "construir canales de agua", "Construir canales de agua"),
    ("script.rpy", "necesito tiempo para pensar", "Necesito tiempo para pensar"),
    ("script day2.rpy", "mira la televisión", "Mirar la televisión"),
    ("script day2.rpy", "mira el telefono", "Mirar el teléfono"),
    ("script day2.rpy", "Nada interesante para mi", "Aquí no hay nada interesante para mí"),
    ("script day2.rpy", "Lo haré. duro", "Lo haré. Duro."),
    ("script day2.rpy", "eso es suficiente", "Eso es suficiente"),
    ("script day2.rpy", "Déjalo deslizar", "Déjalo pasar"),
    ("script day2.rpy", "Dale una bofetada más fuerte", "Darle una bofetada más fuerte"),
    ("script day2.rpy", "Pégale más fuerte", "Pegarle más fuerte"),
    ("script day2.rpy", "opinas del rey títere?", "opinas del Rey Marioneta?"),
    ("script day2.rpy", "eso es todo", "Eso es todo"),
    ("script day2.rpy", "quiero saber más sobre ti", "Quiero saber más sobre ti"),
    ("script day2.rpy", "tengo sueño..", "Tengo sueño..."),
    ("day2 choice.rpy", "eso es suficiente", "Eso es suficiente"),
    ("day2 choice.rpy", "déjalo en paz", "Déjalo en paz"),
    ("day2 choice.rpy", "opinas del rey títere?", "opinas del Rey Marioneta?"),
]
log = []
for fich, viejo, nuevo in FIXES:
    p = os.path.join(GAME, fich)
    txt = io.open(p, encoding="utf-8").read()
    n = txt.count(viejo)
    if n == 0:
        log.append("FALLO " + fich + ": " + viejo[:50])
        continue
    io.open(p, "w", encoding="utf-8").write(txt.replace(viejo, nuevo))
    log.append("OK %s: %dx %s" % (fich, n, viejo[:50]))
io.open(os.path.join(BASE, "menus2_log.txt"), "w", encoding="utf-8").write("\n".join(log))
print("\n".join(log))
