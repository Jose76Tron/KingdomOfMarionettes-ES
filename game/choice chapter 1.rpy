


label q_clean:
    "El jefe dijo que podía limpiarlo poco a poco. No es necesario terminar todo en un día."
    "En ese caso, empezaré limpiando el escenario."

    scene black

    "Me dirijo al almacén para recoger algunos artículos de limpieza."

    scene bg_storage with dissolve

    "Dios... Está tan oscuro aquí dentro que apenas veo nada."
    play sound "switch.mp3" volume 3.0
    "Intenté encender la luz, pero por supuesto está rota. Como era de esperar."
    "Enciendo mi linterna"
    play sound "flashlight.mp3" volume 3.0

    scene bg_storagelight

    "Mucho mejor."
    "El trastero en sí está bastante sucio. Lo limpiaré en otra ocasión."
    play sound "squeeky.mp3" volume 2.0
    "Estoy tan concentrado en reunir los suministros que me estremezco cuando mi pie pisa algo."

    show cg_bola with dissolve

    "Cuando miro hacia abajo, veo una bola roja."
    "Ah. Sólo una bola. No recuerdo haber visto una bola roja antes."
    "Debo habérmelo perdido."

    hide cg_bola with dissolve

    play sound "pickup.mp3" volume 3.0
    "Una vez reunidos todos los artículos de limpieza, vuelvo al escenario."

    scene black with dissolve
    scene bg_corridorjes with dissolve

    "...."
    "No mentiré, este corredor es bastante inquietante. No sólo este corredor tampoco. Todo este lugar se siente espeluznante y oscuro."

    play sound "flashlight.mp3" volume 3.0
    scene bg_corridorlight

    "Las puertas oxidadas están cubiertas con capas de periódicos viejos. Las paredes agrietadas están llenas de graffitis dejados por vándalos."
    "La mayoría de las luces están rotas o apagadas. Solo unas pocas siguen encendidas e incluso esas parpadean. El polvo y la suciedad se aferran a cada rincón."
    "Por supuesto, eso no es sorprendente. Este teatro de marionetas lleva cerrado mucho tiempo. Si no recuerdo mal, Kingdom of Marionettes cerró alrededor del año en que nací."
    "¿Nadie ha intentado realmente apoderarse de este lugar durante todo este tiempo? Se siente como un desperdicio dejarlo abandonado. El lugar todavía parece tan grandioso."
    "Quizás este lugar podría reutilizarse para convertirlo en un cine... o en un restaurante de alto nivel."
    "O tal vez alguien podría incluso reabrir este teatro de marionetas. Sin duda sería interesante."

    scene bg_stage with dissolve

    "Empiezo a barrer el suelo del escenario, moviéndome de un extremo al otro."
    "Sólo barrer el suelo del escenario es suficiente para agotarme. El escenario es enorme y las gruesas capas de polvo son rebeldes y difíciles de barrer."

    play sound "flashlight.mp3" volume 3.0
    scene bg_stagelight 

    "Miro a mi alrededor y luego hacia los asientos del público."

    u "....Esto va a tomar más tiempo de lo que pensaba."

    play sound "movement.mp3" volume 3.0
    scene bg_stageclean with dissolve
    pause 0.5

    "Después de limpiar el escenario durante lo que parecieron dos o tres horas, finalmente termino."

    u "Bueno... al menos el escenario en sí está terminado."
    
    "A este ritmo, probablemente necesitaré alrededor de dos días completos solo para limpiar esta área."
    "Mi cuerpo está completamente agotado después de tanto barrer, trapear, limpiar las cortinas y todo lo demás. No tengo fuerzas para continuar."
    "Probablemente sea porque rara vez hago ejercicio y vivo de fideos instantáneos. No es de extrañar que mi resistencia sea terrible. ¿Qué puedo hacer?"
    "Por ahora dejaré de limpiar."

    jump cleancheck




label q_check:

    scene bg_corridorlight with dissolve
    play sound "footstep.mp3" volume 3.0

    u "Según el jefe, en este teatro hay una veintena de títeres. Eso es bastante."

    scene bg_storageclose

    "Camino hacia la habitación donde están almacenados todos los títeres, ubicada al final del pasillo."
    "En serio. ¿A quién se le ocurrió que sería buena idea colocar la sala de los títeres al final de un pasillo tan oscuro?"
    "Debo estar tan desesperado por conseguir dinero que me siento como alguien a quien realmente le gusta entrar en una casa embrujada."
    "Agarro el pomo de la puerta y respiro profundamente antes de finalmente abrir la puerta."
    scene black with dissolve
    play sound "opendoor.mp3" volume 3.0
    pause 1.0
    scene bg_puppetroom with dissolve
    play sound "closedoor.mp3" volume 3.0

    u "... ¿Esta es la sala de marionetas? No me equivoqué, ¿verdad?"

    "Si me preguntas, parece más una prisión."
    "Esperaba ver un montón de marionetas colgadas en las paredes o algo así."
    "Pero, curiosamente, cada títere parece tener su propia habitación."

    u "Muy bien. Es hora de empezar a contar."

    "Saco un trozo de papel que contiene la lista de títeres."
    "¿A quién debo consultar primero?"

    jump knightjester


default asked_jester = False
default asked_knight = False
default asked_king = False


label knightjester:

    menu:

        "Revisar la marioneta bufón" if not asked_jester:
            $ asked_jester = True
            jump jester

        "Revisar la marioneta caballero" if not asked_knight:
            $ asked_knight = True
            jump knight

        "Revisar al Rey Marioneta" if not asked_king:
            $ asked_king = True
            jump king

        "Mira la próxima marioneta":
            jump after_check

label jester:
    u "Veamos el títere bufón."

    "Camino hacia una puerta con el nombre «Bufón» escrito y luego miro por la mirilla de la puerta."
    "La habitación del títere bufón está decorada con motivos de rayas de varios colores. Principalmente negro, rojo y amarillo."
    "Está lleno de todo tipo de accesorios de acrobacia: bolas, un monociclo y muchos otros."
    "Mientras miro más de cerca, finalmente veo al títere bufón parado en la esquina de la habitación."
    "No puedo ver su cara ya que el títere está ligeramente encorvado, pero al menos sé que está ahí."
    "Marioneta bufón: revisada."

    jump knightjester

label knight:
    "Camino hacia la puerta con la etiqueta «Caballero»."
    "La habitación del títere caballero está perfectamente mantenida."
    "Un escudo robusto e imponente está montado en la pared, junto con... varias otras decoraciones de escudo."
    "Hay bastantes escudos, todos de diferentes formas y diseños."
    "En la cama, veo un títere sentado erguido, con una capa roja oscura cubriendo su rostro."
    "Seguro que es el títere caballero. Revisado."

    jump knightjester

label king:
    "Camino hacia la puerta etiquetada «Rey»."
    "Cuando miro dentro, la habitación es lujosa."
    "Hay una cama king size con dosel, un diván de aspecto cómodo y varios cuadros."
    "Examino cada rincón de la habitación, pero no encuentro al Rey Marioneta por ninguna parte."
    "Oh no... ¿falta el Rey Marioneta?"
    "Reviso la lista de títeres que llevo, pero tampoco veo el nombre del Rey Marioneta."
    "Para empezar, supongo que nunca hubo un Rey Marioneta. ¿O… hace tiempo que está desaparecido?"

    jump knightjester


label after_check:
    "Hasta ahora sólo he revisado dos títeres. Será mejor que me dé prisa e informe los resultados al jefe."
    scene black with dissolve
    "......"
    "......."
    play sound "closedoor.mp3" volume 3.0
    scene bg_corridorlight with dissolve
    "Después de pasar unos minutos más revisando los títeres, finalmente termino. Todos los títeres enumerados están presentes."

    jump cleancheck



label outer_gate:
    play sound "click.mp3" volume 3.0
    show bzzt
    show cctv gate 
    "Compruebo la cámara en la puerta exterior. No hay nada ahí dentro."
    show bzzt
    show cctv main
    jump cctv

label corridor1:
    play sound "click.mp3" volume 3.0
    show bzzt
    show cctv corridor1
    "Compruebo la cámara del pasillo 1. No hay nada allí."
    show bzzt
    show cctv main
    jump cctv

label theater_hall:
    play sound "click.mp3" volume 3.0
    show bzzt
    show cctv theaterhall
    "Compruebo la cámara en la sala del teatro. No hay nada ahí dentro."
    show bzzt
    show cctv main
    jump cctv

label storage:
    play sound "click.mp3" volume 3.0
    show bzzt
    show cctv storage
    "Miro la cámara del trastero. No hay nada-"
    stop music
    show cctv storage2 with dissolve
    pause 0.5
    show cctv storage3 with dissolve
    pause 0.5
    show cctv storage4 with dissolve
    pause 0.5
    show cctv storage with dissolve
    pause 1.0

    "....."
    "Retiro lo que dije."
    "Alguien acaba de pasar por el almacén."
    "..... ¿Fue eso un vándalo?"
    "No. Eso no tiene sentido."

    u "¿Cómo entraron?"

    hide cctv storage with dissolve
    hide screen komputer with dissolve
    scene bg_office

    "Maldita sea. Necesito comprobarlo ahora mismo antes de que esos vándalos hagan algo que dificulte aún más mi trabajo."
    play sound "pickup.mp3" volume 3.0
    "Rápidamente tomo una linterna y un bastón para defenderme, luego salgo corriendo de la habitación hacia el área de almacenamiento."

    scene black with dissolve
    pause 1.0
    scene bg_corridoropen with dissolve

    "Cuando llego al trastero no encuentro nada."
    "Sin embargo, la puerta del almacén está abierta. Prueba de que lo que vi en las cámaras de seguridad era real y no sólo mi imaginación."
    "Tengo un mal presentimiento. Quienquiera que sea esta persona, está en algún lugar del pasillo."
    "Agarro mi bastón tan fuerte como puedo y lentamente salgo al pasillo."
    "....."
    "Está completamente oscuro... Será mejor que encienda la linterna."
    play sound "flashlight.mp3" volume 3.0

    scene bg_corridorkni

    "Muy bien-"
    "......"
    "¿Qué diablos es eso...?"
    "Después de encender la linterna, finalmente puedo ver el camino oscuro que se extiende frente a mí."
    "Pero también puedo ver algo más..."
    "Una figura alta parada al final del pasillo."
    "La figura está envuelta en una capa roja, con los bordes desgarrados y desgarrados. Su vestimenta se asemeja a la de un caballero."
    "..."
    "No... esto no es un vándalo."
    "Es el títere caballero que revisé antes..."
    "¿Cómo podría estar aquí un títere...?"
    "No hay manera. Los títeres no se mueven..."
    "Quizás algunos vándalos irrumpieron y trasladaron al caballero títere aquí. Y como se fijaron en mí, lo guardaron de nuevo para poder escapar lo más rápido posible."
    "Sí. Tiene que ser eso."
    "Antes de que pueda calmarme con todas estas posibilidades, la cabeza del títere se mueve y gira para mirarme directamente."
    "....."
    "Retiro lo que dije."

    knipuppet "... Intruso...."

    play music "horror.mp3" volume 3.0
    "Ese títere puede hablar."
    "Cálmate... cálmate... no entres en pánico..."
    "Pero ¿qué debo hacer en esta situación?"

    menu:
        "Guardar silencio":
            jump keep_silent

        "¿Quién eres?":
            jump who

        "Huir":
            jump run

label keep_silent:
    "Me quedo ahí sin moverme, sin saber qué hacer. Aunque diga algo, temo que solo empeorará las cosas."
    "Nunca imaginé una situación en la que un títere me hablaría."

    jump dicekek

label who:
    "Él no respondió nada."
    "Nunca imaginé una situación en la que un títere me hablaría."

    jump dicekek

label run:
    scene bg_corridorkni at quick_turn_left
    pause 0.1
    scene black
    "Sin pensarlo dos veces, me di la vuelta y corrí directamente hacia mi oficina."
    play sound "closedoor.mp3" volume 3.0
    camera at camera_shake
    show bg_pintu kantor
    "Una vez que llegué, cerré la puerta con llave lo más rápido que pude."
    camera at reset
    
    u "La marioneta estaba realmente viva... hablaba. ¿Estoy soñando...?"
    u "Siento que he perdido la cabeza... ¿o tal vez ya la había perdido..?"
    
    "Intenté calmarme y lentamente retrocedí. Pero manteniendo mis ojos en la puerta"
    "Me preparé para la llegada del títere a mi oficina, pero incluso después de cinco minutos, no escuché nada."
    "¿No me siguió el títere?"
    play sound "movement.mp3" volume 3.0
    show hand_cover
    stop music 
    scene black
    "Estaba a punto de sentirme aliviado cuando de repente, una mano cubrió mis ojos."
    "Todo mi cuerpo se congeló cuando sentí que alguien estaba detrás de mí."
    "¡¿Desde cuando?!"
    "No me atrevía a gritar ni a luchar. Tenía demasiado miedo."
    show cg_run with dissolve
    who "Mm... esperaba que gritaras. Pero parece que te portas bien. Mucho mejor de lo que esperaba."
    
    "Una voz suave susurró justo contra mi oído. Es aguda, extrañamente juguetona, casi infantil."

    "Luego siento que otra mano se posa lentamente sobre mi hombro, haciéndome estremecerme."

    who "Tranquilo. Ya pasó el peligro. Puedes relajarte."
    who "¿Por qué no vienes conmigo por el momento? Te aseguro que no soy alguien a quien debas temer."
    who "Después de todo, cualquier huésped que ponga un pie en este reino debe ser recibido adecuadamente. ¿No estarías de acuerdo?"

    "Muy bien... quien esté detrás de mí suena bastante amigable. Aún así, probablemente sea mejor si lo sigo."
    "Asiento con la cabeza."

    who "Excelente, ahora ven conmigo."

    jump ke_stage


    

label dicekek:
    scene bg_corridoropen
    camera at camera_shake
    show knighter_close
    play sound "movement.mp3" volume 3.0
    "De repente, en un abrir y cerrar de ojos, una mano me agarra la garganta."

    camera at reset

    u "¡¿Agh-?!"

    play sound "nyekek.mp3" volume 3.0
    camera at camera_shake

    "El caballero títere está justo frente a mí, asfixiándome con una velocidad aterradora."

    camera at reset

    knipuppet "Una vez más... un intruso..."
    knipuppet "Parece que últimamente han estado llegando más y más intrusos a este reino."
    knipuppet "Que suerte...."

    "Su agarre se aprieta alrededor de mi cuello, cortándome el aire."
    "¡Me va a matar!"
    "Lucho con todas las fuerzas que tengo. Golpeándole el brazo, pateándole las piernas, intentando desesperadamente liberarme."
    "Pero es inútil. Él es mucho más fuerte que yo. Él ni siquiera se mueve."
    show screen dark_effect with dissolve
    "Mi visión se vuelve más borrosa y se hunde más en la oscuridad."
    "¿Es así realmente como termina mi vida? ¿Asesinado por un títere viviente?"

    stop music
    play sound "jinglebell.mp3" 
    show hand_cover
    scene black
    hide screen dark_effect
    "Justo antes de que mi conciencia se desvanezca por completo, una mano de repente me cubre los ojos."

    knipuppet ".... ¿Qué estás haciendo aquí?"

    "¿Eh? ¿Quién es este detrás de mí? ¿Otra marioneta?"
    
    who "Knighter, creo que ya mencioné esto antes. ¿No sería mejor si me confiaran a mí cualquier visitante que entre en nuestro reino?"
    kni "¿Para qué? ¿Para que puedas llevar a cabo ese absurdo plan tuyo?"
    who "Amigo mío, eres libre de dudar de mí si lo deseas. No te culparía por ello. Pero necesito este visitante. Eso lo entiendes... ¿no?"

    "De repente, el pasillo queda en silencio. No tengo idea de lo que está pasando."
    "El caballero títere llamado Knighter resopla irritado antes de soltar abruptamente su agarre de mi garganta."
    "Escucho sus pasos alejarse, una clara señal de que se ha ido."
    "Sin embargo, la mano que cubre mis ojos no se mueve, manteniendo suavemente mi visión oscurecida."
    "Luego siento que otra mano se posa lentamente sobre mi hombro, haciéndome estremecerme."

    who "Tranquilo. Ya pasó el peligro. Puedes relajarte."
    who "¿Por qué no vienes conmigo por el momento? Te aseguro que no soy alguien a quien debas temer."
    who "Después de todo, cualquier huésped que ponga un pie en este reino debe ser recibido adecuadamente. ¿No estarías de acuerdo?"

    "Muy bien... quien esté detrás de mí suena bastante amigable. Aún así, probablemente sea mejor si lo sigo."
    "Asiento con la cabeza."

    who "Excelente, ahora ven conmigo."

    jump ke_stage

label ke_stage:

    scene black
    play sound "footstep.mp3" volume 3.0
    "La figura detrás de mí me guía hacia adelante, llevándome a donde quiere mientras me mantiene los ojos tapados."
    "Después de un rato, se detiene."

    who "Hemos llegado. Ahora, por favor, siéntate aquí y ponte a gusto."

    scene bg_theaterhall with dissolve

    "Me guían suavemente hasta un asiento."
    "Luego, su mano se aleja de mis ojos y finalmente me permite ver."
    "Esta es... la sala del teatro..."
    "Me doy la vuelta, tratando de ver quién me ha estado guiando todo este tiempo."
    "Pero no hay nadie allí."

    u "¿Qué? ¿A dónde fue esa persona?"
    
    play sound "jumpscare.mp3" volume 3.0
    camera at camera_shake
    show jes close creep 
    show screen dark_effect 
    

    jespuppet "¡¡BUUU!!"

    camera at reset

    u "¡¡AAARGH!!"

    "Todavía sin recuperarme y luchando por procesar lo que estaba pasando, grito cuando, sin previo aviso, noto que hay alguien justo frente a mí."
    play music "abandoned.mp3" volume 3.0

    show jes close creep2 with dissolve

    "Cubre suavemente mi boca, como indicando que no me lastimará y me mantendrá en silencio."

    show close_shdark with dissolve
    
    jespuppet "Shh..."
    
    "Puedo sentir que mi alma casi se escapa de mi cuerpo por un segundo."
    "Lentamente, retira su mano de mis labios."
    "La figura está vestida como un bufón. De las puntas de su capucha cuelgan campanas y su vestimenta es de color rojo, negro, blanco y amarillo."

    hide screen dark_effect with dissolve
    show jes close normal with dissolve
    show close_sh with dissolve

    "..."

    hide close_shdark

    "Espera un segundo... ¿No es eso...?"
    "Él es... el títere bufón."
    "...Él... se está moviendo solo."
    "Recordé la lista de deberes que leí antes de presentar la solicitud ayer."
    "Asegúrate de que no falte ningún títere... y de que no anden por ahí."
    "En ese momento, lo creí después de ver el títere caballero y el títere bufón moviéndose con mis propios ojos y mente."
    "... Esto no es una broma. Están vivos."

    jump performance




label stage:
    play sound "click.mp3" volume 3.0
    show bzzt
    show cctv stage
    "Compruebo la cámara en el escenario. No hay nada-"
    stop music
    "Espera un segundo... ¿qué diablos es eso?"
    "A través de la señal de CCTV, puedo ver una figura de pie en el centro del escenario."
    "Es difícil distinguirlo en la oscuridad, pero seguro que hay alguien allí."
    "¿Son los vándalos? ¿Cómo entraron siquiera?"

    hide cctv stage with dissolve
    hide screen komputer with dissolve
    scene bg_office
    "Maldita sea. Necesito comprobarlo ahora mismo, antes de que esos vándalos hagan algo que dificulte aún más mi trabajo."
    play sound "pickup.mp3"
    "Rápidamente tomo una linterna y un bastón para defenderme, luego salgo corriendo de la habitación hacia la sala del teatro."

    scene black

    "....."

    scene bg_theaterhall

    "Entro a la sala del teatro y miro hacia el escenario a oscuras."
    "Está demasiado oscuro para ver a nadie con claridad. Tendré que acercarme."
    
    play sound "jumpscare.mp3"
    camera at camera_shake
    show jes close creep
    show screen dark_effect 

   
    jespuppet "¡¡BUUU!!"

    camera at reset

    u "¡¡AAARGH!!"

    "Aún sin estar preparado y luchando por procesar lo que estaba sucediendo, dejé escapar el grito más fuerte que jamás haya hecho cuando, sin previo aviso, la figura ya estaba parada justo frente a mí."
    play music "abandoned.mp3" volume 3.0

    show jes close creep2 with dissolve

    "Cubre suavemente mi boca, como indicando que no me hará daño."

    show close_shdark with dissolve

    jespuppet "Shh..."

    "Puedo sentir que mi alma casi se escapa de mi cuerpo por un segundo."
    "Lentamente, retira su mano de mis labios."
    "La figura está vestida como un bufón. De las puntas de su capucha cuelgan campanas y su vestimenta es de color rojo, negro, blanco y amarillo."

    hide screen dark_effect with dissolve
    show jes close normal with dissolve
    show close_sh with dissolve

    "..."

    hide close_shdark

    "Espera un segundo... ¿no es así?"
    "Ese es... el títere bufón que revisé antes."
    "¡¿Él se está... moviendo?! ¿Se mueve él solo?"
    "¡¿Cómo puede ser posible eso?!"
    "De repente, recordé la lista de deberes que leí antes de presentar la solicitud ayer."
    "Asegúrate de que no falte ningún títere... y de que no anden por ahí."
    "En ese momento lo creí después de verlo con mis propios ojos y mente."
    "....Esto no es una broma. Están vivos."

    jump performance



label money:
    "Quizás podría darles dinero... así podrían comprar las cosas que necesitan."
    mc "¿Qué pasa si te doy algunos fondos? Te proporcionaré lo que necesites. Ya sea para comprar semillas nuevas o para cubrir tus necesidades diarias."
    nara "{color=#E0AE4B}Al escuchar la decisión de [title] de proporcionar a los agricultores toda la financiación que necesitaban, el corazón del agricultor bailó de alegría.{/color}"

    "Muy bien, esa voz del narrador, que venía de quién sabe dónde, estaba empezando a inquietarme."

    show farm happy with dissolve

    farm "¡Oh, por supuesto, Su Majestad! Suena como una buena idea. ¡Muchas gracias!"

    hide farm happy with dissolve

    nara "{color=#E0AE4B}Con el corazón alegre, el granjero finalmente salió del palacio para dar la buena noticia.{/color}"

    "El títere del granjero se levantó y abandonó el escenario."

    show jes2_normal at right_pos
    hide jes2 normal2

    "Podía sentir la mirada de Jestyn fija en mí."

    hide jes2_normal with dissolve
    show jes happy2 with dissolve
    
    jes "Oh, Su Majestad. una decisión verdaderamente sabia y bondadosa."
    jes "Proporcionar a los agricultores fondos para satisfacer sus necesidades básicas. No es una mala idea en absoluto."
    
    "Hizo una pausa."

    show jes normal2
    
    jes "Eres muy amable, majestad. Y la bondad es algo hermoso"
    jes "Pero cuando se da sin límites... se convierte en expectativa."
    
    "Inclinó la cabeza."

    show jes bow with dissolve
    
    jes "Dime, ¿cuántas monedas se necesitan para alimentar un reino?"
    mc "Mmm... eso es..."

    show jes happy2 with dissolve

    jes "Ah, perdóname."
    jes "Se me olvidaba que eres muy generoso."

    show jes normal with dissolve
    
    "Él sonrió."
    
    jes "El reino debe ser bastante pequeño... si la generosidad por sí sola es suficiente para sostenerlo."
    
    "Él tiene razón..."
    "Ser un [title] es realmente difícil..."
    "Quiero decir, sólo soy un guardia de seguridad, desesperado por dinero sólo para sobrevivir."
    "Y ahora, de repente, unos títeres vivientes me arrastran a desempeñar el papel de [title]."
    "Realmente no soy tan apto para ser un líder."

    jump problem2

label channels:
    "No sé mucho sobre agricultura, pero una vez leí que la sequía se puede controlar construyendo canales de agua."
    "Mmm... No creo que sea mala idea. Con un poco de suerte."

    mc "¿Qué tal si construimos canales de agua? De esa forma, los cultivos no se secarán."
    nara "{color=#E0AE4B}Al escuchar la decisión de [title] de construir los canales de agua, el corazón del granjero bailó de alegría.{/color}"

    "Muy bien, esa voz del narrador, que venía de quién sabe dónde, estaba empezando a inquietarme."
    
    show farm suprais with dissolve
    show jes2_normal at right_pos
    hide jes2 normal2
   
    
    "El granjero pareció pensar por un momento y luego asintió con la cabeza."
    
    farm "Por supuesto, Su Majestad. Esa es una buena idea."

    "suspiro con alivio"

    mc "Entonces proporcionaré los fondos para construir los canales lo antes posible."

    show farm happy 

    farm "Muy bien, Su Majestad. Muchas gracias."
    nara "{color=#E0AE4B}Con el corazón alegre, el granjero finalmente salió del palacio para dar la buena noticia.{/color}"

    "El títere del granjero se levantó y abandonó el escenario."

    hide farm happy with dissolve
    
    "Después de eso, el granjero se levantó y salió del escenario."
    "Podía sentir la mirada de Jestyn fija en mí."

    hide jes2_normal with dissolve
    show jes talk2 with dissolve
    
    jes "Una elección verdaderamente admirable, Su Majestad."
    jes "Canales de agua para combatir la sequía. una solución que mira hacia el futuro lejano."
    jes "Pensaste en la próxima temporada... y en la siguiente."
    
    "Hizo una pausa, sonriendo."

    show jes normal2 with dissolve
    
    jes "Quizás demasiado lejos."
    jes "Dime, Su Majestad. ¿Cuál era esta vez el problema del granjero?"

    "¿Eh?"
    "La sequía hizo que las cosechas se arruinaran, dejándolos sin ingresos para comprar nuevas semillas... y..."
    
    mc "No hay dinero para cubrir sus necesidades diarias..."

    show jes happy3 with dissolve

    jes "¡Excelente! ¡Te acordaste! ¡Cinco estrellas para la visión!" 

    show jes talk2 with dissolve

    jes "Y, sin embargo... Un granjero hambriento no puede comerse una cosecha futura."
    
    "Él se rió suavemente."

    jes "Parece que es posible que deba hacer algo más que simplemente construir canales de agua."

    show jes normal with dissolve

    "Ah... tiene razón..."
    "Ser un [title] es realmente difícil..."
    "Quiero decir, sólo soy un guardia de seguridad, desesperado por dinero sólo para sobrevivir."
    "Y ahora, de repente, me veo arrastrada a desempeñar el papel de reina por marionetas vivientes."
    "Realmente no soy tan apto para ser un líder."

    jump problem2
    
    

label seeds:
    "Las cosechas fracasaron durante la estación seca. Si no recuerdo mal, hay plantas que pueden sobrevivir en condiciones secas."
    
    mc "¿Existe algún cultivo que pueda sobrevivir a la sequía?"
    "El granjero se quedó en silencio, pensando."

    show farm suprais with dissolve
    
    farm "¡Ah! Los hay, Su Majestad. Tomates, maíz y tubérculos, por ejemplo."
    mc "Entonces, ¿qué tal si cambiamos a cultivos que puedan sobrevivir a la estación seca? Te proporcionaré las semillas que necesitas."
    nara "{color=#E0AE4B}Al escuchar la decisión de [title] de proporcionar nuevas semillas a los agricultores, el corazón del granjero bailó de alegría.{/color}"

    "Muy bien, esa voz del narrador, que venía de quién sabe dónde, estaba empezando a inquietarme."


    show farm happy 
    show jes2 normal at right_pos
    hide jes2 normal2
    
    "El granjero asintió con la cabeza."
    
    farm "Lo entiendo, Su Majestad. Gracias por su ayuda."
    nara "{color=#E0AE4B}Con el corazón alegre, el granjero finalmente salió del palacio para dar la buena noticia.{/color}"

    "El títere del granjero se levantó y abandonó el escenario."

    hide farm happy with dissolve
    
    "Después de eso, el granjero se levantó y salió del escenario."
    "Podía sentir la mirada de Jestyn fija en mí."

    hide jes2 normal
    show jes talk2

    jes "Qué sabia decisión, Su Majestad."
    jes "Elegir cultivos que puedan soportar la intensa luz solar de la estación seca, para que los agricultores ya no tengan que preocuparse de que sus cultivos mueran."
    jes "Tu forma de pensar realmente mira hacia el futuro. Realmente consideraste cómo podría ser su futuro."
    
    "Hizo una pausa."

    show jes normal2 
    
    jes "Un plan brillante para mañana... pero ¿qué comerán esta noche?"
    
    "Me congelo."
    
    jes "¿Recuerdas qué tipo de problema tenía el granjero hace un momento?"

    "¿Eh?"
    "La sequía hizo que las cosechas se arruinaran, dejándolos sin ingresos para comprar nuevas semillas... y..."
    
    mc "No hay dinero para cubrir sus necesidades diarias..."

    show jes happy3 with dissolve
    jes "¡Excelente! ¡Te acordaste! ¡Cinco estrellas para la visión!" 
    show jes normal with dissolve
    jes "Los cultivos no crecen de la noche a la mañana, Su Majestad. Confío en que seas consciente de ello."

    "Él se rió suavemente."
    "Ah... tiene razón..."
    
    jes "Parece que es posible que necesites hacer un poco más que eso." 

    "Ah... tiene razón..."
    "Ser un [title] es realmente difícil..."
    "Quiero decir, sólo soy un guardia de seguridad, desesperado por dinero sólo para sobrevivir."
    "Y ahora, de repente, me veo arrastrada a desempeñar el papel de reina por marionetas vivientes."
    "Realmente no soy tan apto para ser un líder."

    jump problem2

label time:
    "¿Qué necesita un agricultor para evitar la pérdida de cosechas durante la estación seca?"
    "¿Dinero? ¿Semillas? ¿Pero eso basta realmente para hacer frente a esto?"
    "Dios mío..."
    
    mc "Lo siento... yo... necesito más tiempo para pensar."
    nara "{color=#E0AE4B}Al escuchar las palabras del [title], el granjero trató de comprender que tales decisiones no se podían tomar apresuradamente. Aun así, su corazón seguía inquieto{/color}"

    "Muy bien, esa voz del narrador, que venía de quién sabe dónde, estaba empezando a inquietarme."

    show jes2 normal at right_pos
    hide jes2 normal2 with dissolve
    
    "El granjero asintió comprendiendo."

    show farm sad2 with dissolve
    
    farm "Muy bien, Su Majestad. Por favor, pedimos su ayuda..."

    hide farm sad2 with dissolve
    
    "Después de eso, el títere granjero abandonó el escenario."

    nara "{color=#E0AE4B}Desde la esquina de la habitación, el bufón observaba al [title] con una mirada penetrante, su habitual sonrisa aún fija en su rostro.{/color}"
    nara "{color=#E0AE4B}Parecía que el bufón quería ofrecer unas palabras al [title].{/color}"

    "Podía sentir la mirada de Jestyn fija en mí."

    hide jes2 normal with dissolve
    show jes talk2 with dissolve
    
    jes "¿Más tiempo, majestad?"
    
    "Él sonrió, divertido."

    show jes normal with dissolve
    
    jes "Qué encantador."
    jes "Muy bien, tómate todo el tiempo que necesites."
    jes "Sólo recuerda..." 
    
    "Se inclinó ligeramente."
    
    jes "La estación seca no se caracteriza por su paciencia. Tampoco la gente hambrienta"

    "Ah... tiene razón..."
    "Ser un [title] es realmente difícil..."
    "Quiero decir, sólo soy un guardia de seguridad, desesperado por dinero sólo para sobrevivir."
    "Y ahora, de repente, me veo arrastrada a desempeñar el papel de reina por marionetas vivientes."
    "Realmente no soy tan apto para ser un líder."

    jump problem2

label yourselves:
    "...."
    "Esto es estúpido."
    "No soy un [title]. Sólo soy un guardia de seguridad."
    "Quiero ir a casa."
    
    mc "Creo que puedes resolver tu problema por tu cuenta."
    mc "No entiendo la agricultura y, como agricultor, deberías saber mejor qué hacer."

    hide jes2 normal2 with dissolve
    show farm sad2 with dissolve

    farm ".....Su Majestad....te lo ruego..."
    stop music fadeout 2.0
    pause 1.0
    camera at camera_shake
    show farm close
    farm "¡¡¡TE LO ruego!!!"
    camera at reset

    play sound "nyekek.mp3"
    "El títere me agarra fuerte del hombro."
    "Realmente muy apretado"

    farm "{color=#FF2727}{cps=220}otra vez no{/cps}{/color}"
    
    play music "abandoned.mp3"
    play sound "glitch.mp3"
    camera at camera_shake
    show farm close anim
    
    farm "{color=#FF2727}{cps=220} ¡¡NO OTRA VEZ!! {/cps}{/color}"
    "¿Q-qué... es esto...?"
    "De repente, de repente, mi cabeza empezó a palpitar violentamente, como si me la estuvieran retorciendo."
    "Mi visión se volvió borrosa. Sin embargo, a través de la neblina, vi algo. algo que ni siquiera podía empezar a entender."

    show screen dark_effect with dissolve
    farm "{color=#FF2727}{cps=220}Y NO ME DEJARÁS COMO ÉL ¿NO? {/cps}{/color}"
    camera at reset
    farm "{color=#FF2727}{cps=220} ¡¡NO ME DEJES!! {/cps}{/color}"
    stop music fadeout 2.0
    camera at camera_shake
    play sound "jinglebell.mp3"
    hide screen dark_effect
    show farm close6
    jes "¡Ups~!"
    camera at reset
    hide farm close6 with dissolve

    "Jestyn lo agarró del hombro y lo alejó de mí."
    
    show farm sad2 with dissolve
    show jes2 normal2 at right_pos 
    with dissolve
    play music "jestyntheme.mp3" fadein 3.0
    jes "¿No escuchaste lo que dijo [poss] Majestad, mi querido amigo granjero?"
    jes "[poss] Majestad dijo que puedes encontrar tu propia salida. ¡Como mínimo, [poss] Majestad cree en tus habilidades!"
    jes "Que la mismísima [poss] Majestad te conceda la confianza es como si hubieras sido bendecido por el milagro del Hada Madre. Deberías sentirte honrado."
    jes "Ahora lo mejor será que regreses y pienses bien lo que debes hacer. ¿Entiendes, amigo mío?"
    farm "Yo... entiendo... por favor perdona mi insolencia, Su Majestad."

    hide jes2 normal2 with dissolve
    hide farm sad2 with dissolve
    
    nara "{color=#E0AE4B}Con el corazón apesadumbrado, el granjero finalmente abandonó el reino.{/color}"
    nara "{color=#E0AE4B}Al escuchar la decisión de [poss] Majestad anteriormente, Jestyn simplemente mostró su sonrisa habitual.{/color}"

    "Podía sentir la aguda mirada de Jestyn dirigida a mí."

    show jes2 smug with dissolve

    jes "...."

    show jes2 smug2

    jes "Pffft... {size= 15}no muy diferente, ¿eh?{/size}"
    mc "¿Eh? ¿Dijiste algo?"

    hide jes2 smug2 with dissolve
    show jes happy3 with dissolve

    jes "No, no, no. No dije nada, Su Majestad."
    jes "No te equivocas. Todo el poder está en tus manos."
    jes "Puedes hacer lo que quieras con ese poder."

    show jes normal with dissolve
    
    "Aunque Jestyn lo dijo, pude ver su sonrisa agudizarse."
    show jes creep2 with dissolve

    jes "Hmm... aunque, para ser completamente honesto, es bastante decepcionante... si me preguntaras."

    jump problem2



label teach:
    mc "Bueno, como el bufón que es bueno haciendo malabarismos, ¿por qué no me enseñas?"
    show jes suprais2 with dissolve
    "Se congela por un momento."
    
    jes "¿Enseñarte? ¿Quieres decir... enseñarte a hacer malabarismos?"
    mc "Sí. Como mínimo, quiero intentar no dejarlos caer de inmediato."
    
    "La verdad es que ya estoy exhausto. Pero siento que no puedo detenerme aquí."
    show jes happy2 with dissolve
    "La expresión de sorpresa de Jestyn se convierte lentamente en una amplia sonrisa."
    
    jes "Qué interesante, entonces muy bien."
    hide jes happy2 with dissolve
    
    "Recoge las bolas que se habían caído y me las devuelve."
    
    jes "Vamos, inténtalo."
    
    "Me preparo y empiezo a lanzar las bolas, pero la mirada de Jestyn me pone de los nervios."
    "Aun así, las lanzo al aire."
    show jes laugh with dissolve
    "Jestyn deja escapar una risa suave mientras observa mi intento."
    
    jes "Su Majestad, eso difícilmente es malabarismo si lo haces tan despacio."
    mc "¡Vamos, vamos! ¡Estoy aprendiendo aquí!"
    hide jes laugh with dissolve

    "Chasquea los dedos y de repente aparecen más bolas en su mano."
    "Él también comienza a hacer malabarismos. Aunque se siente menos como una práctica y más como un alarde."
    "Él realiza truco tras truco con facilidad, mientras yo... sigo lanzando las bolas lentamente, lo que insisto en llamar 'malabarismo'."
    "La forma en que se burla de mí es realmente irritante."
    "Cuando intento acelerar, algunas bolas casi se me escapan de las manos y otras caen al suelo."
    
    show jes happy2 with dissolve
    jes "¡Jajajaja! Vamos, acéptalo, simplemente no puedes hacerlo, majestad."

    mc "Pero te pedí que me enseñaras. No te burles de mí. No siento que me estés enseñando malabares."
    jes "Claro que sí, cielo, te enseño con la práctica."
    mc "No creo que funcione así..."
    jes "Ah, pero qué entusiasmo tan notable por aprender, cielo. Tanta dedicación merece... un regalo."
    
    "Jestyn lanza de repente una sola bola hacia mí, me asusta y hace que se me caigan todas mis bolas."
    "Mientras trato de atraparla, la bola desaparece de repente en el aire."
    
    show jes close smug with dissolve
    jes "¿Ah? Parece que tus habilidades para atrapar son igual de malas, majestad."
    jes "Permíteme. La atraparé por ti."
    
    "Su brazo se extiende y se detiene justo detrás de mi oreja."
    show jes close normal
    show jescg leftright with dissolve
    
    jes "¿Adivinas dónde está la bola?"
    

    menu:
        "Izquierda":
            jump snakebunny

        "Derecha":
            jump bunnysnake

label snakebunny:
    show jescg snakedoll with dissolve
    jes "Cuando elijo su mano izquierda, aparece una pequeña muñeca con forma de serpiente."
    jes "Una excelente elección, Su Majestad."
    jes "Un regalo de mi parte... para ti."
    hide jescg snakedoll with dissolve
    hide jes close smug with dissolve
    "Da un paso atrás."
    "¿Acaba de hacer un truco de magia?"
    
    mc "¡Ah! ¡Eso es genial! ¡¿Cómo hiciste eso?!"
    show jes happy with dissolve
    
    "Jestyn se quedó en silencio por un momento, antes de que su sonrisa regresara lentamente."
    show jes bow with dissolve
    jes "Ése es el secreto de un bufón, querida. Nunca podría decírtelo ~"

    "Jestyn dijo en broma."
    
    mc "Entonces... ¿Puedo ver más?."
    show jes suprais2 
    jes "Ah..."
    
    "¿Por qué hizo esa expresión? ¿Dije algo mal?"
    
    show jes freak with dissolve
    jes "¡Jajaja! Qué cosita tan curiosa, ¿eh?"
    
    show jes magic with dissolve 
    "Empezó a apretar la mano y luego empezó a sacar un trozo de tela de la palma."
    "Mientras tiraba, la tela se hacía más y más larga."
    show jes magic2 with dissolve
    
    mc "¡¿Cómo es eso posible?!"
    hide jes magic2 with dissolve
    "Apretó la tela con fuerza."
    "¿Qué está haciendo ahora?"
    show jescg bunnydoll with dissolve
    "Cuando la abrió de nuevo, de repente apareció en su interior un pequeño muñeco de conejo."
    
    mc"¡Ah! ¡Eso es asombroso!"
    hide jescg bunnydoll with dissolve
    show jes bow with dissolve
    jes "Y ahora, el espectáculo de magia del bufón real ha llegado a su fin. Gracias por su atención."

    jump home


label bunnysnake:
    show jescg bunnydoll with dissolve
    jes "Cuando elijo su mano derecha, aparece un pequeño conejito."
    jes "Una excelente elección, Su Majestad."
    jes "Un regalo de mi parte... para ti."
    hide jescg bunnydoll with dissolve
    hide jes close smug with dissolve
    "Da un paso atrás."
    "¿Acaba de hacer un truco de magia?"
    
    mc "¡Ah! ¡Eso es genial! ¡¿Cómo hiciste eso?!"
    show jes happy with dissolve
    
    "Jestyn se quedó en silencio por un momento, antes de que su sonrisa regresara lentamente."
    show jes bow with dissolve
    jes "Ése es el secreto de un bufón, querida. Nunca podría decírtelo ~"

    "Jestyn dijo en broma."
    
    mc "Entonces... ¿Puedo ver más?."
    show jes suprais2 
    jes "Ah..."
    
    "¿Por qué hizo esa expresión? ¿Dije algo mal?"
    
    show jes freak with dissolve
    jes "¡Jajaja! Qué cosita tan curiosa, ¿eh?"
    
    show jes magic with dissolve
    "Empezó a apretar la mano y luego empezó a sacar un trozo de tela de la palma."
    "Mientras tiraba, la tela se hacía más y más larga."
    show jes magic2 with dissolve
    mc "¡¿Cómo es eso posible?!"
    
    hide jes magic with dissolve
    "Apretó la tela con fuerza."
    "¿Qué está haciendo ahora?"
    show jescg snakedoll with dissolve
    "Cuando la abrió de nuevo, de repente apareció una pequeña muñeca serpiente en el interior."
    
    mc"¡Ah! ¡Eso es asombroso!"
    hide jescg snakedoll with dissolve
    show jes bow with dissolve
    jes "Y ahora, el espectáculo de magia del bufón real ha llegado a su fin. Gracias por su atención."

    jump home


label agree:

    show jes happy2 with dissolve
    jes "Qué decisivo, Su Majestad."
    jes "El oro tiene una manera de hacer que las decisiones difíciles parezcan... más simples."
    show jes talk with dissolve
    jes "Esperemos que el terreno resulte menos costoso de lo que parece."

    jump acting_end

label Refuse:
    show jes normal2 with dissolve
    jes "¿Ah?"
    jes "Rechazar tanta generosidad... qué admirable."
    show jes talk with dissolve
    jes "Sólo podemos esperar que nuestros vecinos compartan el aprecio de Su Majestad por los principios."

    jump acting_end

label delay:
    if first_delay:
        show jes happy with dissolve
        jes "Jeje... Su Majestad, ¿en serio?"
        jes "¿Seguramente no piensas seguir posponiendo tus decisiones cada vez que surge un problema?"
        show jes talk2 with dissolve
        jes "Ya que me enorgullezco de ser un hombre honesto, debo decir... eso es terriblemente ingenuo. Y bastante lamentable."
        jes "Quizás deberíamos revisar la redacción. En lugar de 'tomarte tu tiempo para decidir'... podríamos llamarlo como realmente es, 'huir de tus problemas'"
        jes "No importa qué tan lejos corras, no importa qué tan rápido corras... el tiempo siempre correrá a tu lado."
        show jes happy2 with dissolve
        jes "Entonces... tic tac, tic tac, Su Majestad~"
        jump acting_end


    else: 
        show jes bow with dissolve
        jes "Por supuesto, Su Majestad."
        show jes talk2 with dissolve
        jes "Después de todo, una elección que no se decide sigue siendo una elección."
        show jes talk
        jes "Sin embargo, el tiempo rara vez es tan paciente como deseamos."
        jump acting_end


label collar:
    show collar with dissolve
    mc "¿Un collar?"
    
    "En su mano aparece un collar rojo, con una campanilla dorada en el centro."
    
    jes "Eso es correcto, Su Majestad."

    hide collar with dissolve
    hide jes talk2 with dissolve
    
    "Luego se quita la corbata y se afloja el cuello de la camisa."
    "Confundido, sólo puedo permanecer sentado, sin poder moverme."
    show cg_collar with dissolve
    "Sin embargo, en el momento en que se pone el collar alrededor del cuello, empiezo a comprender lo que pretende."
    "Una vez que está abrochada, coloca suavemente la correa en mi mano."
    "Lo tomo."
    hide cg_collar with dissolve
    show jes collar talk2 with dissolve
    jes "Por favor..."
    
    
    "Su voz se vuelve pesada."

    show jes collar flush2 with dissolve
    
    jes "Estoy a tus órdenes, Su Majestad... Haz conmigo lo que quieras."

    "¡¿Cómo terminaron las cosas así?!"
    
    mc "J-Jestyn... esto..."
    show jes collar talk with dissolve
    jes "Puedes ordenarme lo que sea, Su Majestad."
    show jes collar flush
    jes "Siéntate. Túmbate. Abre la boca... Lo que me ordenes, obedeceré."
    jes "Por favor, relájate, Su Majestad. Y disfruta conmigo."
    show jes collar freak with dissolve
    jes "Yo te entretendré."
    
    "Nunca antes había hecho algo así."
    "Pero... si dice que hará cualquier cosa... entonces, supongo... bien."
    hide jes collar freak with dissolve

    menu:
        "Siéntate":
            jump sit

        "Acuéstate":
            jump lie

label sit:
    show cg_sit with dissolve
    "En el momento en que doy la orden, Jestyn se sienta obedientemente en el suelo del escenario."
    "Me mira fijamente, esperando mi próxima orden."

    hide cg_sit with dissolve
    play sound "nyekek.mp3"
    camera at camera_shake
    show cg_sit2 with dissolve
    "Tiro de su collar y provoco en él un grito de sorpresa."
    "Su sonrisa sólo se amplía."
    camera at reset
    
    jes "Su Majestad..."
    mc "Acércate."

    hide cg_sit2 with dissolve
    
    "Se arrastra hacia mí."
    play sound "jinglebell.mp3"
    show jes crawl normal with dissolve
    "No puedo creer que realmente esté haciendo esto."
    "Pero extrañamente a pesar de mí todavía siento miedo... se siente emocionante."
    "Ver el rostro que nunca he podido leer detrás de esa sonrisa constante cambiar lentamente a algo casi... adorable."

    show jes crawl talk 
    jes "Supuse que no tenía experiencia, Su Majestad..."
    show jes crawl smug 
    jes "Sin embargo, por lo que estoy presenciando ahora, te pareces a alguien que está mucho más... acostumbrado a esas cosas."
    show jes crawl mad with dissolve
    jes "Con otros..."
    
    "Por sólo un fugaz segundo, la calidez de su sonrisa flaquea."
    "Algo más oscuro se cuela, una emoción que no puedo nombrar. Agudo y repentino, antes de que lo enmascare nuevamente."
    
    mc "Por supuesto que no. Nunca antes había hecho algo así. Sólo sigo mis instintos."

    show jes crawl flush with dissolve
    
    jes "Jeje... ¿es así?"

    show jescg dielus with dissolve
    "Por impulso, levanto la mano y paso suavemente los dedos por su capucha."

    show jescg dielus2 with dissolve
    "Por un momento, se pone rígido. Un poco como si la ternura del gesto lo hubiera tomado por sorpresa."
    show jescg dielus3 with dissolve
    "Luego, lentamente, se relaja."
    show jescg dielus2_1 with dissolve
    "Jestyn cierra los ojos y se inclina hacia mi tacto, como si buscara más."
    "La sonrisa que luce ahora es diferente a la habitual. Es más suave, desprotegido, casi vulnerable."
    ".... Parece que le gusta."
    jes "...Eres una persona amable, Su Majestad."
    mc "¿Qué te hace pensar eso?"
    show jescg dielus2_2 with dissolve
    jes "Esperaba que fueras duro conmigo en esta situación."
    jes "Pero en lugar de eso, elegiste tocarme suavemente... Se siente extraño. Pero ciertamente no me quejaré de eso."

    "¿Es realmente tan extraño ser amable?"
    hide jescg dielus2_2 with dissolve
    play sound "jinglebell.mp3"
    show jes lap with dissolve
    "Me sorprendo cuando Jestyn de repente baja la cabeza hacia mi regazo."
    "....."
    "Por alguna razón, siento como si hubiera ganado una pequeña mascota extraña."
    "El miedo y la confusión que sentí antes se desvanecieron lentamente, reemplazados por algo inesperadamente calmante."

    jes "...."
    jes "Esta es la primera vez que siento algo así, Su Majestad."
    mc "¿Mmm? ¿Sentiste qué?"
    show jes lap2 with dissolve
    jes "No lo sé. Curiosamente, parece que no puedo expresarlo con palabras."
    jes "Para ser alguien a quien le encanta hablar, normalmente nunca me quedo sin palabras a la hora de expresar lo que siento... lo que pienso."
    show jes lap3 with dissolve
    jes "Pero esto... no lo sé. Se siente algo así como felicidad, tal vez. Sin embargo, ni siquiera esa palabra parece correcta."
    jes "¿Quizás Su Majestad me ha hechizado?"
    
    "Dejé escapar una pequeña risa ante su ridícula especulación."
    
    mc "No seas tonto."
    
    show jes lap4 with dissolve
    "El silencio se instala a nuestro alrededor por un rato. Pero no es incómodo."
    "A lo largo de todo, sigo acariciando la cabeza de Jestyn."
    "Esta extraña situación de alguna manera me hace sentir a gusto... mi miserable vida nunca se había sentido así."
    play sound "jinglebell.mp3"
    hide jes lap4 with dissolve
    "Después de varios minutos en la misma posición, Jestyn finalmente chasquea los dedos y en un instante, el collar que lleva alrededor del cuello desaparece."

    jump home


label lie:
    "En el momento en que doy la orden, Jestyn obedientemente se acuesta en el suelo del escenario."
    "Después de que se acuesta, empiezo a caminar hacia él."
    
    play sound "jinglebell.mp3"
    show jes lie with dissolve
    "Me mira desde abajo, esperando mi próxima orden."
    "Tiro de su collar y provoco en él un grito de sorpresa."
    "Su sonrisa sólo se amplía."
    
    jes "Su Majestad..."

    "Muy bien... Nunca he hecho algo así en mi vida. ¿Qué suele hacer la gente en situaciones como ésta?"
    "He visto a personas pisar a sus parejas antes... ¿debería intentarlo?"
    "Armado con el poco conocimiento que aprendí de Internet, coloco con cuidado mi pie sobre su pecho."
    window hide
    show jes lie3 with dissolve
    show screen sepatu with dissolve
    pause 0.5
    window show
    jes "Nnn.."
    
    "Pongo el pie allí, pero sé que se nota que aún dudo."
    "No estoy poniendo ninguna presión real sobre él."
    show jes lie4 with dissolve
    
    jes "Jeje... Su Majestad, eres muy adorable."
    mc "Mmm...?"
    jes "Estás tratando de ser rudo... pero parece que tu corazón es demasiado gentil para eso."
    
    "Tal como pensaba, se dio cuenta."
    
    jes "Es muy dulce saber que no quiere hacerme daño, Su Majestad... Pero ten por seguro que estaré bien."
    jes "Entonces, si deseas ser duro conmigo... por favor no lo dudes."
    
    "Mi corazón comienza a latir con fuerza y el sudor me humedece la espalda."
    "¿Cómo se supone que voy a saber cuándo he ido demasiado lejos... y cuándo no?"
    "Sintiendo mi miedo e incertidumbre, Jestyn decide guiarme."
    show jes lie with dissolve
    
    jes "Concentra tu fuerza en el pie y presiónalo despacio contra mi pecho."
    
    "Sigo sus instrucciones."
    "Cambio mi peso hacia mi pie y presiono suavemente el pecho de Jestyn."
    show jes lie4 with dissolve
    
    jes "...Muy bien..."
    jes "¿Ves? Todavía estoy perfectamente bien..."
    
    "Asiento."
    
    jes "Ahora intenta pisarme, Su Majestad... solo una vez."
    play sound "jinglebell.mp3"
    camera at camera_shake
    show jes lie3 with dissolve
    
    "Cuando pisoteo mi pie contra su pecho, Jestyn deja escapar un sonido suave que instantáneamente hace que mi corazón lata aún más fuerte."
    camera at reset
    "Esto... extrañamente se siente bien."
    show jes lie4 with dissolve
    jes "Ahora estás aprendiendo, Su Majestad... Intenta pisarme el pecho mientras tiras de mi collar."

    "Presiono mi pie contra su pecho nuevamente mientras tiro de su collar."
    play sound "nyekek.mp3"
    camera at camera_shake
    show jes lie5 with dissolve
    
    jes "¡Ah-!"
    camera at reset
    
    "La cara de Jestyn se pone aún más roja."
    show jes lie2 with dissolve
    
    jes "¿Cómo va tu regalo hasta ahora, Su Majestad...? ¿Estás disfrutando...?"
    
    "...."
    
    mc "S-sí... esto es lindo..."
    
    "Quizás podría intentar algo más."
    window hide
    hide screen sepatu with dissolve
    show screen tangan with dissolve
    show jes lie6 with dissolve
    pause 0.5
    window show
    "Esta vez, coloco mi mano sobre su pecho y lentamente la paso sobre él."
    show jes lie7 with dissolve
    jes "Nh... oh... ya veo..."
    jes "De ser rudo a ser gentil... ¿Me estás recompensando por complacerte, Su Majestad?"
    mc "...Puedes pensarlo de esa manera."
    hide screen tangan with dissolve
    show jescg freaky with dissolve
    "Mi mano, que estaba descansando sobre su pecho, se mueve lentamente hacia su cuello hasta el cuello que lo rodea."
    "Empiezo a acariciar su cuello lentamente."
    
    jes "Su Majestad..."

    "Eso es extraño..."
    "Cuando pasé mi mano por su cuello, la textura no era dura como la superficie de una marioneta que había imaginado."
    "Se sentía suave como la piel humana. Pero más frío."
    "¿Qué clase de títere es él, en realidad...?"

    show jescg freaky2 with dissolve
    "Después de permanecer allí por un momento, mi mano se mueve hacia su mejilla."
    "Cada sonido que hace en respuesta a mi toque se siente extrañamente satisfactorio de escuchar."
    "Sus ojos se ven nublados y su rostro enrojecido."
    "Increíble... que un títere pueda sentir algo así."
    show jescg freaky3 with dissolve
    "Mi pulgar roza suavemente sus labios."
    
    jes "...."
    jes "Su Majestad... nunca antes había sentido algo así..."
    mc "¿Te refieres a la sensación de BDSM?"
    show jescg freaky4 with dissolve
    jes "Jeje, no, no, no... Lo he sentido muchas veces antes."
    jes "Lo que quiero decir es este sentimiento... El que ni siquiera puedo expresar con palabras."
    jes "Se siente... agradable. Pero no estoy seguro de que esa palabra sea la adecuada para describir lo que siento en este momento."
    jes "Dime, Su Majestad... ¿Quizás has usado magia prohibida conmigo?"

    "Dejé escapar una risa confusa ante su ridícula especulación."
    
    mc "No seas tonto." 
    hide screen tangan with dissolve
    hide jescg freaky4 with dissolve

    "Esta extraña situación de alguna manera me hace sentir a gusto... mi miserable vida nunca se había sentido así."
    play sound "jinglebell.mp3"
    hide jes lie7 with dissolve
   
    "Después de varios minutos, Jestyn finalmente chasquea los dedos y, en un instante, el collar que lleva alrededor del cuello desaparece."

    jump home


label bad_end:
    stop music fadeout 2.0
    show jes normal2 with dissolve
    jes "Muy bien. Informaré a nuestros vecinos del testamento de Su Majestad."
    jes "Y creo que, por ahora, los asuntos que Su Majestad debía resolver han llegado al final del programa de hoy."

    "Finalmente..... termina. No sé si mi cerebro podrá soportar más estas cosas del reino."
    
    jes "Esto debe de cansar, Su Majestad. ¿Qué tal si hacemos algo... relajante?"
    show jes happy with dissolve
    jes "¿Quizás un baile?"

    play music "dansemacabre.mp3" fadein 1.0
    
    "Jestyn me ofreció la mano invitándome a bailar."
    
    mc "Pero nunca antes había bailado..."
    jes "Eso no será un problema, Su Majestad. Este baile es muy lento. No te molestará en absoluto."
    
    "Dudé por un momento. Pero al ver esa expresión en su rostro, sentí que no podía negarme."
    
    mc "Está bien.."
    play sound "spotlight.mp3"
    scene black
    
    "En el momento en que tomé su mano, las luces del escenario se apagaron de repente."
    play sound "spotlight.mp3"
    show cg dance
    "Y cuando volvieron a encenderse, sin darme cuenta, ya estaba en posición de baile con Jestyn."
    "Los pasos de Jestyn fueron tan lentos como había prometido."
    "Y seguí su ritmo."
    "No dijimos una palabra. Sólo la música de baile llenó el silencio en el escenario."
    
    jes "Lo estás haciendo bastante bien, Su Majestad."
    mc "... Sólo te estoy siguiendo."
    jes "Y eso es más que suficiente."
    
    "La habitación quedó en silencio una vez más."
    
    jes "¿Sabes el nombre de este baile, Su Majestad?"
    mc "No lo creo."
    jes "Se podría decir que este es el baile más icónico de Kingdom of Marionettes."
    jes "Al final de cada actuación, siempre bailamos ésta."
    show cg dance2 with dissolve
    jes "Lo llamamos Danza Macabra."
    
    "Nuestros pasos se sincronizaron más perfectamente después de que Jestyn dijera eso."
    
    mc "Danza Macabra..."
    mc "Nunca había oído hablar de eso antes. ¿Por qué se llama así?"
    camera at camera_shake
    "De repente, un fuerte mareo se apoderó de mi cabeza."
    "Me duele mucho la cabeza."
    "Siento como si algo dentro de mí estuviera siendo sacado lentamente."
    show cg danceblur with dissolve
    "Mis pasos vacilaron y todo mi cuerpo se debilitó en un instante."
    camera at reset
    "Pero el brazo de Jestyn me atrapó y me impidió caer."
    "Todo mi cuerpo se debilitó y tembló."
    show cg dance2 with dissolve
    stop music fadeout 5.0
    mc "J-Jestyn... ¿qué es-?"
    show cg dance3 with dissolve
    
    play music "darkambient.mp3" fadein 1.0 volume 3.0
    jes "Pasaron segundos... luego horas... días... semanas... meses... años..."
    jes"Ha pasado mucho tiempo desde que todo eso se desvaneció."
    jes "Y después de tanto tiempo...."
    show cg dance4 with dissolve
    jes "Parece que el destino aún no ha elegido de nuestro lado."
    jes "Al final, este destino nuestro sin rumbo debe continuar su camino."
    show cg dance5 with dissolve
    show screen dark_effect with dissolve
    jes "Porque, en última instancia... no eres digno."
    jes "Tu reinado como [title] termina aquí. Ahora es el momento de que descanses en paz."
    jes "Cierra los ojos... y deja que esta danza te guíe hacia la eterna serenidad."
    stop music fadeout 5.0
    scene black with dissolve
    jes "Fin."

    return

label cursed1:
    hide farm sad with dissolve
    hide jes2 normal2 with dissolve

    mc "yo-"
    
    camera at camera_shake
    "De repente, mi cabeza se siente tan dolorida"
    "Todo a mi alrededor se vuelve borroso"
    camera at reset
    
    pause 1.0
    show screen dark_effect with dissolve
    pause 1.5

    mc "{color=#FF2727}Mmmm.... que lamentable. Mis pobres agricultores...{/color}"
    mc "{color=#FF2727}Como tu [title], es natural que yo provea para ti. Nunca ignoraría tus dificultades.{/color}"
    mc "{color=#FF2727}¿Dinero? ¿Semillas más finas y de la más alta calidad? ¿Quizás comida para aliviar tus cargas?{/color}"
    show farm happy with dissolve
    farm "O-oh... Su Majestad es demasiado amable..."
    mc "{color=#FF2727}Sin embargo...{/color}"
    mc "{color=#FF2727}Si voy a derramar mi generosidad sobre ti... ¿no deberías ofrecer algo a cambio?{/color}"
    mc "{color=#FF2727}De lo contrario, sería terriblemente injusto, ¿no? ¿Yo doy y tú simplemente recibes?{/color}"
    mc "{color=#FF2727}No... si voy a bendecirte con tanta amabilidad, entonces espero que tu lealtad... y tu trabajo... reflejen tu gratitud.{/color}"
    show farm sad with dissolve
    farm "¡Tienes toda la razón, Su Majestad! ¡Me dedicaré por completo!"

    hide farm sad with dissolve
    show jes2 smug with dissolve
    
    jes "...."
    jes "Qué extraordinario, Su Majestad."
    jes "Sólo podemos esperar que tus acciones resulten tan dulces como tus palabras."
    hide jes2 smug with dissolve
    show jes normal with dissolve
    jes "...¿En efecto?"

    "{color=#FF2727}.......{/color}"
    hide screen dark_effect with dissolve
    "......"
    
    mc "S-...Sí.... De hecho."

    jump problem2


label cursed2:
    show screen dark_effect with dissolve
    mc "{color=#FF2727} ¿Oh? ¿Para el comercio, dices?{/color}"
    mc "{color=#FF2727}Es una oferta bastante interesante.{/color}"
    mc "{color=#FF2727}Muy bien. ¿Por qué no?{/color}"
    mc "{color=#FF2727}Tomo esta decisión por el bien de mi gente.{/color}"
    mc "{color=#FF2727}El comercio será mucho más conveniente para ellos. Y al mismo tiempo, podremos estrechar lazos con otro reino.{/color}"
    
    play sound "jinglebell.mp3"
    show jes bow with dissolve
    jes "Mmm...? Sí, ciertamente es una decisión comprensible, Su Majestad."
    jes "Por tus palabras, se nota que tu pueblo te importa mucho."
    show jes talk2 with dissolve
    jes "Mmm... pero ¿qué pasa con los ciudadanos que residen en la tierra que pretendes vender, Su Majestad?"
    jes "Si te desprendes de ella... ¿no significaría eso que deberán abandonar sus hogares?"
    jes "Parece bastante contradictorio con lo que acaba de decir acerca de preocuparse tanto por su pueblo."
    show jes happy with dissolve
    jes "A menos que… ¿sea usted un mentiroso, Su Majestad~?"
    mc "{color=#FF2727}Jaja... Jestyn..{/color}"
    mc "{color=#FF2727}¿Estás cuestionando mi decisión?{/color}"
    show jes creep with dissolve
    jes "......."
    show jes creep2 with dissolve
    jes "Oh, por supuesto que no, Su Majestad. Qué tonto de mi parte. Incluso pensar en cuestionar tu juicio..."
    
    jes "De hecho. Todo esto es por el bien de todo el reino."
    show jes normal with dissolve
    hide screen dark_effect with dissolve 
    jes "Muy bien entonces. Informaré a nuestros vecinos del testamento de Su Majestad."
    jes "Y creo que, por ahora, los asuntos que Su Majestad debía resolver han llegado al final del programa de hoy."
    jes "Ahora puedes descansar la cabeza, majestad~"

    show jes suprais2 with dissolve
    jes "¡Ah! Casi lo olvido, Su Majestad. Antes de eso, tengo un regalo para ti."
    hide jes suprais with dissolve
    mc "¿Eh...? ¿Qué regalo?"
    camera at reset
    stop music
    play sound "snap.mp3"
    camera at camera_shake
    "De repente, una cuerda se enrolló alrededor de mi cuerpo después de que Jestyn chasqueara los dedos."
    camera at reset
    play sound "snap.mp3"
    "Chasqueó los dedos una vez más. Un hacha apareció en su mano."
    "El pánico se apoderó de mí al instante."
    show jes_normal2_2 with dissolve
    mc "¡¿Q-Qué estás haciendo?!"
    hide jes_normal2_2 
    scene bg_stagelight2 at quick_zoom
    
    pause 0.1
    camera at camera_shake
    show cg cursed
    pause 0.5
    camera at reset
    "Sin responder a mi pregunta, Jestyn giró el hacha hacia mi cuello."

    play sound "swing.mp3"
    show cg cursed2
    pause 0.5
    camera at camera_shake
    play sound "blood.mp3"
    show cg cursed3
    pause 2.0
    scene black with dissolve
    camera at reset
    jes "Espero que tengas un bonito sueño esta vez, [player_call]"
    scene black with dissolve
    

    return







label handsome:
    "Su expresión irritada instantáneamente se convirtió en confusión y conmoción."
    
    kni "¿Qué diablos acabas de decir?"
    mc "Sólo estaba diciendo la verdad."
    
    "Honestamente, no sabía si decir eso era una buena idea."
    
    kni "Debe haber algo mal en tu cabeza. ¿Estás realmente diciendo la verdad?"
    
    "Oh, ¿logré suavizarlo un poco?"
    
    mc "Por supuesto ~. ¿Quién podría resistirse a una cara tan bonita?"
    mc "Seguro que cualquiera que te vea por primera vez se volverá completamente loco por ti al cien por cien."
    
    "Sus labios lentamente se curvaron en una sonrisa."
    
    kni "Je. En ese caso mereces morir."
    
    "Joder."

    jump jestynmuncul

label notreally:
    mc "Bueno... uh en realidad no realmente..."
    kni "En ese caso mereces morir."
    
    "Joder."

    jump jestynmuncul


label juggle:
    mc "¿Dónde aprendiste a hacer malabares?"
    jes "No esperaba que Su Majestad se interesara tanto por los malabarismos."
    jes "Mmmm... déjame pensar un momento...."
    
    "Golpea ligeramente su dedo índice mientras reflexiona."
    
    jes "Ah, sí... Maestro Adam."
    mc "Eh... ¿quién es ese?"
    jes "Él es quien me enseñó cómo desempeñar correctamente el papel de un verdadero bufón real."
    jes "La persona que soy hoy existe gracias a él. Y, naturalmente, eso incluye la forma adecuada de hacer malabarismos."
    mc "Suena como alguien importante."
    jes "De hecho, lo era. Un caballero muy amable."

    jump dinnerask

label hobby:















    






    
    
   






























