"""Revision manual v0.3 (lote 1): correcciones del barrido sistematico.
Humano, sin APIs. Cada entrada verifica su existencia antes de aplicar.
"""
import os
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GAME = os.path.join(BASE, "game")

# (fichero, viejo, nuevo, todas_las_apariciones)
FIXES = [
    # ===== script.rpy =====
    ("script.rpy", '"¿Él... me está examinando???"', '"¿Él... me está examinando?"', False),
    ("script.rpy", 'debt "Entonces?"', 'debt "¿Entonces?"', False),
    ("script.rpy", 'mc "... pelotas?"', 'mc "...¿pelotas?"', False),
    # ===== script day2.rpy =====
    ("script day2.rpy", 'jes "¡Ay! Tartas dulces y nata! ¡Su Majestad! ¡Has olvidado algo!"',
     'jes "¡Ay! ¡Tarta dulce y crema! ¡Su Majestad! ¡Has olvidado algo!"', False),
    ("script day2.rpy", 'mc "Eh??? ¿Qué?"', 'mc "¿Eh? ¿Qué?"', False),
    ("script day2.rpy", '"¿O lo hice por- OOF-!"', '"¿O lo hice por...? ¡Ay-!"', False),
    ("script day2.rpy", '"Me di la vuelta e inmediatamente caminé de cara al pecho de Jestyn."',
     '"Me di la vuelta y me di de cara con el pecho de Jestyn."', False),
    ("script day2.rpy", '"¿Puedo presentarles a las estimadas Maid Sisters? ¡Maidelyn, Maidy y Maidra!"',
     '"¿Puedo presentarles a las estimadas hermanas doncellas? ¡Maidelyn, Maidy y Maidra!"', False),
    ("script day2.rpy", 'maidy "Maidelyn! [poss] majesty es súper linda, ¿verdad? Estás de acuerdo conmigo, ¿no?!?!"',
     'maidy "¡Maidelyn! ¡[poss] Majestad es superpreciosa, ¿verdad?! ¡Estás de acuerdo conmigo, ¿no?!"', False),
    ("script day2.rpy", 'maidelyn "De hecho. Sí."', 'maidelyn "Desde luego que sí."', False),
    ("script day2.rpy", 'maidy "¡¿Y tú, Maidra?! [poss] majesty is super-duper cute too, riiiiight?!?!?!"',
     'maidy "¡¿Y tú, Maidra?! ¡[poss] Majestad también es superpreciosa, ¿nooooo?!"', False),
    ("script day2.rpy", 'maidra "Tsk. Eres tan ruidoso. Cállate ya."',
     'maidra "Tsk. Eres tan ruidosa. Cállate ya."', False),
    ("script day2.rpy", '"{color=#FFC04C}Here.{/color}"', '"{color=#FFC04C}Aquí.{/color}"', False),
    ("script day2.rpy", '"{color=#FFC04C}Again.{/color}"', '"{color=#FFC04C}Otra vez.{/color}"', False),
    ("script day2.rpy", 'jes ".... Fecha....? ¿Acaba de decir fecha, Su Majestad...?"',
     'jes "....¿Una cita....? ¿Acaba de decir «cita», Su Majestad...?"', False),
    ("script day2.rpy", '"La carne que casi se había acabado, la mayor parte de la cual ya comí, se repone de repente."',
     '"La carne, que ya casi se había acabado porque me comí la mayor parte, se repone de repente."', False),
    ("script day2.rpy", 'mc "¿Todavía tenías más??? ¿De dónde lo conseguiste?"',
     'mc "¿Todavía tenías más? ¿De dónde lo has sacado?"', False),
    ("script day2.rpy", '"A juzgar por lo que Wizzy dijo antes... el Rey Puppet no parecía una buena persona."',
     '"A juzgar por lo que Wizzy dijo antes... el Rey Marioneta no parecía una buena persona."', False),
    ("script day2.rpy", '"...... Entonces... ¿me ha estado engañando todo este tiempo? Pero por qué...?"',
     '"......Entonces... ¿me ha estado engañando todo este tiempo? Pero ¿por qué...?"', False),
    ("script day2.rpy", '"Wizzy\'s earlier description of Prieston suddenly felt much more believable. Quienquiera que fuera este títere, mi curiosidad por él no hizo más que crecer."',
     '"La descripción que Wizzy hizo antes de Prieston de pronto me resultó mucho más creíble. Quienquiera que fuese esta marioneta, mi curiosidad por él no hacía más que crecer."', False),
    ("script day2.rpy", 'who "Butley! ¡Así que finalmente atrapaste a ese humano! ¡Jajaja!"',
     'who "¡Butley! ¡Así que finalmente atrapaste a ese humano! ¡Jajaja!"', False),
    ("script day2.rpy", '"Estoy tratando de recordar lo que dijo Butley. Por lo que había dicho Butley... él no quería que reemplazaran al Rey Puppet."',
     '"Intento recordar lo que dijo Butley. Por lo que contaba... no quería que reemplazaran al Rey Marioneta."', False),
    ("script day2.rpy", '"Y no solo Butley se sentía así... Podrían haber varios títeres como los títeres que estuvieron con él mientras me atacaba..."',
     '"Y no solo Butley se sentía así... Podría haber varias marionetas como las que estaban con él cuando me atacó..."', False),
    ("script day2.rpy", 'pri "Puedes llamarme Prieston. Soy la marioneta Priest del reino."',
     'pri "Puedes llamarme Prieston. Soy la marioneta sacerdote del reino."', False),
    ("script day2.rpy", 'pri "...Parece que te has quedado dormido, hija mía. Me alegro que esta historia haya podido adormecerte."',
     'pri "...Parece que el sueño te ha vencido, [gend] mío. Me alegro de que esta historia haya podido adormecerte."', False),
    ("script day2.rpy", '"{size=60}{b}{color=#ff0000}GRACIAS ESPECIALES A FOR{/b}{/size}{/color}\\nProbadores beta y a todos por apoyar a Kingdom Of Marionettes."',
     '"{size=60}{b}{color=#ff0000}AGRADECIMIENTO ESPECIAL{/b}{/size}{/color}\\nA los probadores beta y a todos por apoyar a Kingdom Of Marionettes."', False),
    ("script day2.rpy", "BOFETA", "ZAS", True),
    # ===== day2 choice.rpy =====
    ("day2 choice.rpy", 'jes "¡Y TA-DAA~! ¡Mirad! El arte de ponerse nervioso, realizado a la perfección por este humilde bufón~"',
     'jes "¡Y TA-CHÁN~! ¡Mira! El arte de ponerse nervioso, ejecutado a la perfección por este humilde bufón~"', False),
    ("day2 choice.rpy", 'jes "Mmm~ Sólo mírate ahora... Tu cara está tan roja como un pequeño tomate expuesto al sol de verano."',
     'jes "Mmm~ Solo mírate ahora... Tienes la cara tan roja como un tomatito al sol del verano."', False),
    ("day2 choice.rpy", 'jes "Jeje... ¡Otra actuación impecable de Este Servidor Jestyn y Jester! Me encanta una audiencia que se sonroja en el momento justo~"',
     'jes "Jeje... ¡Otra actuación impecable de este servidor, Jestyn el Bufón! Me encanta un público que se sonroja en el momento justo~"', False),
    ("day2 choice.rpy", '"Y... jaja. No es una buena idea. Entonces, por ahora, no tengo más remedio que aceptar mi papel de Maidra the Maid."',
     '"Y... jaja. No es una buena idea. Entonces, por ahora, no tengo más remedio que aceptar mi papel de Maidra la doncella."', False),
    ("day2 choice.rpy", '"Desde el momento en que la conocí, me di cuenta de que Maidra no era exactamente del tipo femenino."',
     '"Desde el momento en que la conocí, me di cuenta de que Maidra no era muy femenina."', False),
    ("day2 choice.rpy", '"Me estremecí cuando Jestyn de repente agarró mi mano y la apartó del pomo de la puerta del King Puppet."',
     '"Me estremecí cuando Jestyn de repente agarró mi mano y la apartó del pomo de la puerta del Rey Marioneta."', False),
    ("day2 choice.rpy", '"Su agarre era tan fuerte que le dolía."', '"Me agarraba con tanta fuerza que dolía."', False),
    ("day2 choice.rpy", '"El dolor recorrió mi brazo donde sus dedos estaban alrededor de él."',
     '"El dolor me recorrió el brazo allí donde sus dedos lo rodeaban."', False),
    ("day2 choice.rpy", '"Mi mirada se dirigió a la puerta naranja. La placa de identificación simplemente decía: \'Wizard\'."',
     '"Mi mirada se dirigió a la puerta naranja. La placa de identificación simplemente decía: «Mago».', False),
    ("day2 choice.rpy", '"Señalé hacia la habitación de Wizard Puppet."',
     '"Señalé hacia la habitación de la marioneta mago."', False),
    ("day2 choice.rpy", '"Jestyn me llevó hasta la puerta de Wizard Puppet."',
     '"Jestyn me llevó hasta la puerta de la marioneta mago."', False),
    ("day2 choice.rpy", 'jes "Ahora, querido Wizard... ¿no te dijo este magnífico bufón que ordenaras este espantoso desastre esta mañana?"',
     'jes "Ahora, querido mago... ¿no te dijo este magnífico bufón que ordenaras este espantoso desastre esta mañana?"', False),
    ("day2 choice.rpy", 'jes "¿Ah? Entonces, ¿cuándo, por favor, dígame, imaginaba que vendría [subj]? ¿Al año que viene? ¡CIERTAMENTE te lo dije esta mañana!"',
     'jes "¿Ah? Entonces, ¿cuándo, dime, imaginabas que vendría [subj]? ¿El año que viene? ¡Desde luego que te lo dije esta mañana!"', False),
    ("day2 choice.rpy", '"Mis ojos se posaron en la puerta que llevaba la placa Knight."',
     '"Mis ojos se posaron en la puerta con la placa «Caballero».', True),
    ("day2 choice.rpy", '"El caballero títere."', '"El títere caballero."', True),
    ("day2 choice.rpy", 'mc "Me gustaría conocer al títere Knight."',
     'mc "Me gustaría conocer al títere caballero."', False),
    ("day2 choice.rpy", 'jes "Por supuesto, Su Majestad. De esta manera ~"',
     'jes "Por supuesto, Su Majestad. Por aquí~"', False),
    ("day2 choice.rpy", '"Jestyn me lleva a la puerta de Knight Puppet."',
     '"Jestyn me lleva a la puerta del títere caballero."', False),
    ("day2 choice.rpy", 'kni "...Knighter. La marioneta Knight."',
     'kni "...Knighter. El títere caballero."', False),
    ("day2 choice.rpy", '"Que??? ¿Qué hice?"', '"¿Qué? ¿Qué hice?"', False),
    ("day2 choice.rpy", '"...caótico?"', '"...¿caótica?"', False),
    ("day2 choice.rpy", 'jes "¡Jajajaja~! Soy el títere Jester, cariño. Estos labios sólo hablan del dulce sabor de la verdad. No el sabor amargo y agrio de las mentiras y el engaño."',
     'jes "¡Jajajaja~! Soy el títere bufón, cariño. Estos labios solo hablan del dulce sabor de la verdad. No del sabor amargo y agrio de las mentiras y el engaño."', False),
    ("day2 choice.rpy", 'kni "... Crownus era .... nuestro futuro .... Él-"',
     'kni "...Crownus era... nuestro futuro... Él..."', False),
    # ===== choice chapter 1.rpy =====
    ("choice chapter 1.rpy", '"Camino hacia una puerta con el nombre \'Jester\' escrito y luego miro a través de la ranura de visualización en la puerta."',
     '"Camino hacia una puerta con el nombre «Bufón» escrito y luego miro por la mirilla de la puerta."', False),
    ("choice chapter 1.rpy", '"Control de marionetas Jester."', '"Marioneta bufón: revisada."', False),
    ("choice chapter 1.rpy", '"Camino hacia la puerta con la etiqueta \'Knight\'."',
     '"Camino hacia la puerta con la etiqueta «Caballero».', False),
    ("choice chapter 1.rpy", '"La habitación del caballero títere está perfectamente mantenida."',
     '"La habitación del títere caballero está perfectamente mantenida."', False),
    ("choice chapter 1.rpy", '"Estoy seguro de que es el títere del caballero. Comprobado."',
     '"Estoy seguro de que es el títere caballero. Revisado."', False),
    ("choice chapter 1.rpy", '"Hay una cama tamaño king con cortinas, un diván de aspecto cómodo y varios cuadros."',
     '"Hay una cama king size con dosel, un diván de aspecto cómodo y varios cuadros."', False),
    ("choice chapter 1.rpy", '"Examino cada rincón de la habitación, pero no encuentro al rey títere por ninguna parte."',
     '"Examino cada rincón de la habitación, pero no encuentro al Rey Marioneta por ninguna parte."', False),
    ("choice chapter 1.rpy", '"Oh no... ¿falta el rey títere?"', '"Oh no... ¿falta el Rey Marioneta?"', False),
    ("choice chapter 1.rpy", '"Reviso la lista de títeres que llevo, pero tampoco veo el nombre del rey títere."',
     '"Reviso la lista de títeres que llevo, pero tampoco veo el nombre del Rey Marioneta."', False),
    ("choice chapter 1.rpy", '"Pero que debo hacer en esta situación???"',
     '"Pero ¿qué debo hacer en esta situación?"', False),
    ("choice chapter 1.rpy", '"¿Eh? ¿Quién es este detrás de mí? ¿Otra marioneta???"',
     '"¿Eh? ¿Quién es este detrás de mí? ¿Otra marioneta?"', False),
    ("choice chapter 1.rpy", '"¿Dinero? Semillas?? ¿Pero es eso realmente suficiente para hacer frente a esto?"',
     '"¿Dinero? ¿Semillas? ¿Pero eso basta realmente para hacer frente a esto?"', False),
]

fallos = 0
tocados = 0
for fich, viejo, nuevo, todas in FIXES:
    p = os.path.join(GAME, fich)
    txt = open(p, encoding="utf-8").read()
    n = txt.count(viejo)
    if n == 0:
        print(f"AVISO: no encontrado en {fich}: {viejo[:80]}")
        fallos += 1
        continue
    txt = txt.replace(viejo, nuevo)
    open(p, "w", encoding="utf-8").write(txt)
    tocados += 1
print(f"Aplicados: {tocados}/{len(FIXES)}  Fallos: {fallos}")
