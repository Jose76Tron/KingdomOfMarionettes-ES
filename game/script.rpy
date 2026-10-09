# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

default asked_clean = False
default asked_check = False
default choice = ""
default first_delay = False
default cursed_route = False
default hovering_choice = ""
default met_knighter = False

# The game starts here.

label splashscreen:

    scene black
    with fade

    show text "{size=70}{b}{color=#ff0000}WARNING{/color}{/b}{/size}\n\nEste juego contiene malas palabras leves, efectos de vibración de la pantalla, comportamiento manipulador, \ndinámicas de relaciones tóxicas, Jumpscare, comportamiento obsesivo, BDSM ligero y contenido sugerente.\n\nSe recomienda discreción del jugador." at truecenter
    with dissolve

    pause

    return


label start:


    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg_fill onlayer fill
    scene black


    "¿Quién iba a pensar que acabaría atrapado en una situación tan extraña?"
    "Todo empezó porque buscaba trabajo a la desesperada."
    "Y no era para menos. Mis ahorros se agotaban y aún tenía un montón de gastos y deudas por pagar."
    "Eché currículums en todas partes, pero parecía que la suerte me odiaba."
    "A esas alturas ya me daba igual el trabajo mientras pagaran. Limpiar baños, atrapar osos... haría lo que fuera."
    
    show cg_job with dissolve

    "Fue entonces cuando encontré este trabajo en internet..."
    "Vigilante en un teatro abandonado. En serio, ¿para qué querría un sitio cerrado un guardia de seguridad?"
    "Kingdom of Marionettes. Había oído que este sitio fue famoso hace tiempo por sus espectáculos de marionetas."
    "Oh. Solo tres tareas. Tarea uno: mantener el teatro a salvo de vándalos. Mmm... eso creo que puedo hacerlo."
    "Tarea dos: limpiar el teatro. Eso no es muy de guardia de seguridad, pero bueno, mientras paguen..."
    "Tarea tres: asegurarse de que no falte ninguna marioneta y de que no anden por ahí."
    "...."
    "Mmm. Será que he dormido tan poco que lo he leído mal."

    hide cg_job with dissolve
    show cg_jobclose with dissolve

    "Que no falte ninguna marioneta... y que no anden por ahí."
    "E-espera. ¿Que anden por ahí? ¿¡Que me asegure de que no haya marionetas andando por ahí!? ¿¡Qué significa eso!?"
    "Jajaja... seguro que querían decir que no se las robe nadie. Sí. Tiene que ser eso. Quien lo escribió estaba de broma."

    hide cg_jobclose with dissolve
    show cg_job with dissolve

    "Vale. Vamos allá."

    hide cg_job with dissolve
    scene bg_office with dissolve

    play music "abandoned.mp3" fadein 2.0 volume 0.6

    "Aquí está... Después de tanto tiempo, por fin tengo trabajo."
    "Lo raro es que este trabajo no pedía entrevista."
    "Cuando contacté ayer, quedó todo apalabrado casi al momento."
    "Casi pensé que era una estafa, pero por suerte no."
    "Vale. Tengo tres tareas. Primero, proteger el sitio de vándalos. Por suerte, de momento ni rastro de problemas."
    "Solo quedan limpiar el teatro y comprobar que estén todas las marionetas."
    jump cleancheck

label cleancheck:

    menu:


        "Limpiar" if not asked_clean:

            $ asked_clean = True

            jump q_clean

        "Revisar las marionetas" if not asked_check:

            $ asked_check = True
    
            jump q_check

        "Todo listo":

            jump rest



label rest:

    scene bg_office with dissolve

    "Vuelvo directo a mi cuarto e informo al jefe."
    "Tareas terminadas. Ahora solo queda hacer guardia."
    "Ser guardia no está tan mal. Me pagan por vigilar."
    "La paga no es gran cosa, pero mejor que nada."

    u "¿Qué hago mientras vigilo...?"
    u "Estoy agotado... pero no puedo dormirme."

    "Saco el móvil y empiezo a navegar por internet."
    "Sé más bien poco de este teatro y la curiosidad me puede, así que decido buscar información en internet."
    "Kingdom of Marionettes. Un teatro de marionetas que cuenta la vida cotidiana de las marionetas de un reino."
    "Con razón las marionetas que vi antes vestían trajes de época real."
    "Kingdom of Marionettes era conocido por sus espectáculos divertidos y fascinantes, con unos diseños de marionetas encantadores."

    "¿De verdad fue tan famoso? Hasta vendían merchandising y de todo."
    "Hasta había una votación del personaje favorito. Qué mono."
    "El primer puesto fue para el bufón. A la gente le van los personajes raros, ¿eh?"
    "El segundo fue el caballero, y el tercero el mago."
    "Me absorbe tanto la información del teatro que, cuando me doy cuenta, llevo media hora deslizando."

    u "Mierda. Tengo que mirar las cámaras."

    hide bg_office with dissolve
    show screen komputer with dissolve
    show cctv main with dissolve

    jump cctv


label cctv:
    menu: 
        "Mirar la entrada":
            jump outer_gate
            
        "Mirar el pasillo 1":
            jump corridor1
            
        "Mirar la sala del teatro":
            jump theater_hall
            
        "Mirar el almacén":
            $ choice = 'ketemu knighter'
            $ met_knighter = True
            jump storage
            
        "Mirar el escenario":
            jump stage


label performance:
    
    window hide
    show jes close smug with dissolve
    hide close_sh with dissolve
    show close_menjentik with dissolve
    window show

    jespuppet "Mmmm..."

    play sound "snap.mp3" volume 3.0
    hide jes close smug
    hide close_menjentik
    
    "Luego, el títere chasquea los dedos y, en un instante, desaparece frente a mí."
    "¿Q-qué...? ¿A dónde fue ahora?"

    scene bg_theaterhall at slide_right
    pause 1.0
    hide bg_theaterhall
    play sound "jinglebell.mp3"
    camera at camera_shake
    show tangan1
    
    jespuppet "Una mano tan pequeña y suave. como algodón... como la pata de un gatito."

    camera at reset
    show ngelus

    "Él está acariciando mi brazo suavemente con su mano de marioneta."

    jespuppet "Una forma tan pequeña... tan fácil de romper... pero de algún modo rebosante de calidez y movimiento..."
    jespuppet "Un recipiente que reacciona, tiembla y cambia tan bellamente....."

    show stop_ngelus with dissolve

    jespuppet "Y esa cara... siempre cambiando, siempre contando historias sin querer..."

    hide ngelus

    "......"
    "¿Él... me está examinando?"

    jespuppet "Realmente eres humano."
    u "S-sí... soy humano..."
    
    "Respondo con voz nerviosa, mezclada con miedo."

    hide stop_ngelus with dissolve

    jespuppet "Pasaron segundos... luego horas... días... semanas... meses... años..."
    jespuppet "Ha pasado mucho tiempo desde que todo eso se desvaneció."

    show ngelus

    jespuppet "Un reino que alguna vez fue tan vivo, tan magnífico, tan lleno de alegría… ahora ha quedado reducido al silencio."

    hide tangan1

    jespuppet "Un reino que una vez fue dirigido por un gobernante, alguien que nos guió a todos hacia nuestro propósito, hacia nuestras vidas, ahora ha desaparecido."
    jespuppet "Como pájaros novatos abandonados por sus padres antes de que estuvieran listos para volar, fuimos guiados por la confusión... por la desesperación..."

    show ngelus_nosmile with dissolve
    hide ngelus

    jespuppet "Nos movemos sin dirección ni destino, sin saber adónde debemos ir..." 
    jespuppet "Y sin embargo... creemos. Que algún día… aparecerá una nueva luz que nos guiará."

    show tangan1 with dissolve
    hide ngelus_nosmile

    jespuppet "Un líder que nos dará vida una vez más y nos llevará hacia las vidas que siempre debimos vivir..."

    show ngelus
    hide tangan1

    jespuppet "Esperamos... y tuvimos esperanza. Tuvimos esperanza... y esperamos. Vueltas y vueltas, una y otra vez, hasta que ambas se volvieron indistinguibles, como si nunca debieran estar separadas."
    jespuppet "Y así, ese círculo perduró. Permaneció a través del paso del tiempo... hasta ahora. Uuu... hasta este mismo día, que silenciosamente se atreve a llamarse a sí mismo un punto de inflexión."

    show stop_ngelus with dissolve
    hide ngelus 

    jespuppet "¿Continuará este círculo su danza suave y despiadada, ininterrumpida, sin cambios?"
    jespuppet "¿O, por fin, comenzará a resquebrajarse... a fracturarse... y finalmente a hacerse añicos, liberándonos del bucle que llamamos vida?"

    "......"
    "Eh... ¿De qué habla tan de repente? No entiendo. ¿Me está contando un cuento?"
    show bg_theaterhall with dissolve
    hide stop_ngelus with dissolve
    play sound "jinglebell.mp3"
    show jes bow with dissolve

    jespuppet "Un reino... un lugar nunca muy alejado de la política, un reino lleno de tensión, donde la seriedad acecha bajo su lujosa y brillante superficie."
    jespuppet "Como el hielo, muy frío, requiere al menos un toque de calidez. no... tal vez la mitad de ese calor para mantener el equilibrio."

    play sound "jinglebell.mp3"
    show jes normal2

    jespuppet "Y es precisamente por eso que estoy aquí. Suavizar el aire, provocar risas, llevar la alegría dondequiera que se atreva a desvanecerse."
    jespuppet "Ahora... ¿puedes adivinar quién soy?"
    
    "E-Esta persona... no, este títere... parece disfrutar mucho hablar..."

    u "Uh... ¿eres un... bufón?"

    show jes happy3 with dissolve

    jespuppet "¡Din, din, din! ¡Correcto!"

    show jes normal2 with dissolve

    jes "Aunque para ser precisos, el bufón es simplemente mi papel. Permíteme presentarme adecuadamente, dulce humano. Mi nombre es Jestyn. Puedes llamarme Jestyn."
    jes "Aunque me temo que algunos prefieren Jes, Jesy, Tyn-Tyn y muchas otras variaciones."
    jes "Ahora que te he ofrecido mi nombre, permíteme, sólo por esta vez, pedirte el tuyo a cambio."

    call ask_player_name from _call_ask_player_name

    jes "[player_call]....qué hermoso nombre para un alma tan hermosa."
    jes "¿Y tu pronombre es?"

    call pronoun from _call_pronoun
    jes "Entendido."
    show jes talk2

    

    show jes normal2

    jes "Pero dime… ¿qué te trae a este reino, me pregunto? ¿Quizás estás cumpliendo con un deber para la corona?"

    "Sigue refiriéndose a este teatro como un reino. Está empezando a confundirme."
    "Además, su forma de hablar es realmente extraña."
    "Pero... lo que sea. Seguiré el juego por ahora. Sólo quiero salir de aquí lo antes posible."

    mc "Solo soy un guardia de seguridad. Mi trabajo es vigilar este teatro... y hacer un poco de limpieza además."

    "Espero que mi respuesta lo satisfaga."

    show jes laugh2

    "Pero de repente empieza a reírse y no tengo idea de por qué. ¿Mi respuesta es realmente tan divertida para él?"

    show jes talk2

    jes "Ah... un guardián, ¿verdad? Qué vocación tan increíble. Un protector del reino, uno que se mantiene firme, luchando hasta la última gota de sangre."
    jes "Y sin embargo... lamentablemente, aquí no puedes convertirte en guardián."
    mc "¿Q-Qué quieres decir?"

    show jes normal

    jes "Verás, ya tenemos un caballero que sirve como escudo de este reino. Su nombre es Knighter. Y no tenemos intención de darle la bienvenida a otro."
    jes "Un caballero es más que suficiente."
    
    "¿Está... hablando de papeles en este teatro?"
    
    mc "Oh... entonces seré simplemente limpiador, supongo..."

    show jes nosmile2

    jes "Ya tenemos muchas sirvientas aquí y no creo que nos sea posible agregar otra."
    mc "Muy bien entonces. Supongo que simplemente no seré nadie."

    show jes normal2

    jes "Oh no, no... todos los que vienen aquí deben tener su propio papel."
    jes "Y el papel que actualmente está vacante... es el de rey, la reina, el gobernante del reino."
    mc "A-Está bien... uh... pero ¿por qué solo está vacía la posición de rey? ¿Qué pasó con el rey anterior?"

    "Cuando revisé los títeres antes, había una habitación etiquetada como 'El Rey'. Entonces el rey títere debe haber existido."

    show jes nosmile2

    jes "Lamentablemente falleció."
    mc "Oh... lo siento. Mi más sentido pésame."

    show jes talk2
    jes "Está bien, querida. Así es simplemente la vida. la gente viene y se va. Es parte de un ciclo del que no puedes escapar. Creo que los humanos lo entienden mucho."

    "Luego aplaudió."

    show jes normal

    jes "Ha pasado mucho tiempo desde que falleció el rey. Este reino se ha vuelto terriblemente oscuro... lleno de silencio, sin dirección ni alegría."
    jes "Y debo admitir... que esto se ha vuelto bastante aburrido."
    jes "Pero ahora que he conocido a un humano tan dulce antes que yo, ¿por qué no me permite participar en un pequeño juego, majestad?"
    mc "..... ¿Su majestad? ¿a mí?"

    show jes happy with dissolve
    
    "Su sonrisa se amplió."

    show jes happy2 with dissolve
    
    jes "Sí. Juguemos un poco a actuar. Tú fingirás ser el [title] y yo... seré tu bufón."

    show jes talk2

    jes "Oh, perdóname. He sido un bufón desde el principio. Qué tonto de mi parte."
   
    
    "Jestyn luego chasqueó los dedos y, antes de que me diera cuenta, ya había subido al escenario."
    
    play sound "snap.mp3" volume 3.0
    hide jes talk2
    pause 1.5
    play sound "spotlight.mp3" volume 3.0
    scene bg_theaterhall_light 
    pause 0.5

    show jes_on_stage with dissolve
    
    jes "Ahora bien... ¿debemos permitir que comience la actuación?"
    mc "¡Espera, espera! ¡Nunca antes había actuado! Ni siquiera se como-"
    jes "Oh no, querida... Simplemente vive, como si siempre hubieras sido el [title] de este reino."

    hide jes_on_stage with dissolve
    show jes_on_stage2 with dissolve
    
    "Jestyn volvió a chasquear los dedos." 

    stop music
    play sound "snap.mp3" volume 3.0
    scene bg_stagelight2
    camera at camera_shake

    "Y en un instante me encontré ya en el escenario. Sentado en un trono de felpa, con una corona apoyada sobre mi cabeza."

    camera at reset
    hide jes_on_stage2

    play music "jestyntheme.mp3" fadein 2.0
    mc "¡¿Qué-qué?!"
    nara "{color=#E0AE4B}Un día, bajo el sol abrasador del verano, el reino volvió a verse afectado por los problemas. Los agricultores se llenaron de tristeza cuando el implacable calor del verano quemó la tierra.{/color}"
    nara "{color=#E0AE4B}Las cosechas se marchitaron y fracasaron debido a la sequía, dejando los campos estériles. Como resultado, los agricultores sufrieron grandes pérdidas y no quedaron cosechas para vender.{/color}"
    nara "{color=#E0AE4B}Al final, los agricultores llevaron su situación ante [poss] Majestad, con la esperanza de que [subj] pudiera recibir ayuda y alivio.{/color}"

    "Miré a mi alrededor, tratando de encontrar la fuente de la voz que sonaba como la de un narrador."

    nara "{color=#E0AE4B}Dentro del reino, [poss] Majestad se sentó en el trono de [poss], la expresión de [poss] se nubló por la confusión, cuando Jestyn, el bufón real apareció ante [poss] para transmitir los problemas que enfrentaban los granjeros.{/color}"

    play sound "jinglebell.mp3"
    show jes bow with dissolve
    
    jes "Buenas noches, majestad."
    
    "Jestyn apareció y se inclinó ante mí con la mayor reverencia."

    play sound "jinglebell.mp3"
    show jes talk2
    
    jes "Qué día tan realmente hermoso es hoy."
    jes "Un día igualmente apropiado para solucionar los pequeños problemas que se agitan en el reino... ¿No está de acuerdo, Su Majestad?"
    mc "¿Problemas... en el reino?"
    jes "De hecho, Su Majestad."

    show jes nosmile2

    jes "Últimamente, la gente del pueblo ha comenzado a expresar sus preocupaciones. Las cosechas han fracasado, afectadas por la implacable sequía de la estación seca."
    jes "Y como era de esperar, tal desgracia los ha dejado... bastante carentes de medios."

    hide jes nosmile2 with dissolve
    show jes2 normal2 at center_to_right
    with move

    jes "Por favor, entra querido invitado."
    nara "{color=#E0AE4B}Un hombre que trabajaba como granjero entró, después de que Jestyn le concediera permiso para entrar.{/color}"
    
    "De repente, un títere vestido de granjero dio un paso adelante y se arrodilló ante mí."

    show farm sad with dissolve
    
    farm "Saludos, Su Majestad. Por favor, perdona mi audacia, pero venimos ante ti para buscar humildemente tu ayuda."
    farm "Debido a las malas cosechas, ya no tenemos los medios para reponer los cultivos que se marchitaron, ni tenemos los fondos para satisfacer nuestras necesidades diarias..." 
    farm "Por ello, te rogamos... que nos concedas tu guía."

    "Después de haber sido arrastrado al papel de [title] sin previo aviso, la confusión se apoderó de mí."
    "Mis propios problemas estaban lejos de resolverse, ¡¿y ahora se esperaba que yo también encontrara una manera de salvar a los granjeros?!"
    
    mc "U-um..."
    
    "¿Qué se supone que debo hacer...?"

    $ affection = 0

    menu:
        "Darles dinero":
            $ choice = "a"
            $ affection += 2

            if cursed_route:
                jump cursed1
            
            else:
                jump money

        "construir canales de agua":
            $ choice = "a"
            $ affection += 2

            if cursed_route:
                jump cursed1
            
            else:
                jump channels

        "Dales nuevas semillas":
            $ choice = "a"
            $ affection += 2

            if cursed_route:
                jump cursed1
            
            else:
                jump seeds

        "necesito tiempo para pensar":
            $ first_delay = True
            $ choice = "b"

            if cursed_route:
                jump cursed1
            
            else:
                jump time

        "Deberíais encontrar una solución vosotros mismos.":
            $ affection -=1
            
            if cursed_route:
                jump cursed1
            
            else:
                jump yourselves

label problem2:
    mc "..... ¿Está terminado?"
    
    show jes happy 
    jes "¿Terminado?"
    show jes talk2 with dissolve
    jes "Si gobernar un reino fuera así de simple, Su Majestad, me temo que tendríamos muchas menos reinas."
    
    "Todavía hay más..."

    hide jes talk2 with dissolve
    

    nara "{color=#E0AE4B}El día transcurrió lentamente dentro del reino. Y sin que [poss] Majestad se diera cuenta, la hora que antes marcaba las nueve de la mañana ya había avanzado a la una de la tarde.{/color}"
    nara "{color=#E0AE4B}En ese mismo momento, de repente llegó una carta formal de otro reino.{/color}"
    nara "{color=#E0AE4B}Al enterarse de esto, el mayordomo rápidamente tomó la carta y se dispuso a entregársela a [poss] Majestad.{/color}"
    
    show jes2 normal2 at right_pos
    with dissolve
    show butley_surat at left
    with dissolve

    "De repente, un títere vestido de mayordomo se acercó a Jestyn y le entregó un pergamino."
    hide butley_surat with dissolve
    hide jes2 normal2 with dissolve
    show jes2 normal3 with dissolve
    "Jestyn lo leyó por un momento. Su expresión se volvió concentrada, antes de que sus ojos se dirigieran hacia mí y esa amplia sonrisa volviera a su rostro."

    show jes2 talk with dissolve
    
    jes "Su Majestad, hemos recibido una petición sorprendente y bastante intrigante de un reino vecino."

    show jes2 talk2 with dissolve
    
    "Todo está escrito aquí, con tinta, en este pergamino."

    show jes2 normal3 with dissolve
    
    jes "En resumen, desean comprar un pequeño terreno a lo largo de nuestra frontera, con el pretexto de facilitar el comercio."

    show jes2 talk with dissolve
    jes "Si Su Majestad acepta este acuerdo, están dispuestos a ofrecer una compensación en monedas de oro. una cantidad que estoy bastante seguro le provocaría a Su Majestad un ataque al corazón en el acto~"
    jes "Entonces... ¿qué hará, Su Majestad?"
    
    "Oh no... esto está empezando a parecer complicado. ¿Qué tengo que hacer?"

    hide jes2 talk with dissolve

    menu:
        "Aceptar":
            $ affection -= 1

            if cursed_route:
                jump cursed2
            
            else:
                jump agree

        "Rechazar":
            $ affection += 1

            if cursed_route:
                jump cursed2
            
            else:
                jump Refuse

        "Posponer":
            if cursed_route:
                jump cursed2
            
            else:
                jump delay

label acting_end:
    if affection < 2:
        jump bad_end

    else:
        jump after_acting


label after_acting:
    stop music fadeout 2.0
   
    show jes normal2 with dissolve
    jes "Muy bien entonces. Informaré a nuestros vecinos del testamento de Su Majestad."
    jes "Y creo que, por ahora, los asuntos que Su Majestad debía resolver han llegado al final del programa de hoy."
    jes "Ahora puedes descansar la cabeza, majestad~"

    "Finalmente..... termina. No sé si mi cerebro podrá soportar más estas cosas del reino."
    show jes suprais2
    play sound "ringtone.mp3" 
    "Antes de que finalmente pudiera relajarme, sonó mi teléfono."
    "Oh no... tiene que ser mi cobrador de deudas."
    show jes nosmile2
    "Realmente no quiero lidiar con esto ahora. No tengo dinero para pagar."
    "Pero realmente no tengo otra opción..."
    
    play sound "pickupphone.mp3" volume 3.0
    mc "¿Hola?"
    debt "¡[player_call]! Sabes por qué te llamo, ¿no?"
    mc "Por supuesto...."
    debt "¿Entonces?"
    mc "Lo siento... no puedo pagarlo ahora."
    mc "Pero acabo de conseguir un trabajo otra vez. Sólo tienes que esperar hasta el día de pago."
    show jes annoy with dissolve
    debt "Aaah... vale. Pero recuerda, ya has retrasado esto cinco meses."
    mc "Lo sé... lo sé... gracias por tu comprensión..."

    play sound "pickupphone.mp3"
    "Momentos después de finalizar la llamada, recosté mi cuerpo contra mi asiento, necesitando un breve descanso."
    "Tengo que pagarlo dentro de un mes..."
    show jes normal
    "Me pasé los dedos por el pelo con frustración, antes de recordar que Jestyn todavía estaba de pie frente a mí."
   
    mc "Oh, lo siento, Jestyn. Eso fue solo un asunto personal."

    play sound "jinglebell.mp3" volume 6.0
    hide jes normal with dissolve
    show jes close normal with dissolve
   
    "De repente, la mano de Jestyn se cerró suavemente alrededor de mi hombro. Me miró con esa amplia sonrisa suya."
   
    jes "Su Majestad, sus asuntos personales son asuntos del reino."
    jes "Y eso los convierte en mi preocupación también, como bufón del reino."

    show jes close nosmile 
    jes "Por lo que observé en su conversación a través de esa tecnología hace un momento, parece que Su Majestad está en deuda... con otro reino, ¿estoy en lo cierto?"
    mc "..."
    mc "Sí...."
   
    "Su mano sobre mi hombro amasó suavemente la tensión. Al instante, sentí que me relajaba."

    show jes close soft with dissolve
    jes "Puede contarme sus problemas, Su Majestad."
    jes "Después de todo, soy tu más leal y único bufón..."


    "......"
    
    play music "seduction.mp3" fadein 2.0 volume 0.5
    mc "... Llevo mucho tiempo pensando en las finanzas del reino. Han ido disminuyendo cada vez más."

    show jes close normal
    jes "Dios mío ~"
    mc "Sí... en aquel entonces yo... se podría decir que formé una especie de amistad con el gobernante de otro reino."
    mc "Ese reino necesitaba ayuda porque enfrentaba un problema similar."
    mc "Pero al final ese reino solo me estaba explotando y luego me traicionaron."
    mc "Entonces... tuve que pedir prestado fondos de otros reinos. Y ahora... nuestro reino está agobiado por una deuda considerable."
    mc "He estado tratando de encontrar otras fuentes de ingresos sólo para mantener las cosas estables."

    show jes close nosmile with dissolve
    "Después de que le expliqué todos mis problemas llenos de metáforas, Jestyn no dijo nada por un tiempo."
    "El silencio envolvió el aire entre nosotros."

    show jes close normal with dissolve
    jes "¿Sabe por qué se honra al león como rey del bosque, Su Majestad?"


    "Por un segundo, me siento confundido por su repentina pregunta sobre el león."


    mc "Um... ¿porque son majestuosos?"
    jes "De hecho. Son majestuosos. Son temibles. Son superdepredadores resistentes y se encuentran en la cima."
    jes "Ahora imagina un conejo. ¿Por qué al conejo nunca se le llama rey del bosque?"
    mc "Porque... ¿los conejos son demasiado amables? ¿Pequeño? ¿No es lo suficientemente aterrador?"
    jes "Gentil."
    show jes close nosmile with dissolve
    jes "Demasiado vacilante... y, ah, trágicamente humano."
    jes "Y lo más importante... confiar en los demás con demasiada facilidad."
    jes "Cualidades muy nobles... para un alma que sufre. Menos para un [title]."
    show jes close smug
    jes "Pensaste que al ayudar a los demás, les agradarías. Que te sonrían, se paren a tu lado y te llamen amigo."
    jes "Y luego ¡BUM! ¡Qué agradable sorpresa! ¡Te han engañado! ¡Te han burlado! ¡Te han manipulado como una pequeña melodía! ¡Jajajajajaja!"


    "Se ríe como un maníaco"

    show jes close annoy 
    jes "¿No es eso perfectamente irónico?"


    "Jestyn habló con una sonrisa, cada risa delicada y educada... pero cada palabra se sentía como una cuchilla afilada presionada contra mi pecho."
    "Una vez leí que la tarea de un bufón en un reino... es entretener. Y parte de eso... es revelar la verdad a través de la broma."
   
    menu:
        "Reírse con él":
            $ affection +=1
            jump funny


        "Qué molesto":
            jump annoying


label funny:
    "Lo veo ahora. Sí, debo seguir el juego."


    mc "¡Jajajaja! no estás... equivocado Jestyn."


    jump advice


label annoying:
    "Pero la forma en que dijo eso..."
    "Sus palabras perforaron mortalmente mi corazón."
    "No mentiré, eso es tan molesto."


    jump advice


label advice:
    show jes close normal with dissolve
    jes "Mira, Su Majestad, las reglas de este mundo no son una pequeña y dulce fábula donde la bondad siempre se paga con la misma moneda. Creo que ya lo sabes."
    jes "A veces el juego es mucho más simple que eso. A veces, la regla es simplemente comer... o ser comido."
    mc "¿Quieres decir que debería convertirme en un león?"
    show jes close smug with dissolve
    jes "Oh no, no, Su Majestad. Eso no será necesario. Vaya, la expresión de tu cara, tan privada de sueño, ya es bastante aterradora."
   
    "Se ríe burlonamente mientras me ve fruncir el ceño."

    jes "Jeje, perdóname, Su Majestad. Solo estaba bromeando. No te estoy diciendo que te conviertas en un león."
    show jes close normal
    jes "¿Alguna vez has considerado... combinar un conejo y un león?"
    mc "Uh... ¿no parecería una especie de mutante?"
    show jes close nosmile
    jes "No ese tipo de combinación, Su Majestad..."
   
    "Agita un dedo ligeramente."

    show jes close normal
    jes "La apariencia de un conejo, pero el corazón de un león. Como un lobo bajo piel de oveja, si me preguntas."

    "Hace una pausa."

    jes "Y además... confía sólo en aquellos que te rodean a quienes realmente conoces."
    jes "Aquellos que te seguirán siendo leales, pase lo que pase. ¿Difícil? Sí. Pero esa es simplemente la verdad."
    show screen dark_effect with dissolve
    show jes close creep with dissolve
    jes "Y después de eso... tal vez, aquellos que te son leales puedan incluso ayudarte a destruir a los que te han hecho daño."
    jes "{color=#FF2727}Solo para ti.{/color}"
    hide screen dark_effect with dissolve
    show jes close normal with dissolve
    jes "Entiende lo que quiero decir, ¿no es así, Su Majestad?"
   
    "Sus palabras me dejan perdido en mis pensamientos."
    "Ahora que lo pienso... realmente soy una persona que complace a la gente."
   
    mc "Lo entiendo... pero cambiar eso no es fácil."
   
    "Jestyn deja escapar una suave risa. Sus ojos se estrechan mientras su sonrisa se amplía lentamente."
   
    jes "Muy bien, Su Majestad... y es precisamente por eso."
    show jes close smug with dissolve
    jes "Quizás en lugar de preguntar qué más puedes dar... deberías preguntarte qué es lo que todavía te niegas a recibir."

    play sound "jinglebell.mp3" 
    hide jes close smug with dissolve

    "Jestyn se aleja de mí, dándome espacio para reflexionar sobre el significado de sus palabras."
    "Sus palabras siempre son difíciles de entender..."
    show jes happy with dissolve
    "Él aplaudió, sacándome de mis pensamientos."

    jes "Ahora... permíteme presentarte el entretenimiento. Debes estar cansado de trabajar todo el día, ¿no, majestad?"
    jes "Por mucho que adoro esa expresión tuya, como la de un murciélago despertado a plena luz del día. Todavía preferiría no verte para siempre con una cara tan desprovista de alegría..."
    
    "Él se ríe suavemente. Me deja muy poco de qué reírme."
    
    jes "Te haré sonreír una vez más. Derritiendo el frío de tu vida con el fuego del deleite que traigo."
    show jes talk2 with dissolve
    jes "Permíteme ~"

    "Jestyn chasqueó los dedos. En un instante aparece algo en sus manos."
    "Era un pequeño objeto rectangular, envuelto en una capa de oro y cuidadosamente atado con una cinta roja."
    show coklat with dissolve
    
    mc "¿Qué es?"
    hide coklat with dissolve
    hide jes talk2 with dissolve
    
    "Jestyn luego me lo entregó, permitiéndome abrirlo yo mismo."
    
    mc "¿Chocolate?"
    show jes normal2 with dissolve
    jes "De hecho, Su Majestad. A todo el mundo le encanta el chocolate. ¿Quién no? Así que espero que te guste."
    jes "Y no es un chocolate cualquiera."
    show jes talk2
    jes "Diseñé cada paso con todo mi corazón. Con cuidado, delicadeza y con la máxima devoción."
    show jes bow with dissolve
    jes "Así que espero que saborees mi chocolate hecho a mano y no olvides el color de su envoltorio, Su Majestad~"

    menu:
        "Comer":
            $ affection -=1
            jump eatchocolate

        "No comer":
            jump donteat

label eatchocolate:
    hide jes nosmile2_2 with dissolve
    hide jes bow with dissolve
    "Bueno... como ya me lo dieron, no pude negarme. No tuve el corazón para hacerlo."
    "Rompí un trozo de chocolate y me lo metí en la boca."
    "En el momento en que tocó mi lengua, pude sentirlo derretirse."
    "Pero al mismo tiempo, vi que la sonrisa de Jestyn se agudizaba y fue entonces cuando la sentí."
    
    mc "¡¿Uf-?!"
    
    "Una sensación de ardor se extendió por mi lengua."
    show jes happy2 with dissolve
    jes "Dios mío, parece que alguien olvidó el color del envoltorio ~"
    
    "Jestyn se rió suavemente cuando mi cara se puso roja por el calor."
    
    mc "¿Q-qué tipo de chocolate es este?"
    jes "Jeje. Es chocolate, por supuesto. Pero los ingredientes habituales me parecen bastante aburridos. Nada nuevo. Que aburrido."
    hide jes happy2 with dissolve
    show jes2 smug with dissolve
    jes "¡Y luego! Se me ocurrió una idea brillante. ¿Por qué no añadir algo nuevo a la receta?"
    jes "Entonces agregué chile en polvo."
    
    "Lo miré, completamente sin palabras. ¡¿Qué clase de pensamiento es ese?!"
    hide jes2 smug with dissolve
    show jes happy with dissolve
    jes "Pobre de ti, Su Majestad. Pero esa expresión tuya, nerviosa y enrojecida, es simplemente adorable."
    hide jes happy with dissolve
    "Jestyn luego me entregó un vaso de agua para beber."
    "¿Cómo caí en su broma tan fácilmente?"

    jump freakymomen

label donteat:
    "Me quedé mirando el chocolate por un momento."
    "No quería rechazar el regalo de alguien... pero mis instintos me decían que algo andaba mal."
    "........."
    
    mc "¿Jestyn?"
    jes "¿Sí, Su Majestad?"
    mc "Esto no es chocolate común, ¿verdad?"
    
    "Su sonrisa no se desvaneció en lo más mínimo cuando me miró."
    show jes normal2 with dissolve
    jes "¿Ah? ¿Y qué te hace decir eso, Su Majestad?"
    show jes nosmile2_3 with dissolve
    jes "Ah... para ser honesto, me duele el corazón que me acuses así. Te di ese chocolate sinceramente."
    show jes nosmile2_2 
    "Su sonrisa se desvaneció lentamente, reemplazada por la expresión de alguien profundamente herido."
    menu:
        "Confía en él":
            $ affection -=1
            jump eatchocolate

        "No confíes en él":
            jump donteat2

label donteat2:
    mc "No me mientas."
    mc "Hay algo en este chocolate, ¿no? No me dejaré engañar."
    stop music fadeout 2.0
    jes "....."
    show jes normal2_2 
    jes "Pfft... khuhu..."
    
    "Jestyn dejó escapar una suave risa. Y sólo con eso quedó todo demostrado."
    show jes laugh2 with dissolve
    jes "Jejejejeje... ¡jajajajajaja!"
    show jes talk 
    jes "Ahh... entonces alguien no olvidó el color del envoltorio después de todo."
    jes "Eres más perspicaz de lo que pareces, Su Majestad..."
    show jes creep2 with dissolve
    jes "Sí. Le agregué algo al chocolate."
    
    "Dejé caer el chocolate al suelo."
    
    mc "¡¿E-entonces qué le pusiste?! No me digas que es veneno. ¿Estás tratando de matarme?"
    show jes laugh with dissolve 
    jes "¿Veneno? ¡AJAJAJAJAJAJAJA!"
    show jes happy
    jes "Oh, Su Majestad, no soy tan cruel. Fue simplemente una broma. Y nunca haría algo tan despiadado por una broma."
    play music "seduction.mp3" fadein 2.0 volume 0.5
    hide jes happy with dissolve
    show jes2 smug with dissolve
    jes "Es chocolate, por supuesto. Pero los ingredientes habituales me parecen bastante aburridos. Nada nuevo. Que aburrido."
    jes "¡Y luego! Se me ocurrió una idea brillante. ¿Por qué no añadir algo nuevo a la receta?"
    jes "Entonces agregué chile en polvo."
    hide jes2 smug with dissolve
    show jes happy with dissolve
    "Lo miré, completamente sin palabras. ¡¿Qué clase de pensamiento es ese?!"
    

    jump freakymomen

label freakymomen:

    show jes talk2 with dissolve
    jes "Jejeje. Por favor perdóname, Su Majestad. Esta vez te daré un entretenimiento adecuado. Prometo que esto no es otra broma."

    "Jestyn chasqueó los dedos."

    menu:
        "Las bolas":
            $ choice = "juggling"
            jump balls

        "El collar" if affection >= 4:
            $ choice = "collar"
            jump collar

label balls:

    stop music fadeout 1.0
    show bola with dissolve
    
    mc "...¿bolas?"
    jes "Correcto"
    
    play music "jestyntheme.mp3" volume 3.0 fadein 1.0
    hide bola with dissolve
    hide jes talk2 with dissolve
    
    "Sin esperar más, comenzó a hacer malabarismos con notable habilidad."
    "Las bolas volaban de una mano a otra, mezcladas con algunos trucos llamativos. Era obvio que había hecho esto innumerables veces antes."
    "Entonces, su mirada se dirigió hacia mí."
    
    jes "¡Debes continuar con mis malabares, majestad!"
    mc "Espera que-"
    
    "Antes de que pudiera terminar mi frase, Jestyn arrojó todas las bolas hacia mí."
    "No importa cuánto lo intenté, fue inútil. Las bolas se deslizaron de mis manos y cayeron al suelo antes de que pudiera mantenerlas en el aire."
    "Al ver mi patético intento, Jestyn se echó a reír."
    show jes happy with dissolve
    jes "¿Verdaderamente su majestad? Ni siquiera puedes atraparlos, y mucho menos hacer malabarismos."
    mc "¡Por supuesto que no! ¡Nunca había hecho esto antes!"
    
    "Las bolas rodaron por el escenario y se esparcieron a mis pies."
    show jes talk with dissolve
    
    jes "¡Ah, ah, ah! No te vengas abajo, majestad."
    jes "Aquí pensé que los humanos eran bastante buenos atrapando cosas. Oportunidades, promesas, responsabilidades."
    
    "Se ríe suavemente, como si acabara de contar un chiste inofensivo."
    
    mc "Me los arrojaste sin previo aviso..."
    show jes bow with dissolve
    jes "¿Lo hice?"
    
    "Inclina la cabeza y las campanas de su capucha suenan débilmente."
    
    jes "Mis disculpas entonces. A veces olvido que no a todo el mundo le gustan tanto las sorpresas como a mí."
    hide jes bow with dissolve
    
    "Se agachó y recogió una de las bolas caídas, girándola ligeramente sobre su palma."
    show jes normal with dissolve
    
    jes "Dime, ¿qué crees que es hacer malabarismos, majestad?"
    mc "Uh... ¿tirar cosas? ¿Tratando de no dejarlos caer?"
    show jes happy with dissolve
    jes "Hoho... una respuesta honesta. Me gusta eso."
    show jes talk2 with dissolve
    jes "Hacer malabarismos es equilibrio. Momento. Saber qué bola atrapar primero y cuál debes dejar caer."
    "Casualmente lanza la pelota al aire y la atrapa con facilidad."
    show jes normal with dissolve
    "Luego deja que la pelota se le escape de los dedos y golpea el escenario con un sonido sordo. luego me mira fijamente"
    
    jump teach


label home:
    show jes normal2 with dissolve
    jes "Creo que su tiempo en este reino ha llegado a su fin."
    
    "Estoy confundido por lo que quiere decir, pero cuando miro mi reloj, marca las 5:30 a.m."
    
    mc "Oh... mi turno ha terminado."

    "Él toma mi mano y le da un beso en el dorso."
    "Sus labios se sienten fríos, pero la sensación envía calor a través de mi cuerpo y directo a mi corazón."

    jes "Luego, hasta que nos volvamos a encontrar," 
    show jes flush with dissolve
    jes "dulce humano..."
    hide jes flush with dissolve
    "Después de decir eso, Jestyn camina hacia el lado oscuro del escenario y desaparece."
    scene black with dissolve
    stop music fadeout 2.0
    "Finalmente regreso a mi pequeño y miserable departamento."
    "Y lo que pasó hoy fue realmente algo..."
    "Marionetas vivientes... y encima me hacen pasar por [title]."
    "Qué día tan extraño. siento que me estoy volviendo loco"
    "¿Debería volver mañana? Toda esta situación se siente tan espeluznante..."
    "....."
    "... Por supuesto que tengo que irme. Mi deuda no se pagará sola. Necesito el dinero. Buscar otro trabajo sería demasiado difícil para mí en este momento."
    "No sé qué me pasará después."
    "Por ahora será mejor que duerma un poco. Estoy completamente agotado."
    "..."
    "...."
    "......"

    window hide
    show jescg obsess5 with dissolve
    pause 2.0
    show jescg obsess6 with dissolve
    pause 1.0
    window show
    play music "darkambient.mp3" 
    jes "Pasaron segundos... luego horas... días... semanas... meses... años..."
    jes"Ha pasado mucho tiempo desde que todo eso se desvaneció."
    jes "Y después de tanto tiempo.... finalmente te encontré..."
    show jescg obsess with dissolve
    jes "Mi [title]."
    jes "Su Majestad... realmente te agradezco lo de hoy. Me has hecho tan insoportablemente feliz..."
    show jescg obsess2 with dissolve
    jes "Ah... pero... volverás esta noche, ¿no...?"
    jes "Por supuesto... por supuesto que lo harás. Todavía hay muchas cosas que podemos hacer juntos. Simplemente no podría soportarlo si no lo hicieras."

    if choice == "juggling": 
        jes "Te enseñaré a hacer malabarismos. Dijiste que querías que lo hiciera, ¿no? Entonces te enseñaré todo. cada truco, cada movimiento, hasta que tus manos se muevan exactamente como lo hacen las mías."
        jes "Luego te mostraré trucos de magia... unos que te prometo te dejarán sin aliento. Ah, y hay tantos títeres esperando que los conozcas... para que los organices... para que pertenezcan a donde quieras. Y luego... y luego..."
        
    if choice == "collar": 
        jes "Podemos volver a jugar como lo hicimos antes, Su Majestad. Soy tu leal bufón, arrodillado ante mi amo como un perro devoto."
        jes "Oh, no tienes idea de cómo ese sentimiento hizo que mi corazón se acelerara... cómo me hizo sentir como si te perteneciera... sí... te pertenezco, [title] [player_call]."
       

    jes "Podemos cenar juntos, dormir juntos, cantar juntos, bailar juntos... siempre juntos.. y luego... y luego..."
    show jescg obsess3 with dissolve
    jes "Oh, dulce tarta y crema, simplemente hay demasiadas cosas que podríamos hacer y no sé por dónde empezar... siempre y cuando nunca te apartes de mi lado."
    jes "En verdad... qué me ha hecho, Su Majestad... Estoy empezando a creer que es un hechicero de poder aterrador. Incluso Wizzy, el mago real, no podría torcer un corazón como este..."

    if choice == "collar":
        jes "Siento como si hubiera sido atrapado en tu red... envuelto fuertemente, incapaz de escapar... simplemente esperando ser devorado por ti... y aún así... no creo que quiera luchar en absoluto."
        
    jes "Ya casi no me reconozco, Su Majestad... pero de alguna manera, no deseo regresar."
    jes "El reino te necesita... yo te necesito."
    show screen dark_effect with dissolve
    show jescg obsess4 with dissolve
    jes "No. Te quiero... Te anhelo... Mi [title], [player_call]..."
    jes "Nunca antes había sentido algo tan abrumador... Quiero quedarme a tu lado, verte respirar, tallar tu imagen en mi mente, tocarte... y tal vez... hundirme aún más profundamente en ti, hasta que no quede nada más que nosotros..."
    jes "Ah- no, no, no. Qué impropio de mi parte. Un simple bufón tocando su [title] con tanta valentía... pero si me concedieras permiso, apreciaría cada centímetro de ti con la mayor devoción."
    jes "Oh, mi [title], apenas puedo soportar la espera para volver a verte... Desearía que el tiempo avanzara... y aún así se congelara por completo cuando estoy contigo. Si tan solo pudiera doblar el tiempo mismo. Sólo para ti."
    jes "Me despido ahora, Mi [title]... que tus sueños se llenen conmigo..."
    scene black with dissolve
    stop music fadeout 2.0
    jes "[player_call]."

    jump kom_day2
