"""Revision v0.3 (lote 3): reintento de los 34 fallos con anclas minimas exactas."""
import os, io
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GAME = os.path.join(BASE, "game")
FIXES = [
    ("script.rpy", "examinando???", "examinando?"),
    ("script.rpy", "Uuuhasta este mismo d\u00eda", "Uuu... hasta este mismo d\u00eda"),
    ("script.rpy", "A un hombre que trabajaba como granjero entr\u00f3", "Un hombre que trabajaba como granjero entr\u00f3"),
    ("script.rpy", "...\u00bfpelotas?", "...\u00bfbolas?"),
    ("script day2.rpy", "tuve el descaro de golpearlo tan fuerte", "ten\u00eda el valor de golpearlo tan fuerte"),
    ("script day2.rpy", "pareces tan despistado.", "pones esa cara de no enterarte de nada."),
    ("script day2.rpy", "\u00bfEsperabas que te insultara otra vez? \u00bfTe llama una peque\u00f1a mascota humilde y fea?",
     "\u00bfEsperabas que volviera a insultarte? \u00bfQue te llamara una peque\u00f1a mascota insignificante y fea?"),
    ("script day2.rpy", "Necesitado, \u00bfeh? Realmente ten\u00edas tantas ganas de verme.", "Con ganas de verme, \u00bfeh? Realmente ten\u00edas tantas ganas."),
    ("script day2.rpy", "termina tu tarea, tonto.", "termina tu tarea, tontaina."),
    ("script day2.rpy", "no escuchar a Jestyn ladrar como sol\u00eda hacer", "no escuchar a Jestyn parlotear como sol\u00eda hacer"),
    ("script day2.rpy", 'mc "Quieres tanto mi atenci\u00f3n, \u00bfverdad? Entonces aqu\u00ed. T\u00f3malo."',
     'mc "Quieres tanto mi atenci\u00f3n, \u00bfverdad? Entonces aqu\u00ed. T\u00f3mala."'),
    ("script day2.rpy", '"Pero yo lo sab\u00eda mejor. Incluso ahora, s\u00f3lo estaba tratando de provocarme.',
     '"Pero yo ya lo conoc\u00eda. Incluso ahora, solo estaba tratando de provocarme.'),
    ("choice chapter 1.rpy", 'etiquetada \\"Rey\\"', 'etiquetada \u00abRey\u00bb'),
    ("choice chapter 1.rpy", '"Cuando revis\u00e9 los t\u00edteres antes, hab\u00eda una habitaci\u00f3n etiquetada como \'El Rey\'. Entonces el rey t\u00edtere debe haber existido."',
     '"Cuando revis\u00e9 las marionetas antes, hab\u00eda una habitaci\u00f3n etiquetada como \u00abEl Rey\u00bb. Entonces el Rey Marioneta debi\u00f3 de existir."'),
    ("choice chapter 1.rpy", "Pero tenga la seguridad de que estar\u00e1 bien", "Pero ten por seguro que estar\u00e9 bien"),
    ("day2 choice.rpy", '"Si le place a Su Majestad, \u00bftal vez podr\u00edamos compartir el t\u00e9 juntos alg\u00fan d\u00eda?"',
     '"Si es del agrado de Su Majestad, \u00bfquiz\u00e1 podr\u00edamos compartir el t\u00e9 alg\u00fan d\u00eda?"'),
]
rep = io.open(os.path.join(BASE, "revision_lote3.txt"), "w", encoding="utf-8")
fallos = 0
for fich, viejo, nuevo in FIXES:
    p = os.path.join(GAME, fich)
    txt = io.open(p, encoding="utf-8").read()
    n = txt.count(viejo)
    if n == 0:
        rep.write(f"FALLO {fich}: {viejo[:70]}\n")
        fallos += 1
        continue
    io.open(p, "w", encoding="utf-8").write(txt.replace(viejo, nuevo))
    rep.write(f"OK {fich}: {n}x {viejo[:60]}\n")
rep.write(f"Aplicados: {len(FIXES)-fallos}/{len(FIXES)}\n")
rep.close()
print("hecho, ver revision_lote3.txt")
