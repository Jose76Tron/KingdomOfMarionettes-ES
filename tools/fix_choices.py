"""Corrige opciones de menu: restos en ingles + malas traducciones MT (v0.2).
Reemplazos exactos con conteo de verificacion.
"""
import os
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GAME = os.path.join(BASE, "game")

# (fichero, viejo, nuevo, replace_all)
FIXES = [
    # --- script.rpy ---
    ("script.rpy", '"darles dinero":', '"Darles dinero":', False),
    ("script.rpy", '"Agree":', '"Aceptar":', False),
    ("script.rpy", '"ríe con eso":', '"Reírse con él":', False),
    ("script.rpy", '"Refuse":', '"Rechazar":', False),
    ("script.rpy", '"Eat":', '"Comer":', False),
    ("script.rpy", '"eso es molesto":', '"Qué molesto":', False),
    ("script.rpy", '"no comas":', '"No comer":', False),
    ("script.rpy", '"Balls":', '"Las pelotas":', False),
    ("script.rpy", '"Collar" if affection >= 4:', '"El collar" if affection >= 4:', False),
    # --- script day2.rpy ---
    ("script day2.rpy", '"mira la ventana":', '"Mirar por la ventana":', False),
    ("script day2.rpy", '"no gracias":', '"No, gracias":', False),
    ("script day2.rpy", '"no estoy seguro":', '"No estoy seguro":', False),
    ("script day2.rpy", '"castigarlo":', '"Castigarlo":', False),
    ("script day2.rpy", '"Dale una palmada en la mejilla":', '"Darle una bofetada en la mejilla":', False),
    ("script day2.rpy", '"Dale una bofetada":', '"Darle una bofetada":', False),
    ("script day2.rpy", '"darle una palmada":', '"Darle un azote":', False),
    ("script day2.rpy", '"Again":', '"Otra vez":', True),
    ("script day2.rpy", '"AGAIN":', '"OTRA VEZ":', True),
    ("script day2.rpy", '"Yes":', '"Sí":', True),
    # --- choice chapter 1.rpy ---
    ("choice chapter 1.rpy", '"Marque la marioneta Jester" if not asked_jester:', '"Revisar la marioneta bufón" if not asked_jester:', False),
    ("choice chapter 1.rpy", '"guardar silencio":', '"Guardar silencio":', False),
    ("choice chapter 1.rpy", '"Left":', '"Izquierda":', False),
    ("choice chapter 1.rpy", '"Right":', '"Derecha":', False),
    ("choice chapter 1.rpy", '"Sit":', '"Siéntate":', False),
    # --- day2 choice.rpy ---
    ("day2 choice.rpy", '"Jealous":', '"Celos":', False),
    ("day2 choice.rpy", '"Nothing":', '"Nada":', False),
    ("day2 choice.rpy", '"Yes":', '"Sí":', False),
    ("day2 choice.rpy", '"rosa roja":', '"Rosa roja":', False),
    ("day2 choice.rpy", '"rosa blanca":', '"Rosa blanca":', False),
    ("day2 choice.rpy", '"rosa negra":', '"Rosa negra":', False),
    ("day2 choice.rpy", '"rosa rosa":', '"Rosa rosa":', False),
    ("day2 choice.rpy", '"rosa amarilla":', '"Rosa amarilla":', False),
    ("day2 choice.rpy", '"rosa naranja":', '"Rosa naranja":', False),
    ("day2 choice.rpy", '"rosa morada":', '"Rosa morada":', False),
    ("day2 choice.rpy", '"tengo miedo":', '"Tengo miedo":', False),
    ("day2 choice.rpy", '"No, no lo soy":', '"No, no lo tengo":', False),
    ("day2 choice.rpy", '"Golpéalo de nuevo":', '"Tocarle la mejilla otra vez":', False),
    ("day2 choice.rpy", '"Golpéalo de nuevo.":', '"Tocarle la mejilla otra vez.":', False),
    ("day2 choice.rpy", '"Mejor para":', '"Mejor parar":', False),
]

fallos = 0
for fich, viejo, nuevo, todas in FIXES:
    p = os.path.join(GAME, fich)
    txt = open(p, encoding="utf-8").read()
    n = txt.count(viejo)
    if n == 0:
        print(f"AVISO: no encontrado en {fich}: {viejo}")
        fallos += 1
        continue
    if not todas and n > 1:
        print(f"AVISO: {n}x apariciones en {fich} (se esperaba 1): {viejo}")
    txt = txt.replace(viejo, nuevo)
    open(p, "w", encoding="utf-8").write(txt)
    print(f"OK {fich}: {n}x {viejo} -> {nuevo}")
print("FALLOS:", fallos)
