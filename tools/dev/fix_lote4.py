import io, os
BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
GAME = os.path.join(BASE, "game")
FIXES = [
    # snacks (bocadillos = sandwiches; son chuches de turno)
    ("script day2.rpy", "Necesitaba algunos bocadillos para sobrevivir mi turno.",
     "Necesitaba algo de picar para aguantar mi turno."),
    ("script day2.rpy", "Pagué mis bocadillos y me dirigí directamente al teatro.",
     "Pagué lo que había cogido para picar y me dirigí directo al teatro."),
    # "al MC" meta sin traducir -> jugador
    ("script day2.rpy", "con cuidado levantó al MC en sus brazos.",
     "con cuidado levantó a [player_call] en sus brazos."),
    ("script day2.rpy", "Sosteniendo al MC con fuerza en sus brazos, Jestyn salió silenciosamente",
     "Sosteniendo a [player_call] con fuerza en sus brazos, Jestyn salió silenciosamente"),
    # genero neutro para jugador elegible
    ("script day2.rpy", "Sorprendida, rápidamente me aparté de Jestyn.",
     "Del susto, me aparté rápidamente de Jestyn."),
    ("script day2.rpy", "solo logró hacer que mis mejillas ardieran aún más y dejarme aún más nerviosa.",
     "solo logró que me ardieran aún más las mejillas y que se me acelerara el pulso."),
    ("script day2.rpy", "Perdida en mis pensamientos, seguí avanzando sin prestar mucha atención a hacia dónde me dirigía.",
     "Con la mente en otra parte, seguí avanzando sin prestar atención a dónde iba."),
    ("script day2.rpy", "Perdido en mis pensamientos, de repente me di cuenta de que Prieston no había apartado la mirada de mí ni una sola vez.",
     "Con la mente en otra parte, de repente me di cuenta de que Prieston no había apartado la mirada de mí ni una sola vez."),
    ("script day2.rpy", "Dejándome sola en el pasillo, completamente confundida.",
     "Dejándome en el pasillo, sin entender nada."),
    ("script day2.rpy", "No estoy seguro de si me gusta Jestyn de esa manera.",
     "No sé si me gusta Jestyn de esa manera."),
    ("script day2.rpy", "Lo siento... no estoy seguro si me estoy explicando muy bien.",
     "Lo siento... no sé si me estoy explicando muy bien."),
    ("script day2.rpy", "Se está volviendo necesitado, ¿no?",
     "Se está volviendo muy dependiente, ¿no?"),
    ("script day2.rpy", "antes de eso asintió levemente en señal de comprensión.",
     "y luego asintió levemente en señal de comprensión."),
    ("script day2.rpy", "Era suave... suave... inconfundiblemente cálido.",
     "Era blando... suave... inconfundiblemente cálido."),
    ("script day2.rpy", "Se siente... reconfortante.", "Es... reconfortante."),
    ("script day2.rpy", "lanza la pelota al aire y la atrapa con facilidad.",
     "lanza la bola al aire y la atrapa con facilidad."),
    ("script day2.rpy", "deja que la pelota se le escape de los dedos y golpea el escenario",
     "deja que la bola se le escape de los dedos y golpea el escenario"),
    ("script.rpy", "Sólo una pelota. No recuerdo haber visto una bola roja",
     "Sólo una bola. No recuerdo haber visto una bola roja"),
    ("choice chapter 1.rpy", "Una vez que estoy seguro de haber reunido todos los artículos de limpieza, vuelvo al escenario.",
     "Una vez reunidos todos los artículos de limpieza, vuelvo al escenario."),
    ("choice chapter 1.rpy", "Estoy seguro de que es el títere caballero. Revisado.",
     "Seguro que es el títere caballero. Revisado."),
    ("choice chapter 1.rpy", "pero estoy seguro de que hay alguien allí.",
     "pero seguro que hay alguien allí."),
    ("choice chapter 1.rpy", "Estoy seguro de que cualquiera que te vea por primera vez se volverá completamente loco por ti al cien por cien.",
     "Seguro que cualquiera que te vea por primera vez se volverá completamente loco por ti al cien por cien."),
    ("choice chapter 1.rpy", "no estaba seguro de si decir eso era una buena idea",
     "no sabía si decir eso era una buena idea"),
    ("choice chapter 1.rpy", "¡¿Él se está... moviendo?! ¿Se muda solo?",
     "¡¿Él se está... moviendo?! ¿Se mueve él solo?"),
    ("choice chapter 1.rpy", "Luego se quita la corbata y se afloja el cuello.",
     "Luego se quita la corbata y se afloja el cuello de la camisa."),
    ("choice chapter 1.rpy", "nuevamente mientras tiro de su cuello.",
     "nuevamente mientras tiro de su collar."),
    ("day2 choice.rpy", "estoy seguro de que aún puedes lucir fuerte y genial",
     "sé que aún puedes lucir fuerte y genial"),
    ("day2 choice.rpy", "No estoy realmente seguro. Ayer, Jestyn estuvo",
     "No lo sé realmente. Ayer, Jestyn estuvo"),
    ("day2 choice.rpy", "Estoy bastante seguro de que Jestyn mencionó ese nombre ayer. Bueno, supongo que intentaré conocerlo primero.",
     "Seguro que Jestyn mencionó ese nombre ayer. Bueno, supongo que intentaré conocerlo primero."),
    ("day2 choice.rpy", "no estaba seguro de si decir eso era una buena idea",
     "no sabía si decir eso era una buena idea"),
    ("day2 choice.rpy", "Estoy seguro de que cualquiera que te vea por primera vez se volverá completamente loco por ti.",
     "Seguro que cualquiera que te vea por primera vez se volverá completamente loco por ti."),
    ("day2 choice.rpy", "¿Seguro?", "¿De verdad?"),
]
log = []
for fich, viejo, nuevo in FIXES:
    p = os.path.join(GAME, fich)
    txt = io.open(p, encoding="utf-8").read()
    n = txt.count(viejo)
    if n == 0:
        log.append("FALLO " + fich + ": " + viejo[:60])
        continue
    io.open(p, "w", encoding="utf-8").write(txt.replace(viejo, nuevo))
    log.append("OK %s: %dx %s" % (fich, n, viejo[:60]))
io.open(os.path.join(BASE, "tools", "dev", "lote4_log.txt"), "w", encoding="utf-8").write("\n".join(log))
print("\n".join(log))
