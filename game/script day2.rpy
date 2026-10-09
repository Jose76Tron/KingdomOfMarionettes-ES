default crownus_room = 0
default jestyn_location = 0
default found_jestyn = False
default crownus_secret_point = 0
default prieston_route_point = 0
default repeat_route = 0
default domjes = False
default subjes = False

label kom_day2:
    window hide
    $ quick_menu = False
    
    scene black
    with fade
    
    show text "{size=80}{cps=15}{color=#EEC594}...{/color}{/cps}{/size}" at nightmare_text
    with dissolve
    pause 2.5
    
    hide text
    
    show text "{size=90}{cps=15}{color=#EEC594}.....{/color}{/cps}{/size}" at nightmare_text
    with dissolve
    pause 2.5
    
    hide text
    
    voice "CROWNUS01_DAY2.ogg"
    show text "{size=90}{cps=15}{color=#EEC594}Despierta, despierta~....{/color}{/cps}{/size}" at nightmare_text
    with dissolve
    pause 4.5
    
    voice "CROWNUS02_DAY2.ogg"
    show text "{size=90}{cps=15}{color=#EEC594}Levántate y brilla~{/color}{/cps}{/size}" at nightmare_text
    with dissolve
    pause 4.5

    voice "CROWNUS03_DAY2.ogg"
    show text "{size=90}{cps=15}{color=#EEC594}El sol se pone y la luna sale. Es tu turno de iluminar el mundo, cariño.{/color}{/cps}{/size}" at nightmare_text
    with dissolve
    pause 7.5

    voice "CROWNUS04_DAY2.ogg"
    show text "{size=90}{cps=15}{color=#EEC594}Ahora levántate{/color}{/cps}{/size}" at nightmare_text
    with dissolve
    pause 3.5

    voice "CROWNUS05_DAY2.ogg"
    show text "{size=110}{cps=15}{color=#EEC594}Nuestro reino nos necesita, pequeña majestad.{/color}{/cps}{/size}" at nightmare_text
    with dissolve
    pause 4.5

    hide text
    with dissolve

    hide screen dark_effect
    
    $ quick_menu = True
    window show


    scene bg_apt with dissolve
    "Abrí lentamente los ojos. Lo primero que vi fue el techo encima de mi cama."
    "Uf... me siento como una mierda..."
    "¿Qué hora es ahora...?"
    "Busqué a tientas en mi colchón, tratando de descubrir dónde había dejado mi teléfono anoche."
    "Cuando finalmente lo encontré y revisé la pantalla, ya eran las 4 de la tarde."
    "Gracias a Dios no me quedé dormido. Todavía tengo tiempo suficiente para prepararme..."
    "Dejé mi teléfono sobre la cama y pasé un momento mirando fijamente al techo, reuniendo suficiente fuerza de voluntad para funcionar."
    "Finalmente, salí de mi cama ridículamente cómoda y comencé a prepararme para ir a trabajar." 
    
    hide bg_apt with dissolve

    "Después de pasar aproximadamente una hora preparándome, decidí salir un poco más temprano y pasar por la tienda de conveniencia."
    "Necesitaba algunos bocadillos para sobrevivir mi turno."
    "Originalmente, también estaba planeando comprar alimentos para el mes. La última vez que revisé, mi refrigerador estaba casi tan vacío como mi billetera."
    "Pero, curiosamente, cuando revisé después de mi ducha antes, estaba llena de comida."
    "¿Olvidé que ya tenía compras?"
    "No. Recuerdo claramente que mi refrigerador estaba prácticamente vacío. Entonces... ¿de alguna manera olvidé que ayer había ido de compras al supermercado?"
    "Ah, no lo sé. Estoy demasiado cansado para recordar."

    play music "seduction.mp3" fadein 2.0 volume 0.5
    scene bg_minimart with dissolve

    "Finalmente llegué a la tienda que frecuentaba, sobre todo porque estaba a pocos pasos de mi apartamento."
    "En ese punto, conocía el diseño mejor que probablemente algunos de los empleados."
    
    mc "Hmm... leche y un par de barras de chocolate."
    mc "Aunque un refresco suena tentador. Quizás también algunas patatas fritas."
    
    "Después de un breve debate interno, tomé mi decisión y me puse en la fila de la caja registradora."
    "La tienda estaba más ocupada de lo habitual hoy. Por otra parte, eso no era exactamente infrecuente."
    "Sin nada más que hacer mientras esperaba, miré casualmente alrededor de la tienda."

label minimarket_day2:
    menu:
        "mira la ventana":
            jump lookwindow_day2

        "mira la televisión":
            jump tv_day2

        "mira el telefono":
            jump phone_day2

        "Nada interesante para mi":
            jump tothetheater_day2


label tothetheater_day2:

    "Después de esperar un rato, finalmente llegó mi turno de pagar." 
    "Pagué mis bocadillos y me dirigí directamente al teatro." 
    "El teatro no estaba exactamente lejos de mi departamento, pero tampoco cerca." 

    hide bg_minimart with dissolve

    "Entonces, como de costumbre, tomé el transporte público." 
    "...Aquí estoy. De vuelta otra vez."
    "Todavía no sé si lo que vi ayer fue un sueño o no."
    "Me cuesta creer que los títeres de este teatro estén vivos."
    "Bueno, al menos ese títere bufón lo es. Jestyn. Es el único que vi moverse ayer."
    "Honestamente, es un milagro que todavía esté cuerdo."
    "O tal vez no lo soy."
    "De cualquier manera, lo que pasó ayer parecía demasiado real. En este punto, siento más bien que soy yo quien lo niega."
    "Bueno, al menos a mí me pagan."
    "¿Qué no vale la pena aguantar en esta economía, verdad?"
    "Muy bien entonces. Hora de empezar el día."
    "Esperemos que hoy sea al menos un poco menos loco que ayer."
    stop music fadeout 2.0
    "Con una sensación nerviosa retorciéndose en mi estómago, lentamente abrí las enormes puertas de entrada del teatro. Se parecían menos a las puertas de un teatro y más a las puertas de un castillo real." 
    
    scene bg_theaterhall with dissolve
    "Entré."

    camera at camera_shake
    play sound "trumpet.mp3" volume 3.0
    mc "AAAAAAHHHHHHHHHHH!!!"
    camera at reset
    mc "¡¿QUÉ?!"

    play sound "spotlight.mp3" volume 3.0
    scene bg_theaterhall_light 
    show jes_on_stage with dissolve

    jes "Pasaron segundos... luego horas... días... semanas... meses... años... Ha pasado mucho tiempo desde que todo eso se desvaneció."
    jes "Iban y venían, uno tras otro... pero el frío de la noche nunca flaqueó."
    jes "Justo cuando creíamos que el último rayo de luz había sido tragado por la despiadada oscuridad... apareció una pequeña chispa."
    
    hide jes_on_stage with dissolve

    "Con cada paso tan elegante como el de un bailarín, Jestyn se acercó y continuó su relato como si estuviera narrando un cuento de hadas."

    play sound "jinglebell.mp3" volume 3.0
    show jes close normal with dissolve 
    
    jes "Perdido en medio de las sombras, vagando sin propósito... y aún así... oh, qué brillante y adorable era."
    jes "Con la expresión de un tonto desconcertado, miró fijamente al bufón más hermoso, encantador y absolutamente maravilloso de todo el reino."
    mc ".........."
    mc "¿Terminaste, Jestyn?"

    play music "seduction.mp3" fadein 2.0 volume 0.6
    show jes close smug with dissolve
    jes "Hermosa, magnífica, sexy, irresistible, impresionante-"
    mc "En serio, no puedes dejar de hablar de ti ni un segundo, ¿verdad?"

    show jes close flush with dissolve 

    "Un leve sonrojo se extendió por las mejillas de Jestyn mientras se reía y se mordía ligeramente la punta de su dedo."
    
    jes "Entonces sé tú quien me silencie."

    menu:
        "no gracias":
            jump nothx_day2

        "Brat":
            jump brat_day2

        "Lo haré. duro":
            jump dohard_day2


label timetowork_day2:
    "Dio un paso atrás, dándome algo de espacio."

    $ voice_duck_start()
    play sound "jinglebell.mp3" volume 3.0
    show jes flush with dissolve
    voice "JESTYN01_DAY2.ogg"
    jes "¡Ah! Mis más sinceras disculpas por mi mala educación, Su Majestad."

    voice "JESTYN01_2_DAY2.ogg"
    jes "Simplemente estaba... muy, muy, muy, muy, muuuy feliz de verte de nuevo."
    mc "Pero sólo dejamos de hablar durante unas horas..."
    $ voice_duck_end()

    show jes nosmile2_2 with dissolve 
    jes "¡Ese es precisamente el problema!"
    jes"¡Unas pocas horas son una eternidad cuando uno se ve privado de la compañía de Su Majestad!"
    jes "¡Estuve así de cerca de marchar directamente a tu casa sólo para verte de nuevo!"
    
    "Habló con tanta confianza que casi parecía como si realmente supiera dónde vivía."
    
    show jes freak with dissolve
    jes "¡Pero ay! ¡El destino por fin nos ha reunido! Y ahora podemos reanudar nuestras deliciosas conversaciones~" 
    
    show jes normal2 with dissolve
    jes "Ahora bien, Su Majestad~"
    jes "¿Cómo pasarás tu segundo día gobernando este reino?"
    
    "¿Cómo iba a pasar hoy...?"
    
    mc "Bueno, supongo que haré mi trabajo como siempre..."

    show jes suprais2 
    jes "¡Ay! Tartas dulces y nata! ¡Su Majestad! ¡Has olvidado algo!"
    mc "Eh??? ¿Qué?"

    hide jes suprais2 with dissolve
    "Jestyn chasqueó los dedos y, en un instante, apareció una corona en su mano."
    "La corona de ayer..."
    "Jestyn colocó suavemente la corona sobre mi cabeza."
    
    show jes flush with dissolve
    jes "Ah... mucho mejor..."
    show jes laugh 
    camera at camera_shake
    jes "¡¡¡HUZZAAAHHH!!! ¡Todos saluden a [poss] Majestad!"
    camera at reset
    hide jes laugh 
    "Jestyn estalló en vítores al unísono, mientras yo todavía intentaba procesar todo lo que acababa de suceder."
    "Una vez que Jestyn terminó de hacer un espectáculo de lo mucho que me había extrañado, comenzó a ahuyentar a los otros títeres a sus habitaciones."

    scene bg_office with dissolve
    "Rápidamente me dirigí a mi oficina para dejar mi bolso antes de ir a trabajar." 
    "Y, por supuesto, Jestyn me siguió justo detrás." 
    "Incluso con él caminando detrás de mí, podía sentir su intensa mirada fija en mi espalda."
    "Vale, ahora lo primero es lo primero, limpiar el teatro. Como ayer ya me ocupé del escenario, creo que hoy limpiaré el pasillo."

    scene bg_corridor with dissolve
    "Me dirigí al almacén para coger los artículos de limpieza."

    scene bg_storage with dissolve
    "Ah... escoba... cubo... fregona..."
    "... ¿Eh?"
    "¿Dónde están?"
    "¿A dónde fueron todos mis artículos de limpieza?"
    "Ayer devolví todo a su lugar, ¿no?"
    "¿O lo hice por- OOF-!"
    "Me di la vuelta e inmediatamente caminé de cara al pecho de Jestyn."
    "¡¿Este títere me había estado siguiendo todo el tiempo?!"
    
    mc "Uf, Jestyn... ¿por qué sigues siguiéndome?"

    show jes nosmile2_2 with dissolve
    jes "Su Majestad, me hiere."
    jes "¿Realmente esperabas que te abandonara por algo tan trivial como un viaje al almacén?"
    mc "...¿Sí?"

    show jes nosmile2
    jes "Ni se te ocurra."
    jes "Te seguiré dondequiera que vayas."

    show jes normal2
    jes "Sin."
    show jes talk2
    jes "A."
    show jes happy2
    jes "Soltero."
    show jes flush2
    jes "Excepción, cariño ~"
    mc "Está bien, solo estoy buscando algunos artículos de limpieza y luego regresaré."
    
    hide jes flush2
    "De repente, Jestyn apareció detrás de mí y puso sus manos sobre mis hombros."

    play sound "jinglebell.mp3" volume 3.0
    camera at camera_shake
    show jes backday2
    "El movimiento abrupto casi me hizo saltar."
    

    jes "Tsk, tsk, tsk ~"
    jes "¡Escucha! Parece que ha olvidado algo, Su Majestad."
    jes "Dijiste que ibas a limpiar el reino, ¿no?"

    camera at reset
    show jes backday2_2 with dissolve
    jes "Pfft... Esta es la primera vez que escucho de un gobernante que tan voluntariamente deja de lado su estatus real para hacer el trabajo de sus propios sirvientes."
    
    "Había olvidado que Jestyn me veía como el [title] de este lugar."
    "Pero mi puesto como guardia de seguridad era mucho más importante en estos momentos."
    "Si no hiciera mi trabajo, no me pagarían."
    "O peor aún, me despedirían."
    "Y resultó que me gustaba mucho tener dinero para seguir con vida."
    
    mc "¿Qué hay de malo en eso? ¿Olvidaste que aquí no soy solo tu [title]?"
    jes "Ah, ciertamente no~"
    jes "Soy plenamente consciente de que Su Majestad tiene todo tipo de responsabilidades humanas que atender."
 
    show jes backday2_3 with dissolve
    jes "Pequeñas cosas mundanas como el empleo, los ingresos y la trágica necesidad de seguir con vida."
    jes "Al contrario, Su Majestad."
    jes "¿Por qué un [title] debería desperdiciar su preciosa energía fregando pisos cuando tiene sirvientas leales a su disposición?"
    mc "¿Eh?"
    
    hide jes backday2_3 with dissolve
    "Con una floritura, Jestyn chasqueó los dedos."
    
    show jes talk with dissolve
    jes "¡Damas~!"
    hide jes talk 
    camera at camera_shake
    stop music
    play sound "jumpscare.mp3" volume 3.0
    show maidelyn normal
    show maidy polite at left
    show maidra polite at right
    maid "¡SÍ, JESTÍN!"
    camera at reset
    
    "Me sobresalté cuando tres marionetas sirvientas aparecieron aparentemente de la nada."
    
    jes "¿Puedo presentarles a las estimadas Maid Sisters? ¡Maidelyn, Maidy y Maidra!"
    jes "Señorías, este es nuestro querido nuevo [title], [player_call]."
    
    "Las tres doncellas inclinaron la cabeza con gracia después de la presentación."
    
    play music "bgs_medieval normal.mp3" volume 2.0 fadein 3.0
    show maidy normal with dissolve
    maidy "¡Ay! ¡Es un verdadero honor conocerle, Su Majestad [player_call]! ¡¡Soy Maidy!!"
    maidy "Jestyn nos habló un poco sobre ti, ¡y ahora finalmente puedo conocerte en persona!"
    show maidy nosmile with dissolve
    maidy "...Para ser honesto..."
    maidy "Esperaba que fueras lindo."
    
    "El cambio repentino en su tono me puso nervioso."
    
    mc "Um... perdón por decepcionarte..."
    
    show maidy happy
    maidy "¡SÍ! ¡NO ERES LINDO!"
    camera at camera_shake
    show maidy estatic 
    maidy "¡¡¡ERES SUPER-DUPER CUUUUUUTEEEEEE!!!"
    camera at reset
    
    "Bien, al menos logré superar sus expectativas. Creo."
    
    maidy "Maidelyn! [poss] majesty es súper linda, ¿verdad? Estás de acuerdo conmigo, ¿no?!?!"
    show maidelyn talk with dissolve
    maidelyn "De hecho. Sí."
    maidy "¡¿Y tú, Maidra?! [poss] majesty is super-duper cute too, riiiiight?!?!?!"
    show maidra nosmile with dissolve
    maidra "Tsk. Eres tan ruidoso. Cállate ya."
    show maidy pout with dissolve
    maidy "¡Mmm! ¡¡No eres divertido!!"
    show maidelyn annoy with dissolve
    maidelyn "Señoras, eso es suficiente."
    maidelyn "[poss] La Majestad está ante nosotros. Por favor compórtense con cierta dignidad."
    
    "El recordatorio inmediatamente llamó la atención de las otras dos sirvientas."
    show maidelyn normal with dissolve
    show maidy normal with dissolve
    show maidra normal with dissolve
    
    maidelyn "Mis más sinceras disculpas por nuestra descortesía, Su Majestad."
    
    "Maidelyn puso una mano sobre su corazón e inclinó la cabeza respetuosamente."
    
    maidelyn "Por favor permítanos presentarnos. Soy Maidelyn."
    show maidy happy
    maidy "¡Soy Maidyyyyy~!"
    show maidy normal 
    show maidra nosmile 
    maidra "Maidra."
    
    "Bueno, eso ya me dijo bastante."
    "Maidelyn parecía ser el que estaba compuesto."
    "Maidy fue definitivamente el más alegre y enérgico."
    "Y Maidra..."
    "Digamos que parecía que preferiría golpear a alguien que tener una conversación educada."
    "Definitivamente la marimacho del grupo."
    
    maidelyn "Como puede ver, Su Majestad, ahora que es nuestro [title], eso nos convierte en sus sirvientas."
    show maidy happy
    maidy "¡Sí!"
    show maidy normal
    maidelyn "En otras palabras, no es necesario que limpies el reino tú mismo."
    maidelyn "Permítanos asumir sus deberes humanos."
    camera at camera_shake
    show maidy happy 
    maidy "¡¡SÍ!!"
    camera at reset
    show maidelyn annoy
    show maidy panic
    show maidra smug
    maidelyn "¡Silencio!"
    
    show maidy pout
    "Los miré fijamente por un momento."
    "¿Qué?"
    "¿Iban a limpiarme el teatro?"
    
    hide maidelyn
    hide maidy
    hide maidra
    show jes normal2 with dissolve
    jes "Eso es correcto, Su Majestad."
    show jes bow with dissolve
    jes "Ahora bien, señoras, por favor ayuden a nuestro querido [title]."
    
    scene bg_corridor with dissolve
    hide jes
    "Sin pensarlo dos veces, las criadas sacaron los mismos artículos de limpieza que había estado buscando e inmediatamente se pusieron a trabajar."
    "..."
    "¿Habían planeado esto desde el principio?"
    "Sabían que hoy iba a limpiar el teatro..."
    "La atención de Jestyn volvió a mí."
    
    show jes normal2 with dissolve
    jes "Ahora bien, creo que una de tus otras tareas es controlar a los títeres, ¿no es así?"
    mc "Ah... cierto."
    jes "En ese caso, ¿por qué no aprovechar esta oportunidad para familiarizarse con sus sujetos?"
    jes "Como [title], al menos deberías conocer a los ciudadanos de tu reino, ¿no?"
    
    "Guió suavemente mi atención hacia las criadas que trabajaban cerca. Era obvio lo que quería que hiciera."
    
    show jes talk with dissolve
    jes "Pruébalo."
    show jes talk2
    jes "Estaré justo detrás de ti."

label maidconvo:
    hide jes with dissolve
    menu:
        "Habla con Maidelyn":
            jump maidelyn_day2

        "Habla con Maidy":
            jump maidy_day2 

        "Habla con Maidra":
            jump maidra_day2
            
        "eso es suficiente":
            jump otherpuppet_day2
        
label otherpuppet_day2: 
    "Después de hablar con las criadas, Jestyn me guió hacia la sala de marionetas."
    
    show jes normal2 with dissolve
    jes "Ahora que conoces a las criadas, permíteme presentarte algunas de las otras marionetas."
    mc "¿Realmente tengo que familiarizarme con cada uno de los títeres?"
    jes "Pues sí. Por supuesto."
    jes "Como dije antes, es importante que un gobernante conozca a sus súbditos."
    
    show jes nosmile2_3
    "Hizo una pausa por un momento. Su mirada cayó al suelo antes de continuar."
    
    show jes normal2 
    jes "Aunque, naturalmente, lo entiendo. Hay bastantes marionetas en este reino."
    jes "Entonces, si Su Majestad sólo logra conocer a cinco de ellos, supongo que sería aceptable."
    
    "¿Cinco?"
    "Esperaba que me dijera que conociera al menos a la mitad de los títeres. Cinco parecían sorprendentemente manejables."

    hide jes normal2 with dissolve
    scene bg_puppetroom with dissolve
    "Entramos al cuarto de los títeres y todo se veía exactamente igual que la última vez que estuve aquí."
    
    show jes nosmile with dissolve
    mc "Cuando revisé ayer, ninguno de los títeres parecía moverse en absoluto."
    mc "¿Estaban dormidos o algo así?"

    show jes normal with dissolve
    jes "Ah, eso fue por orden mía."
    mc "¡¿Por qué?!"

    show jes happy2 with dissolve
    jes "Jeje, porque habías venido al reino."
    jes "Quería ponerte a prueba. Y no quería que vieras los títeres moviéndose antes de que comenzara la representación."
    jes "Pero ahora son libres de moverse como quieran."
    mc "Mmm... pero todavía no he visto ningún títere deambulando por ahí. Además de ti y las criadas, claro está."
    mc "Y las criadas sólo aparecieron porque las llamaste."
    
    "Él se rió entre dientes."
    
    show jes normal with dissolve
    jes "La mayoría de nosotros, los títeres, pasamos el tiempo en nuestras habitaciones."
    jes "Entonces, si no has visto a nadie deambulando, es simplemente porque todos están ocupados en sus propios asuntos."
    
    hide jes normal with dissolve
    "Jestyn se paró frente a mí."
    "Luego abrió los brazos y cada mano señaló hacia un pasillo diferente lleno de salas de títeres."

    show jes normal2 with dissolve
    jes "Ahora bien, conozcamos a algunos residentes más del reino."
    jes "Recomendaría conocer a Knighter y Wizzy."
    jes "Wizzy es nuestro títere mago. Es gentil y amable."

    show jes happy2 with dissolve
    jes "Y Knighter es nuestro caballero títere. Es bastante impulsivo... pero perfectamente seguro, te lo aseguro."
    
    "Eso no me tranquilizó en absoluto."
    
    show jes normal2 with dissolve
    jes "Ahora bien, Su Majestad. ¿A quién te gustaría conocer primero?"

    jump chooseroom_day2

label chooseroom_day2:

    if repeat_route < 2:
        $ crownus_text = "La habitación de Crownus"
        
    elif crownus_room == 0:
        $ crownus_text = "{color=#FFC04C}Here.{/color}"
        
    elif crownus_room == 1:
        $ crownus_text = "{color=#FFC04C}Again.{/color}"
        
    else:
        $ crownus_text = "{color=#FFC04C}Una vez más.{/color}"

    menu: 
        "La habitación de Knighter":
            jump knighterroom_day2

        "La habitación de Wizzy":
            jump wizzyroom_day2
            
        "[crownus_text]" if crownus_room < 3:
            $ crownus_room += 1
            
            if crownus_room == 1:
                jump crownus_room1
                
            elif crownus_room == 2:
                jump crownus_room2
                
            elif crownus_room == 3:
                jump crownus_room3

        "Done":
            if crownus_secret_point >= 5:
                jump the_truth_route
                
            else:
                jump repeat_route

    

#REPEAT ROUTE----------------------------------------------------REPEAT ROUTE-------------------------------------------------------REPEAT ROUTE
label repeat_route:
    stop music fadeout 3.0
    mc "Entonces... ¿con quién me reuniré a continuación?"
    
    show jes nosmile2 with dissolve
    "Jestyn se quedó en silencio, su mirada se dirigió hacia las salas de marionetas que aún no había visitado."
    "Entrecerró los ojos mientras pensaba antes de volver a mirarme."
    
    show jes normal2 with dissolve
    jes "Creo que es suficiente por hoy, Su Majestad."
    mc "¿Qué? ¿¿En realidad?? Sólo hemos conocido a las criadas, Wizzy, Knighter-"
    jes "Y eso es más que suficiente."
    
    hide jes normal2
    camera at camera_shake
    scene bg_office 
    "Jestyn me interrumpió chasqueando los dedos."
    camera at reset
    "Y en un instante estaba de vuelta en mi oficina, con Jestyn detrás de mí."
    
    show jes normal with dissolve
    jes "¿Tiene hambre, Su Majestad? No has comido nada desde esta mañana."
    
    "Antes de que pudiera responder, mi estómago se me adelantó."
    
    show jes happy2 with dissolve
    jes "Pff..."
    jes "No hay necesidad de avergonzarse, Su Majestad. Sé lo trágicamente arruinado que estás."
    
    "Gilipollas."
    
    jes "Por favor espera aquí. Ya vuelvo."
    
    play music "bgs_medieval normal.mp3" volume 3.0 fadein 3.0
    hide jes happy2
    "Con un chasquido de dedos, Jestyn desapareció de la habitación."
    "¿Adónde fue ahora...?"
    "......"
    "Muy bien, mientras espero que regrese Jestyn, ¿qué se supone que debo hacer ahora...?"
    "Ah, claro... Tal vez revise el circuito cerrado de televisión. No he hecho esa tarea."

    hide bg_office with dissolve
    show screen komputer with dissolve
    show cctv main with dissolve

    jump cctv_day2

label cctv_day2:
    $ jestyn_location = renpy.random.choice([
        "outergate",
        "corridor1",
        "theaterhall",
        "storage",
        "stage"
    ])

    menu: 
        "Mirar la entrada":
            jump outergate_day2
            
        "Mirar el pasillo 1":
            jump corridor1_day2
            
        "Mirar la sala del teatro":
            jump theaterhall_day2
            
        "Mirar el almacén":
            jump storage_day2
            
        "Mirar el escenario":
            jump stage_day2

        "Todo listo":
            jump dinner_day2

label outergate_day2:
    play sound "click.mp3" volume 3.0
    show bzzt
    show cctv gate 

    if jestyn_location == "storage" and not found_jestyn:
        $ found_jestyn = True
        "Compruebo la cámara en la puerta exterior. Se ve bien"
        stop music
        play sound "jumpscare.mp3" volume 3.0
        camera at camera_shake
        show jes_cctv_jumpscare
        jes "¡¡¡BUOOOO!!!"
        camera at reset
        mc "AAAAAAHHHHHHHH!!!!!"

        "La cara de Jestyn apareció de repente en mi monitor. Casi salté de mi piel."
        "Maldita sea... Este títere me está jugando otra vez."
        play music "bgs_medieval normal.mp3" volume 3.0 fadein 3.0
        mc "¡JESTÍN!"
        mc "¡¡DEJA DE HACER ESO!!"
        
        "Jestyn simplemente se rió antes de desaparecer de la pantalla nuevamente."
        hide jes_cctv_jumpscare with dissolve
        "En serio..."

    else:
        "Compruebo la cámara en la puerta exterior. Se ve bien."

    show bzzt
    show cctv main
    jump cctv_day2

label corridor1_day2:
    play sound "click.mp3" volume 3.0
    show bzzt
    show cctv corridor1

    if jestyn_location == "corridor1" and not found_jestyn:
        $ found_jestyn = True
        "Compruebo la cámara en la puerta exterior. Se ve bien"
        stop music
        play sound "jumpscare.mp3" volume 3.0
        camera at camera_shake
        show jes_cctv_jumpscare
        jes "¡¡¡BUOOOO!!!"
        camera at reset
        mc "AAAAAAHHHHHHHH!!!!!"

        "La cara de Jestyn apareció de repente en mi monitor. Casi salté de mi piel."
        "Maldita sea... Este títere me está jugando otra vez."
        play music "bgs_medieval normal.mp3" volume 3.0 fadein 3.0
        mc "¡JESTÍN!"
        mc "¡¡DEJA DE HACER ESO!!"
        
        "Jestyn simplemente se rió antes de desaparecer de la pantalla nuevamente."
        hide jes_cctv_jumpscare with dissolve
        "En serio..."

    else:
        "Compruebo la cámara en el pasillo 1. Se ve bien."

    show bzzt
    show cctv main
    jump cctv_day2

label theaterhall_day2:
    play sound "click.mp3" volume 3.0
    show bzzt
    show cctv theaterhall

    if jestyn_location == "theaterhall" and not found_jestyn:
        $ found_jestyn = True
        "Compruebo la cámara en la puerta exterior. Se ve bien"

        stop music
        play sound "jumpscare.mp3" volume 3.0
        camera at camera_shake
        show jes_cctv_jumpscare
        jes "¡¡¡BUOOOO!!!"
        camera at reset
        mc "AAAAAAHHHHHHHH!!!!!"

        "La cara de Jestyn apareció de repente en mi monitor. Casi salté de mi piel."
        "Maldita sea... Este títere me está jugando otra vez."
        play music "bgs_medieval normal.mp3" volume 3.0 fadein 3.0
        mc "¡JESTÍN!"
        mc "¡¡DEJA DE HACER ESO!!"
        
        "Jestyn simplemente se rió antes de desaparecer de la pantalla nuevamente."
        hide jes_cctv_jumpscare with dissolve
        "En serio..."

    else: 
        "Compruebo la cámara en la sala del teatro. Se ve bien."

    show bzzt
    show cctv main
    jump cctv_day2

label storage_day2:
    play sound "click.mp3" volume 3.0
    show bzzt
    show cctv storage

    if jestyn_location == "storage" and not found_jestyn:
        $ found_jestyn = True
        "Compruebo la cámara en la puerta exterior. Se ve bien"

        stop music
        play sound "jumpscare.mp3" volume 3.0
        camera at camera_shake
        show jes_cctv_jumpscare
        jes "¡¡¡BUOOOO!!!"
        camera at reset
        mc "AAAAAAHHHHHHHH!!!!!"

        "La cara de Jestyn apareció de repente en mi monitor. Casi salté de mi piel."
        "Maldita sea... Este títere me está jugando otra vez."
        play music "bgs_medieval normal.mp3" volume 3.0 fadein 3.0
        mc "¡JESTÍN!"
        mc "¡¡DEJA DE HACER ESO!!"
        
        "Jestyn simplemente se rió antes de desaparecer de la pantalla nuevamente."
        hide jes_cctv_jumpscare with dissolve
        "En serio..."
        
    else:
        "Reviso la cámara en el almacenamiento. Se ve bien."

    show bzzt
    show cctv main
    jump cctv_day2

label stage_day2:
    play sound "click.mp3" volume 3.0
    show bzzt
    show cctv stage2

    if jestyn_location == "stage" and not found_jestyn:
        $ found_jestyn = True
        "Compruebo la cámara en la puerta exterior. Se ve bien"

        stop music
        play sound "jumpscare.mp3" volume 3.0
        camera at camera_shake
        show jes_cctv_jumpscare
        jes "¡¡¡BUOOOO!!!"
        camera at reset
        mc "AAAAAAHHHHHHHH!!!!!"

        "La cara de Jestyn apareció de repente en mi monitor. Casi salté de mi piel."
        "Maldita sea... Este títere me está jugando otra vez."
        play music "bgs_medieval normal.mp3" volume 3.0 fadein 3.0
        mc "¡JESTÍN!"
        mc "¡¡DEJA DE HACER ESO!!"
        
        "Jestyn simplemente se rió antes de desaparecer de la pantalla nuevamente."
        hide jes_cctv_jumpscare with dissolve
        "En serio..."

    else:
        "Compruebo la cámara en el escenario. Se ve bien."
        
    show bzzt
    show cctv main
    jump cctv_day2

label dinner_day2:
    hide cctv main with dissolve
    hide screen komputer with dissolve
    scene bg_office with dissolve

    "Creo que ya todo se ha calmado."
    "......"
    "Me pregunto adónde fue Jestyn esta vez..."

    mc "Al principio pensé que había ido a buscar comida..."

    camera at camera_shake
    stop music
    play sound "jumpscare.mp3" 
    show jes close creep
    jes "Lo hice."
    camera at reset
    mc "¡¡JESTYN, DEJA DE APARECER DE LA NINGUNA PARTE ASÍ!!"

    show jes close smug with dissolve
    play music "bgs_medieval normal.mp3" volume 3.0 fadein 3.0
    jes "Jeje... Mis más sinceras disculpas, Su Majestad~ ¿Pero cómo podría resistirme? Tus reacciones son demasiado encantadoras. Un pobre bufón simplemente no puede evitar pedir un bis."
    mc "En serio. De hecho me vas a dar un infarto."

    show jes close soft with dissolve
    jes "Ahh... Por favor, no digas cosas tan espantosas. Incluso la idea de que Su Majestad se derrumbe hace que me duela el corazón."
    jes "Muy bien. Me abstendré de asustarte otra vez."
    show jes close smug 
    jes "Quizás."
    
    hide jes close smug with dissolve
    "Dejé escapar un largo suspiro. ¿Qué esperaba yo de este títere...?"
    "Entonces mis ojos se posaron en lo que llevaba."
    "......"
    
    mc "Jestyn... Este es..."

    show jes normal with dissolve
    jes "¿Mmm? Ah, sí. Su cena, Su Majestad."
    mc "Sí, puedo verlo, pero..."
    mc "¿No es esto... demasiado sofisticado?"
    
    show jes happy with dissolve
    "Jestyn dejó escapar una risita orgullosa."
    
    jes "Naturalmente. Nada menos que la mejor cocina es digna de Su Majestad."
    
    "Me quedé mirando el banquete en las manos de Jestyn."
    "Había todo tipo de platos lujosos, algunos de los que nunca había oído hablar, y mucho menos visto antes."
    "Había pan fresco servido con un plato de sopa cremosa, lo que parecía un bistec perfectamente cocido e incluso un rico pastel de chocolate de postre."
    "... Vaya. Mi cerebro de fideos instantáneos definitivamente no estaba equipado para procesar una comida tan elegante."
    
    show jes talk2 with dissolve
    jes "Además, sé que Su Majestad ha vivido una vida trágicamente empobrecida. Lo mínimo que puedo hacer es permitirte experimentar una fiesta real adecuada."
    mc "Vaya. Qué increíblemente amable de tu parte."
    mc "Pero... ¿de dónde sacaste todo esto????"

    show jes bow with dissolve
    jes "Un restaurante de cinco estrellas, por supuesto."
    
    "...Está bien. De hecho, este títere salió del teatro sólo para ir a cenar."
    
    mc "¿Y? ¿Cómo pagaste por todo esto? Incluso si tuvieras dinero, esto parece ridículamente caro."

    show jes unimpress2 with dissolve
    jes "¿Por qué parece tan sospechoso, Su Majestad? ¡Por supuesto que tengo el dinero! ¡Más que suficiente, de hecho!"
    show jes pout2 with dissolve
    jes "Hmph. Pensar que Su Majestad dudaría tanto de este humilde bufón."
    mc "Entonces, ¿de dónde sacaste el dinero?"
    jes "...El banco."
    mc "Y... ¿tienes tarjeta de crédito?"

    show jes nervous2 with dissolve
    jes "......"
    mc "......"
    mc "Jestyn, tú-"

    camera at camera_shake
    show jes laugh2 with dissolve
    jes "¡Ah! ¿Mirarías eso? ¡Ya son las diez! ¡Es hora de la cena de Su Majestad!"
    
    camera at reset
    "Jestyn dejó la bandeja sobre la mesa antes de hacerme un gesto para que me sentara en la cama."
    "Cogió una cesta de pan con mantequilla y un plato de sopa cremosa."
    "Luego se sentó a mi lado."
    
    hide jes laugh2 with dissolve
    show jescg dinner with dissolve
    jes "Aquí estamos, Su Majestad. Todo festín comienza con un aperitivo."
    jes "Entonces, permita que este humilde bufón presente pan con mantequilla con una rica sopa de crema. Espero que agrade el paladar de Su Majestad."
    
    hide jescg dinner with dissolve
    "Cogí un trozo de pan y le di un mordisco."
    "Fue increíble. La corteza estaba perfectamente crujiente, mientras que el interior era suave y esponjoso."
    "Nunca antes había probado un pan tan rico."
    
    show jes talk2 with dissolve
    jes "Parece que Su Majestad lo aprueba. Ahora, intenta mojar el pan en la sopa."
    
    "Hice lo que me sugirió, mojando el pan en la sopa cremosa antes de darle otro bocado."
    "Sabía incluso mejor que antes. El pan suave y mantecoso combina perfectamente con la rica y aterciopelada sopa, haciendo que cada bocado sea increíblemente satisfactorio."

    show jes normal with dissolve
    "... Sólo entonces me di cuenta de que Jestyn me había estado observando todo el tiempo."
    
    mc "¿Por qué me miras así?"
    
    "Él simplemente sonrió."
    
    show jes happy with dissolve
    jes "Oh, no es nada, Su Majestad. ¿No puedo admirar a Su Majestad mientras cena?"
    mc "......"
    mc "Si tienes hambre... podemos compartir."
    
    show jes suprais with dissolve
    "Jestyn se quedó en silencio por un momento."
    
    show jes nosmile with dissolve
    jes "No tengo hambre, Su Majestad. No necesito comer."
    
    "...Correcto. Es un títere. Eso realmente tenía sentido."
    
    show jes normal2 with dissolve
    jes "Podemos comer comida humana si lo deseamos e incluso podemos saborearla. Pero simplemente no hace nada por nosotros."
    mc "Ya veo... Entonces, ¿podrías-?"

    show jes normal2_2
    jes "No es necesario, Su Majestad~ Usted es el que tiene hambre. Eso es todo lo que importa."
    mc "¿Qué pasa si hago un pedido? Se siente raro comer solo."
    
    show jes suprais2 with dissolve
    "Los ojos de Jestyn se abrieron con sorpresa antes de que un leve sonrojo se extendiera por sus mejillas."
    
    show jes flush2 with dissolve
    jes "...Su Majestad es demasiado amable... Mostrando tal preocupación por un humilde bufón..."

    show jes normal2_2 with dissolve
    jes "Muy bien, muy bien~ ¿Qué posibilidades tiene este humilde bufón contra una orden de la Corona?"

    "Cogió un trozo de pan y le dio un mordisco."
    
    mc "Bueno, ¿no?"

    show jes talk2 with dissolve
    jes "De hecho. Es bastante delicioso."
    
    "......"

    mc "Ya sabes... esto se siente como una cita."
    
    camera at camera_shake
    show jescg dinner2 with dissolve
    "Jestyn inmediatamente dejó de masticar y me miró con los ojos muy abiertos."
    camera at reset
    
    mc "U-uh... ¿Jestyn?"

    show jescg dinner3 with dissolve
    jes "......D...."
    jes ".... Fecha....? ¿Acaba de decir fecha, Su Majestad...?"
    mc "¿Dije algo malo?"
    jes "No. No, no... Todo lo contrario."
    jes "Me acabo de dar cuenta de algo..."
    
    "Una amplia sonrisa se dibujó en su rostro y el sonrojo de sus mejillas se hizo más intenso."
    
    show jescg dinner4 with dissolve
    jes "Tienes razón... SÍ se siente como una cita. Casi."
    
    hide jescg dinner with dissolve
    "Se aclaró la garganta y rápidamente se levantó de la cama."
    
    show jes nosmile2_2 with dissolve
    jes "Perdóneme, Su Majestad, pero esto simplemente no sirve."

    show jes unimpress
    jes "¡Tengo que hacer que esta cita sea aún mejor!"
    mc "Espera, eso no es lo que quiero decir."
    
    play sound "snap.mp3"
    hide jes unimpress
    "Ni siquiera pude terminar la frase antes de que Jestyn chasqueara los dedos y desapareciera."
    
    mc "¿Eh? ¿A dónde fue?"
    
    "Esperé un rato, disfrutando tranquilamente de mi pan."
    "Pasaron los segundos. Luego minutos. Y después de varios minutos más, Jestyn todavía no había regresado."
    
    mc "¿A dónde fue siquiera...? A este paso, realmente me voy a comer todo el pan yo solo."
    
    "Como todavía tenía hambre, tomé otro trozo de pan y..."

    play sound "snap.mp3"
    stop music
    camera at camera_shake
    scene bg_dinner
    ".........."
    camera at reset
    "¿Qué...?"
    
    mc "¡¿Eh?! ¡¿Dónde estoy?!"
    
    "En un abrir y cerrar de ojos, me encontré en otro lugar, sentado en una silla frente a una mesa modestamente decorada."
    "Una flor roja. Lo que parecía una rosa descansaba en el centro de la mesa, con una vela aromática colocada al lado."
    "Un mantel blanco adornado con elegantes diseños dorados cubría la mesa."
    "... Sólo hay una persona que haría algo como esto."
    
    mc "¿Jestyn? ¿Está ahí?"

    "......"

    show jescg hand with dissolve
    "El sonido de pasos acercándose se hizo más cercano cuando llamé el nombre de Jestyn."

    hide jescg hand with dissolve
    "Una mano rozó lentamente la mía, sobresaltándome. Casi aparté la mano por instinto."

    show jescg kisshand with dissolve
    "Pero entonces la mano tomó suavemente la mía. Y un segundo después, sentí unos labios suaves besar el dorso de mi mano."
    "Estaría mintiendo si dijera que no estaba nervioso."
    "En la oscuridad, forcé la vista, tratando de distinguir quién estaba besando mi mano."
    "Y finalmente... vi a alguien."

    play music "date.mp3" volume 3.0 fadein 3.0
    show jescg kisshand2 with dissolve
    "Alguien con el pelo ondulado, de color marrón oscuro y cuidadosamente recogido hacia atrás."
    "Su ropa era inmaculada y elegante, complementada con una túnica de color rojo intenso."
    "A primera vista... casi parecía un rey."
    "Pero en el momento en que vi su cara, finalmente me di cuenta."
    
    mc "......Jestyn...?"
    
    "La sonrisa de Jestyn se amplió aún más al oír su nombre."
    $ voice_duck_start()
    voice "JESTYN02_DAY2.ogg"
    jes "Quiero preguntarle si a Su Majestad le gusta el ambiente de nuestra pequeña cena. Aunque... supongo que también estás disfrutando de la vista frente a ti, ¿hm~?"
    $ voice_duck_end()
    "Salí de mi aturdimiento."
    
    hide jescg kisshand2 with dissolve
    mc "¿Por qué estás vestido así?"

    show jes dinner normal with dissolve
    jes "¡Porque simplemente tenía que impresionar a Su Majestad!"
    jes "Para ser honesto... nunca he estado en algo llamado cita. Sólo he leído sobre ellos en libros."
    jes "Entonces... este es el primero."
    jes "Estuve bastante tiempo decidiendo qué ponerme..."
    jes "Supongo que me veo un poco diferente... pero dígame, Su Majestad..."
    show jes dinner smug with dissolve
    jes "¿Te gusta~?"

    menu:
        "Yes":
            mc "Sí. Te ves diferente y guapo."
            show jes dinner horny with dissolve
            "Jestyn se rió como una chica de secundaria enamorada."
            jes "Mnhh~ Me alegro mucho que le guste a Su Majestad~"

        "No":
            mc "Realmente no."
            
            show jes dinner pout with dissolve
            "Su sonrisa instantáneamente se convirtió en un puchero."
            
            jes "Hmph. Qué cruel. Me tomé la molestia de vestirme sólo para usted, Su Majestad."

            show jes dinner horny with dissolve
            jes ".....Mmmnnn... pero claro... Supongo que tampoco puedo rechazarlo..."
            jes "Si Su Majestad desea seguir insultándome... por favor, sea mi invitado~"
            
            "Qué fenómeno."

    show jes dinner normal with dissolve
    jes "Ahora bien~ ¿Qué tal si continuamos con la cena que fue tan bruscamente interrumpida?"
    
    "Jestyn chasqueó los dedos y, en un instante, la sopa de pan y crema que habíamos estado comiendo antes reapareció en la mesa."
    
    show jes dinner smirk with dissolve
    jes "Por favor, disfrute su comida, Su Majestad~"
    
    show jes dinner normal with dissolve
    "Ya tenía hambre, así que no perdí el tiempo comiendo la sopa de pan y crema."
    "Pero Jestyn no tocó su propia comida. En cambio, simplemente me miró con su habitual sonrisa."
    
    mc "Jestyn, tú también deberías comer."

    show jes dinner horny with dissolve
    jes "Jeje... Por supuesto... por supuesto, Su Majestad... Estoy disfrutando de mi comida..."
    mc "Tu comida no soy yo."
    
    "Jestyn soltó una risita silenciosa antes de finalmente darle un mordisco a su pan y mojarlo en la sopa de crema."
    
    show jes dinner normal with dissolve
    jes "Su Majestad... ¿puedo preguntarle algo?"
    mc "¿Mmm?"
    jes "Antes, cuando Su Majestad estaba pasando tiempo con Knighter y Wizzy..."
    mc "...¿Sí?"
    show jes dinner nosmile with dissolve
    jes "...Se sintió... extraño."
    mc "¿Qué quieres decir?"
    
    "Se quedó en silencio por un momento, dando otro bocado a su pan."
    
    jes "...Su Majestad parecía... cercana a ellos."
    jes "Y me hizo sentir... no sé muy bien cómo decirlo."
    
    "..."
    "... ¿Ah? No me digas que él es..."
    "Tenía la sensación de que ya sabía lo que estaba tratando de decir. Aun así, quería oírlo decirlo él mismo."
    
    mc "Sólo dime qué tienes en mente."
    jes "... Estoy tan confundido conmigo mismo, Su Majestad."
    jes "Quiero que Su Majestad los conozca..."
    jes "...Pero no quiero que Su Majestad se acerque tanto a ellos."

    show jes dinner mad with dissolve
    jes "Especialmente... si eso significa que Su Majestad podría olvidarse de mí..."
    jes "Desde que conocí a Su Majestad... he sentido tantas cosas que ni siquiera puedo empezar a explicar."
    jes "Son todos tan... desconocidos. Nunca antes había experimentado algo parecido."
    jes "Me siento como un pajarito que finalmente escapó de su nido... extendiendo sus alas y volando hacia el gran mundo por primera vez..."
    mc "........"
    mc "Jestyn... eso se llama celos."
    
    show jes dinner suprais2 with dissolve
    jes "...Celos..."
    
    "Jestyn levantó lentamente su mirada para encontrarse con la mía."
    
    show jes dinner mad2 with dissolve
    jes "...Entonces sí."
    jes "Este humilde bufón está terriblemente celoso."
    jes "Dolorosamente... descaradamente... irremediablemente celoso."

    show jes dinner sad with dissolve
    jes "...Y sin embargo, ¿qué derecho tiene un simple bufón de la corte? No soy más que el fiel juguete de Su Majestad... un tonto destinado a divertir a la Corona. No tengo ningún lugar para exigir la atención de Su Majestad."
    jes "...Pero..."
    show jes dinner mad with dissolve
    jes "...¿Sería realmente tan egoísta... si este pobre bufón deseara ser el único juguete que Su Majestad alguna vez buscó?"
    
    "Me miró con una intensidad que nunca antes había visto. Su voz se hizo más pesada."
    "...¿Eso significaba... que se había enamorado de mí?"
    "¿Tan rápido...?"
    
    mc "Jestyn... ¿Eso significa que estás enamorado de mí?"

    show jes dinner suprais2 with dissolve
    jes "...¿Amor...?"
    
    "Jestyn se quedó en silencio, dando vueltas a mis palabras en su mente."
    
    jes "...Amor... amor... amor..."
    jes "Un sentimiento que se agita cada vez que tus ojos se posan en alguien... alguien verdaderamente especial..."
    jes "Un anhelo de permanecer a su lado... un anhelo de tenerlos todos para ti..."
    
    "Murmuró las palabras para sí mismo. Luego, poco a poco, la sonrisa volvió a su rostro. Más ancho que antes."
    
    show jes dinner love2 with dissolve
    jes "...Sí... ¡Sí!"
    jes "Yo... yo os amo... ¡Su Majestad!"
    jes "Siempre supe lo que era el amor... al menos conocía su definición. Pero yo nunca lo había sentido realmente."
    show jes dinner love with dissolve
    jes "Así es como se siente el amor... Jaja..."
    
    "Hizo una pausa."
    
    jes "...Entonces..."
    jes "...¿Qué siente Su Majestad por mí?"
    jes "Ahora que has aprendido cómo se siente este humilde bufón... ¿qué lugar ocupa este tonto corazón en el tuyo?"
    
    "...¿Cómo me sentí con respecto a Jestyn?"

    menu:
        "Me gusta Jestyn":
            "Podía ser insoportablemente descarado con todas sus burlas... pero también era reflexivo, afectuoso y sorprendentemente divertido."
            "Me gustaba... pero todo estaba sucediendo muy rápido."

        "no estoy seguro":
            "...."
            "No estoy seguro de si me gusta Jestyn de esa manera."
            "Claro, es un títere divertido... pero todo está sucediendo demasiado rápido para mí."
            
    mc "...La verdad es, Jestyn... nos conocimos ayer."
    mc "Me gustas... pero necesito tiempo."

    show jes dinner sad2 with dissolve
    "Un destello de decepción cruzó el rostro de Jestyn, aunque asintió entendiendo."
        
    jes "Lo entiendo, Su Majestad... Los corazones humanos necesitan tiempo. Este bufón impaciente puede esperar."

    show jes dinner sad with dissolve
    "El silencio se instaló entre nosotros una vez más mientras regresamos a nuestro pan."

    if mc_jealous:
        mc "Bueno, Jestyn... si realmente estás enamorado de mí... entonces ¿por qué abrazabas así a Maidy?"

        show jes dinner suprais 
        jes "¿Maidy?... ¡Ah!"
        
        "Esa sonrisa traviesa suya regresó de inmediato."
        
        show jes dinner smirk2 with dissolve
        jes "Simplemente le di a Maidy un pequeño y cálido abrazo. ¿Seguramente no hay ningún crimen en eso~?"
        
        "Lo dijo con el mismo tono burlón y juguetón."
        

    else:
        jes "...Para ser honesto, Su Majestad... Esperaba que al menos se pusiera un poco celoso."
        mc "¿Celoso...?"
        show jes dinner nosmiletalk2 with dissolve
        jes "Cuando abracé a Maidy... no reaccionaste en absoluto. Ni siquiera el más mínimo cambio en tu expresión."
        show jes dinner nosmile2 
        jes "........"
        show jes dinner sad with dissolve
        jes "...Me puso un poco triste."
        
        "Oh... ¿entonces ese abrazo realmente fue intencional?"

    "...Ya veo. Entonces ese es el juego que quería jugar."
        
    mc "Ya veo."
    mc "¿Era esa tu manera de llamar mi atención?"

    show jes dinner horny with dissolve   
    "Jestyn dejó escapar una suave risita mientras el sonrojo en sus mejillas se hacía más profundo."
        
    jes "No tengo la menor idea de qué está hablando Su Majestad~"

    menu:
        "castigarlo":
            jump punishment_day2

        "Déjalo deslizar":
            jump let_it_slide

label punishment_day2:
    $ subjes = True
    mc "Muy bien."

    camera at camera_shake
    show jes dinner suprais2 
    "Me levanté de mi silla y caminé hacia Jestyn."
    camera at reset
    "Tomé el pedazo de pan de su mano."
    "Me miró confundido por un momento antes de que suavemente le metiera el pan en la boca."
    camera at camera_shake
    show jescg gagbread 
    "Sus ojos se abrieron con sorpresa."
    camera at reset
    "...Tal vez, estaba empezando a descubrir cómo mantener a raya a este problemático bufón."
    
    mc "¿Estás realmente tan desesperado por ser castigado?"
    
    show jescg gagbread2 with dissolve
    "Su cuerpo comenzó a temblar y su respiración se volvió irregular."
    "... Parecía que estaba disfrutando esto mucho más de lo que debería."
    
    jes "Mmph..."
    mc "¿Quieres decir algo?"
    
    "Él asintió. Le saqué el trozo de pan de la boca."
    
    if mc_jealous:
        show jescg gagbread5 with dissolve
        jes "Ehe... ¿Está Su Majestad... celosa~?"
        "........"
        "La forma en que dijo esas palabras despertó algo dentro de mí."
        "Me hizo querer ponerlo en su lugar... hacer que se portara bien."
    
    else:
        show jescg gagbread3 with dissolve
        jes "S-Sí... p-por favor..."
        mc "¿Por favor qué?"
        jes "Por favor…castígame….préstame atención…"
        jes "Lo necesito... lo necesito... lo necesito... lo necesito..."
        show jescg gagbread4 with dissolve
        jes "MÍRAME. SOLO YO."

    "... ¿Así que esto era lo que se sentía al tener realmente ventaja sobre alguien...?"
    show jescg gagbread2 with dissolve
    "Antes de darme cuenta, una sonrisa se dibujó en mi rostro mientras empujaba el pan hacia su boca."
    "Luego le di un mordisco al otro extremo del mismo trozo de pan."
    "Mis ojos nunca dejaron los suyos."
    "Su mirada permaneció fija en la mía, inquebrantable, mientras su respiración se hacía cada vez más irregular."

    mc "Ya sabes, Jestyn... No tengo ninguna experiencia siendo el dominante."
    mc "Pero... después de todo lo que me has enseñado desde ayer... creo que me empieza a gustar."
    mc "Y creo... que esta es la oportunidad perfecta para aprender."
    jes "Nngh... Mmh..."
    
    "Intenté recordar lo que había leído antes sobre este tipo de dinámica."
    "Si no recuerdo mal... había algo llamado 'domesticación de mocosos', donde la pareja más dominante disciplina a un sumiso travieso hasta que se porta bien."
    "...O al menos eso es lo que recuerdo haber leído en línea."
    "Pero… ¿qué debo hacer desde aquí?"
    "Al ver la expresión confusa en mi rostro, Jestyn comenzó a hacer gestos."
    "Se dio unas palmaditas en la mejilla... luego le dio unas cuantas palmaditas en el trasero antes de hacer un movimiento de golpe con la mano."

    mc "... ¿Abofetearte... o azotarte...?"

    "Él asintió."
    "....."
    "Tengo 2 opciones. ¿Qué se supone que debo hacer?"

    menu:
        "Dale una palmada en la mejilla":
            hide jes dinner with dissolve
            show jescg slap with dissolve
            "Decidí darle una palmada en la mejilla."
            "Lentamente levanté la mano."
            "Pero… ¿realmente tuve el descaro de golpearlo tan fuerte…?"
            "......"
            "No... Pase lo que pase, no quería lastimar a Jestyn."
            "Mi mano aterrizó suavemente contra su mejilla."

            play sound "slap.mp3"
            camera at camera_shake
            show jescg slap2_2       
            jes "¡Mmm!"
            camera at reset
            "La bofetada fue ligera, dejando sólo un leve sonrojo en su mejilla."
            show jescg slap4 with dissolve
            "Jestyn me miró confundido, como si estuviera comprobando si algo había salido mal, antes de darme cuenta de que simplemente no podía hacerle daño."
            "Su expresión se suavizó gradualmente."
            "Sin decir una palabra, sus ojos parecieron decirme... que estaba bien si lo golpeaba más fuerte."
            "Esta vez le di una bofetada más fuerte."
            play sound "slap.mp3"
            camera at camera_shake
            show jescg slap2
            "¡¡¡BOFETA!!!"
            camera at reset
            jes "MNNHHH-!!"
            
            "La respiración de Jestyn se hizo más pesada. Parecía estar disfrutandolo."
            "Finalmente decidí decir algo."
            
            mc "Eres un mocoso, ¿lo sabías, Jestyn?"
            
            show jescg slap3 with dissolve
            "En el momento en que las palabras salieron de mi boca, todo su cuerpo tembló."

            jes "Nghhh~..."

            "Acaricié suavemente la mejilla de Jestyn... antes de darle otra bofetada."

            menu:
                "Dale una bofetada":
                    play sound "slap.mp3"
                    camera at camera_shake
                    show jescg slap2 with dissolve
                    "Le di una bofetada a Jestyn nuevamente."
                    camera at reset
                    "¡BOFETA!"
                    
                    jes "Mnhhhh!!"

                    mc "Quieres tanto mi atención, ¿verdad? Entonces aquí. Tómalo."
                    mc "Yo te daré. Mucha de mi atención."
                    show jescg slap3 with dissolve
                    "Jestyn asintió con entusiasmo."

                    jes "Nhhh...hhhh...."

                "Dale una bofetada más fuerte":
                    play sound "slap.mp3"
                    camera at camera_shake
                    show jescg slap2 with dissolve
                    "Lo abofeteé una vez más... esta vez incluso más fuerte que antes."
                    camera at reset
                    jes "¡¡¡NGHHHH!!! MNHHHH!!"

                    mc "Quieres tanto mi atención, ¿verdad? Entonces aquí. Tómalo."
                    mc "Yo te daré. MUCHA de mi atención."

                    "Jestyn asintió con entusiasmo."
                    show jescg slap3 with dissolve
                    jes "Nhhh...hhhh...."

            menu:
                "Again":
                    play sound "slap.mp3"
                    camera at camera_shake
                    show jescg slap2 with dissolve
                    "¡¡¡BOFETA!!!"
                    camera at reset
                    jes "NGHHH!!!"
                    show jescg slap3 with dissolve
                    menu: 
                        "Again":
                            play sound "slap.mp3"
                            camera at camera_shake
                            show jescg slap2 with dissolve
                            "BOFETA!!!!"
                            camera at reset
                            jes "MNHHHHNN!!! ¡¡NHH!!"

                            menu:
                                "AGAIN":
                                    play sound "slap.mp3"
                                    camera at camera_shake
                                    show jescg slap2 with dissolve
                                    "¡¡BOFETA!!"
                                    camera at reset 
                                    pause 0.5
                                    play sound "slap.mp3"
                                    camera at camera_shake
                                    "¡¡¡BOFETA!!!"
                                    camera at reset 
                                    pause 0.5
                                    play sound "slap.mp3"
                                    camera at camera_shake
                                    "BOFETA!!!!"
                                    camera at reset 
                                    pause 0.5
                                    play sound "slap.mp3"
                                    camera at camera_shake

                                    jes "¡NGH! ¡¡GHHH!! ¡¡¡NHHHHHH!!!"
                                    show jescg slap5 with dissolve

                                    stop music fadeout 2.0
                                    menu:
                                        
                                        "AGAIN":
                                            play sound "glitch.mp3"
                                            camera at camera_shake
                                            show glitch jesslap 
                                            "!!!!!"
                                            show jescg slap6
                                            hide glitch jesslap 
                                            "¿Qué... qué acaba de pasar?"
                                            "Por un breve momento... me sentí extrañamente ligero."
                                            "Cuando escuché a alguien llorar, me di cuenta de que era Jestyn."

                                            jes ".... sollozo.... sollozo...."

                                            "Oh no... ¡¿Qué he hecho?!"
                                            show jescg slap7 with dissolve
                                            "Rápidamente saqué el trozo de pan de la boca de Jestyn."
                                            play music "date.mp3" volume 3.0 fadein 3.0
                                            mc "¡JESTÍN! ¡Lo siento mucho! ¡Realmente lo soy! ¡¿Estás bien?!"
                                            
                                            "Pero Jestyn no pareció escucharme."
                                            
                                            mc "Jestyn... oye... lo siento... fui demasiado lejos..."
                                            
                                            "Suavemente acaricié su mejilla, esperando que eso lo reconfortara, aunque fuera un poco."
                                            "Por fin, Jestyn me miró."
                                            
                                            jes "...sollozo... Su Majestad... Lo siento..."
                                            mc "No, no, no. Soy yo quien debería disculparse. Lo llevé demasiado lejos, ¿vale?"
                                            show jescg slap8 with dissolve
                                            jes "...Eje... Está bien..."
                                            jes "...me gustó..."
                                            show jescg slap9 with dissolve
                                            jes "...Aunque, por un momento... pensé que Su Majestad..."
                                            
                                            "Jestyn se detuvo antes de que pudiera terminar."
                                            
                                            show jescg slap10 with dissolve
                                            jes "...No es nada, jeje... No se preocupe, Su Majestad..."
                                            

                        "eso es suficiente":
                            show jescg slap11 with dissolve
                            "Creo que es suficiente."
                            show jescg slap12 with dissolve
                            "Acaricié suavemente la mejilla de Jestyn de nuevo, pasando mis dedos por la piel sonrojada."
                            
                            jes "Mnh... nh..."
                            
                            "Finalmente le saqué el trozo de pan de la boca, permitiéndole hablar."
                            show jescg slap13 with dissolve
                            
                            jes "Hahh... hahh... S-Su Majestad..."
                            mc "¿Has aprendido la lección?"
                            
                            "Jestyn asintió."
                            
                            mc "¿Entonces qué dices?"
                            jes "Lo-lo siento, Su Majestad... me equivoqué..."
                            mc "Buen chico."
                            
                            "Le acaricié suavemente la cabeza y Jestyn prácticamente se derritió bajo los elogios, pareciendo genuinamente feliz con el afecto que le di."

                "eso es suficiente":
                    show jescg slap11 with dissolve
                    "Creo que es suficiente."
                    show jescg slap12 with dissolve
                    "Acaricié suavemente la mejilla de Jestyn de nuevo, pasando mis dedos por la piel sonrojada."
                    jes "Mnh... nh..."
                    
                    "Finalmente le saqué el trozo de pan de la boca, permitiéndole hablar."
                    show jescg slap13 with dissolve
                    
                    jes "Hahh... hahh... S-Su Majestad..."
                    mc "¿Has aprendido la lección?"
                    
                    "Jestyn asintió."
                    
                    mc "¿Entonces qué dices?"
                    jes "Lo-lo siento, Su Majestad... me equivoqué..."
                    mc "Buen chico."
                    
                    "Le acaricié suavemente la cabeza y Jestyn prácticamente se derritió bajo los elogios, pareciendo genuinamente feliz con el afecto que le di."


        "darle una palmada":
            "Le pedí a Jestyn que se inclinara sobre la mesa."
            hide jes dinner with dissolve
            show jescg spank with dissolve
            "El rostro de Jestyn se sonrojó con ansiosa anticipación al pensar en lo que podría suceder a continuación."
            "Se inclinó sobre la mesa tal como le había ordenado."
            show jescg spank5 with dissolve
            "Lentamente pasé mi mano por su espalda, desde sus hombros hasta su espalda baja, haciéndolo temblar ante el suave toque."
            
            jes "Ngh......"
            
            "Cuando mi mano llegó a la parte baja de su espalda, le di una ligera palmadita en el trasero."
            
            jes "Mnh-"
            
            show jescg spank with dissolve
            "Luego retiré mi brazo, preparándome para azotarlo."
            "Pero… ¿realmente tuve el descaro de golpearlo tan fuerte…?"
            "......"
            "No... Pase lo que pase, no quería lastimar a Jestyn."
            "Mi mano aterrizó suavemente contra su trasero."
            play sound "slap.mp3"
            camera at camera_shake
            show jescg spank2 
                    
            jes "¡Mmm!"
            camera at reset
            "La bofetada fue ligera, solo una bofetada normal."
            "Jestyn me miró confundido, como si estuviera comprobando si algo había salido mal, antes de darme cuenta de que simplemente no podía hacerle daño."
            show jescg spank3 with dissolve
            "Su expresión se suavizó gradualmente."
            "Sin decir una palabra, sus ojos parecieron decirme... que estaba bien si lo golpeaba más fuerte."
            "Le di una palmada más fuerte esta vez."
            play sound "slap.mp3"
            camera at camera_shake
            show jescg spank4 
            "¡¡¡BOFETA!!!"
            camera at reset
            jes "MNNHHH-!!"
            
            "La respiración de Jestyn se hizo más pesada. Parecía estar disfrutandolo."
            "Finalmente decidí decir algo."
            
            mc "Eres un mocoso, ¿lo sabías, Jestyn?"
            show jescg spank5 with dissolve
            "En el momento en que las palabras salieron de mi boca, todo su cuerpo tembló."

            jes "Nghhh~..."

            "Acaricié suavemente el trasero de Jestyn... antes de darle otro azote."

            menu:
                "darle una palmada":
                    "Le di una palmada a Jestyn nuevamente."
                    play sound "slap.mp3"
                    camera at camera_shake
                    show jescg spank4 
                    "¡BOFETA!"
                    camera at reset
                    jes "Mnhhhh!!"

                    mc "Quieres tanto mi atención, ¿verdad? Entonces aquí. Tómalo."
                    mc "Yo te daré. Mucha de mi atención."
                    show jescg spank5 with dissolve
                    "Jestyn asiente con entusiasmo"

                    jes "nhh...hhhh...."

                "Pégale más fuerte":
                    "Le di una palmada una vez más... esta vez incluso más fuerte que antes."
                    play sound "slap.mp3"
                    camera at camera_shake
                    show jescg spank4 
                    jes "¡¡¡NGHHHH!!! MNHHHH!!"

                    mc "Quieres tanto mi atención, ¿verdad? Entonces aquí. Tómalo."
                    mc "Yo te daré. MUCHA de mi atención."
                    show jescg spank5 with dissolve
                    "Jestyn asintió con entusiasmo."

                    jes "Nhhh...hhhh...."
                    show jescg spank5 with dissolve

            menu:
                "Again":
                    play sound "slap.mp3"
                    camera at camera_shake
                    show jescg spank4 
                    "¡¡¡BOFETA!!!"
                    camera at reset
                    jes "NGHHH!!!"
                    show jescg spank5 with dissolve

                    menu: 
                        "Again":
                            play sound "slap.mp3"
                            camera at camera_shake
                            show jescg spank4 
                            "BOFETA!!!!"
                            camera at reset
                            jes "MNHHHHNN!!! ¡¡NHH!!"
                            show jescg spank5 with dissolve

                            menu:
                                "AGAIN":
                                    play sound "slap.mp3"
                                    camera at camera_shake
                                    show jescg spank4 
                                    "¡¡BOFETA!!"
                                    camera at reset
                                    pause 0.5
                                    play sound "slap.mp3"
                                    show jescg spank4 
                                    camera at camera_shake
                                    "¡¡¡BOFETA!!!" 
                                    camera at reset
                                    pause 0.5
                                    play sound "slap.mp3"
                                    show jescg spank4 
                                    camera at camera_shake
                                    "BOFETA!!!!"
                                    camera at reset

                                    jes "¡NGH! ¡¡GHHH!! ¡¡¡NHHHHHH!!!"

                                    show jescg spank6 with dissolve
                                    stop music fadeout 2.0
                                    menu:
                                        "AGAIN":
                                            play sound "glitch.mp3" 
                                            show glitch2 jesspank
                                            "!!!!!"
                                            show jescg spank7 
                                            hide glitch2 jesspank
                                            "¿Qué... qué acaba de pasar?"
                                            "Por un breve momento... me sentí extrañamente ligero."
                                            "Cuando escuché a alguien llorar, me di cuenta de que era Jestyn."

                                            jes ".... sollozo.... sollozo...."

                                            "Oh no... ¡¿Qué he hecho?!"
                                            show jescg spank8 with dissolve
                                            "Rápidamente saqué el trozo de pan de la boca de Jestyn."
                                            play music "date.mp3" volume 3.0 fadein 3.0
                                            mc "¡JESTÍN! ¡Lo siento mucho! ¡Realmente lo soy! ¡¿Estás bien?!"
                                            
                                            "Pero Jestyn no pareció escucharme."
                                            
                                            mc "Jestyn... oye... lo siento... fui demasiado lejos..."
                                            show jescg spank9 with dissolve
                                            "Suavemente acaricié su mejilla, esperando que eso lo reconfortara, aunque fuera un poco."
                                            "Por fin, Jestyn me miró."
                                            
                                            jes "...sollozo... Su Majestad... Lo siento..."
                                            mc "No, no, no. Soy yo quien debería disculparse. Lo llevé demasiado lejos, ¿vale?"
                                            show jescg spank10 with dissolve
                                            jes "...Eje... Está bien..."
                                            jes "...me gustó..."
                                            show jescg spank11 with dissolve
                                            jes "...Aunque, por un momento... pensé que Su Majestad..."
                                            
                                            "Jestyn se detuvo antes de que pudiera terminar."
                                            show jescg spank12 with dissolve
                                            jes "...No es nada, jeje... No se preocupe, Su Majestad..."
                                            

                        "eso es suficiente":
                            "Creo que es suficiente."
                            "Acaricié suavemente el trasero de Jestyn nuevamente."
                            show jescg spank5 with dissolve
                            jes "Mnh... nh..."
                            
                            "Finalmente le saqué el trozo de pan de la boca, permitiéndole hablar."
                            show jescg spank10 with dissolve
                            jes "Hahh... hahh... S-Su Majestad..."
                            mc "¿Has aprendido la lección?"
                            
                            "Jestyn asintió."
                            
                            mc "¿Entonces qué dices?"
                            jes "Lo-lo siento, Su Majestad... me equivoqué..."
                            mc "Buen chico."
                            
                            "Le acaricié suavemente la cabeza y Jestyn prácticamente se derritió bajo los elogios, pareciendo genuinamente feliz con el afecto que le di."

                "eso es suficiente":
                    "Creo que es suficiente."
                    "Acaricié suavemente el trasero de Jestyn nuevamente."
                    show jescg spank5 with dissolve
                    jes "Mnh... nh..."
                    
                    "Finalmente le saqué el trozo de pan de la boca, permitiéndole hablar."
                    show jescg spank10 with dissolve
                    jes "Hahh... hahh... S-Su Majestad..."
                    mc "¿Has aprendido la lección?"
                    
                    "Jestyn asintió."
                    
                    mc "¿Entonces qué dices?"
                    jes "Lo-lo siento, Su Majestad... me equivoqué..."
                    mc "Buen chico."
                    
                    "Le acaricié suavemente la cabeza y Jestyn prácticamente se derritió bajo los elogios, pareciendo genuinamente feliz con el afecto que le di."
            
    hide jescg with dissolve
    show jes dinner love with dissolve
    jes "...Jeje... Hora del plato principal, Su Majestad."
    
                                                                                                                      
    "Jestyn tomó el plato principal. Un filete servido con puré de patatas."
    "Pude ver sus manos temblar de anticipación."
    
    show jes dinner normal2 with dissolve
    jes "El plato principal fue un bistec con salsa BBQ, servido junto con una generosa ración de puré de patatas."
    show jes dinner love with dissolve
    jes "Por favor, disfrute su comida, Su Majestad... O tal vez... ¿Le gustaría Su Majestad que yo le dé de comer en su lugar~?"
    
    "Lo pensé por un momento. Eso... no fue tan mala idea."
    
    show jes dinner horny with dissolve
    jes "...Con mi boca."
    mc "......"

    "Puedo sentir mis mejillas calentarse. Maldita sea. Hace mucho calor."
    "Odio el hecho de que no estoy en contra de esa idea."
    mc "Entonces continúa... Dame de comer, mi bufón."
    jes "...Como Usted ordene, Su Majestad."
    
    show jescg meat with dissolve
    "Jestyn tomó un trozo de filete con la boca y se inclinó hacia mí."
    "Mordí el otro extremo."
    "Sabía a carne de res asada con una rica salsa barbacoa, aunque los sabores eran mucho más profundos, con capas de hierbas aromáticas y especias. Estaba delicioso."
    "Pero más que la comida en sí... lo que me cautivó fue ver a Jestyn someterse tan obedientemente."

    show jesmeat2 with dissolve
    "Le di otro mordisco."
    "Nuestros labios casi se rozaron, haciendo que Jestyn dejara escapar un suspiro tembloroso."
    "Con un gemido suave y desesperado, empujó el trozo restante de filete hacia mí, pidiéndome en silencio que lo terminara."
    "Se está volviendo necesitado, ¿no?"
    
    mc "No, Jestyn. Los buenos chicos saben comportarse, ¿no?"
    
    "Se quedó paralizado por un segundo, antes de eso asintió levemente en señal de comprensión."

    hide jescg meat with dissolve
    hide jesmeat2 with dissolve
    "Acaricié suavemente su mejilla. Jestyn cerró los ojos y se inclinó hacia mi tacto."
    "Amaba cada segundo."
    "Verlo volverse tan obediente, casi como un cachorrito leal, fue inesperadamente adorable. No pude evitar sentir una suave calidez florecer dentro de mi pecho."

    show jes dinner love with dissolve
    $ voice_duck_start()
    voice "JESTYN03_DAY2.ogg"
    jes ".... ¿Soy un buen chico, Su Majestad...?" 
    $ voice_duck_end()
    mc "Sí. Has sido un buen chico, Jestyn."
    show jes dinner horny with dissolve
    jes "Ahora bien, este bufón ha sido un buen tonto para Su Majestad. Seguramente eso me hace ganar una recompensa, ¿no?"
    mc ".... ¿Una recompensa?"
    jes "Mmm..."
    
    "Jestyn asintió con entusiasmo."
    "Ah si... una recompensa así es..."
    "Me incliné y tomé el último trozo de filete de entre sus labios."
    show jes dinner love2 with dissolve
    "Por un breve momento, mi lengua rozó la suya mientras la tomaba."
    "Era suave... suave... inconfundiblemente cálido."
    "Dejó escapar otro gemido necesitado."
    
    show jes dinner pout with dissolve
    jes "Su Majestad... ¿por qué... por qué fue sólo por un momento...?"
    mc "¿Qué pasa? ¿No fue esa recompensa suficiente?"

    "Se movió inquieto por un momento antes de asentir tímidamente."

    jes "Mmmnh... este bufón es terriblemente codicioso, ¿no es así, Su Majestad? Una sola gota de dulce miel nunca podría satisfacerme..."
    
    "Jestyn hace una pausa por un momento."
    
    show jes dinner horny with dissolve
    jes "¿Eso significa... que este bufón debe ofrecer una pieza de oro... algo mucho más precioso... si desea ganar más que una sola gota de miel de Su Majestad?"
    
    "Aunque nunca lo dice abiertamente, Jestyn está insinuando claramente que podría pedirle que me dé algo más..."
    "Algo digno de una recompensa mayor."
    "Ya veo."

    mc "¿Y qué has hecho exactamente para merecer algo más?"
    show jes dinner suprais2 with dissolve
    jes "¡Yo-yo...!"
    show jes dinner love with dissolve
    jes "Su humilde bufón haría cualquier cosa que Su Majestad me pida."
    show jes dinner giggle3 with dissolve
    jes "Sólo... dame la atención de Su Majestad... te prometo que me comportaré..."
    mc "Mmm..."

    "Cogí un trozo de carne y lo sostuve entre mis labios."
    "Luego se lo ofrecí a Jestyn."
    
    show jes dinner suprais2 with dissolve
    jes "Su... Su Majestad... eso es..."
    
    "Los ojos de Jestyn se abrieron y no pudo reprimir la sonrisa que se extendía por su rostro, llena de anticipación."
    "Pero al ver mi impaciencia, Jestyn se inclinó lentamente."
    
    show jes dinner horny with dissolve
    jes "Entonces... si me disculpan..."
    
    hide jes dinner horny with dissolve
    "Jestyn mordió suavemente el extremo opuesto del trozo de carne que tenía entre mis labios."
    "Me di cuenta de que no estaba prestando atención a la carne en sí ni a su sabor."
    "Sus ojos nunca dejaron los míos mientras tomaba bocados lentos y deliberados, como si saboreara el momento mucho más que la comida."
    "Nuestros ojos permanecieron fijos el uno en el otro."
    "Por mucho que intenté actuar como un dom experimentado, no pude evitar que el calor subiera a mis mejillas o los frenéticos latidos de mi corazón."
    "Su mirada me estaba haciendo sonrojar. Aun así, hice todo lo que pude para no fallar."
    "Después de tragar, Jestyn dio otro mordisco, sin romper ni una sola vez el contacto visual."
    "En este punto, pensé que iba a perder la cabeza."
    "Lo que me tomó completamente desprevenido fue cuando dejó de intentar morder el trozo de carne restante."
    "En cambio, lentamente pasó su lengua a lo largo de su punta... lentamente... deliberadamente... centímetro a centímetro, su lengua trazó su camino hacia arriba."
    "Mi mente luchó por procesar lo que estaba haciendo hasta que una suave sensación rozó mi labio inferior."
    "La lengua de Jestyn había llegado a mis labios, rozando suavemente mi labio inferior con movimientos lentos y deliberados."
    "Sorprendida, rápidamente me aparté de Jestyn."
    "Y mi cara se sonrojó incontrolablemente."
    
    mc "Jestyn, ¿qué estás-?"
    
    "Jestyn simplemente se rió de mi reacción."
    
    show jes dinner horny with dissolve
    jes "Mmmh~ Te ves muy sexy cuando intentas dominarme, Su Majestad..."
    show jes dinner giggle3 with dissolve
    jes "Pero esta pequeña alma mía, salvaje y traviesa... es como tratar de mantener a un mono atado. Simplemente no puedo evitarlo."
    jes "Y parece que, después de todo, Su Majestad no es más que una oveja vestida de lobo. Jaja ~"
    
    "Lo dijo con una inconfundible sonrisa burlona."
    "Si no conociera a Jestyn tan bien como lo sabía, podría haber tomado esas palabras al pie de la letra."
    "Pero yo lo sabía mejor. Incluso ahora, sólo estaba tratando de provocarme. Sinceramente... fue casi impresionante."
    
    mc "Jestyn, ¿pensé que querías una recompensa?"
    show jes dinner smirk with dissolve
    jes "Oh, ciertamente lo hago~ Pero como dije... simplemente no puedo evitar ser... travieso."
    jes "Especialmente... cuando se trata de Su Majestad. Jejeje~"

    "Entonces... todavía quería actuar como un mocoso."
    "Algo me dijo que necesitaba hacerlo un poco más obediente."
    "Y creo que la creatividad me golpeó la cabeza."

    mc "Creo que es hora del postre, ¿no?"
    show jes dinner normal2 with dissolve
    jes "Sí, lo es... hora del postre, Su Majestad."
    
    "Cogió un trozo de pastel de chocolate cubierto con mermelada de fresa. Y me ofreció el pastel."
    
    mc "Jestyn... Creo que deberías probarlo primero."
    show jes dinner nosmiletalk with dissolve
    jes "¿Mmm? ¿Y por qué podría ser eso, Su Majestad?"

    "Levanté suavemente su barbilla antes de acariciarla suavemente."
    camera at camera_shake
    show jes dinner suprais2 
    "Se sobresaltó por mi movimiento repentino."
    camera at reset
    "Froté un poco de mermelada de fresa de la parte superior del pastel en la punta de mi dedo y luego se lo tendí."
    "Jestyn parpadeó y se tomó un momento para procesar lo que estaba haciendo. Entonces se le escapó una risa cómplice."
    
    show jes dinner giggle3 with dissolve
    jes "Dios mío... Parece que Su Majestad ha empezado a comprender bastante bien a este humilde bufón."
    jes "Ahora bien, ¿cómo podría rechazar una ofrenda tan generosa de la Corona?"
    mc "Entonces abre la boca..."
    
    "Mis dedos viajaron más alto. Lentamente subí hasta sus labios hasta que lentamente deslicé uno en su boca."
    show jescg lick with dissolve
    "Jestyn me agarró suavemente la muñeca y probó la mermelada de fresa con la yema del dedo."
    "La lengua de Jestyn lamió lentamente la mermelada de fresa de mi dedo índice. Sus movimientos eran lentos y cuidadosos."
    "Durante todo ese tiempo, sus brillantes ojos rojos nunca dejaron los míos."
    show jescg lick2 with dissolve
    "Notó mi expresión sonrojada y su sonrisa se amplió con satisfacción."
    "Como si quisiera ver más de mi reacción, Jestyn ralentizó aún más sus movimientos, haciendo que cada movimiento fuera más deliberado y provocativo."
    "Maldita sea… de alguna manera, solo logró hacer que mis mejillas ardieran aún más y dejarme aún más nerviosa."
    "Mi reacción sólo pareció alimentar su ego."
    "Uf... tenía que recordar que yo era el que estaba a cargo aquí. No iba a dejar que tomara el control cuando quisiera."
    "¿Pero qué se suponía que debía hacer...?"
    "...."
    camera at camera_shake
    show jescg lick3
    "Ni siquiera sé qué me pasó. Por impulso, agarré su lengua."
    camera at reset
    "Y Jestyn inmediatamente dejó escapar un grito de sorpresa."
    "Lo sentí suave y aterciopelado bajo mis dedos."
    "Su lengua era negra, pero no se sentía diferente a la de un humano... aparte de su color inusual."
    show jescg lick4 with dissolve
    "Él comienza a gemir por la sensación."
    
    jes "A-Ah... hnn... ja... S-Su... Majestad..."
    jes "P-Podría... puedo... nnh..."
    mc "¿Puedes qué?"
    jes "...quiero..."
    jes "...para lamer el brazo de Su Majestad."

    "Me congelé ante la petición de Jestyn. Era lo último que esperaba escuchar."
    "Podía sentir mis mejillas calentarse, pero..."

    menu:
        "Yes":
            mc "Mmm... Creo que te lo mereces, Jestyn. Seguir."

            "Le di permiso."
            show jescg lick6 with dissolve
            "La lengua de Jestyn se extendió lentamente, curvándose suavemente alrededor de mi brazo."
            "Me estremecí de sorpresa. No esperaba que su lengua se estirara tanto."
            "Se deslizó lenta y sensualmente a lo largo de mi piel, la sensación era extrañamente cosquilleante, casi como el toque de un tentáculo."
            "Mi mano libre encontró su mejilla, acariciándola suavemente mientras él instintivamente se inclinaba hacia mi palma una vez más mientras yo continuaba acariciando su lengua."
            "Con solo mirarlo, era obvio lo abrumado que estaba. Su cuerpo temblaba, su rostro estaba sonrojado y húmedo de sudor, y su respiración se hacía entrecortada y irregular."
            
        "No":
            mc "No, Jestyn. Necesito disciplinarte. Ten un poco más de paciencia y te recompensaré con algo más."
            jes "Hnnnhhh~...."

            "¿Qué pasaría si presionara su lengua?"
            "La curiosidad se apoderó de mí y presioné suavemente la lengua de Jestyn."
            show jescg lick5 with dissolve
            jes "Hnngghh-h-ahh..."
            
            "La reacción de Jestyn se sintió como una luz verde, así que continué, frotando su lengua un poco más firmemente."
            
            jes "Ahh- y-tu-... ah-"

            "Mi mano libre encontró su mejilla, acariciándola suavemente mientras él instintivamente se inclinaba hacia mi palma una vez más mientras yo continuaba acariciando su lengua."
            "Con solo mirarlo, era obvio lo abrumado que estaba. Su cuerpo temblaba, su rostro estaba sonrojado y húmedo de sudor, y su respiración se hacía entrecortada y irregular."
            
    "Después de un rato, finalmente retiré mi dedo de su boca, permitiendo que Jestyn recuperara el aliento."
    hide jescg lick with dissolve
    show jes dinner giggle3 with dissolve
    jes "Ja... ja..."
    
    "Estabilizó su respiración y se tomó unos momentos para recomponerse antes de mirarme con una sonrisa descarada."
    show jes dinner horny with dissolve
    jes "...Él... jeje... Su Majestad se está volviendo notablemente hábil en esto..."
    
    mc "¿Bueno?"
    
    "Jestyn asintió, todavía luciendo un poco aturdido por el momento que acabábamos de compartir."
    "Me acerqué y le revolví suavemente el pelo."
    
    mc "Has sido un buen chico, Jestyn."
    jes "Mmh... Gracias, Su Majestad..."
    mc "Bebe algo."
    jes "...No necesito beber, Su Majestad..."

    mc "Esa es una orden, Jestyn. Sé que no lo necesitas, pero tal vez te ayude a aclarar tu mente."
            
    "Aunque sabía que había dicho que no tenía ningún efecto real en los de su especie."
            
    mc "... ¿O planeas desobedecerme otra vez?"
    show jes dinner pout2 with dissolve
    jes "Mmmhh..."
    hide jes dinner pout2 with dissolve
    "A mi orden, Jestyn tomó el vaso de agua y se lo bebió."

    mc "¿Se siente mejor?"
    show jes dinner love with dissolve
    jes "...Sí..."
    mc "......"
    mc "Lo siento, Jestyn... Creo que fui demasiado duro antes. Realmente no estaba pensando."
    
    "Jestyn simplemente se rió."
    
    show jes dinner smirk with dissolve
    jes "¿Por qué se disculpa, Su Majestad? Lo que hiciste no fue nada comparado con lo que ha soportado este pobre bufón."
    jes "Todavía es como un pequeño novato dando sus primeros pasos, Su Majestad. Jeje... ¿Seguramente no pensaste que te volverías tan hábil de la noche a la mañana~?"
    mc "...Estoy tratando de ser amable aquí y tú me lo pagas con insultos. Impresionante."

    show jes dinner giggle2 with dissolve
    jes "¡Jajaja! Su Majestad simplemente tendrá que acostumbrarse a la burla de este bufón~"

    jump end_repeat_route

label let_it_slide:
    $ domjes = True
    "...Él realmente es molesto y realmente quiero castigar a Jestyn."
    "Pero, por otro lado, no estoy de humor para jugar."
    
    mc "Tienes suerte, Jestyn. No estoy de humor para castigarte."
    
    show jes dinner pout with dissolve
    "La sonrisa de Jestyn lentamente se convirtió en un puchero."
    
    jes "....¿Suerte? Oh, Su Majestad... Me temo que tenemos definiciones muy diferentes de esa palabra."
    mc "Sí, lo sé. Pero aún así."
    show jes dinner giggle with dissolve
    jes "Jeje, por supuesto, Su Majestad. Nunca se me ocurriría obligarte a castigarme."
    jes "Pero si ese es el caso... entonces supongo que simplemente tendré que hacer un desempeño aún mejor y trabajar un poco más duro para conseguir lo que quiero."
    
    "Así que debería prepararme para lo que venga después, ¿eh...? Maravilloso."
    "Continué comiendo mi pan."
    show jes dinner normal
    "Jestyn no me quita los ojos de encima ni una sola vez. Él tampoco dice una palabra."
    "¿De qué podría hablar...?"
    "Mis ojos vagan por la habitación, buscando algo que pueda contarle, hasta que finalmente se posan en su ropa."
    "......"
    "Ahora que lo pienso, probablemente podría preguntarle sobre su ropa."

    mc "Tu ropa se ve genial. Pareces un rey."
    
    show jes dinner suprais
    "Noté que Jestyn de repente se congeló por un momento."

    jes "......."
    jes "¿En serio?"
    mc "Sí. Te conviene. Te ves elegante."
    
    "Sé que felicitarlo así probablemente solo lo hará aún más orgulloso de sí mismo, pero ahora mismo, solo quiero decir lo que tengo en mente."
    show jes dinner love with dissolve
    "Pero sorprendentemente, en lugar de alardear como esperaba, desvió ligeramente la mirada."
    "Y pude ver sus mejillas ponerse rojas."
    "... ¿Está avergonzado?"
    
    jes "...Qué dulces palabras, Su Majestad... Incluso el corazón de este bufón se derrite al oírlas."
    
    "Eh... Para que pueda avergonzarse después de todo. Eso es inesperado."
    
    mc "Tengo curiosidad. ¿Qué sueles usar con ese outfit?"
    show jes dinner nosmile2 
    jes "¿Mmm? ¿Qué significa Su Majestad?"
    mc "Quiero decir, eres un bufón títere. Así que esperaría que solo tuvieras trajes de bufón."
    mc "Pero lo que llevas puesto no parece en absoluto un traje de bufón. Pareces más un noble."
    show jes dinner nosmile
    jes ".........."
    
    "Jestyn se queda en silencio por un momento. Parece perdido en sus pensamientos."
    "¿Dije algo mal?"
    "Antes de que pueda preguntar, Jestyn sale de sus pensamientos y me da su sonrisa habitual."

    jes "Mmm... en realidad, no es realmente un traje para nada. Es sólo una ropa vieja que no he usado en mucho tiempo."
    show jes dinner sad
    jes "Solía usarlo cuando el teatro todavía estaba en funcionamiento. Hubo un tiempo en el que usaba esta ropa con bastante frecuencia. Entonces... puedes imaginar cuántos años tienen."
    jes "Y... bueno, me los quedé porque supongo que pensé que ya no serían necesarios....."
    
    "La voz de Jestyn se vuelve más pesada con cada palabra."
    
    mc "...Ya veo."
    mc "......"
    mc "¿Pero te gustó usarlos?"
    
    show jes dinner suprais
    "Los ojos de Jestyn se abren mientras me mira, ligeramente sorprendido por mi pregunta."
    
    jes "....¿Me gustaron...?"
    mc "Sí. No sé por qué dejaste de usarlos. ¿Pero te gustó usarlos?"
    show jes dinner nosmile with dissolve
    jes "Mmmm....."
    
    "Los ojos de Jestyn se dirigen lentamente hacia la mesa."
    
    jes "........Sí. Hice."
    jes "Pero supongo que es un sentimiento de hace mucho tiempo. Ya no siento lo mismo por ellos."
    show jes dinner sad
    jes "Se siente... incómodo."

    "El ceño de Jestyn se frunce, la incomodidad evidente en su rostro mientras habla de su ropa."
    "Quiero preguntar qué es exactamente lo que lo hace sentir tan incómodo. Pero dudo. No quiero hacerlo sentir aún peor."
    show jes dinner nosmile with dissolve
    "Los ojos de Jestyn se alejan de la mesa y regresan a mí. En el momento en que nuestras miradas se encuentran, el surco de su frente desaparece."
    
    jes ".......Y aún así, Su Majestad me hace querer usarlos de nuevo."
    show jes dinner love2 with dissolve
    jes "Yo... quería impresionarte. Así que decidí volver a ponerme esta ropa."
    jes "La incomodidad sigue ahí, persistiendo en mi corazón... pero de alguna manera, todo parece desvanecerse cuando veo tu reacción."
    jes "Y sí... supongo que todo valió la pena."
    
    "La sonrisa de Jestyn regresa y se hace más amplia."
    "Ver a Jestyn soportar voluntariamente esa incomodidad sólo por mí hace que mi corazón se acelere."
    "Uf, en serio... este títere..."
    
    mc "Mhh... sí... Realmente te ves genial. Tal como dije."
    
    show jes dinner horny with dissolve
    "Él asiente, luciendo satisfecho."
    
    show jes dinner normal with dissolve
    jes "Eso me hace muy feliz, Su Majestad..."

    "Antes de darme cuenta, ya me he comido todo el pan de mi plato."
    
    jes "Mmm... Creo que es hora de pasar al plato principal, Su Majestad."
    
    show jes dinner normal2 
    "Jestyn luego chasquea los dedos. En un instante, mi plato vacío es reemplazado por uno lleno de rebanadas de carne asada, generosamente cubiertas con salsa BBQ."
    
    jes "Por favor, disfrute, Su Majestad. No me hagas caso."
    show jes dinner smirk 
    jes "Ese pobre estómago tuyo merece probar de vez en cuando una rica carne asada."
    
    "Qué bastardo más descarado."
    "Pero no se equivoca. Sólo mirarlo es suficiente para hacer que mi estómago retumbe. No puedo esperar para probarlo."
    show jes dinner normal with dissolve
    "Sin pensarlo más, tomo un trozo de carne con el tenedor y me lo meto en la boca."
    "El sabor es muy rico en especias. La salsa BBQ estalla en mi paladar, cubriendo mi lengua con su dulzura ahumada y sabrosa."
    "La carne en sí es espesa, pero maravillosamente tierna."
    "Quien haya cocinado esto realmente sabía lo que estaba haciendo."
    "Al verme devorar la carne, Jestyn sólo pudo sonreír ampliamente, luciendo bastante satisfecho consigo mismo."
    
    jes "¿Bueno?"
    
    "Asiento sin pensarlo dos veces."
    
    mc "¡Sí!"
    
    show jes dinner smirk
    "Jestyn deja escapar una risa silenciosa ante mi entusiasta respuesta."
    
    jes "Si quieres un poco más, solo di la palabra."
    mc "Espera, ¿puedes hacer más?"
    
    play sound "snap.mp3"
    show jes dinner normal2
    "Jestyn no se molesta en contestar. Simplemente chasquea los dedos."
    "La carne que casi se había acabado, la mayor parte de la cual ya comí, se repone de repente."
    
    mc "¿Todavía tenías más??? ¿De dónde lo conseguiste?"
    show jes dinner normal 
    jes "Compré el doble, por si Su Majestad quisiera unos segundos. Y parece que mis instintos estaban en lo cierto, ¿eh?"
    jes "Además, parecías hambriento."
    
    "Inmediatamente me siento avergonzado."
    "¿Era realmente tan obvio?"
    "Bueno... como fideos instantáneos con bastante frecuencia..."
    
    show jes dinner nosmile
    jes "No, no. No pareces alguien que se esté muriendo de hambre. Más bien como alguien que no ha dormido lo suficiente."
    jes "Pero comer fideos instantáneos todos los días no es saludable, Majestad."
    jes "Aún así, no puedo culparte exactamente por ello. A veces, las circunstancias nos dejan sin otra opción que hacer cosas que realmente no deseamos hacer."
    jes "Es una sensación desagradable, ¿no? Cuando las circunstancias te obligan a hacer algo que nunca quisiste hacer."
    mc "...Sí...."

    "....."
    "Espera, ¿cómo supo que como fideos con frecuencia? Nunca se lo dije, ¿verdad?"
    "O tal vez simplemente lo olvidé..."
    show jes dinner normal with dissolve
    "Jestyn suspiró suavemente ante mi respuesta."
    
    jes "Pero está bien, Su Majestad. Estoy aquí ahora, ¿no?"
    jes "Lo que significa que ya no estás solo."
    jes "Y también significa que hay alguien aquí que se preocupará sinceramente por ti... y te mantendrá a salvo."
    
    "La voz de Jestyn no era como siempre. Suena más profundo, más suave."
    "Se siente... reconfortante."
    "La idea de tener a alguien que pueda protegerte de la crueldad del mundo se siente como estar envuelto en algo cálido en medio de un viento frío."
    
    mc "Pero no eres más que una marioneta... Quiero decir, somos diferentes."
    jes "Es sólo su propia mente la que limita las posibilidades, Su Majestad."
    show jes dinner smirk2 with dissolve
    jes "Quizás parezca nada más que un títere común y corriente, aunque bastante alto. Pero créame... puedo hacer mucho más que eso."
    jes "Mucho más de lo que la razón humana jamás podría comprender."

    "Los ojos de Jestyn se posaron en la carne que aún no había terminado."
    
    show jes dinner normal with dissolve
    jes "Continúe, Su Majestad. Sigue comiendo."
    jes "Termínalo."
    
    "Quería seguir comiendo."
    "Pero por alguna razón, mi mano se sentía extrañamente pesada cuando intenté levantarla, aunque sabía que podía hacerlo."
    
    jes "O... ¿Su Majestad preferiría que yo le diera de comer?"
    mc "Yo....."
    
    "Mi corazón late contra mi pecho. Duro. Demasiado duro."
    
    mc "...yo...lo haría..."
    
    show jes dinner smirk2 with dissolve
    "Jestyn dejó escapar una risa tranquila y cómplice ante mi vacilación. Sin decir más, tomó suavemente el tenedor de mi mano."
    
    jes "Ahí estamos. Simplemente podrías habérmelo dicho."
    jes "No es necesario que te pongas las cosas difíciles."
    
    "Jestyn pinchó un trozo de carne con el tenedor y lentamente lo acercó a mi boca."
    
    show jes dinner normal2 with dissolve
    jes "Ahora... abre."
    
    "Mis labios se separaron antes de que me diera cuenta de lo que estaba haciendo."
    "No había sido mi intención obedecerle."
    "Simplemente... lo hice."
    
    jes "Bien."
    
    "Su sonrisa se amplía ligeramente."
    
    jes "¿Ver? Eso no fue tan difícil, ¿verdad?"
    jes "Ahora, ¿quieres otro?"
    
    "Asiento."
    "Jestyn tomó otro trozo de carne."
    "Y lo metí en mi boca."
    "Una y otra vez..."
    "Hasta que no quedó ni un solo trozo de carne en el plato."
    
    jes "¿Quieres un poco más?"
    
    "Sacudí la cabeza, sintiéndome completamente llena."
    
    show jes dinner horny with dissolve
    jes "Terminaste todo. Estoy orgulloso de ti."
    
    "Jestyn luego tomó una servilleta que estaba a mi lado y me limpió suavemente la boca."
    
    show jes dinner normal with dissolve
    jes "¿Aún tienes espacio para el postre?"
    mc "Mhh... No lo creo... Comí bastante carne."
    jes "Luego podrás llevarte el postre a tu apartamento y disfrutarlo más tarde."
    jes "¿Cómo suena eso?"
    mc "Suena como una buena idea...."
    
    "Comer una comida tan lujosa en mi pequeño y destartalado apartamento... Supongo que sería toda una experiencia."
    show jes dinner normal2
    pause 0.5

    jump end_repeat_route




label end_repeat_route:

    stop music fadeout 3.0
    play sound "snap.mp3" volume 3.0
    camera at camera_shake
    scene bg_office
    hide jes dinner
    "Jestyn chasqueó los dedos. En un instante, los dos estábamos de regreso en el dormitorio de mi oficina."
    camera at reset
    "Se sentó en mi cama, se quitó la bata y se dejó caer el cabello. Mechones suaves y ondulados enmarcaban maravillosamente su rostro."
    
    jes "......"
    jes "...Su Majestad..."
    mc "¿Mmm? ¿Qué es?"
    
    "Jestyn lentamente abrió los brazos."
    
    jes "...... ¿Abrazo...?"
    
    "..."
    "¿Cómo se suponía que iba a decirle que no a esa cara? Además, Jestyn parecía exhausto."
    show jessidecg hug with dissolve
    "Entonces me acerqué. En el momento en que estuve a su alcance, envolvió sus brazos alrededor de mi cintura y suavemente me abrazó."
    
    mc "......"
    mc "¿Estás cansado, Jestyn?"
    jes "...Mmmm..."
    jes "Un poco..."
    jes "......"
    show jessidecg hug2 with dissolve
    jes "...¿Que este humilde bufón descanse en el regazo de Su Majestad?"
    mc "Por supuesto."
    hide jessidecg hug2 with dissolve
    "Jestyn se acostó con cuidado, apoyando su cabeza en mi regazo."
    show jescg sleep with dissolve
    jes "...Aunque debo confesar..."

    if subjes :
        jes "...Me gustó aún más la forma en que Su Majestad jugó conmigo."
        jes "La forma en que me trataste... como si fuera tu juguete más preciado..."
        jes "...Hizo que este tonto bufón se sintiera verdaderamente precioso."
        show jescg sleep2 with dissolve
        jes "...Soy más feliz cuando estoy contigo."

    else :
        jes "Es usted tan obediente, Su Majestad. Tan inocente, tan pura, tan gentil."
        jes "Como un conejito perdido, simplemente siguiéndote dondequiera que te lleve."
        jes "Me hace sentir aún más protector contigo que antes."
        jes "Y supongo que así es exactamente como debería ser. Después de todo... es por la seguridad de Su Majestad."

    "Mi corazón latía tan fuerte que parecía un tambor. Jestyn de repente se había vuelto tan... descaradamente dulce."
    "Por otra parte... ¿por qué me sorprendió tanto? Este era Jestyn. El títere más impredecible del teatro."
    "...Aun así, no pude evitar que me tomaran con la guardia baja."
    "Mientras lo observaba, sus párpados gradualmente se volvieron más pesados. Su mirada se suavizó por el sueño."
    
    mc "Tienes sueño, ¿verdad, Jestyn?"
    show jescg sleep3 with dissolve
    "Él asintió lentamente y adormilado."
    "Sus brazos se deslizaron perezosamente alrededor de mi cintura, sosteniéndome suavemente en mi lugar."
    "Probablemente estaba exhausto después de todo lo que había sucedido antes. Es comprensible que así sea."
    "Acaricié suavemente el cabello de Jestyn. Parecía disfrutar cada segundo."
    
    jes "...Su Majestad todavía estará aquí cuando despierte... ¿no es así?"
    mc "¿Cómo se supone que voy a irme cuando estás acostada encima de mí así?"
    jes "Jeje... bastante cierto..."
    jes "...Entonces... buenas noches, Su Majestad..."
    mc "...Buenas noches, Jestyn."
    show jescg sleep4 with dissolve
    "Jestyn cerró lentamente los ojos."
    hide jescg sleep4 with dissolve

    "......"
    "Todavía no podía creer que hubiera hecho todo eso voluntariamente. Al principio, había estado completamente fuera de mi elemento... pero poco a poco, este títere de alguna manera lo había hecho sentir casi natural."
    "Seguí distraídamente acariciando el cabello de Jestyn cuando de repente mi teléfono vibró con una notificación."
    "... Ah. Jefe."
    "No esperaba tener noticias de ellos hoy. El mensaje decía que mi primer cheque de pago ya había sido transferido."
    
    mc "Eh... No esperaba que me pagaran tan pronto. Sólo llevo dos días trabajando aquí."
    
    "Supongo que podrías llamarlo una bonificación."
    
    mc "...Mi jefe es sorprendentemente generoso... A este ritmo, tal vez disfrute trabajando aquí."
    
    "El sueldo fue suficiente para cubrir mis deudas y mis gastos de manutención por un tiempo. Nada mal."
    "Miré el reloj. Era sólo medianoche."
    "Todavía quedaban unas seis horas antes de que terminara mi turno... Ya terminé todo mi trabajo... entonces, ¿qué se supone que debo hacer ahora?"
    "Veamos..."
    "Hoy aprendí que todos los títeres de este teatro están vivos. También conocí varios títeres nuevos. Juro que no estoy perdiendo la cabeza y sigo negando que estos títeres no estén vivos."

    if crownus_wizzy:
        "Y... aprendí un poco sobre el Rey Marioneta."
        "A juzgar por lo que Wizzy dijo antes... el Rey Puppet no parecía una buena persona."
        "Si eso es cierto... entonces tal vez su muerte realmente fue lo mejor."
        "Después de todo... la gente cruel no merece vivir."
        "...Mi vida probablemente también sería mejor sin gente así."

    mc "Olvídalo. En lugar de pensar demasiado en todo esto... debería simplemente jugar un juego para pasar el tiempo."
    
    "Cogí mi teléfono y comencé a jugar."
    "Hoy nada me había asustado realmente. Quizás finalmente me estaba acostumbrando a este lugar."
    "Mañana... probablemente estaría aún más acostumbrado."
    stop music fadeout 2.0
    scene black with dissolve

    window hide
    $ quick_menu = False
    
    scene black
    with fade

    $ repeat_route += 1

    if repeat_route == 1:
        voice "CROWNUS06_DAY2.ogg"
        show text "{size=80}{cps=15}{color=#EEC594}¿Estás seguro?{/color}{/cps}{/size}" at nightmare_text
        with dissolve
        pause 3.5
        
        hide text
        
        voice "CROWNUS07_DAY2.ogg"
        show text "{size=90}{cps=15}{color=#EEC594}... Oh, pequeña majestad...{/color}{/cps}{/size}" at nightmare_text
        with dissolve
        pause 3.5
        
        hide text
        
        voice "CROWNUS08_DAY2.ogg"
        show text "{size=90}{cps=15}{color=#EEC594}La curiosidad puede ser algo tan peligroso..{/color}{/cps}{/size}" at nightmare_text
        with dissolve
        pause 4.5
        
        voice "CROWNUS09_DAY2.ogg"
        show text "{size=90}{cps=15}{color=#EEC594}Pero la ignorancia puede ser igual de mortal..{/color}{/cps}{/size}" at nightmare_text
        with dissolve
        pause 4.5
        
        voice "CROWNUS10_DAY2.ogg"
        show text "{size=90}{cps=15}{color=#EEC594}Tarde... o temprano..{/color}{/cps}{/size}" at nightmare_text
        with dissolve
        pause 3.5
        
        voice "CROWNUS11_DAY2.ogg"
        show text "{size=90}{cps=15}{color=#EEC594}Continúa... sé el conejito curioso que siempre debiste ser.{/color}{/cps}{/size}" at nightmare_text
        with dissolve
        pause 5.5
        
        voice "CROWNUS12_DAY2.ogg"
        show text "{size=110}{cps=15}{color=#EEC594}... entonces.....{/color}{/cps}{/size}" at nightmare_text
        with dissolve
        pause 2.5

    
    elif repeat_route == 3:
        show text "{size=80}{cps=15}{color=#EEC594}¿Todavía estás aquí? ¿En serio?{/color}{/cps}{/size}" at nightmare_text
        with dissolve
        pause 2.5
        
        hide text
        
        show text "{size=90}{cps=15}{color=#EEC594}...Sigh...{/color}{/cps}{/size}" at nightmare_text
        with dissolve
        pause 2.5
        
        hide text
        
        show text "{size=90}{cps=15}{color=#EEC594}Pequeña Majestad... eres aún más tonta de lo que pensaba.{/color}{/cps}{/size}" at nightmare_text
        with dissolve
        pause 2.5
        
        show text "{size=90}{cps=15}{color=#EEC594}Eso fue un cumplido, por cierto. Al menos para mí.{/color}{/cps}{/size}" at nightmare_text
        with dissolve
        pause 2.5
        
        show text "{size=90}{cps=15}{color=#EEC594}Eres bastante adorable cuando pareces tan despistado.{/color}{/cps}{/size}" at nightmare_text
        with dissolve
        pause 2.5
        
        show text "{size=90}{cps=15}{color=#EEC594}Pero no estoy de humor para mirar esa cara tonta tuya ahora mismo.{/color}{/cps}{/size}" at nightmare_text
        with dissolve
        pause 2.5
        
        show text "{size=110}{cps=15}{color=#EEC594}... entonces.....{/color}{/cps}{/size}" at nightmare_text
        with dissolve
        pause 2.5


    elif repeat_route == 2:
        show text "{size=80}{cps=15}{color=#EEC594}....{/color}{/cps}{/size}" at nightmare_text
        with dissolve
        pause 2.5
        
        hide text
        
        voice "CROWNUS13_DAY2.ogg"
        show text "{size=90}{cps=15}{color=#EEC594}Supongo que simplemente querías verme.{/color}{/cps}{/size}" at nightmare_text
        with dissolve
        pause 4.0
        
        hide text
        
        voice "CROWNUS14_DAY2.ogg"
        show text "{size=90}{cps=15}{color=#EEC594}¿Qué? ¿Esperabas que te insultara otra vez? ¿Te llama una pequeña mascota humilde y fea? {/color}{/cps}{/size}" at nightmare_text
        with dissolve
        pause 8.5
        
        voice "CROWNUS15_DAY2.ogg"
        show text "{size=90}{cps=15}{color=#EEC594}Jaja... no. No eres tan interesante.{/color}{/cps}{/size}" at nightmare_text
        with dissolve
        pause 7.5
        
        voice "CROWNUS16_DAY2.ogg"
        show text "{size=110}{cps=15}{color=#EEC594}Ahora vamos. Y termina tu tarea.{/color}{/cps}{/size}" at nightmare_text
        with dissolve
        pause 2.5

    elif repeat_route == 4:
        show text "{size=80}{cps=15}{color=#EEC594}Necesitado, ¿eh? Realmente tenías tantas ganas de verme. Esta ya es la cuarta vez. {/color}{/cps}{/size}" at nightmare_text
        with dissolve
        pause 2.5
        
        hide text
        
        show text "{size=90}{cps=15}{color=#EEC594}Casi me conmueve que estés dispuesto a pasar por todo eso sólo por tener la oportunidad de verme.{/color}{/cps}{/size}" at nightmare_text
        with dissolve
        pause 2.5
        
        hide text
        
        show text "{size=90}{cps=15}{color=#EEC594}Desafortunadamente, no te lo volveré a contar. Estoy ocupado.{/color}{/cps}{/size}" at nightmare_text
        with dissolve
        pause 2.5
        
        show text "{size=90}{cps=15}{color=#EEC594}Y ciertamente no estoy dispuesto a perder más de mi precioso tiempo sólo para ver una pequeña criatura fea como tú.{/color}{/cps}{/size}" at nightmare_text
        with dissolve
        pause 2.5
        
        show text "{size=90}{cps=15}{color=#EEC594}¡Ahora, shoo!{/color}{/cps}{/size}" at nightmare_text
        with dissolve
        pause 2.5

    elif repeat_route == 5:
        show text "{size=80}{cps=15}{color=#EEC594}.....Hhhhhhaaaaaaaahhhhhhhhhhhhh...... cariño.... {/color}{/cps}{/size}" at nightmare_text
        with dissolve
        pause 2.5
        
        hide text
        
        show text "{size=90}{cps=15}{color=#EEC594}Sé mi buena mascota y termina tu tarea, tonto.{/color}{/cps}{/size}" at nightmare_text
        with dissolve
        pause 2.5
        
        hide text

    elif repeat_route == 6:
        show text "{size=80}{cps=15}{color=#EEC594}Déjame en paz o no te llamaré más mi mascota. {/color}{/cps}{/size}" at nightmare_text
        with dissolve
        pause 2.5
        
        hide text
        
    elif repeat_route == 7:
        show text "{size=80}{cps=15}{color=#EEC594}Mira lo que tengo ~ ¡Oh! ¡Un hueso! Ahora ve allí. Coger algo. {/color}{/cps}{/size}" at nightmare_text
        with dissolve
        pause 2.5

        hide text

    else:
        show text "{size=80}{cps=15}{color=#EEC594}Hola, mi mascota fea. Tu dueño está cansado ahora mismo. Por favor, deja un masaje después del pitido. BIP. {/color}{/cps}{/size}" at nightmare_text
        with dissolve
        pause 2.5

        hide text

    call reset_chapter2 from _call_reset_chapter2
    

    jump kom_day2



label the_truth_route :
    stop music fadeout 3.0
    show jes normal2 with dissolve
    jes "Ahora bien, creo que este es un buen lugar para detenernos por hoy, Su Majestad."
    jes "Debes estar cansado."
    show jes bow with dissolve
    jes "Permítame acompañarle de regreso a su habitación."
    hide jes bow with dissolve
    
    "......"
    "Una parte de mí quería descansar."
    "Pero otra parte de mí insistía en que ahora no era el momento."
    "Había un sentimiento de inquietud persistiendo en el fondo de mi mente."
    "Algo en todo esto se negaba a sentarme bien."
    "¿Por qué tuve la sensación de que Jestyn ocultaba algo?"
    "Ese extraño sentimiento había comenzado en el momento en que se negó a dejarme entrar a la habitación del Rey Marioneta."

label letorno_jestynfollow:
    menu:
        "Deja que Jestyn te siga":
            jump repeat_route


        "No dejes que Jestyn te siga":
            jump jestynotfollow_day2

label jestynotfollow_day2:
    "......."
    "Tengo que descubrir qué está pasando realmente."
    "Salí de mis pensamientos y miré a Jestyn, que me estaba esperando pacientemente."
    "Pareció darse cuenta de que algo estaba en mi mente."
    
    show jes normal2 with dissolve
    jes "¿Hay algo que le preocupa, Su Majestad?"
    mc "...En realidad, estoy cansado de estar sentado en mi habitación."
    mc "Creo que necesito un poco de aire fresco para aclarar mi cabeza."
    mc "Así que voy a dar un paseo un rato."
    jes "En ese caso, permítame-"
    mc "Solo."
    
    play music "abandoned.mp3" volume 3.0 fadein 3.0
    show jes unimpress with dissolve
    "Jestyn se quedó en silencio."
    "Su ceño se frunció, haciendo evidente que no le gustaba la idea."
    
    jes "Su Majestad, respeto sus deseos..."
    show jes nosmile with dissolve
    jes "Pero vagar solo por el reino no es exactamente..."
    
    "Hizo una pausa, eligiendo sus palabras con cuidado."
    show jes nosmile2 with dissolve
    jes "Como tu bufón y tu mano derecha, es mi deber acompañarte dondequiera que vayas."
    show jes annoy with dissolve
    jes "¿Seguramente no eres tan ingenuo como para pensar que te dejaría vagar solo? Jaja..."
    
    "Trató de ocultar su inquietud detrás de una broma y un comentario burlón."
    
    mc "Y como tu gobernante, te ordeno que te tomes un descanso... y me dejes en paz."
    
    show jes creep with dissolve
    "La sonrisa en el rostro de Jestyn se volvió notablemente más tensa."
    "Su expresión se oscureció, haciendo evidente que estaba cada vez más disgustado."
    "Por primera vez, pude ver una irritación genuina asomando a su rostro." 
    
    jes "Hmph... Qué pequeño monarca más desagradecido he sido bendecido." 
    jes "Dejar de lado al tonto más leal... Qué trágico."
    
    "Sus palabras me tomaron completamente por sorpresa."
    "No esperaba que algo tan afilado... tan venenoso... saliera de su boca."
    "¿Por qué estaba tan decidido a no dejarme en paz?"
    "Algo no estaba bien."
    "Claramente no tenía intención de irse."
    "¿Qué se supone que debo hacer?"
    "Tenía la sensación de que si seguía presionándolo o levantaba la voz nuevamente, las cosas solo empeorarían."
    "Si la fuerza no iba a funcionar, entonces tendría que intentar un enfoque más suave."
    "Volví a mirar su expresión frustrada."
    
    mc "Jestyn..."
    mc "Eres un bufón bueno y leal... ¿no?"
    
    stop music
    camera at camera_shake
    show jes suprais
    "La irritación en su rostro desapareció en un instante, reemplazada por pura sorpresa. No creo que esperara esas palabras de mi parte."
    camera at reset
    "Tal vez... Sólo tal vez... Un enfoque más amable funcionaría después de todo."
    "Di unos pasos lentos hacia él."
    
    play music "bgs_mystery.mp3" volume 3.0 fadein 3.0
    mc "Sé que estás haciendo todo lo posible por ser un bufón que siempre es leal a su gobernante."
    mc "Y... realmente lo aprecio."
    
    show jes flush1_2 with dissolve
    "Levanté la mano y acaricié suavemente su mejilla. Mi pulgar acarició suavemente su piel, esperando calmarlo."
    "Un leve sonrojo se extendió gradualmente por las mejillas de Jestyn."
    
    mc "Pero quiero estar solo ahora mismo."
    mc "Y como mi leal bufón... quiero que me dejes en paz. Sólo por ahora."
    mc "Lo entiendes... ¿no?"
    
    show jes conflic with dissolve
    "Sus manos lentamente alcanzaron las mías, envolviéndolas suavemente en las suyas, mucho más grandes."
    "Sin embargo, sus ojos nunca encontraron los míos."
    "En cambio, miró nuestras manos unidas."
    "Parecía... en conflicto."
    
    jes "Pero..."
    mc "Eres mi buen chico, ¿verdad, Jestyn?"
    
    show jes flush1_2 
    "Todo su cuerpo se estremeció en el momento en que las palabras salieron de mis labios."
    "El rubor de su rostro se hizo más intenso y su respiración se volvió notablemente irregular."
    
    mc "Dime..."
    mc "Eres un buen chico para mí... ¿no?"
    
    "Él también tomó suavemente mi otra mano, acunándolos a ambos juntos."
    "Luego lentamente se los llevó a los labios."
    show jescg puppy with dissolve
    hide jes flush1_2 
    "Acariciando mis palmas, depositó un suave beso contra ellas."
    
    jes "...Sí..."
    show jescg puppy2 with dissolve
    jes "Sí... soy su buen chico, Su Majestad..."
    
    "Sus ojos miraron a los míos con inconfundible afecto."
    "No esperaba que reaccionara así."
    "No podía negarlo... Se veía increíblemente lindo."
    
    mc "Entonces ve a descansar, ¿vale?"
    mc "No voy a ninguna parte."
    mc "Sólo quiero estar solo por un rato."
    jes ".........."
    
    hide jescg puppy2 with dissolve
    "Jestyn asintió de mala gana y lentamente soltó mis manos."
    "Aunque había aceptado irse, la tristeza en su rostro hacía dolorosamente obvio que en realidad no quería hacerlo."
    
    show jes conflic with dissolve
    jes "...Si eso es realmente lo que Su Majestad desea....Muy bien."
    jes "Volveré en... quizás diez minutos."
    mc "Jestyn."
    mc "...Quince, entonces."
    mc "......"
    jes "...Treinta..."
    mc "Dos horas y treinta minutos."
    jes "......"
    jes "...¿No podría al menos velar por Ti desde lejos?"
    mc "Entonces ¿cuál es tu definición de dejarme en paz? No."
    show jes pout with dissolve
    jes "Mmmmmnnnghhhrrrghhh..."
    jes "....."
    show jes conflic with dissolve
    jes "...Muy bien... Hasta que nos volvamos a encontrar, Su Majestad..."
    hide jes conflic with dissolve
    "Se alejó lentamente, haciendo pucheros todo el tiempo."
    "Abrió la puerta de su habitación y luego se detuvo."
    "Por unos momentos, simplemente me miró con expresión abatida. Sólo entonces entró silenciosamente y cerró la puerta detrás de él."
    stop music fadeout 2.0
    "......"
    "... Parecía un cachorro triste."
    "Pero... Esta es mi oportunidad."
    "Necesito descubrir qué está pasando realmente."
    "Luego mi mirada se desvió hacia el extremo más oscuro del pasillo de las marionetas."
    "Sabía muy bien que este pasillo era mucho más largo de lo que parecía."
    "Ayer no le había prestado mucha atención. Sólo quería terminar mis deberes. Pero ahora que mi situación había empezado a parecer algo sacado directamente de una historia de fantasía, pensé que sería mejor explorarla."
    "Maldita sea, olvidé traer mi linterna. ¿Dónde lo puse?"
    "Finalmente decidí seguir caminando sin uno. No puede ser tan oscuro... ¿verdad?"
    "Luego caminé más profundamente por los pasillos bordeados por las habitaciones de los títeres."
    play sound  "footstep.mp3"
    scene black with dissolve
    "Cuanto más avanzaba, más oscuro se volvía el pasillo."
    "No había ninguna luz tan lejos."
    "Ayer no me había aventurado tan profundamente en la sala de marionetas, así que no tenía idea de que el pasillo se extendía tan lejos."
    "Incluso comencé a preguntarme si tendría algún final."
    "Cuanto más caminaba, menos salas de títeres había..."
    "...hasta que finalmente, no hubo más salas de títeres, dejando nada más que paredes de piedra desnuda."
    "Entonces lo vi."
    show bg_blackdoor with dissolve
    "Al final del oscuro pasillo había una única puerta negra."
    "Una sensación de inquietud comenzó a invadirme."
    "¿Qué puerta es esa, me pregunto...?"
    "La curiosidad me carcomía, atenuada por una sensación de inquietud en la boca del estómago, mientras lentamente avanzaba hacia allí."
    "¿Debería abrirlo...?"
    "Mi mano alcanzó lentamente el pomo de la puerta."

    stop music
    who "¿Su Majestad?"
    
    "Me estremecí cuando de repente una voz gritó detrás de mí."
    "Rápidamente me volví hacia la fuente de la voz."
    
    show but normal with dissolve
    who "Te noté caminando sola por este pasillo..."
    who "¿Está todo bien?"
    
    "Un títere vestido de mayordomo se me acercó."
    "Oh, él es el mayordomo títere de ayer..."
    "No me di cuenta de que no estaba en su habitación."
    
    play music "bgs_medieval normal.mp3" volume 3.0 fadein 3.0
    butpuppet "Terminará caminando hacia algo en un pasillo así de oscuro, Su Majestad."
    butpuppet "¿Adónde te diriges?"
    mc "Oh, en ninguna parte, de verdad."
    mc "Sólo estaba explorando."
    mc "No me di cuenta de que el barrio de los títeres llegaba tan lejos."
    butpuppet "Ah. Ciertamente son más grandes de lo que parecen, Su Majestad."

    show but smile with dissolve

    but "Por favor, perdone mi intrusión, Su Majestad. Permítanme presentarme. Mi nombre es Butley y soy el mayordomo títere."
    but "Aún no he tenido la oportunidad de conocer a Su Majestad, así que decidí salir de mi habitación y presentarme adecuadamente."
    
    "Incliné la cabeza confundida."
    
    mc "¿Qué quieres decir? Nos conocimos ayer, ¿no? Durante el juego de roles."
    
    show but confuse with dissolve
    "Butley parecía igual de confundido por mi expresión de desconcierto."
    
    but "Perdóneme, Su Majestad... No estoy seguro de entender lo que quiere decir."
    but "Nunca salí de mi habitación ayer. Así que no he conocido a Su Majestad en absoluto."
    mc "¿Qué? Pero... podría haber jurado que te vi ayer en el escenario... parado al lado de Jestyn mientras estábamos jugando."
    show but normal with dissolve
    but "Ah... Jestyn me pidió que participara en el juego de rol de antemano."
    but "Pero al día siguiente me dijo que tenía otros planes, por lo que cancelaron mi participación en la actuación."
    but "Quizás Su Majestad simplemente recordó incorrectamente y confundió a alguien más conmigo. Después de todo, ayer fue tu primer día aquí."
    mc "....Mmhh... Supongo que eso es posible..."

    "Pero... ¿es realmente...?"

    show but smile with dissolve
    but "...... ¿Qué tal si te hago compañía? Realmente no hemos tenido la oportunidad de hablar antes."
    
    hide but smile with dissolve
    scene black with dissolve
    "Dudé por un momento antes de finalmente aceptar su oferta."
    "Quizás podría hacerle algunas preguntas."
    "Si alguien supiera lo que estaba pasando por aquí, podría ser alguno de los otros títeres."
    scene bg_corridor with dissolve
    "Los dos comenzamos a caminar juntos, dejando atrás el cuarto de los títeres."
    "Intercambiamos una pequeña charla antes de que finalmente me decidiera a hacer las preguntas que habían estado rondando por mi mente."

    mc "Butley, ¿puedo hacerte algunas preguntas?"
    show but smile with dissolve
    but "Por supuesto, Su Majestad."

label butley_askday2:
    show but normal with dissolve
    menu:
        "¿Qué opinas sobre Jestyn?":
            show but confuse
            "Su cuerpo de repente se puso rígido por un momento."
            
            but "¿Jestyn...? Mmm..."
            but "Él... está bien... supongo."
            mc "......"
            mc "No pareces muy convencido."
            but "......"
            
            "Butley miró alrededor de la habitación, con ojos cautelosos como si se asegurara de que nadie más estuviera escuchando."
            
            but "Para ser honesto, Su Majestad... no debería decirle esto..."
            but "Pero... ya que me pediste mi opinión..."
            show but normal with dissolve
            but "No me gusta Jestyn."
            
            "La respuesta me tomó completamente desprevenido y no pude ocultar mi sorpresa."
            
            mc "... ¿Por qué?"
            but "Él, en mis ojos, no sabe nada."
            show but annoy with dissolve
            but "Sin embargo, actúa como si supiera qué es lo mejor para todos nosotros."
            but "Se comporta como un líder sabio y capaz... pero la verdad no es nada de eso."
            
            "Butley me miró. Una mano se aferró con fuerza a su camisa mientras una sola gota de líquido negro se deslizaba de su ojo."
            
            but "Él no quiere que tengamos una vida mejor."
            but "Para Su Majestad, Jestyn es un títere alegre, amable y adorable... ¿no es así?"
            but "Él te está mintiendo. Es todo un acto. Sólo finge para que confíes en él."
            
            "¿Jestyn...? ¿Mentirme?"
            "Mi mente luchó por procesar todo lo que Butley acababa de decirme."
            "...... Entonces... ¿me ha estado engañando todo este tiempo? Pero por qué...?"
            "¿Sobre qué ha estado mintiendo exactamente?"
            
            but "No sé qué está planeando... pero..."
            but "Tarde o temprano... puede que intente utilizarla, Su Majestad."
            
            "Un escalofrío de miedo e inquietud se deslizó lentamente por mi cuerpo."
            
            but "....."
            show but confuse with dissolve
            but "Ah... perdóneme, Su Majestad. No quise asustarte... es sólo..."
            but "Quería advertirte mientras pudiera. Por favor... ten cuidado."

            jump butley_askday2


        "¿Qué opinas del rey títere?":
            show but suprais with dissolve
            "En el momento en que mencioné el Rey Marioneta, la cabeza de Butley se giró hacia mí."
            show but happy
            "Su rostro se iluminó y una amplia sonrisa se dibujó en él."
            
            but "¡Ah! ¡Se refiere al Señor Crownus, Su Majestad!"
            but "¡Él es el mejor!"
            but "¡Él quiere lo mejor para todos nosotros! Él está ayudando a todos y cada uno de nosotros a encontrar nuestro camino."
            but "¡Y estamos más que felices de darle todo lo que tenemos a Lord Crownus como muestra de nuestra inmensa gratitud!"
            show but annoy with dissolve
            but "Lord Crownus realmente nos salvó... a diferencia... de otra persona..."
            
            "Escuché atentamente todo lo que Butley tenía que decir."
            "Por la forma en que habló, estaba claro que, a los ojos de Butley, Crownus era nada menos que un salvador."
            
            mc "Pareces admirar mucho a Crownus."
            show but happy with dissolve
            but "¡Por supuesto que sí!"
            but "Y no soy el único. Muchos de los otros títeres sienten lo mismo."
            
            "¿Los demás también piensan lo mismo...?"
            
            but "Para la mayoría de los títeres aquí, Lord Crownus es un genio."
            but "Yo incluido."
            mc "Ya veo..."

            jump butley_askday2


        "¿Tienes una buena relación con cada títere?":
            mc "¿Qué tal... tu relación con los otros títeres? No hay ningún problema, ¿verdad?"
            but "....."
            
            "Butley se quedó en silencio mientras seguíamos caminando."
            "¿Dije algo que no debería haber...?"
            
            mc "Lo siento si es un tema delicado."
            show but smile
            but "En absoluto, Su Majestad."
            but "......"
            show but normal
            but "Me llevo bien con algunos de los otros títeres... y no tan bien con otros."
            mc "... ¿Por qué es eso?"
            but "..... Se podría decir... tenemos diferentes puntos de vista."
            but "...Y... lamentablemente, tampoco estoy de acuerdo con mis hermanas mayores."
            
            "Mi curiosidad se despertó inmediatamente cuando Butley mencionó a sus hermanas mayores."
            
            mc "¿Tienes hermanas mayores?"
            but "Yo lo hago. Son trillizos. Si ya las conociste, son las criadas."
            
            "¡Ah! Entonces, ¿Maidelyn, Maidy y Maidra son las hermanas mayores de Butley?"
            
            mc "Los he conocido a los tres, sí."
            show but smile with dissolve
            but "Espero que hayan causado una buena primera impresión a Su Majestad."
            but "Los cuatro solíamos ser muy cercanos... pero..."
            show but normal
            "Butley hizo una pausa por un momento."
            
            but "Ya no. Desde que murió Lord Crownus, hemos tomado caminos separados."
            but "Todavía hablamos de vez en cuando... pero no es más que intercambiar saludos. Como... extraños que se encuentran casualmente."
            but "Para ser honesto... desearía que pudiéramos ser cercanos nuevamente."
            
            show but confuse
            "Intenté consolarlo dándole unas suaves palmaditas en la espalda."
            "Al principio, Butley se estremeció sorprendido, pero después de un momento, simplemente me dejó continuar."
            
            mc "Mmm... ¿Qué pasa con Wizzy? Parece un lindo títere. Pensé que era cercano a todos."
            
            show but annoy with dissolve
            "En el momento en que mencioné a Wizzy, la expresión de Butley se endureció de inmediato."
            
            but "Ya no."
            but "Realmente es un títere amable. Pero… una vez más, tenemos creencias muy diferentes. Y esas diferencias son tan fundamentales que simplemente no puedo estar cerca de él."
            but "Y él tampoco se siente cómodo cerca de mí... así que... no hemos hablado desde entonces."
            
            "¿Qué pudo haber pasado entre Butley y Wizzy que los hizo sentir tan incómodos el uno con el otro...?"

            mc "¿Qué pasó entre ustedes dos en realidad?"
            show but confuse with dissolve
            but "....."
            but "Sólo asuntos personales. Nada importante."

            "Parece que no quiere hablar de eso."

            mc "Entonces... ¿eres cercano a Knighter?"
            show but smile with dissolve
            but "Ah... Knighter..."
            but "Para ser honesto, no somos particularmente cercanos. Pero nos respetamos unos a otros."
            but "Dicho esto... Creo que Knighter es una marioneta extraordinaria."
            show but happy with dissolve
            but "Su lealtad es inquebrantable. Incluso ahora, sigue siendo devoto de Lord Crownus y me alivia que eso no haya cambiado."
            but "Él también me inspira a permanecer leal a Lord Crownus. Por eso le tengo tanto respeto."

            "Entonces, al menos Butley y Knighter no tienen ningún problema entre sí. Eso es un alivio... creo."

            if visited_wizzy:
                $ prieston_route_point += 1
                "....."
                
                mc "¿Qué pasa con el títere llamado Prieston? ¿Eres cercano a él?"
                
                show but confuse
                "En el momento en que mencioné el nombre de Prieston, Butley se volvió hacia mí con expresión de desconcierto."
                
                but "...¿Su Majestad conoce a Prieston?"
                mc "En realidad no... Aún no lo conozco. Wizzy fue quien me habló de él."
                mc "¿Pasa algo mal?"
                but "No, por supuesto que no..."
                but "Es sólo que... creo que él es... no lo sé..."
                but "¿Extraño...? Aunque... no creo que \"extraño\" sea la palabra correcta."
                mc "¿Qué te hace decir eso?"
                show but normal
                but "El día que Lord Crownus murió... muchos de los títeres estaban abrumados por la emoción..."
                but "Había lágrimas... ira... miedo... todo estaba mezclado."
                but "Pero él... todavía lo recuerdo claramente..."
                but "Estaba sonriendo detrás de las cortinas... mientras miraba el cuerpo de Lord Crownus."
                
                "Wizzy's earlier description of Prieston suddenly felt much more believable. Quienquiera que fuera este títere, mi curiosidad por él no hizo más que crecer."
                
                mc "¿Alguna vez has hablado con él?"
                but "Algunas veces, pero muy raramente. Casi nunca sale de su habitación."
                but "La única forma de conocer a Prieston es si él decide salir... o si alguien va a su habitación."
                but "Y... hubo una vez que lo encontré parado solo en el escenario, rodeado de oscuridad."
                
                "Por alguna razón, un escalofrío recorrió mi espalda."
                
                mc "¿Qué estaba haciendo allí...?"
                but "Yo tampoco lo sé. Le pregunté lo mismo cuando me acerqué a él."
                but "Y me dijo... que ver la muerte de Lord Crownus fue... fascinante."
                but "Entonces... creo que puedes entender por qué mis sentimientos hacia Prieston son... complicados."
                but "Ni siquiera estoy seguro de si lo odio o no."
                mc "Ya veo."

                "Interesante... Ahora me pregunto qué aspecto tendrá..."

            jump butley_askday2

        "eso es todo":
            jump the_truth_route_2


label the_truth_route_2:
    hide but normal with dissolve
    scene bg_stage with dissolve
    "Antes de que ninguno de los dos nos diésemos cuenta, habíamos llegado al escenario."
    
    show but normal with dissolve
    but ".........."
    but "Su Majestad..."
    but "...Ha pasado mucho tiempo desde la última vez que hablé con un humano."
    
    "Hizo una pausa."
    
    but "Yo... no le guardo rencor a los humanos."
    but "Es solo..."

    stop music fadeout 3.0
    
    show but confuse
    "Butley volvió a quedarse en silencio, luchando por encontrar las palabras adecuadas."
    
    show but normal with dissolve
    but "Rey Crownus..."
    but "...nos dio esperanza."
    show but happy with dissolve
    but "Nos mostró una manera para que nosotros, los títeres, vivamos una vida mejor."
    but "Pensé..."
    but "...todos pensamos..."
    but "... finalmente todo iba a estar bien."
    show but annoy with dissolve
    but "Pero todo se vino abajo en un instante..."
    but "Nuestra esperanza se hizo añicos..."
    but "Todo fue..."
    but "...por culpa de Jestyn."
    
    play music "abandoned.mp3" volume 3.0 fadein 3.0
    "Me congelé cuando la voz de Butley se hizo notablemente más pesada cuando pronunció el nombre de Jestyn."
    "Una sensación de inquietud se deslizó por mi cuerpo."
    "Instintivamente di un pequeño paso atrás."
    
    but "Él es quien destruyó todo."
    
    show but angry with dissolve
    but "Lo odio."
    but "Y odio el hecho de que él sea mucho más fuerte que yo..."
    but "Significa que no puedo hacer nada."
    but "...La verdad es..."
    but "...He querido matarlo durante mucho tiempo."
    
    "Esto no es bueno."
    
    but "Y luego..."
    but "...tuvo la audacia de coronar a un humano como nuestro gobernante..."
    but "Como si pudiera simplemente reemplazar al Rey Crownus..."
    
    "Después de murmurar para sí mismo por un rato, Butley levantó lentamente la cabeza y me miró."
    "Un extraño líquido negro goteaba de sus ojos y de las comisuras de su boca."
    play sound "nyekek.mp3" 
    camera at camera_shake
    "Antes de que pudiera reaccionar, de repente me agarró la muñeca."
    camera at reset
    "Inmediatamente luché por liberarme de su agarre."
    show but happy with dissolve
    but "Pero eso está bien..."
    but "Eres humano."
    but "Eso significa que todavía puedes sernos útil."
    but "El rey Crownus descubrió una manera para que nosotros, los títeres, tengamos una vida mejor..."
    but "Todo lo que tengo que hacer..."
    but "...es seguir el mismo camino que él."
    mc "B-Butley, ¡déjame ir!"
    
    camera at camera_shake
    "Le di una patada con todas las fuerzas que tenía, tratando de liberarme."
    camera at reset
    show screen dark_effect with dissolve
    "Pero poco a poco mi cuerpo empezó a debilitarse."
    "Una oleada de mareos me invadió."
    "Sentí como si… algo dentro de mí estuviera siendo sacado a la fuerza."
    "Mi visión se volvió borrosa y ya no podía concentrarme."

    scene black with dissolve
    hide but happy
    who "Butley! ¡Así que finalmente atrapaste a ese humano! ¡Jajaja!"
    who "¡No puedo creer que tu plan realmente haya funcionado!"
    but "Sí..."
    
    "Débilmente, pude escuchar otras voces hablando con Butley."
    "¿Eran esos... otros títeres?"
    
    pup1 "Hola, Butley, ¡comparte algunos con nosotros! ¡Yo también necesito a ese humano!"
    pup2 "¿Por qué tardas tanto? ¡Apresúrate!"
    but "........."
    but "Yo... yo..."
    
    "Por alguna razón, poco a poco dejé de sentir esa fuerza invisible tirando de mí."
    scene bg_stage with dissolve
    show but confuse with dissolve
    but "Yo... no puedo..."
    pup3 "¿Qué quieres decir con que no puedes? Date prisa, antes-"

    if prieston_route_point >= 3:
        jump prieston_route_day2

    else:
        jump jestyn_route_day2

label jestyn_route_day2:
    mc "¡¡JESTÍN!!"
    
    stop music
    show but suprais
    but "?!"
    play sound "nyekek.mp3" volume 3.0
    camera at camera_shake
    hide but suprais
    show butcg drag
    "No sabía lo que había pasado, pero, de repente, me liberé de las garras de Butley."
    camera at reset
    "Entonces escuché un fuerte estrépito."
    play sound "thud.ogg" volume 3.0 
    camera at camera_shake
    hide butcg drag
    but "¡AGH-!"
    camera at reset
    "Mi visión volvió lentamente a enfocarse y allí vi a Jestyn inmovilizando a Butley en el suelo."
    camera at camera_shake
    show butcg pinning
    "El rostro de Jestyn estaba torcido por la ira."
    camera at reset
    
    jes "Butley."
    jes "¿Qué estabas tratando de hacer hace un momento?"
    but "Yo-yo no estaba haciendo nada-"
    
    play sound "nyekek.mp3"
    camera at camera_shake
    "Jestyn presionó a Butley con más fuerza contra el suelo, haciéndolo gritar de dolor."
    camera at reset
    
    but "¡BIEN! ¡Estaba tratando de comer [obj]! ¡Lo lamento!"
    jes "........"

    hide butcg pinning with dissolve
    "Jestyn finalmente se soltó, permitiendo que Butley respirara nuevamente."
    
    show jes creep with dissolve
    jes "Vuelve a tu habitación. Todos ustedes. AHORA."
    
    hide jes creep with dissolve
    "Sin decir una palabra más, Butley salió corriendo del escenario, seguido por los otros títeres."
    hide screen dark_effect with dissolve
    "Me quedé congelada en el lugar, tratando de procesar todo lo que acababa de suceder."
    "Salí de mis pensamientos cuando Jestyn de repente me abrazó con fuerza."
    "No sabía qué hacer, pero mis brazos instintivamente lo rodearon."
    "... ¿Está temblando?"
    
    mc "...Jestyn... gracias..."
    
    "Jestyn se apartó lentamente y me miró. Su rostro estaba lleno de miedo." 
    "No sabía que era capaz de hacer una expresión así."
    
    show jes scared with dissolve
    jes "Su Majestad... no tiene idea de lo aliviado que estoy..."
    jes "Desde entonces no he podido dejar de pensar demasiado..."
    jes "Simplemente no podía calmarme."
    jes "...Entonces te escuché decir mi nombre."
    show jes breakdown with dissolve
    jes "Si hubiera llegado tarde aunque fuera un momento después... habrías..."
    
    "Su respiración se hizo irregular mientras las terribles posibilidades pasaban por su mente."
    
    mc "Jestyn, estoy aquí... Todo está bien."
    
    "Él no me estaba escuchando. Estaba demasiado perdido en sus propios pensamientos."
    "Tomé suavemente sus mejillas, tratando de hacerlo volver a sus sentidos."
    show jes suprais
    "Se estremeció levemente, pero pronto salió de sus pensamientos."
    
    jes "...¿Su Majestad...?"
    mc "Jestyn, estoy aquí. ¿No es eso lo que más importa?"
    jes "........."
    show jes conflic with dissolve
    jes "...Sí... Tiene razón, Su Majestad."
    
    "Se apoyó en mi palma."
    
    jes "...Estoy muy agradecido."
    jes "...Me siento mucho más tranquilo ahora... Gracias."
            
    "Mientras intentaba ponerme de pie, el mareo y la debilidad me hicieron perder el equilibrio."
    "Jestyn me atrapó antes de que pudiera caer."
    
    camera at camera_shake
    show jes suprais
    jes "¡Su Majestad!"
    camera at reset
    mc "Yo... me siento tan mareado... y débil..."
    show jes conflic with dissolve
    jes "...Por supuesto. Son las secuelas de lo que pasó antes..."
            
    "Jestyn luego me tomó en sus brazos y no protesté. Estaba demasiado débil para siquiera levantar la mirada."
            
    jes "Te llevaré de regreso a tu habitación..."
    
    play sound "snap.mp3"
    hide jes conflic
    scene bg_office
    "Jestyn chasqueó los dedos y, en un instante, estábamos de vuelta en mi habitación."
    "Me recostó suavemente en la cama."
    
    show jes nosmile with dissolve
    jes "¿Hay algo que le gustaría, Su Majestad? ¿Quizás algo caliente para beber?"
            
    "Asentí."
    "Jestyn se acercó a la puerta y la cerró."
            
    jes "Espere aquí, Su Majestad."
    
    play sound "snap.mp3"
    hide jes nosmile
    "Con otro chasquido de dedos, desapareció."
    ".........."
    "Mi cabeza todavía palpitaba por el mareo... pero no importa cuánto lo intentara, no podía dejar de pensar en todo lo que acababa de pasar."
    "Una sensación de horror se apoderaba de mi cuerpo cada vez que imaginaba lo que podría haberme pasado."
    "Unos momentos después, Jestyn regresó con una taza de chocolate caliente en sus manos."
    "Me ayudó a sentarme y colocó una almohada detrás de mi espalda para sostenerme."
    
    show jes nosmile with dissolve
    jes "Cuidado, Su Majestad. Todavía hace calor."
    
    "Soplé el chocolate caliente antes de tomar un pequeño sorbo."
    play music "sad.mp3" volume 3.0 fadein 3.0
    "Su rico y aterciopelado sabor se extendió por mi lengua y el calor se filtró lentamente por mi cuerpo."
    "Esa calidez gradualmente calmó la tormenta de pensamientos que se arremolinaban en mi mente."
    "...Me sentí un poco mejor ahora, aunque mi cuerpo todavía estaba débil."
    "Sentado a mi lado, Jestyn nunca me quitó los ojos de encima."
    "Tenía la sensación de que todavía estaba conmocionado por lo que había sucedido antes."
    "Se sentía extraño no escuchar a Jestyn ladrar como solía hacer. Normalmente, nunca dejaba de hablar, de burlarse de mí, de hacer comentarios sarcásticos o de decir lo que se le ocurría sólo para mantener la conversación."
    "Pero no esta vez. Simplemente se sentó allí, mirándome en silencio."
    
    mc "¿Jestyn?"
    jes "¿Sí, Su Majestad?"
    mc "¿Todavía tienes miedo?"
    show jes conflic with dissolve
    jes ".........."
    jes "...Sí."
    
    "Entonces tenía razón."
    
    mc "... me asustas"
    show jes suprais
    jes "...¿Qué le hace pensar eso, Su Majestad...?"
    show jes scared with dissolve
    jes "¿Es por… cómo actué antes…?"
    mc "No. Has estado muy callado."
    mc "De hecho, prefiero cuando estás ladrando como lo haces normalmente."
    show jes suprais with dissolve
    jes "Ah..."
    mc "Di algo. Cualquier cosa. Incluso puedes burlarte de mí como siempre lo haces."
    jes "......"
    show jes laugh with dissolve
    jes "Pfff... Jajaja..."
    
    "Lentamente, pude ver regresar el habitual Jestyn."
    
    show jes happy with dissolve
    jes "¿Oh~? ¿Quiere que me burle de usted, majestad? No tenía idea de que te gustaba que te degradaran..."
    jes "Pequeño masoquista..."
    
    "...Sí. Este imbécil había vuelto por completo."
    
    mc "Ve a buscar un espejo, Jestyn."
    
    show jes laugh
    "Él se rió y, de alguna manera, escuchar su risa me hizo reír también."
    "Entonces… el pensamiento de antes volvió."
    
    mc "......"
    mc "Jestyn, tengo una pregunta."
    mc "Se trata de Butley... y los otros títeres."
    
    show jes nosmile with dissolve
    "La expresión de Jestyn inmediatamente se volvió seria."
    
    mc "Antes de que llegaras, Butley seguía hablando de lo leal que era a Crow-"
    
    "Antes de que pudiera terminar de decir el nombre, Jestyn presionó su dedo índice contra mis labios, silenciándome de inmediato."
    
    jes "Sé lo que quiere decir, Su Majestad. No necesitas decir una palabra más."
    
    "Jestyn lentamente apartó su dedo de mis labios. Luego se quedó en silencio una vez más."
    
    jes "........."
    show jes conflic with dissolve
    jes "..........."
    
    "Sus ojos recorrieron nerviosamente la habitación, escaneando cada rincón que podía ver."
    show jes breakdown
    "Se agarró el cuello mientras su respiración se hacía gradualmente más rápida."
    
    mc "¡¿JESTÍN?!"
    
    "Inmediatamente tomé su mano."
    
    mc "¡¿Qué pasa?!"
    hide jes breakdown with dissolve
    "Poco a poco volvió a sus sentidos y comenzó a estabilizar su respiración."
    
    show jes conflic with dissolve
    jes "...Mis disculpas, Su Majestad..."
    
    "Incluso después de que se calmó, todavía no podía dejar de preocuparme por él."
    
    mc "...Acuéstate conmigo."
    
    show jes suprais with dissolve
    "Sus ojos se abrieron con sorpresa."
    
    jes "...¿Indulto?"
    mc "Creo que ambos necesitamos descansar un poco, ¿no? Así que... acuéstate conmigo."
    
    show jes flush with dissolve
    "Un leve sonrojo se extendió lentamente por las mejillas de Jestyn."
    
    jes "Jeje... vaya, vaya... ¿Está haciendo algo conmigo, Su Majestad~?"
    mc "Esa es una orden."
    jes "...Como desee, Su Majestad."
    
    hide jes flush with dissolve
    "Lo que no esperaba era que se quitara la corona... seguida de su capucha."
    "Luego se acostó a mi lado, frente a mí."
    "...Esta es la primera vez que veo su cabello. Era largo y ondulado. Y el color granate intenso le sentaba maravillosamente."

    show jescg bed normal with dissolve
    jes "...¿Le gusta, Su Majestad?"
    
    "Me notó mirando su cabello."
    
    mc "...Te ves hermosa."
    
    show jescg bed blush with dissolve
    "El rubor de sus mejillas se hizo más intenso."
    
    jes "¿Está intentando coquetear conmigo, Su Majestad~?"
    mc "Muy bien. Eres feo."
    show jescg bed pout with dissolve
    jes "Hmph... cruel."
    
    "........"
    
    show jescg bed nosmile with dissolve
    jes "...Su Majestad... Quiero saber si he hecho algo mal."
    
    "Me animé. ¿Por qué preguntaba eso de repente?"
    
    mc "¿Qué quieres decir?"
    show jescg bed lookaway 
    jes "Arrastrándote a todo esto... y..."
    
    "Hizo una pausa, incapaz de terminar la frase."
    
    mc "...Bueno... yo trabajo aquí. Eso significa que ya me he involucrado en los asuntos del reino, me guste o no... ¿no es así?"
    show jescg bed sad with dissolve
    jes "......"
    jes "...Sí..."
    mc "...Dime qué tienes en mente. ¿No es ese el deber de un gobernante? Escuchar las voces de su pueblo."
    
    show jescg bed normal with dissolve
    "Jestyn me sonrió una vez más."
    
    jes "Está mejorando en el desempeño de su papel, Su Majestad."
    show jescg bed nosmile 
    jes "........."
    
    show jescg bed sad with dissolve
    "Jestyn dejó escapar un largo y cansado suspiro."

    jes "Yo... honestamente, todavía no me siento muy cómodo hablando de este tema, Su Majestad..."
    mc "Ah..."
    
    "Sólo por sus palabras, pude sentir el trauma que llevaba, aunque no tenía idea de qué lo había causado."
    "Solo me dio más curiosidad... pero al mismo tiempo, ver a Jestyn tan incómodo me hizo sentir triste."
    
    mc "...Si es realmente tan desagradable, no tienes que decírmelo, Jestyn."
    mc "Podemos simplemente relajarnos aquí."
    jes "........"
    jes "Pero... como ya hemos llegado hasta aquí, Su Majestad tiene derecho a saber..."
    show jescg bed nosmile with dissolve
    jes "Quizás... sólo puedo contarte una parte, de otra manera....."
    
    stop music fadeout 3.0
    show merem
    pause 1.5
    show jescg fairytale with dissolve
    hide merem with dissolve

    play music "fairy tale.mp3" volume 3.0 fadein 3.0
    jes "Érase una vez un bosque envuelto en seda y sombra, donde cada criatura desempeñaba el papel que le daba la luz de la luna."
    show jescg fairytale
    pause 0.2
    show jescg fairytale2
    pause 0.2
    show black_area 
    pause 0.2
    show jescg fairytale3
    hide black_area
    jes "En el centro estaba sentado un rey León con una melena sin sol,"
    jes "¡Prometió: '¡Nos levantaremos juntos!', ¡una y otra vez!"
    
    show jescg fairytale4
    pause 0.2
    show jescg fairytale5
    pause 0.2
    show black_area
    pause 0.2
    show jescg deerfairytale with dissolve
    hide black_area with dissolve
    jes "Los ciervos corrieron hasta que sus patas cedieron,"
    show jescg owlfairytale with dissolve
    jes "El búho leyó las estrellas y les dijo que obedecieran."
    show jescg dogfairytale with dissolve
    jes "El perro hacía guardia sin parpadear,"
    show jescg lionfairytale with dissolve
    jes "Mientras que el león se alimentaba de mentiras prestadas."

    show jescg fairytale6
    pause 0.2
    show black_area 
    pause 0.2
    show jescg bunnyfairytale 
    hide black_area with dissolve
    jes "Entre las raíces, bajo el escenario de los árboles,"
    jes "Un conejo bailaba con cascabeles de cristal y dientes."
    show jescg bunnyfairytale2 with dissolve
    jes "El león se rió y lo acercó,"
    jes "Llamó al dolor una broma, llamó al miedo \"sincero\"."
    
    show jescg bunnyfairytale3 with dissolve
    jes "Oh, el bosque escuchó, o eligió fingir,"
    jes "Que así era como debían terminar todas las historias."
    show black_area with dissolve
    jes "Susurraron en voz baja: \"Aguanta, aguanta\"."
    jes "Como si el silencio pudiera purificar la crueldad."
    
    show jescg fairytale with dissolve
    hide black_area with dissolve
    jes "Una noche, la luna contuvo el aliento entre los árboles,"
    show jescg lionbunfairytale with dissolve
    jes "Cuando el conejo eligió la verdad antes que rogar de rodillas."
    show jescg lionbunfairytale2 with dissolve
    jes "El león nunca se dio cuenta, ebrio de su propio nombre,"
    jes "Cuando el veneno poco a poco encontró el latido del corazón de la vergüenza del bosque."
    
    camera at camera_shake
    show jescg fairytale7
    pause 0.5
    camera at reset

    jes "Los perros ladraron furiosos al suelo carmesí,"
    jes "El ciervo se quedó petrificado y no emitió ningún sonido."
    jes "Los búhos miraron hacia abajo y luego hacia otro lado."
    show jescg fairytale8 with dissolve
    jes "Pero el conejo sonrió tranquilo y limpio."
    jes "Porque la libertad rara vez parece serena."

    play sound "swing.mp3"
    hide jescg fairytale8
    show cg cursed2
    pause 0.5
    camera at camera_shake
    play sound "blood.mp3"
    show cg cursed3
    pause 2.0
    scene black with dissolve
    camera at reset
    stop music fadeout 3.0
    "......."
    
    jes "...¿Tiene sueño, Su Majestad?"
    show jescg bed nosmile with dissolve
    mc "Quizás un poco..."
    
    play music "sad.mp3" volume 3.0 fadein 3.0
    "Mis párpados se volvieron más pesados mientras escuchaba la historia de Jestyn."
    "Esa historia... fue tan dolorosamente triste."
    
    mc "Jestyn... ¿estás bien...?"
    jes ".........."
    show jescg bed lookaway 
    jes "...Para ser honesto... No puedo decir que lo sea, Su Majestad."
    show jescg bed sad with dissolve

    $ voice_duck_start()
    voice "JESTYN04_DAY2.ogg"
    jes "Todo sucedió hace mucho tiempo... pero cada vez que lo recuerdo... siento como si lo estuviera viviendo todo de nuevo."
    $ voice_duck_end()
    show jescg bed blush with dissolve
    "Se quedó dormido por un momento antes de mirarme con una suave sonrisa."
    
    $ voice_duck_start()
    voice "JESTYN05_DAY2.ogg"
    jes "Pero al menos... me siento un poco mejor sabiendo que está aquí conmigo, Su Majestad."
    voice "JESTYN06_DAY2.ogg"
    jes "...¿Puedo tocarte?"
    $ voice_duck_end()

    menu:
        "Yes":
            show jescg bed caress with dissolve
            "Jestyn acarició suavemente mi cabello. Se sintió tan reconfortante que mis párpados se volvieron aún más pesados."
            
            jes "Entonces duerme un poco. Esas ojeras le quedan feas... aunque tengo que admitir que todavía se ve adorable, Su Majestad."
            show merem
            mc "Mmmmm...pendejo..."

            "Él se rió suavemente."
            stop music fadeout 3.0
            jes "Dulces sueños, Su Majestad... Estaré aquí cuando despierte."

        "No":
            show jescg bed pout with dissolve
            "La expresión de Jestyn se convirtió en un puchero triste, pero pronto fue reemplazada por una sonrisa amable."
            
            show jescg bed blush with dissolve
            jes "Entonces duerme un poco. Esas ojeras le quedan feas... aunque tengo que admitir que todavía se ve adorable, Su Majestad."
            show merem
            mc "Mmmmm...pendejo..."

            "Él se rió suavemente."
            stop music fadeout 3.0
            jes "Ahora, dulces sueños, Su Majestad... Estaré aquí cuando despierte..."


    jump credits










label prieston_route_day2:
    who "Butley."

    stop music
    camera at camera_shake
    show but suprais
    but "...?!"
    camera at reset
    "A través de mi conciencia que se desvanecía, escuché una voz familiar."
    
    mc "... Jestyn...?"
    hide but suprais with dissolve
    "En el momento en que Butley se dio cuenta de quién era, inmediatamente me soltó."
    "Jestyn me atrapó antes de que pudiera desplomarme en el suelo."
    
    pup4 "Mierda... ¡él está aquí!"
    show but confuse at left 
    with dissolve
    but "J-J-Jestyn... Yo..."
    but "Yo solo... no era mi intención-"
    show jes normal at right
    with dissolve
    jes "Entiendo lo que intentas decir, Butley, querida."
    jes "Desafortunadamente para ti... tengo ojos."
    hide jes normal with dissolve
    show jespri creep with dissolve
    jes "Y sé exactamente lo que intentabas hacer."
    but "Yo-yo..."
    
    "Butley se movía nerviosamente donde estaba, incapaz de encontrar las palabras."
    
    jes "Les sugiero que todos regresen a sus habitaciones."
    jes "...Antes de que decida hacer algo de lo que te arrepientas."
    
    hide but confuse with dissolve
    "Los otros títeres rápidamente lo agarran por el hombro, indicándoles que se vayan rápidamente. Y sin decir una palabra más, Butley y otros títeres se dieron vuelta y huyeron hacia sus propias habitaciones."
    "Jestyn volvió a centrar su atención en mí y me ofreció una suave sonrisa."
    show jespri nosmile at center
    with dissolve
    jes "¿Se encuentra bien ahora, Su Majestad?"
    
    "Me ayudó a ponerme de pie."
    "Mi cuerpo todavía estaba demasiado débil para sostenerse por sí solo, así que Jestyn tomó mi mano y me estabilizó con una mano contra mi espalda." 
    "Si Jestyn no hubiera aparecido….No quería ni imaginar lo que me habría pasado."
    
    hide screen dark_effect with dissolve
    mc "Jestyn..."
    mc "Gracias..."
    jes "No piense en ello, Su Majestad."
    jes "Parece que Butley y otros títeres te causaron bastantes problemas."
    jes "Por favor perdónalos."
    
    play music "sad.mp3" volume 3.0 fadein 3.0
    "No pensé que sería capaz de actuar normalmente con ellos, especialmente con Butley, la próxima vez que nos encontráramos."
    "Pero… ¿Por qué actuó así tan de repente?"
    "¿Es porque... no quiere que reemplace al rey títere...?"
    
    mc "Jestyn..."
    mc "¿Por qué...? ¿Por qué hizo eso?"
    jes "...¿Por qué Butley se comportó de esa manera?"
    jes "Es una larga historia."
    
    "Hizo una pausa."
    
    jes "Pero me temo que Su Majestad todavía no está en condiciones de resistir. ¿Me harías el honor de descansar un rato en mi habitación?"
    mc "...Está bien."
    
    hide jespri with dissolve
    "Jestyn me asintió levemente y me indicó que siguiera adelante."
    scene bg_corridor
    "Mientras caminábamos, mi mente seguía volviendo a lo que acababa de suceder."
    "Estoy tratando de recordar lo que dijo Butley. Por lo que había dicho Butley... él no quería que reemplazaran al Rey Puppet."
    "Eso significaba que era ferozmente leal al Rey Crownus."
    "Y no solo Butley se sentía así... Podrían haber varios títeres como los títeres que estuvieron con él mientras me atacaba..."
    "...o quizás muchos más de ellos que permanecieron leales al Rey Marioneta y se negaron a aceptarme como su sucesor."
    "......"
    "...Harían cualquier cosa para deshacerse de mí."
    "Un sudor frío se extendió por mi cuerpo mientras una horrible posibilidad tras otra llenaba mi mente."
    "Perdida en mis pensamientos, seguí avanzando sin prestar mucha atención a hacia dónde me dirigía."
    "Mis pies simplemente se movían solos."
    show hand_cover
    "De repente, me estremecí cuando una mano cubrió suavemente mis ojos, sacándome de mi espiral de pensamientos."
    
    jes "Parece que Su Majestad tiene muchas cosas en la cabeza..."
    
    "dijo suavemente."
    
    scene black
    jes "Me gustaría que aclararas tu mente antes de hablar."
    jes "Así que... relájate. Respira lenta y profundamente..."
    
    "Seguí sus instrucciones e inhalé lentamente."
    
    jes "Ahora... déjalo salir suavemente por Tu boca."
    
    "Exhalé lentamente."

    jes "Bueno [gend]."
    jes "Ahora... Permíteme guiarte a mi habitación."
    
    "Manteniendo una mano sobre mis ojos, Jestyn me llevó suavemente hacia su habitación."
    "Y después de caminar un rato, escuché un crujido de puerta al abrirse. Supuse que era la entrada al barrio de los títeres."
    "Una vez que estuvimos dentro, Jestyn continuó guiándome hacia adelante."
    play sound "opendoor.mp3"
    "Un momento después, escuché que se abría otra puerta. Y pensé que debía haber sido la puerta de la habitación de Jestyn."
    "Me condujo suavemente al interior."
    play sound "closedoor.mp3"
    "Tan pronto como escuché que la puerta se cerraba detrás de nosotros, Jestyn quitó su mano de mis ojos, permitiéndome ver de nuevo."
    hide hand_cover with dissolve
    scene bg_priestonroom
    "Y fue entonces cuando finalmente pude ver... la habitación de Jestyn..."
    stop music fadeout 3.0
    "......"
    "Estaba impecablemente ordenado. Estantes de libros se alineaban en las paredes y cruces adornaban casi todos los rincones."
    "La habitación tenía una atmósfera casi sagrada."
    "...Espera... esta no parece la habitación de Jestyn..." 
    "No, esta no es la habitación de Jestyn..."
    
    mc "Jestyn... esto es..."
    show pricg reveal with dissolve
    "Antes de que pudiera girarme para mirarlo, me detuvo suavemente colocando una mano en mi hombro."
    show pricg reveal2 with dissolve
    "Mi corazón comenzó a latir con fuerza."
    "El sudor frío volvió a correr por mi espalda."
    "Algo estaba terriblemente mal."
    
    mc ".........."
    mc "...quien..."
    mc "...¿Quién eres?"
    voice "PRIESTON01_DAY2.ogg"
    who "Tenía muchas ganas de conocerte... hija mía."
    play music "seduction.mp3" volume 3.0 fadein 3.0
    show pricg reveal3 with dissolve
    pause 1.0
    show pricg reveal4 with dissolve
    pause 1.0
    show pricg reveal5 with dissolve
    pause 1.0
    show pricg reveal6 with dissolve
    pause 1.0

    $ voice_duck_start()
    voice "PRIESTON02_DAY2.ogg"
    who "Seguro que me has llamado la atención..."
    voice "PRIESTON03_DAY2.ogg"
    who "Como un conejito curioso, has estado tratando de descubrir qué pasó realmente con este reino... ¿No es así?"
    $ voice_duck_end()

    show pricg revealyey with dissolve
    "Reuniendo cada gramo de coraje que tenía, me di la vuelta lentamente."
    show pricg revealyey2 with dissolve
    "Y ahí estaba él..."
    "Una marioneta con brillantes ojos violetas mirando directamente a mi alma."
    show pricg revealyey3 with dissolve
    "Dejó escapar una suave risita."
    
    show pricg revealyey4 with dissolve
    who "Adoro esa mirada curiosa en Tus ojos."
    hide pricg revealyey4 with dissolve
    "Retiró su mano de mi hombro antes de dar la vuelta para pararse frente a mí, permitiéndome verlo claramente."

    show pri normal with dissolve
    "Frente a mí había un títere vestido de sacerdote."
    "Su largo cabello negro estaba bien cuidado y un único cuerno sobresalía del lado izquierdo de su cabeza."
    "Cada movimiento que hizo fue compuesto y deliberado."
    "Sólo por la forma en que se comportaba, me di cuenta de que era alguien que siempre mantenía una imagen impecable frente a los demás."
    "Y de alguna manera, me puso nervioso."
    
    who "A juzgar solo por mi apariencia, imagino que ya habrás adivinado el papel que desempeño dentro de este reino. Aun así, antes de continuar, permíteme presentarme, hija mía."
    show pri talk 
    pri "Puedes llamarme Prieston. Soy la marioneta Priest del reino."
    show pri normal
    "Dio unos pasos mesurados hacia mí y simplemente me miró fijamente durante unos momentos."
    "Al mirar más de cerca, noté que sus pupilas se parecían a las de una cabra."
    show pri nosmile2 with dissolve
    "Su mirada recorrió lentamente mí, de pies a cabeza, examinando cuidadosamente cada detalle de mi apariencia."
    show pri happy2 with dissolve
    "Después de un breve silencio, finalmente habló. Su sonrisa se amplió."
    
    pri "Interesante..."
    mc "?"
    pri "Un humano tan pequeño... frágil. Y, sin embargo, a pesar de todas esas debilidades... Jestyn todavía te eligió."
    pri "Intrigante... Realmente intrigante... Oh, cómo me pregunto por qué es así."
    show pri creep2 with dissolve
    pri "Esto se ha vuelto mucho más fascinante de lo que había anticipado."
    show pri normal with dissolve
    pri "Te he estado observando. Desde el momento en que entraste por primera vez en este reino. Hasta el momento en que Jestyn te coronó como nuestro nuevo gobernante."
    pri "Y como dije antes, eres como un conejito curioso, con muchas ganas de descubrir todo lo que te rodea."
    show pri nosmile2
    pri "Desafortunadamente... Jestyn no tiene intención de permitirte descubrir lo que realmente sucedió aquí."
    show pri normal
    pri "Tú mismo lo has sentido... ¿no?"
    
    "Mis pensamientos volvieron a todo lo que había sucedido con Jestyn hoy."
    "Realmente me había estado alejando de ciertas cosas."
    "Como si… hubiera algo que él desesperadamente no quería que yo supiera."
    "Intenté pensar en las cosas, pero el mareo de antes aún persistía y mi cuerpo se sentía demasiado débil."
    show pri suprais with dissolve
    "Al ver lo débil que estaba, Prieston me ofreció su mano para ayudarme a levantarme."
    
    show pri talk2 with dissolve
    pri "Ven, hija mía. Déjame guiarte en la silla. Necesitas descansar."
    
    "Después de un breve momento de vacilación..."
    "... Extendí la mano y tomé su mano."
    
    pri "Disculpe."
    
    show pri normal 
    camera at camera_shake
    "Me estremecí de sorpresa cuando Prieston de repente me tomó en sus brazos. Pero yo estaba demasiado débil para cuestionarlo, así que simplemente dejé que me cargara."
    camera at reset
    "Me dejó suavemente en la suave silla."

    show pri talk with dissolve
    pri "¿Quieres un té caliente?"
    
    "El té caliente sonaba reconfortante en mi estado actual, así que asentí." 
    hide pri talk with dissolve
    "Prieston luego se acercó a lo que supuse era su escritorio de trabajo y comenzó a prepararme una taza de té caliente."
    "Mientras se ocupaba preparando el té, Prieston me miraba de vez en cuando para ver cómo estaba."
    "Unos momentos más tarde, Prieston regresó con una taza de té humeante."
    "Antes de tomar un sorbo, percibí el delicado aroma a jazmín que emanaba del té. Mientras bebía, su calidez floral permaneció en mi lengua antes de calmar suavemente mi garganta."
    
    show pri normal with dissolve
    pri "¿Se siente mejor?"
    
    "Asentí."
    
    show pri nosmile2 with dissolve
    pri "¿Todavía te sientes mareado?"
    mc "En realidad no... Pero todavía estoy demasiado débil..."
    
    show pri gentle with dissolve
    "Prieston me dio una suave sonrisa antes de acariciarme suavemente la cabeza."

    show pri normal with dissolve
    pri "Que pobre corderito..."
    "Fue extraño. Solo había conocido a este títere hace unos minutos, pero de alguna manera... me sentí a gusto con él."
    "... ¿Es realmente seguro sentirse así...? Dado que esta es la primera vez que lo conozco..."
    hide pri normal with dissolve
    show pri table normal with dissolve
    "Luego tomó asiento también al otro lado de la mesa."
    "Este títere... por alguna razón, no podía quitarme la sensación de que estaba envuelto en un velo de misterio."
    "Tal como lo habían descrito Wizzy, Knighter y Butley, la forma en que trabajaba su mente era difícil de predecir."
    "Y eso sólo me hizo querer saber qué estaba realmente pasando dentro de su cabeza."

    jump prieston_ask


label prieston_ask:
    show pri table normal 
    menu:
        "¿Por qué me ayudaste?":
            mc "¿Por qué me ayudaste?"
            
            "Él se rió entre dientes."
            
            show pri table amused with dissolve
            pri "¿No tengo derecho a ayudar a alguien aquí?"
            pri "Hija mía... Debo admitir que no esperaba una pregunta como esa después de haber renunciado tan voluntariamente a mi tiempo para ayudarte."
            
            "Maldita sea... Ahora me siento culpable por preguntar algo tan sin rodeos..."
            
            mc "...lo siento. Y... gracias por ayudarme antes."
            show pri table normal with dissolve
            pri "Jaja... Hija mía, solo te estaba tomando el pelo un poco. Por supuesto que mereces saber por qué."
            pri "Además... ahora eres el [title] de este reino."
            pri "Ahora bien, volvamos a tu pregunta. ¿Me preguntaste por qué te ayudé?"
            pri "No hubo ninguna razón en particular."
            pri "Simplemente te vi... parado solo en ese escenario, rodeado por una multitud de marionetas hambrientas."
            pri "Y allí estabas, justo en medio de ellos... indefenso, necesitando que alguien te extendiera una mano."
            
            show pri table annoy with dissolve
            "Prieston colocó una mano sobre su pecho, un gesto tranquilo que hablaba de su sinceridad."
            "La sonrisa de su rostro se desvaneció y fue reemplazada por una expresión solemne."
            
            pri "Simplemente no pude, hija mía."
            $ voice_duck_start()
            voice "PRIESTON04_DAY2.ogg"
            pri "No podría soportar ver a alguien tan vulnerable... y tan puro como tú... quedar en tal peligro."
            $ voice_duck_end()
            show pri table annoy2 with dissolve
            pri "Soy un sacerdote títere."
            pri "Es mi deber ayudar a los que sufren."
            pri "Sin excepción."
            
            show pri table normal with dissolve
            "Su suave sonrisa regresó como si nunca se hubiera ido."
            
            pri "¿Eso responde a tu pregunta, hija mía?"

            menu:
                "Yes":
                    "Ahora que lo pienso... su explicación tenía mucho sentido. ¿Por qué necesitaría alguna razón más profunda sólo para ayudarme...?"
                    "Sentí como si estuviera sospechando injustamente de él."
                    
                    mc "Sí... eso responde a mi pregunta."
                    mc "Lo siento si soné como si no confiara en ti."
                    show pri table amused with dissolve
                    pri "Está muy bien, hija mía. Entiendo por qué eres tan cauteloso. Nos acabamos de conocer. Es natural."
                    pri "Uno no debería confiar en alguien que acaba de conocer. Aun así, te puedo asegurar... que no te haré daño."
                    pri "Tenemos mucho tiempo para conocernos unos a otros."

                    jump prieston_ask


                "No":
                    "Por mucho que quisiera creerle, no podía quitarme la sensación de que algo estaba... mal."
                    "Sentí como si hubiera otra razón... una escondida debajo de la explicación que acababa de darme."
                    "Algo no estaba bien."
                    show pri table gentle with dissolve
                    "Prieston notó la duda escrita en mi rostro. Su expresión se suavizó casi de inmediato."
                    
                    pri "Está bien, hija mía. Entiendo si aún no confías en mí. Después de todo, nos acabamos de conocer."
                    pri "Uno no debería confiar en alguien que acaba de conocer. Aun así, te puedo asegurar... que no te haré daño."
                    pri "Tenemos mucho tiempo para conocernos unos a otros."

                    jump prieston_ask

        "¿Qué opinas sobre Crownus?":
            mc "¿Qué opinas de Crownus?"
            show pri table amused with dissolve
            pri "Pareces bastante interesado en Crownus, hija mía."
            mc "Lo soy... y no es solo eso..."
            mc "Lo que pasó antes me hizo darme cuenta de que algunos de los títeres de este teatro todavía son ferozmente leales a Crownus."
            mc "Tan leales, de hecho... que estaban dispuestos a matarme."
            
            "Hice una pausa por un momento, eligiendo cuidadosamente mis palabras, o al menos las que me parecía más seguro decir frente a Prieston."
            
            mc "Entonces... quería preguntar... ¿qué piensas de Crownus?"
            mc "Y... ¿eres tú uno de los títeres que le son leales?"
            show pri table normal2 with dissolve
            pri "Mmm... ya veo."
            
            "Hizo una pausa por un momento, sus ojos mirándome sin una sola mirada antes de que finalmente comenzara a hablar."
            
            pri "Cuando pienso en Crownus..."
            pri "Sólo me viene a la mente una palabra."
            pri "Fascinante."
            mc "... ¿Fascinante?"
            pri "De hecho."
            show pri table amused2 with dissolve
            pri "Cómo pudo capturar los corazones de tantos..."
            show pri table normal2
            pri "Cómo logró reunir tantos seguidores..."
            show pri table gentle2 with dissolve
            pri "Cómo inspiró una lealtad tan inquebrantable en ellos..."
            show pri table creep2 with dissolve
            pri "Y… hacia dónde pretendía llevar a esos seguidores al final."
            pri "Todo esto me parece... absolutamente fascinante."
            pri "En aquel entonces... quería ver cómo llegarían a su fin las ambiciones de Crownus."
            
            show pri table normal with dissolve
            "......"
            
            mc "¿Eso significa... que eres uno de los títeres leales a Crownus?"
            show pri table gentle with dissolve
            pri "Entonces permíteme devolverte esa pregunta, hija mía."
            pri "¿Qué piensas TÚ?"

            menu:
                "Él es el fiel seguidor de Crownus.":
                    mc "......"
                    mc "Creo... que eres uno de los fieles seguidores de Crownus."
                    
                    show pri table amused with dissolve
                    "La sonrisa de Prieston se amplió y una de sus cejas se arqueó con genuino interés ante mi respuesta."
                    
                    pri "¿Es así?"
                    pri "Entonces, ¿te importaría decirme por qué piensas eso?"
                    mc "Por la forma en que hablas de Crownus..."
                    mc "Y por las cosas que encuentras tan fascinantes sobre él..."
                    mc "Tengo la sensación de que eres uno de sus seguidores más leales."
                    mc "Parece que... lo admiras."


                "Él no es el fiel seguidor de Crownus.":
                    mc "......"
                    mc "Creo... que no eres uno de los fieles seguidores de Crownus."
                    
                    show pri table amused with dissolve
                    "La sonrisa de Prieston se amplió y una de sus cejas se arqueó con genuino interés ante mi respuesta."
                    
                    pri "¿Es así?"
                    pri "Entonces, ¿te importaría decirme por qué piensas eso?"
                    mc "Porque... si realmente fueras uno de los fieles seguidores de Crownus, no me habrías salvado."
                    mc "Quiero decir... cuando Butley y los otros títeres me atacaron y trataron de devorarme... no te uniste a ellos."
                    mc "Entonces, aunque encuentres fascinante a Crownus... el hecho de que hayas elegido salvarme hace que sea difícil para mí verte como uno de ellos."

            mc "Lo siento... no estoy seguro si me estoy explicando muy bien."
            show pri table gentle with dissolve
            pri "No hay necesidad de disculparte, hija mía. Entiendo exactamente lo que quieres decir."
            pri "Y debo decir... agradezco tanto su respuesta como su observación."
            mc "Entonces... ¿tenía razón?"
            show pri table normal with dissolve
            pri "La respuesta, hija mía... es paciencia."
                    
            "No pude evitar hacer pucheros."
                    
            mc "....Eso no responde a mi pregunta..."

            show pri table amused with dissolve        
            "Él se rió de mi reacción."
                    
            pri "Hmm... qué cosita más adorable y curiosa."
            pri "Pero a veces... la paciencia es la clave."

            "¿Qué significa eso siquiera...?"

            jump prieston_ask

        "¿Qué opinas sobre Jestyn?":
            mc "¿Qué opinas de Jestyn?"
            show pri table gentle with dissolve
            pri "Ah... Jestyn. El querido títere bufón del reino."
            pri "Una marioneta que es casi imposible de controlar... pero que de alguna manera mantiene vivo el espíritu de este reino."
            show pri table normal with dissolve
            pri "¿Tienes curiosidad por él?"
            
            "Asentí sin dudarlo."
            
            mc "Antes dijiste que Jestyn no quiere que aprenda ciertas cosas... y he tenido la sensación de que me está ocultando algo."
            mc "Y luego está lo que me dijo Butley... que Jestyn sólo me está utilizando a mí. Manipulándome."
            mc "Entonces... ya no sé qué creer. ¿Es todo eso cierto?"
            pri "Ya veo."
            pri "Me temo que sólo puedo contarles un hecho sobre ese hombre."
            pri "Jestyn odia a Crownus."
            
            "Mis ojos se abrieron ante esas palabras. Así que todo este tiempo..."
            
            show pri table talk with dissolve
            pri "Si has estado prestando atención a su comportamiento, probablemente hayas notado que siempre evita decir el nombre de Crownus..."
            pri "E insiste en que los demás títeres eviten hablarlo también."
            show pri table normal with dissolve
            mc "......"
            mc "¿Por qué odia a Crownus? Por lo que me dijo Wizzy, Crownus era un mentiroso. ¿Es por eso?"
            mc "Pero Butley dijo que él era su salvador... entonces... ¿quién dice la verdad?"
            pri "Puedo ver que tu mente está llena de preguntas."
            pri "Pero primero te sugiero que te calmes."
            pri "Es difícil pensar con claridad cuando estás abrumado, ¿no?"
            show pri table gentle with dissolve
            pri "Respira lenta y profundamente."
            
            "Siguiendo las instrucciones de Prieston, inspiré profundamente por la nariz y luego exhalé lentamente por la boca."
            "Tenía razón... No había manera de que pudiera pensar con claridad mientras mi mente estaba tan llena de ruido."
            show pri table normal with dissolve
            "Una vez que vio que me había calmado, Prieston asintió levemente antes de continuar."
            
            pri "Preguntaste cuál de ellos dice la verdad."
            pri "La única respuesta que realmente importa... es la que llegas a ti mismo."
            pri "Tú eres quien debe decidir qué es verdad... y qué es falso."
            
            "Sus palabras sólo me dejaron aún más confundido."
            "¿Por qué tenía que ser yo? ¿Por qué era yo quien tenía que decidir qué estaba bien y qué estaba mal?"
            "Necesitaba saber más."
            
            mc "Entonces... volvamos a la pregunta original."
            mc "¿Qué opinas de Jestyn?"
            
            show pri table amused with dissolve
            "Él se rió entre dientes."
            
            pri "¿Qué pienso de Jestyn...?"
            pri "Es como una oruga."
            mc "¿Un qué? ¿Oruga?"
            pri "Sí."
            pri "Una pequeña oruga inofensiva... inocente, ingenua, que no sabe nada más que comer hojas."
            pri "Luego, poco a poco, esa inocente oruga se envuelve en un capullo."
            pri "Y cuando el capullo finalmente se abre... la oruga emerge como algo completamente diferente."
            show pri table gentle with dissolve
            pri "Una mariposa."
            show pri table normal with dissolve
            pri "Así veo a Jestyn."
            
            "Prieston habló con tal convicción filosófica que tuve que pensar detenidamente para seguir el ritmo de lo que decía."
            "Estudió mi expresión por un momento. Aparentemente satisfecho por lo que vio, continuó."
            
            pri "Jestyn... es el hombre más amable e inocente que he conocido."
            pri "Todo lo que siempre ha querido... es que todos sean felices."
            pri "Quizás, desde donde estás ahora, veas a Jestyn como un títere travieso... sarcástico... aficionado a burlarse de los demás... tal vez incluso un poco malvado."
            show pri table nosmile2 with dissolve
            pri "Pero el Jestyn ya sabes... no es el mismo Jestyn que yo conozco, hija mía."
            pri "Después de todo... he vivido mucho más que tú."
            pri "Para mí, sigue siendo el mismo Jestyn que siempre he conocido..."
            pri "Simplemente lleva... una cara diferente."
            show pri table gentle2 with dissolve
            pri "Y eso es precisamente lo que hace a ese hombre tan fascinante."
            show pri table normal with dissolve
            pri "Eso es todo lo que pienso sobre Jestyn. Espero que eso alimente tu curiosidad, hija mía."

            "No. Eso sólo añade más a mi curiosidad."
            "Pero incluso si vuelvo a preguntar, no creo que me dé una respuesta concreta."

            jump prieston_ask

        "quiero saber más sobre ti":
            mc "Me gustaría saber más sobre ti."
            show pri table amused with dissolve
            pri "Mmmm~?"
            
            "La sonrisa de Prieston se amplió. Sus ojos se entrecerraron mientras me miraba, agudo pero divertido, mientras apoyaba cómodamente su barbilla en una mano."
            
            pri "Mi, mi..."
            pri "¿Quieres saber más sobre mí?"
            pri "No tenía idea de que era tan misterioso a tus ojos, hija mía."
            show pri table amused2 with dissolve
            pri "Nosotros dos, sentados aquí en la misma mesa... solos... disfrutando tranquilamente de la compañía del otro... Alguien podría tener una idea equivocada, ¿no crees?."
            show pri table normal2 with dissolve
            pri "...Aunque no me importaría exactamente si lo hicieran."
            
            "Mi rostro se calentó solo con sus palabras... y, sinceramente... no estaba del todo equivocado."
            "Nunca esperé que un títere, y mucho menos uno con el papel de sacerdote, coqueteara tan descaradamente."
            "... ¿O simplemente estaba leyendo demasiado sobre ello?"

            pri "Ahora bien... ¿qué es lo que te gustaría saber de mí, hija mía?"
            mc "Sólo... cosas simples."
            mc "Los otros títeres me dijeron que rara vez sales de tu habitación, así que me preguntaba por qué."
            mc "¿Eres introvertido?"
            
            show pri table nosmile with dissolve
            "Prieston hizo una pausa para pensar por un momento."
            
            pri "¿Mmm? ¿Un introvertido?"
            show pri table nosmile2 with dissolve
            pri "No estoy seguro de entender lo que eso significa, hija mía."
            pri "Pero la razón por la que rara vez salgo de mi habitación es bastante simple. Simplemente no tengo muchas razones para salir."
            pri "Prefiero disfrutar de una taza de té en la comodidad de mi habitación."
            pri "Aunque no siempre estoy aquí. De vez en cuando salgo a charlar con los otros títeres. Pero aun así, todavía no salgo tan a menudo."
            mc "¿Eres cercano a muchos de los otros títeres?"
            pri "No particularmente. Los respeto a todos como amigos comunes y corrientes."
            pri "Con quien hablo más a menudo es Wizzy. Es amable por naturaleza y se lleva bien con casi todo el mundo."
            pri "Entonces... se podría decir que no soy especialmente cercano a los demás."
            
            "Entonces sería difícil aprender mucho sobre él de los otros títeres si ni siquiera ellos apenas lo conocían."
            "Me gustara o no, tendría que descubrir las respuestas yo mismo."
            "Aún así, no quería que pareciera que lo estaba interrogando."
            "Así que hice lo mejor que pude para mantener la conversación informal."
            
            mc "Eres bastante misterioso, ¿no?"
            show pri table gentle with dissolve
            pri "Lo tomaré como un cumplido. Muchas gracias."
            mc "Si pasas la mayor parte del tiempo en tu habitación… ¿qué sueles hacer ahí dentro?"
            show pri table nosmile with dissolve
            pri "No mucho."
            pri "Tomo té... leo libros, escribo, ordeno mi habitación, tejo... Eso es todo, supongo. Estaría mintiendo si dijera que hay mucho que hacer en mi habitación."
            pri "La verdad es... realmente no lo hay."
            
            "Fue casi divertido. De todos los títeres con los que había hablado, la mayoría pasaba el día leyendo, escribiendo o bebiendo té."
            "Parecía que realmente no tenían mucho más que hacer, ¿eh? Pero eso tiene sentido."
            "Perdido en mis pensamientos, de repente me di cuenta de que Prieston no había apartado la mirada de mí ni una sola vez."
            
            show pri table normal with dissolve
            pri "Ya sabes, hija mía..."
            pri "No hay mucho que hacer en mi habitación."
            pri "Pero ahora que estás aquí..."
            show pri table amused2 with dissolve
            pri "Quizás podrías convertirte en mi nuevo pasatiempo."
            
            "Sus palabras fueron tan ambiguas que no pude evitar sentir un aleteo de anticipación."
            
            mc "¿Q-Qué quieres decir...?"
            show pricg poke with dissolve
            pause 0.7
            show pricg poke2 with dissolve
            pri "Lo que quiero decir es... deberíamos hablar más a menudo, Su Majestad."
            pri "Ahora eres el [title] de este reino. Y como es [title], es natural que sepas cómo les va a tus sujetos, ¿no te parece?"
            show pricg poke3 with dissolve
            pri "Yo no soy una excepción."
            show pricg poke4 with dissolve
            pri "Aún así... no parece justo si eres el único que sabe de mí... y cómo estoy."
            pri "Entonces, como uno de tus sujetos... me gustaría tener la oportunidad de conocerte también."
            
            $ voice_duck_start()
            voice "PRIESTON05_DAY2.ogg"
            pri "Después de todo, es mi deber comprender cada parte de ti... tus pensamientos, tus preocupaciones, tus deseos. Escucharé cada palabra sin juzgar."
            $ voice_duck_end()
            pri "Guiar a aquellos que han perdido el rumbo es para lo que fui creado."
            pri "Así que... si alguna vez deseas hablar de algo... ven a verme. Llama a mi puerta... y siempre te la abriré."
            
            "La voz de Prieston se hizo más baja con cada palabra. Hipnótico, atractivo... casi lo suficientemente seductor como para que sea difícil rechazarlo."
            "...Pero si esta era la única manera de entender realmente cómo pensaba Prieston... entonces no me importaba en absoluto."
            hide pricg poke4 with dissolve
            jump prieston_ask


        "tengo sueño..":
            jump prieston_convo2

label prieston_convo2:
    "De repente… mis párpados comenzaron a sentirse pesados."
    
    pri "Ah... parece que te está entrando sueño, hija mía."
    pri "Eso es natural después de todo lo que has pasado. Necesitas recuperar tus fuerzas."
    
    hide pri table with dissolve
    show pri nosmile with dissolve
    "Prieston se levantó de su silla y se acercó a mí."
    
    pri "Disculpe."
    camera at camera_shake
    
    "Suavemente me tomó en sus brazos una vez más y me recostó en su cama."
    camera at reset
    "El colchón era suave y cómodo. Sentí que podía quedarme dormido en cualquier momento."
    show pri normal with dissolve
    pri "Hmm... ¿Qué tal si te cuento un cuento de hadas, hija mía?" 
    
    "....."
    
    mc "Eso... suena bien." 
    hide pri normal with dissolve
    "Regresó a la mesa y se quitó la bufanda antes de regresar a la cama."
    show pricg bed smile with dissolve
    "Lo último que esperaba era que Prieston se tumbara de repente a mi lado."
    "Se volvió hacia mí y levantó la cabeza con una mano mientras me miraba."
    "Su mano izquierda descansaba contra mi espalda, dándome palmaditas lentas y suaves como si intentara adormecerme." 
    "Una persona normal probablemente se sorprendería o incluso se asustaría si alguien a quien había conocido hace sólo unos minutos de repente se acostara a su lado y le acariciara suavemente la espalda."
    "Pero creo que tenía demasiado sueño para sentir algo de eso. Esta vez, mi cansancio y mi somnolencia realmente habían ganado."
    
    show anim pri cg bed
    pri "¿Te gustan los animales, hija mía?"
    mc "Eso creo..."
    pri "Entonces quizás disfrutes de este cuento de hadas."
    hide anim pri cg bed with dissolve
    show pricg bed close with dissolve
    pri "Cuando este reino todavía estaba vivo, nosotros, los títeres, solíamos contar esta historia a los niños."
    mc "...¿Los niños también venían aquí?"
    show pricg bed smile with dissolve
    pri "Lo hicieron. Aunque tenían sus propias sesiones, por supuesto. Las historias que les contamos a los adultos habrían sido demasiado difíciles de entender para los niños."
    pri "Entonces, de vez en cuando, les contábamos cuentos de hadas sobre animales."
    
    "No pude evitar preguntarme cómo había sido el Kingdom of Marionettes cuando todavía estaba lleno de vida."
    
    show pricg bed smile5 with dissolve
    pri "Cierra los ojos, hija mía. Empezaré la historia."
    
    stop music fadeout 3.0
    show merem
    "Seguí sus instrucciones y cerré los ojos."
    "........."
    scene black
    pri "¿Te sientes cómodo?"
    mc "Mmm..."
    voice "PRIESTON06_DAY2.ogg"
    pri "Ahora... quiero que imagines algo para mí. ¿Puedes hacer eso, hija mía?"
    mc "Si...."
    pri "Bueno..."
    pri "Ahora imagina un bosque."
    play music "morning.mp3" volume 3.0
    scene anim fairytale with dissolve
    pri 'A vast, beautiful forest... lush and green, with trees stretching high above your head.'
    pri "¿Puedes verlo?"
    mc "Sí."
    pri "Bueno..."
    pri "Ahora... escuche atentamente. ¿Qué crees que encontrarías en un bosque como ese?"
    mc "mmmm...."
    show dog_fairytale with dissolve
    pri "¿Quizás un perro?"
    show owl_fairytale with dissolve
    pri "¿Búho?"
    show snake_fairytale with dissolve
    pri "¿Serpiente?"
    show elep_fairytale with dissolve 
    show squirel_fairytale with dissolve
    pri "¿O... elefantes, ardillas y otros animales?"
    pri "Tantas pequeñas criaturas, cada una viviendo su propia vida tranquila."
    pri "¿Puedes imaginártelos, hija mía?"
    mc "Yo puedo."
    pri "Maravilloso."
    pri "Ahora... dirijamos nuestra atención a dos criaturas en particular. Primero... un león."
    pri "Fuerte. Orgulloso. Una criatura que llama la atención simplemente entrando a la habitación."
    show lion_fairytale with dissolve
    pri "Ah, sí. Y el león tiene pelaje rosa."
    mc "Que absurdo..."
    pri "Pero adorable, ¿no?"
    mc "Sí..."
    show bunny_fairytale with dissolve
    pri "Y a su lado... Un conejito. Pequeño... gentil... aparentemente inofensivo."
    pri "¿Puedes verlos?"
    mc "Sí..."
    pri "Bien."
    hide lion_fairytale with dissolve
    hide bunny_fairytale with dissolve
    hide dog_fairytale with dissolve
    hide owl_fairytale with dissolve
    hide snake_fairytale with dissolve
    hide elep_fairytale with dissolve
    hide squirel_fairytale with dissolve
    show lionking_fairytale with dissolve
    pri "Ahora, hija mía... quiero que imagines algo asombroso. Ese león... lleva una corona."
    mc "Jeje... eso es genial."
    pri "¿No es así?"
    hide lionking_fairytale with dissolve
    pri "Ahora, comencemos nuestra historia."


    pri "Érase una vez, en lo profundo de un frondoso bosque... vivían muchos animales."
    show dog_fairytale with dissolve
    show owl_fairytale with dissolve
    show snake_fairytale with dissolve
    show elep_fairytale with dissolve
    show squirel_fairytale with dissolve
    pri "Había perros, búhos, leones, serpientes y muchas otras criaturas."
    show lionking_fairytale with dissolve
    pri "Y todos estaban gobernados por un rey poderoso... el Rey León."
    hide lionking_fairytale with dissolve
    show lovelionking_fairytale with dissolve
    pri "Bajo el reinado del Rey León, los animales del bosque vivieron vidas prósperas y nunca les faltó comida."
    pri "El Rey León era muy querido por sus súbditos, ya que siempre deseó darles la mejor vida posible."
    pri "Todos los animales del bosque estaban felices."
    hide lovelionking_fairytale with dissolve
    hide dog_fairytale with dissolve
    hide owl_fairytale with dissolve
    hide snake_fairytale with dissolve
    hide elep_fairytale with dissolve
    hide squirel_fairytale with dissolve
    show anim feast fairytale with dissolve
    pri "Un día llegó el momento de la fiesta anual del bosque."
    pri "Desafortunadamente, la fiesta era siempre la misma año tras año. El menú nunca cambió."

    show bunnythink with dissolve
    pri "El conejo creía que su comida podría ser incluso mejor de lo que ya era."
    show bunnythink2 with dissolve
    pri "Y... encontró una manera de hacer que eso sucediera. Al menos, creía que era una idea brillante."
    pri "Entonces el Conejo presentó su brillante idea al Rey León."
    hide bunnythink2 with dissolve
    hide bunnythink with dissolve
    show lionbunny with dissolve
    pri "'¡Su Majestad! ¡Sé cómo podemos tener una fiesta completamente nueva este año!' exclamó el Conejo."
    hide lionbunny with dissolve
    show lionbunny2 with dissolve
    pri "Pero, lamentablemente, el Rey León se negó. Descartó la idea del Conejo como una tontería, insistiendo en que la comida que ya tenían era más que suficiente."
    pri "'La fiesta de este año seguirá siendo exactamente como está. No habrá cambios. No aceptaré una idea tan ridícula\", dijo el Rey León."
    pri "Pero el Conejo siguió suplicando al Rey León, insistiendo en que todos los animales del bosque merecían una mejor comida."
    pri "Desafortunadamente... el Rey León todavía se negó."
    hide lionbunny2 with dissolve
    show bunnymad with dissolve
    pri "A medida que pasó el tiempo, la frustración del Conejo poco a poco se convirtió en ira. Pero tenía otra idea."
    pri "Como no logró convencer al Rey León, decidió presentar su idea a los animales del bosque."
    hide bunnymad 
    pri "\"Si no puedo convencer al Rey León, convenceré a los animales del bosque\", dijo el Conejo."
    
    stop music fadeout 3.0
    play sound "glitch.mp3"
    show anim glitch fairytale
    pause 1.0
    pri "Y tal como esperaba, todo el bosque quedó asombrado cuando el conejo sirvió un nuevo tipo de comida. Una comida diferente a todo lo que habían probado antes."
    scene bg_darkfairytale
    hide anim glitch fairytale
    play music "fairy tale.mp3" volume 3.0 fadein 3.0
    pri "Algunos lo llamaron genio. Otros lo aclamaron como un salvador. Y uno a uno... los animales empezaron a seguir al Conejo."
    show animals_fairytale with dissolve
    pri "Cuando el Rey León escuchó lo sucedido, se puso furioso. Advirtió a los animales que este no era un alimento que deberían comer."
    show lionbunny3 with dissolve
    pri "'¡Para! ¡Esta no es la comida que debemos comer! ¡Esto está mal!' El Rey León gritó a sus súbditos."
    pri "Pero, lamentablemente, el Rey León no logró convencerlos. En cambio, el Conejo le devolvió la culpa al rey delante de todos."
    pri "'¡El Rey León no quiere que tengamos mejor comida! ¡Nunca se ha preocupado realmente por ninguno de nosotros! ¡Por eso rechazó mi plan!'"
    pri "¡Escúchenme todos! ¡Solo quiero que tengamos mejor comida que la que siempre hemos tenido! ¿No es eso lo que todos ustedes también quieren? ¿No estás cansado de comer lo mismo una y otra vez? Entonces, ¿qué hay de malo en querer algo mejor? declaró el Conejo."
    pri "¡EL REY LEÓN ES EL TRAIDOR!"
    hide lionbunny3 with dissolve
    show darkanimals_fairytale with dissolve
    hide animals_fairytale with dissolve
    pri "En ese mismo momento... cada par de ojos en el reino se volvieron hacia el rey con miradas frías y acusadoras."
    show anim lionfall 
    pri "Al final, el pueblo denunció al rey y lo derrocó... arrojándolo de su trono."
    pri "Y en su lugar, coronaron al Conejo... como su nuevo Rey León."
    pri "¿En cuanto al ex Rey León?... se convirtió en el juguete del nuevo Rey León."
    scene black with dissolve
    hide anim lionfall
    pri "Qué destino más trágico para el pobre ex Rey León..."
    
    stop music fadeout 3.0
    "........"
    
    pri "...Parece que te has quedado dormido, hija mía. Me alegro que esta historia haya podido adormecerte."

    "Dejó escapar una suave risita."
    
    pri "Hmm~... Me pregunto cuál será tu respuesta..."
    pri "¿Quién estaba realmente equivocado... y quién tenía razón?"
    pri "El León... o el Conejo..."
    pri "Hija mía... como puedes ver, al final... cada uno tiene sus propios deseos."
    pri "Pero ahora... eres nuestro [title]."
    pri "El futuro de todos nosotros está en tus manos." 
    pri "Una cosita tan poderosa... Todo ese poder está en tus pequeñas manos."
    pri "La elección es tuya. Y te guiaré siempre que me necesites."
    pri "Y espero ver cómo termina tu historia..."
    
    "........"
    "............"
    
    scene bg_priestonroom with dissolve
    pause 5.0
    show pri amused2 with dissolve
    pri "........."
    show pri gentle with dissolve
    pri "Entonces... finalmente has llegado, Jestyn."
    
    show pri normal at center_to_right
    show jes3 furious at left
    with dissolve
    "Jestyn miró a Prieston, con los ojos ardiendo de ira. Especialmente cuando vio el [player_call] tirado a su lado."
    "Los celos y la rabia estaban escritos en todo su rostro."
    
    jes "Prieston."
    jes "¿Qué le hiciste a [player_call]...?"
    
    play music "sad.mp3" volume 3.0 fadein 3.0
    show pri happy with dissolve
    "Prieston respondió a la mirada asesina de Jestyn con nada más que una sonrisa."
    "Luego se levantó de la cama y con cuidado levantó al MC en sus brazos."
    "Después de eso, Prieston se acercó a Jestyn."
    
    show pri amused with dissolve
    pri "No hice nada. Simplemente dejo descansar a [player_call]. [subj] casi muere después de ser devorado por Butley y otros títeres."
    
    show jes3 sadsuprais with dissolve
    "Los ojos de Jestyn se abrieron mientras apretaba los dientes."
    
    show pri normal with dissolve
    pri "Todo está bien ahora."
    
    "Prieston entregó suavemente [player_call] a Jestyn."
    
    pri "Tengo la sensación de que las cosas sólo se volverán más complicadas a partir de aquí."
    show pri gentle with dissolve
    pri "Así que cuiden bien de nuestra Majestad, Jestyn."
    
    show jes3 sad with dissolve
    "Sosteniendo al MC con fuerza en sus brazos, Jestyn salió silenciosamente de la habitación de Prieston."
    hide jes3 with dissolve
    hide pri with dissolve
    "Justo cuando llegaba a la puerta, Jestyn se detuvo de repente."
    
    show jes3 sad with dissolve
    jes "Prieston."
    jes "Estoy agradecido de que haya salvado a Su Majestad."
    jes "Pero..."
    
    show jes3 annoy with dissolve
    "Jestyn se giró, fijando a Prieston con una mirada grave."
    
    jes "Eso no significa que confíe en ti."
    
    hide jes3 with dissolve
    show pri happy2 with dissolve
    "Prieston respondió tanto a la mirada sospechosa de Jestyn como a sus palabras con nada más que una risa relajada."
    
    pri "Por supuesto, Jestyn."
    show pri amused2 with dissolve
    pri "Eres libre de sospechar de mí tanto como quieras. No me importa."
    show pri normal with dissolve
    pri "Hasta que nos volvamos a encontrar."

    scene black with dissolve
    hide pri 
    
    play sound "footstep.mp3" 
    "......."
    "........"
    show jescg anxiety with dissolve
    jes "......"
    play sound "movement.mp3" volume 3.0 
    jes "...Aquí tienes...."
    jes "Estás a salvo aquí..."
    jes "En mi habitación..."
    jes "....."
    show jescg anxiety2 with dissolve
    jes "...Lo siento, Su Majestad... Lo siento."
    jes "Nunca debí dejarte sola... debí haberte ignorado y seguir siendo el mocoso que siempre fui..."
    $ voice_duck_start()
    voice "JESTYN07_DAY2.ogg"
    jes "Sólo imaginándolos devorándote... jadeo... tu cuerpo sin vida tirado allí... no queda nada más que tu caparazón congelado, tan frío como el hielo del Ártico... yo... jadeo... No puedo... jadear..."
    $ voice_duck_end()
    jes "No volveré a cometer el mismo error."
    jes "...Yo... simplemente no quería que te asustaras... y te fueras..."
    jes ".....No quiero que sepas más de lo que deberías saber..."
    jes "No sabía cómo iba a decírtelo..."
    jes "Yo......"
    jes "......."
    show jescg anxiety3 with dissolve
    jes "Estaba planeando contarte todo... después de que te convirtieras en nuestro [title]... pero..."
    jes "...Cuanto más tiempo paso contigo... más temo por tu seguridad."
    jes "¿Qué pasaría si desaparecieras simplemente porque aprendiste demasiado...? ¿Qué te pasaría si siguieras profundizando más?"
    show jescg anxiety4 with dissolve
    jes "Tengo miedo."
    jes "Ha pasado tanto tiempo desde que sentí miedo... ansiedad... y paranoia, todos juntos de esta manera..."
    jes "Y ahora... este sentimiento... este nuevo y extraño sentimiento..."
    jes "Cuando no quieres que alguien querido para ti esté en peligro... y siempre deseas estar a su lado..."
    jes "...Ahora entiendo... este debe ser el sentimiento que llaman amor... ¿no es así?"
    jes "Claro... claro que esa es la razón... si..."
    jes "Todo porque mi amor por ti se ha vuelto mucho más fuerte de lo que jamás imaginé..."
    jes "Sé que estos sentimientos llegaron demasiado rápido. Sé que no tienen ningún sentido."
    jes "Pero por favor... créeme. Puedo sentir, en lo profundo de mi corazón, que cada uno de ellos es genuino."
    jes "Eres el único amor que he tenido... y quiero que te quedes a mi lado para siempre."
    jes "Por eso..."
    jes "..... "
    show jescg anxiety5 with dissolve
    jes "....."
    show jescg anxiety6 with dissolve
    pause 1.0
    show jescg anxiety7 with dissolve
    pause 1.5
    show jescg anxiety8 with dissolve
    jes "....."
    jes "No.... No..."
    jes "Ten paciencia, Jestyn. No puedes hacer eso mientras [poss] majestad está dormida. [poss] majestad nunca te dé permiso para hacerlo... puedes esperar."
    jes "Sólo un poco más."
    jes "...Contrólate, bufón tonto."
    show jescg anxiety7 with dissolve
    jes "......"
    show jescg anxiety9 with dissolve
    jes "Sí... sí, puedo esperar."
    jes "Hasta que llegue ese día, seguiré protegiéndote."
    jes "Mientras esté aquí, no dejaré que nadie te ponga un dedo encima..."
    stop music fadeout 3.0
    jes "Mi amor."
    scene black with dissolve

    jump credits


label credits:

    window hide
    $ quick_menu = False

    scene black
    with fade

    play music "bgs_medieval normal.mp3" volume 3.0 fadein 2.0

    pause 1.0

    show text "{size=60}{b}{color=#ff0000}REINO DE LAS MARIONETTES{/b}{/size}{/color}\n\nCreado por Thepipi\nMúsica de Pixabay" at truecenter with dissolve

    pause 

    hide text
    with dissolve

    show text "{size=60}{b}{color=#ff0000}ACTORES DE VOZ{/b}{/size}{/color}\n\nJestyn y Prieston por ShadowCarnival\nWizzy y Knighter por Erik Smith\nCrownus por Seraphim" at truecenter with dissolve
    
    pause

    hide text
    with dissolve

    show text "{size=60}{b}{color=#ff0000}GRACIAS ESPECIALES A FOR{/b}{/size}{/color}\nProbadores beta y a todos por apoyar a Kingdom Of Marionettes." at truecenter with dissolve

    pause
    stop music fadeout 3.0
    return
