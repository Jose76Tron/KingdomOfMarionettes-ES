default examinecornerwizzy = 0
default examinetableknighter = 0
default visited_wizzy = False
default mc_jealous = False
default crownus_wizzy = False
default jestyn_gagged = False
default sit_on_jestyn = False

label lookwindow_day2:
    "Mi mirada se dirigió hacia la gran ventana."
    "Afuera no había mucho que ver. Sólo multitudes de personas regresando a casa después de un largo día de trabajo."
    "Algunos otros se quedaron en la tienda de conveniencia, ocupándose de sus propios asuntos."
    "Al menos eso es lo que pensé al principio."
    "Varias personas seguían mirando en la misma dirección."
    "Algunos parecieron sorprendidos. Otros parecían confundidos."
    "Curioso, seguí su mirada y me encontré mirando a un... ¿hombre?"
    "Ah. Eso lo explicaba."
    "Se elevaba sobre todos los que lo rodeaban, lo que hacía imposible pasarlo por alto."
    "Y por un breve momento, sentí una extraña sensación de familiaridad."

    jump minimarket_day2


label tv_day2:
    "Mi mirada se dirigió hacia el televisor dentro de la tienda."
    "Estaban sonando las noticias de la mañana."
    "Por lo que pude deducir, estaban cubriendo un caso de asesinato."
    "Un hombre había sido encontrado muerto en un callejón."
    "Su cuerpo había sido dividido limpiamente en dos."
    "Oh Dios."
    "Había oído hablar de muchos asesinatos antes, cada uno con sus propios detalles espantosos, pero ¿cortado por la mitad?"
    "Eso fue horrible."
    "¿Qué clase de persona enferma podría hacer algo así...?"

    jump minimarket_day2


label phone_day2:
    "Saqué mi teléfono para comprobar si había recibido algún mensaje nuevo."
    "Nada."
    "Lo comprobé de nuevo."
    "Todavía nada."
    "Esperaba otro mensaje de los cobradores de deudas, pero hasta ahora no se habían comunicado conmigo."
    "Por ahora, eso me trajo algo de alivio."
    "Aunque no tenía idea de cuánto duraría ese alivio."
    "Bueno, no tiene sentido preocuparse por eso ahora."
    "Por el momento, simplemente disfrutaría la sensación mientras durara."

    jump minimarket_day2


label nothx_day2:
    "Por supuesto, el títere pervertido estaba pidiendo algo más que eso para mantenerlo callado." 
    
    mc "No, gracias."

    show jes close pout with dissolve
    
    "Jestyn infló sus mejillas en un puchero exagerado."
    
    jes "Mmmhh... ¿por qué no? Gentilmente te hice una oferta."
    mc "Porque cada vez que haces una oferta, se convierte en algo extraño."
    jes "Mmmrrghhhh… que crueldad, Su Majestad…"

    hide jes close pout with dissolve

    jump timetowork_day2


label brat_day2:
    "........Está bien."
    "No tenía exactamente experiencia con este tipo de cosas, pero por lo que había leído en fanfics y cómics, la persona más dominante solía decir..."
    "'Mocoso'."
    "...¿Realmente debería decirlo?"
    "Ah, lo que sea. Al diablo."
    
    mc "Jestyn..."

    show jes close suprais 

    mc "Estás siendo un mocoso."

    show jes close laugh
    
    "Jestyn se echó a reír ante mi patético intento de actuar como uno de esos personajes dominantes de un fanfic."
    "Podía sentir mis mejillas arder de vergüenza. Maldita sea."
    "Parecía un idiota."
    
    show jes close smug with dissolve
    
    jes "Vaya, vaya... ¿Está Su Majestad intentando que este pobre bufón pierda la compostura~?"
    jes "Un esfuerzo valiente... aunque debo admitir que a Su Majestad aún se le da fatal."
    mc ".....No tenías que decírmelo."
    jes "Ahora, ahora. No hagas pucheros."

    show jes close normal with dissolve

    jes "Ningún rompecabezas está completo desde el principio."
    jes "Cada uno dedica un rato a buscar la pieza que les falta."
    jes "Al igual que un rompecabezas, simplemente necesitas la pieza que falta para completarlo."
    
    "Se inclinó hasta que nuestros rostros estuvieron a sólo unos centímetros de distancia, su expresión era tranquila y relajada."

    show jes close flirt with dissolve
    
    jes "En otras palabras... podría ser la pieza que te falta, Su Majestad."
    
    "Mi cara se puso aún más caliente."
    "Aunque esta vez no fue por vergüenza."
    "Mi corazón latía con fuerza."

    show jes close smug with dissolve

    jes "¡Y TA-CHÁN~! ¡Mira! El arte de ponerse nervioso, ejecutado a la perfección por este humilde bufón~"
    jes "Mmm~ Solo mírate ahora... Tienes la cara tan roja como un tomatito al sol del verano."
    jes "Jeje... ¡Otra actuación impecable de este servidor, Jestyn el Bufón! Me encanta un público que se sonroja en el momento justo~"

    "Parpadeé una vez, luego dos veces después de darme cuenta de que solo me estaba tomando el pelo."
    "Instintivamente empujé contra su pecho y puse cierta distancia entre nosotros antes de que mi cara se calentara más." 
    "Jestyn respondió de la misma manera que siempre lo hacía, con una risa burlona." 

    jes "Su Majestad se sonroja muy fácilmente. Eres absolutamente adorable~"
    jes "Dios mío... Qué pequeño y frágil [title]. ¿Eres realmente el soberano de este reino... o simplemente una mota de polvo? ¡Una pequeña bocanada y listo! ¡Jajaja!"
    
    "Le respondí con una sonrisa forzada. No tenía energías para seguirle el juego."
    "Esta marioneta realmente tenía un talento notable para ponerme de los nervios. Constantemente."

    hide jes close smug with dissolve

    jump timetowork_day2


label dohard_day2:
    "Sus palabras burlonas sólo complicaron más mis emociones."
    "Me irritaron, y sin embargo..."
    "También me hicieron sentir extrañamente audaz."
    "Por alguna razón, sentí que por una vez podía tomar la delantera."
    "La idea de ponerlo en su lugar me resultaba inesperadamente excitante."
    "....."
    
    mc "¿Sabes, Jestyn?"
    mc "Si eso es lo que estás pidiendo, entonces está bien."
    mc "Para un mocoso como tú... estaría feliz de enseñarte cómo permanecer callado."
    mc "De una manera más difícil."
    
    show jes close suprais with dissolve
    "Los ojos de Jestyn se abrieron sorprendidos por el tono de mi voz y las palabras que acababan de salir de mi boca."

    show jes close flush 
    "Un momento después, una amplia sonrisa se dibujó en su rostro mientras el sonrojo de sus mejillas se intensificaba."
    
    jes "Mmhh... decir cosas tan escandalosas en público..."
    jes "... Qué descarado ~"
    mc "¿QUÉ-? ¡Tú fuiste quien empezó a decir todas esas cosas raras!" 
    mc "¡Y aquí no hay nadie más que nosotros!"
    jes "Y sin embargo, nunca imaginé que palabras tan traviesas saldrían de mi dulce e inocente peque [title]~"
    jes "Sigue sorprendiéndome, Su Majestad..."

    show jes close flirt with dissolve
    jes "Me gusta ~"
    
    "ESTA AMENAZA ABSOLUTA."

    hide jes close flirt with dissolve

    jump timetowork_day2

    

# NGOBROL BARENG MAIDY--------------------------------------------------------------------------------------------------------

label maidy_day2:
    "Decidí hablar con Maidy."
    "Estaba ocupada limpiando una sección sucia de la pared mientras tarareaba una melodía alegre y se balanceaba de un lado a otro."
    "Parecía que realmente disfrutaba de su trabajo."
    "En el momento en que me acerqué, ella me vio e inmediatamente dejó lo que estaba haciendo."
    
    show maidy happy with dissolve
    maidy "¡AHHH! ¡¡ES LINDA MAJESTAD!!"
    maidy "¿Qué te trae por aquí~?"
    show maidy panic 
    maidy "Espera, espera, espera... ¡Lo sé!"
    show maidy estatic with dissolve
    maidy "¿No me digas que ya fuiste víctima del encanto de Maidy y querías volver a ver a Maidy?"
    
    "..."
    "......A ella realmente le gusta hablar, ¿no?"
    "Ella me recuerda un poco a Jestyn."
    
    mc "Eh... no. Espera, no, quiero decir..."
    show maidy happy with dissolve
    maidy "¡Ejejeje! Es broma~"
    maidy "Sé que probablemente solo querías charlar conmigo. ¡Estaría feliz de hacerlo!"
    show maidy normal with dissolve
    maidy "Espero que no te importe si sigo limpiando mientras hablamos, Cutie Majesty~"
    maidy "Además, Tyntyn parecía muy ansioso de que habláramos los dos."
    show maidy happy 
    maidy "¿Y honestamente? Haría cualquier cosa por Tyntyn. Jeje~"
    
    "¿Tyntyn?"
    "¿Ese es el apodo que usa para Jestyn?"
    "Ella parece muy cercana a él."
    
    mc "Pareces bastante cercano a Jestyn."
    
    show maidy estatic with dissolve
    "En el momento en que escuchó su nombre, los ojos de Maidy prácticamente brillaron."
    
    maidy "¡¡OH, TYNTYN ES EL BUFÓN MÁS LINDO DE TODOS!!"
    show maidy happy 
    maidy "A ver... lindo, alegre, tonto, guapo..."
    camera at camera_shake
    show maidy estatic 
    maidy "¡AHHHHH! ¡HAY DEMASIADAS COSAS PARA ENUMERAR!"
    camera at reset
    maidy "¡¡SI NECESITO ELEGIR, ES EL JESTYN MÁS PERFECTO DE TODOS!!"
    
    "Maidy continuó divagando una y otra vez, colmando de elogios a Jestyn."
    "A mi lado, Jestyn tenía una amplia sonrisa mientras escuchaba cada palabra."
    
    show maidy happy at center_to_right
    show jes happy with dissolve
    jes "Ah, basta. Eres demasiado generosa, Maidy."
    jes "...Aunque soy bastante sorprendente~"
    show maidy estatic with dissolve
    maidy "¡SÍ, SÍ! ¡¡ERES INCREÍBLE TYNTYN!!"
    
    camera at camera_shake
    "Sin previo aviso, Maidy envolvió sus brazos con fuerza alrededor de uno de los de Jestyn."
    camera at reset
    show jes normal with dissolve
    "Jestyn respondió dándole unas suaves palmaditas en la cabeza."
    "..."
    "Sentí..."

    menu:
        "Celos":
            jump jealous_maidy

        "Nada":
            jump nothing_maidy

label jealous_maidy:
    $ mc_jealous = True
    
    "....."
    "Sentí... algo." 
    "...Aquella escena me resultó extrañamente molesta." 
    "La forma en que Maidy se aferró con tanta fuerza al brazo de Jestyn..."
    "La forma en que él le acariciaba la cabeza con cariño..."
    "La forma en que se sonrieron el uno al otro..."
    "......"
    "Un peso doloroso se instaló en mi pecho."
    "Sentí como si una mano invisible apretara mi corazón."
    "Maldita sea... ¿Fueron celos?"
    "Mi ceño se hizo más profundo antes de que me diera cuenta."
    "Lo último que quería era que Jestyn me viera así."
    show jes happy with dissolve
    "Desafortunadamente, parecía que Jestyn había visto mi expresión. Su sonrisa se amplió al instante."
    "..."
    "Ese bastardo. Él lo sabía."
    "Y a juzgar por esa sonrisa, lo estaba disfrutando muchísimo."

    jump maidy_convo2

label nothing_maidy:
    "......"
    "No pude evitar preguntarme sobre la naturaleza de su relación."
    "Parecían increíblemente cercanos. ¿Quizás eran pareja?"
    "Si ese fuera el caso, entonces estaba realmente feliz por ellos."
    show jes nosmile with dissolve
    "Por el rabillo del ojo, noté que Jestyn me miraba. Su mirada se detuvo."
    "Parecía estar buscando algo en mi rostro."
    show jes unimpress with dissolve
    "Luego, poco a poco, su expresión se fue oscureciendo. Sus cejas se fruncieron y su sonrisa desapareció en una delgada línea."
    "Parecía disgustado."
    "Por alguna razón, esa expresión estaba dirigida a mí."
    "¿Qué? ¿Qué hice?"

    jump maidy_convo2

label maidy_convo2:
    show maidy happy with dissolve
    show jes normal with dissolve
    jes "Maidy, cariño~"
    jes "Por muy encantado que esté con su afecto, tal vez deberíamos abstenernos de tales demostraciones frente a [poss] Majestad."
    
    "Maidy jadeó e inmediatamente soltó su brazo."
    
    camera at camera_shake
    show maidy panic
    maidy "¡AHHHHH! ¡Lo siento mucho, Su Majestad!"
    camera at reset
    maidy "¡Me emocioné demasiado!"
    mc "Oh... está bien. En realidad."
    hide jes with dissolve
    show maidy estatic at center
    with dissolve
    maidy "¡Eeeh! ¡Eres tan adorable, Su Majestad!"
    show maidy nosmile with dissolve
    maidy "Pero... ¿puedo ser honesta?"
    mc "¿Seguro?"
    maidy "La primera vez que te vi, lo que tenía en la cabeza es... ¡Tenía tantas ganas de vestirte!"
    show maidy pout
    maidy "Pero Maidelyn nunca lo permitiría. Ella sigue diciendo que no sería apropiado."
    maidy "Y sí... sé que tiene razón, pero aún así..."
    maidy "¡¿Cómo puede nuestro gobernante andar con ropa así cuando eres el [title] de este reino?! ¡¡Ufhh!!"
    maidy "Pero… ¡ah, claro! Yo no te obligaría."
    
    "Maidy infló sus mejillas en un puchero."
    "¿Quiere vestirme...?"
    "Uh... no creo que eso me importe."
    
    mc "Bueno, supongo que no hay nada malo en ello."
    
    show maidy estatic with dissolve
    "El rostro de Maidy se iluminó instantáneamente."
    
    maidy "¡¿¡¿¡¿EN REALIDAD?!?!?!"
    maidy "¡¡OH, NO PUEDO ESPERAR!!"
    mc "Mmm... ¿eso significa que te gusta disfrazar a otras personas?"
    show maidy happy with dissolve
    maidy "¡Sí! ¡Si pudiera, vestiría a todos los títeres de este reino!"
    maidy "¡Los pondría a todos con ropa rosa! Bonita, ¿verdad?"
    mc "Err... ¿sí...?"
    show maidy pout with dissolve
    maidy "Pero Su Majestad probablemente no permitiría eso... Además, Maidra me odiaría."
    show maidra nosmile at right
    with dissolve
    maidra "Escuché eso."
    maidy "¡Eso es porque quería que me escucharas!"
    show maidra smug with dissolve
    maidra "¿Qué tal si te tiñes el cerebro de rosa? Entonces todo te parecería color de rosa."
    show maidy estatic 
    maidy "¡Ah! Buena idea, espera... ¿no está ya el cerebro rosado?"
    maidra "¿Quién sabe? Quizás los nuestros sean negros."
    show maidy nosmile with dissolve
    maidy "Pero... ¿tenemos siquiera cerebro?"
    show maidra nosmile 
    maidra "......"
    maidy "......"
    hide maidy dissolve
    hide maidra with dissolve
    "De alguna manera, la conversación se había descarrilado por completo... y todo lo que hice fue preguntarle a Maidy sobre moda."
    "Maidy finalmente ahuyentó a Maidra y le dijo que volviera al trabajo. Finalmente, su atención volvió a mí."
    
    mc "Pero debiste haber disfrazado a algunos de los títeres aquí antes, ¿verdad?"
    show maidy estatic with dissolve
    maidy "¡Ah, por supuesto! De hecho, algunos de ellos. Maidra, por ejemplo. Ella es la más difícil de disfrazar."
    show maidy pout
    maidy "Ella dice que vestirse elegante la hace sentir como Jestyn. Ya sabes... como un payaso."
    maidy "Aunque Jestyn es genial. ¡Mmm!"
    show maidy happy 
    maidy "Y luego está Butl-"
    maidy "........."

    stop music fadeout 3.0
    show maidy nosmile with dissolve
    "Me sentí confundido cuando Maidy de repente se detuvo a mitad de la frase."
    "Su expresión alegre desapareció, reemplazada por una triste. El repentino cambio en su humor sólo me dejó aún más confundido."
    
    mc "¿Qué pasa, Maidy?"
    show maidy happy with dissolve
    play music "bgs_medieval normal.mp3" volume 2.0 fadein 3.0
    maidy "¡Quiero decir! ¡Sí! ¡Maidra es uno de los títeres que he disfrazado antes!"
    show maidy normal 
    maidy "Por ahora, sin embargo, todavía tengo que terminar de limpiar este corredor."
    maidy "Si Su Majestad necesita algo alguna vez... o quieres que te vista de gala, ven a mi habitación, ¿vale?"
    show maidy happy with dissolve
    maidy "¡Así que nos vemos en otro momento, Su Majestad~!"
    hide maidy with dissolve

    jump maidconvo

# NGOBROL BARENG MAIDY--------------------------------------------------------------------------------------------------------



# NGOBROL BARENG MAIDELYN-------------------------------------------------------------------------------------------------------
label maidelyn_day2:
    "Caminé hacia Maidelyn."
    "Por lo que había visto hasta ahora, ella parecía ser la más tranquila de las tres sirvientas."
    "Estaba ocupada quitando el polvo de los estantes, completamente concentrada en su trabajo."
    "Decidí observarla en silencio por un momento."
    "Sin embargo, al poco tiempo, Maidelyn notó mi presencia y me ofreció una suave sonrisa."
    show maidelyn normal with dissolve
    maidelyn "Su Majestad, ¿hay algo en lo que pueda ayudarle?"
    
    "Ella se inclinó respetuosamente."
    
    mc "Mm... parecías muy concentrado, así que no quería interrumpir tu trabajo."
    
    show maidelyn talk with dissolve
    "Ella dejó escapar una suave risita."
    
    maidelyn "Su Majestad, no me estás molestando en lo más mínimo, así que no te preocupes por eso."
    maidelyn "¿Supongo que Su Majestad se acercó a mí porque deseaba tener una conversación?"
    
    "Ah. Ella era bastante observadora."
    
    mc "En realidad, sí. Si no te importa."
    show maidelyn normal
    maidelyn "Por supuesto, Su Majestad."
    mc "......Entonces..."
    
    "Miré alrededor de la habitación mientras intentaba pensar en un tema."
    "Probablemente debería empezar con algo sencillo."
    
    mc "¿Tienes algún pasatiempo?"
    show maidelyn nosmile
    maidelyn "¿Pasatiempos?"
    mc "Sí. Me gustaría conocerte mejor... quiero decir, como gobernante de este reino."
    maidelyn "Ya veo."
    
    "Se quedó en silencio por un momento, golpeándose pensativamente la barbilla."
    show maidelyn normal with dissolve
    maidelyn "¿Le gustan las fiestas de té, Su Majestad?"
    
    "Me animé."
    
    mc "¿Fiestas de té?"
    maidelyn "Sí."
    maidelyn "De vez en cuando organizo fiestas de té con mis hermanas o los otros títeres."
    maidelyn "A veces incluso las organizo yo sola."
    maidelyn "Ahora que lo pienso, supongo que ese sería mi pasatiempo."
    show maidelyn talk with dissolve
    maidelyn "Si es del agrado de Su Majestad, ¿quizá podríamos compartir el té algún día?"
    
    "La idea de asistir a una fiesta de té sonaba increíblemente elegante."
    "Para mí, las fiestas de té eran el tipo de reuniones que sólo celebraban los nobles ricos y la gente de la alta sociedad."
    "Al menos, así es como siempre fueron retratados en los libros que había leído."
    "Por eso, nunca me imaginé asistiendo a uno."
    "Aún así..."
    "No podía negar que esa idea me hacía sentir extrañamente sofisticada."
    
    mc "Para ser honesto, nunca he asistido a una fiesta de té en toda mi vida."
    mc "Pero suena divertido, ¿por qué no?"
    
    show maidelyn laugh with dissolve
    "La sonrisa de Maidelyn se amplió y asintió con aprobación."
    
    maidelyn "Me alegra oír eso, Su Majestad."
    show maidelyn talk
    maidelyn "Y no se preocupe si nunca antes ha asistido a uno."
    maidelyn "Estaré más que feliz de enseñarte la etiqueta adecuada para la fiesta del té cuando llegue el momento."
    
    "Asentí con entusiasmo."
    "Los dos pasamos los siguientes minutos charlando sobre las fiestas de té."
    show maidelyn nosmile with dissolve
    maidelyn "... Algo acaba de pasar por mi mente, Su Majestad."
    mc "¿Ah? ¿Qué es?"
    
    "Maidelyn dejó de quitar el polvo del área a su alrededor. Su mirada se dirigió hacia mí, completamente concentrada."
    "Por alguna razón, la atmósfera a nuestro alrededor de repente se sintió un poco más tensa... más seria."
    "Y de alguna manera, eso me puso un poco nervioso."
    
    maidelyn "¿Beberás el té que te sirvo cuando Su Majestad asista a mi fiesta de té más tarde?"
    mc "¿Eh?"
    
    "Su repentina pregunta me hizo dudar."
    "Quiero decir... ¿por qué pensaría que no bebería el té que me sirvió?"
    "Pero... ¿era esta una pregunta capciosa? ¿Me estaba poniendo a prueba?"

    menu:
        "Sí":
            mc "Por supuesto. ¿Por qué no lo haría? Después de todo, pasaste por todos esos problemas para hacerlo por mí."
            
            "Maidelyn dejó escapar una suave risa."
            show maidelyn normal with dissolve
            maidelyn "¿Es así? Es usted una persona amable, Su Majestad."

        "No":
            "....."
            "Ahora que lo pensaba... no podía quitarme la sensación de que algo estaba mal. Una sensación de precaución comenzó a apoderarse de mí."
            "Por supuesto... ella debe haber tenido otra razón para hacerme esa pregunta."
            
            mc "Después de que me preguntaste eso... honestamente, me hiciste pensar dos veces..."
            mc "Lo siento."
            show maidelyn normal with dissolve
            "Maidelyn simplemente respondió con una sonrisa antes de volver a quitar el polvo."
            
            maidelyn "Está bien, Su Majestad. Es bueno tener cuidado."

    show maidelyn nosmile with dissolve
    maidelyn "No quise asustarte. No pondría nada en tu té, así que no te preocupes."
    maidelyn "Solo quería recordarte que hay mucha gente con dos caras en este mundo, Majestad."
    maidelyn "Están por todas partes. En las amistades, en nuestras casas..."
    maidelyn "O incluso... en este reino."
    
    "La mirada de Maidelyn volvió a mí."
    
    maidelyn "No te apresures a confiar en quienes te rodean."
    mc "G-gracias por el consejo... pero... ¿por qué de repente me cuentas esto...?"
    show maidelyn normal with dissolve
    "Maidelyn simplemente sonrió."
    
    maidelyn "Lo descubrirás... si no tienes cuidado."
    mc "¡Oye, no me asustes así!"
    show maidelyn laugh
    maidelyn "Jajaja, perdóname. Sólo estaba bromeando, Su Majestad."
    mc "¿Estabas bromeando o hablabas en serio?"
    show maidelyn talk with dissolve
    maidelyn "Tal vez lo estaba~ Quizás no lo estaba~"
    mc "¡Oye!"
    
    hide maidelyn talk with dissolve
    "Al final de nuestra conversación, me encontré con muchas ganas de asistir a uno."


    jump maidconvo

# NGOBROL BARENG MAIDELYN-------------------------------------------------------------------------------------------------------





# NGOBROL BARENG MAIDRA-------------------------------------------------------------------------------------------------------
label maidra_day2:
    "Me dirigí a Maidra."
    "......"
    "Para ser honesto, esta criada me asustó un poco."
    "Quiero decir, solo mirar su cara me hizo sentir como si ella pudiera golpearme si dijera algo incorrecto..."
    "Quizás."
    "Estaba ocupada barriendo el piso, completamente concentrada en su trabajo."
    "Mi cuerpo vaciló antes de que pudiera acercarme a ella. Al final, me detuve en seco."
    "¿Fue realmente una buena idea?"
    "Jestyn puso una mano en mi espalda, animándome a seguir adelante."
    show jes normal with dissolve
    jes "Está bien, Su Majestad."
    jes "Maidra puede parecer intimidante, pero en realidad es bastante divertida."
    show jes happy with dissolve
    jes "...Bueno. Un poco."
    hide jes happy
    camera at camera_shake
    show maidra nosmile with dissolve
    maidra "¿Qué diablos quieres decir con \"un poco\", payaso idiota?"
    
    "Salté cuando Maidra de repente le gritó a Jestyn."
    camera at reset
    
    show maidra nosmile at center_to_right
    show jes bitch2 at left
    with dissolve
    jes "Uf... ¿Esa voz tuya podría sonar más fuerte? Las trompetas reales se están poniendo celosas."
    camera at camera_shake
    maidra "¡¿Dije qué diablos quisiste decir, payaso idiota?!"
    camera at reset
    
    "Jestyn dejó escapar un suspiro de cansancio."
    
    show jes unimpress with dissolve
    jes "Tsk. Eres incluso más problemática que Knighter."
    show maidra smug with dissolve
    maidra "Pues, gracias."
    maidra "Disfruto poder rivalizar con ese bastardo impulsivo."
    show jes happy2 with dissolve
    jes "Je. Al menos no grita como un lunático cada cinco minutos."
    camera at camera_shake
    show maidra mad
    maidra "¡¿QUÉ?!"
    camera at reset
    
    "Jestyn simplemente se rió en respuesta al grito indignado de Maidra."
    "Finalmente, se volvió hacia mí."
    
    show jes normal2 with dissolve
    jes "Ahora cierra esa boca tuya."
    jes "Vas a ahuyentar a [poss] Majestad."
    
    "La mirada de Maidra se dirigió hacia mí."
    "Ella me miró con una ceja levantada."
    show maidra smug with dissolve
    "Luego ella sonrió."
    
    maidra "Ohhh..."
    maidra "Asusta a [poss] Majestad, ¿eh?"
    maidra "¿Qué clase de [title] se deja intimidar tan fácilmente?"
    maidra "¿Un pequeño gruñido y salen corriendo como un conejo asustado?"
    
    "Fruncí el ceño."
    
    maidra "¿Qué pasa, Su Majestad?"
    maidra "¿No me digas que estás ofendido?"
    
    "Sus palabras me irritaron."
    "Sabía que le tenía miedo, pero..."
    "Por alguna razón, que me llamaran cobarde me molestaba mucho más de lo que debería."
    "No quería que me vieran como alguien débil. Así que respiré profundamente."
    
    mc "Tu..."
    mc "¿Qué te da derecho a llamarme cobarde?"
    
    show maidra nosmile with dissolve
    "Una de las cejas de Maidra se levantó."
    
    mc "No se puede juzgar a una persona con sólo mirarla."
    mc "Así que no andes llamándome cobarde."
    mc "Si tienes tanta confianza, entonces ven a pelear conmigo."
    show maidra suprais with dissolve
    show jes suprais2 with dissolve
    maidra "..................."
    jes "..................."
    mc "................"
    
    "¡¿Qué diablos acabo de decir?!"
    
    show maidra smug
    show jes happy
    maidra "Pff..."
    
    hide maidra with dissolve
    hide jes with dissolve
    "Después de escuchar mi ridículo desafío, Maidra se echó a reír como si fuera la cosa más divertida que jamás había escuchado."
    "A mi lado, Jestyn claramente estaba luchando por mantener la cara seria."
    
    show maidra smug with dissolve
    maidra "¡Jajaja! Su Majestad, en realidad eres bastante divertido."
    maidra "Je, sólo estaba bromeando contigo."
    maidra "Pero después de esa reacción, ahora quiero seguir metiéndome contigo."
    maidra "Desafiar a un títere que mide el doble de tu tamaño requiere agallas."
    maidra "Estúpidas agallas, pero agallas al fin y al cabo."
    
    "Podía sentir mi cara arder de vergüenza."
    "En ese momento, no deseaba nada más que cavar el hoyo más profundo imaginable y arrojarme en él."
    
    maidra "Pero claro, Su Majestad. ¿Por qué no?"
    maidra "Quizás algún día podamos echar un pulso. O una carrera."
    maidra "O luchar."
    
    "Estaba empezando a arrepentirme de haberla desafiado."
    "Estaba absolutamente a punto de morir."
    
    show maidra normal with dissolve
    maidra "Y si ganas, tal vez te conceda lo que quieras."
    maidra "Pero si gano..."
    show maidra smug with dissolve
    stop music
    maidra "Tienes que dejarme comerte."
    
    "......"
    
    mc "Lo siento, ¿qué?"
    
    hide maidra smug with dissolve
    "Miré a Maidra confundido."
    "Por un momento pensé que debía haberla escuchado mal."
    "Pero a juzgar por la sonrisa todavía plasmada en su rostro, definitivamente no lo había hecho."
    
    jes "Maidra."
    
    "Sentí la mano de Jestyn posarse contra mi omóplato, acercándome suavemente un poco más a él."
    
    show jes creep at right
    with dissolve
    jes "Esas son cosas bastante inapropiadas para decirle a Su Majestad, ¿no crees?"
    
    show maidra nosmile at left
    with dissolve
    "Maidra puso los ojos en blanco y chasqueó la lengua."
    
    play music "bgs_medieval normal.mp3" fadein 3.0 
    maidra "Obviamente estaba bromeando, payaso idiota."
    maidra "No hay necesidad de volverse tan posesivo de esa manera."
    maidra "En serio, es vergonzoso verlo."
    show jes unimpress2 with dissolve
    jes "¿Posesivo? ¿A mí?"
    show maidra smug with dissolve
    maidra "Por favor. Eres tan sutil como un ladrillo en la cara."
    
    hide maidra smug with dissolve
    hide jes unimpress2 with dissolve
    "Maidra lo despidió."
    
    show maidra normal with dissolve
    maidra "Ahhh, está bien. Entonces, ¿por qué has venido a verme, Su Majestad? Supongo que querías charlar un rato conmigo?"
    mc "Sí. ¿Es tan obvio?"
    maidra "Realmente no. No estaba prestando mucha atención. Es solo que Jestyn planeaba que hablaras conmigo, así que..."
    maidra "¿Qué quieres saber de mí?"
    show maidra nosmile with dissolve
    maidra "Si me preguntas sobre mis pasatiempos o cosas que me gustan, está bien... pero eso es algo común."
    
    "......En realidad, eso era exactamente lo que estaba a punto de preguntar."
    "¿Qué tipo de tema le parecería realmente interesante a Maidra...? No soy muy bueno para proponer temas de conversación inusuales."
    "¿En serio iba a preguntar: '¿Y si fueras un gusano?'"
    
    maidra "Y no me preguntes: '¿Y si soy un gusano?' Eso es raro y no me gusta. ¿Qué demonios? No soy un gusano. No existe el 'qué pasaría si'."
    
    "......Está bien.."
    "Maidra continuó barriendo el piso."
    "Noté que de vez en cuando parecía molesta con su vestido de sirvienta."
    
    show maidra mad 
    maidra "Uf, este vestido de sirvienta sigue estorbando cuando estoy barriendo... ¿Cómo pueden Maidelyn y Maidy limpiar con trajes como este? Uf, que molesto..."
    show maidra nosmile
    maidra "De todos modos, seguiré barriendo mientras espero tu pregunta, Su Majestad."
    mc "Oh... uh... ¿no te gusta tu vestido de sirvienta?"
    maidra "¿Qué? Oh sí. Se podría decir eso."
    mc "¿Por qué?"
    show maidra mad with dissolve
    maidra "Bueno... ¡es difícil moverse! Quiero decir... quiero poder correr todo lo que quiera sin tener que levantarme el vestido primero."
    maidra "Como pantalones. Si quieres correr, simplemente corre. Es mucho menos problemático que un vestido."
    mc "Ya veo... Tal vez te gustaría más tu uniforme de sirvienta si tuviera pantalones en lugar de falda."

    maidra "........"
    show maidra sad with dissolve
    maidra "Sinceramente, no me gusta mucho mi papel de criada."
    maidra "No lo sé... el traje de sirvienta me parece demasiado femenino. ¡Y prefiero usar algo genial!"
    maidra "Como una armadura..."
    maidra "......"
    maidra "¿Por qué no podría haber conseguido el papel de Knighter en su lugar...? Si pudiera, cambiaría de lugar con él. Él podría ser Maidra y yo sería Knighter..."
    mc "¿Eh? ¿Es posible cambiar roles así?"
    
    show maidra nosmile with dissolve
    "Maidra me miró por un momento antes de continuar."
    
    maidra "...Sí y no. Podría suceder, pero la forma de hacerlo es... uh... no exactamente buena. Quiero decir, básicamente tendríamos que derrotarnos unos a otros."
    maidra "Es como la cadena alimentaria en la naturaleza. El más fuerte es el que llega a la cima."
    maidra "Y... jaja. No es una buena idea. Entonces, por ahora, no tengo más remedio que aceptar mi papel de Maidra la doncella."
    
    "Honestamente, su reacción no me sorprendió tanto."
    "Desde el momento en que la conocí, me di cuenta de que Maidra no era muy femenina."
    "Tenía sentido que no le gustara su papel."
    "Aún así… no pude evitar sentir un poco de lástima por ella. Tenía que vivir con algo que no le gustaba."
    "......"
    "Pero... honestamente, pensé que ser sirvienta era genial."
    
    mc "Lo siento, Maidra."
    mc "Pero... creo que ya te ves muy bien como sirvienta."
    show maidra sad with dissolve
    maidra "Mmh... gracias por el cumplido... pero todavía no me gusta este vestido."
    mc "Por supuesto. Pero… ¿alguna vez has oído hablar de espías que se disfrazan de sirvientas?"
    show maidra nosmile
    maidra "¿Eh?"
    
    "Aproveché todo lo que había aprendido de las novelas, los cómics y las películas que había consumido a lo largo de los años. Todas esas historias le habían dado a mi imaginación bastante espacio para trabajar."
    "Por una vez, todo ese conocimiento aparentemente inútil podría resultar útil."

    mc "Una vez leí un cómic sobre una espía que se coló en un palacio enemigo y se disfrazó de doncella."
    maidra "¿Qué? Nunca he oído hablar de eso."
    mc "Ella era realmente genial. Mientras trabajaba como sirvienta, actuó con toda gracia y gentileza. Pero cuando llegó el momento de hacer su movimiento, se volvió increíblemente hábil y fuerte."
    mc "Incluso mantenía pequeñas armas escondidas alrededor de sus muslos, debajo de su vestido de sirvienta."
    mc "Y cada vez que las usaba, se veía increíblemente genial, a pesar de que sus armas no eran un hacha enorme o un arma gigante."
    show maidra estatic with dissolve
    "Mientras explicaba la historia, los ojos de Maidra lentamente comenzaron a brillar de admiración."
    "¿Realmente logré hacerla sentir un poco mejor?"

    maidra ".....Entonces..."
    maidra "¿Yo... podría ser genial así...?"
    mc "¿Por qué no? Quiero decir, estoy seguro de que aún puedes lucir fuerte y genial, y ser tú misma, incluso con algo femenino."
    maidra "Yo....."
    maidra "...Sí. Quizás pueda."
    maidra "....."
    maidra "¡Sí, puedo!"
    camera at camera_shake
    show maidra blush
    maidra "M-quiero decir... sí... eso suena muy bien... ejem."
    camera at reset
    
    "No pude evitar reírme de lo mucho que Maidra intentaba mantener la compostura."
    
    maidra "Mmh... está bien... Su Majestad... en realidad me hizo sentir un poco mejor ahora... uhm..."
    maidra "....Gracias... Supongo..."
    mc "No hay problema."
    maidra "U-uhm... de todos modos, será mejor que vuelva al trabajo."
    maidra "Cuanto antes termine, antes me dormiré."
    maidra "... G-gracias de nuevo por hoy, Su Majestad..."
    hide maidra blush with dissolve
    "Volvió a concentrarse en barrer el suelo, dejándome aquí junto a Jestyn."
    jump maidconvo

# NGOBROL BARENG MAIDRA-------------------------------------------------------------------------------------------------------


#CROWNUS ROOM CHOICE--------------------------------------------------------------------------------------------------------------------------

label crownus_room1:
    "Mi atención se desvió hacia la puerta del Rey Marioneta."
    "Comparado con las otras salas de títeres, esa parecía la más..."
    "...¿caótica?"
    "En la puerta principal había un nombre garabateado que decía \"Crownus\"."
    "¿Ese era el nombre del Rey Marioneta?"
    "Sentí curiosidad por lo que había dentro."
    
    mc "Uhm... Me gustaría echar un vistazo a la habitación del Rey Marioneta por un momento."

    show jes suprais2
    "Jestyn se congeló."
    "Sus ojos se abrieron y, por un breve momento, su sonrisa desapareció."

    show jes annoy2 with dissolve
    "Luego regresó."
    "Pero esta vez pareció forzado."
    
    jes "Ah, ¿la habitación del Rey Marioneta?"
    jes "Está bastante desordenado y no hay nada interesante allí dentro."
    jes "De verdad."

    show jes normal2 with dissolve
    jes "Aconsejaría a Su Majestad que no se moleste en esa habitación."

    jump chooseroom_day2

label crownus_room2:
    ".........."
    "Mis ojos seguían volviendo a la habitación del Rey Marioneta."
    "Cuanto más intentaba Jestyn desanimarme, más curiosidad sentía."
    
    mc "Sólo echaré un vistazo rápido."
    mc "No me importa si está desordenado."
    mc "Sólo quiero ver lo que hay dentro."

    show jes normal2 with dissolve
    jes "Su Majestad podrá hacerlo más tarde."
    jes "Por ahora, sin embargo, creo que sería mejor para nosotros conocer primero a los otros títeres."
    jes "Ésta es la cuestión más importante en este momento."

    jump chooseroom_day2


label crownus_room3:
    $ crownus_secret_point += 1

    stop music fadeout 3.0
    hide jes with dissolve
    who "{color=#FFC04C}Puedes mirar dentro de esa habitación.{/color}"
    who "{color=#FFC04C}Continúa...{/color}"
    who "{color=#FFC04C}Da un paso adelante...{/color}"
    who "{color=#FFC04C}Now...{/color}"
    who "{color=#FFC04C}Abrelo...{/color}"
    jes "dije..."

    play sound "slap.mp3" volume 3.0
    camera at camera_shake
    show matageter
    jes "{color=#FF253E}{cps=15}NO!! {/cps}{/color}"
    
    "....."
    "...¿Eh...?"
    "Me estremecí cuando Jestyn de repente agarró mi mano y la apartó del pomo de la puerta del Rey Marioneta."
    "Me agarraba con tanta fuerza que dolía."
    play sound "nyekek.mp3" volume 2.0
    "El dolor me recorrió el brazo allí donde sus dedos lo rodeaban."
    "Su mirada era aguda. Mortal."
    "No había lugar a dudas. Jestyn estaba enojado."
    "¿Pero por qué?"
    
    camera at reset
    mc "Uf- Jestyn..."
    mc "T-Me estás lastimando...."
    
    show jes crownus room with dissolve
    "Jestyn inmediatamente pareció darse cuenta de lo que estaba haciendo."
    "Su agarre se aflojó de inmediato."
    "Pero no me soltó el brazo."
    
    show jes crownus room2 with dissolve
    hide matageter
    jes "Perdóneme, Su Majestad..."
    jes "Es solo..."
    
    "Dejó de hablar."
    "Durante varios momentos permaneció en silencio, tratando de recomponerse."
    
    jes "Su Majestad, por favor perdone mi impertinencia, pero..."
    jes "Por favor no entres en esa habitación."

    show jes crownus room3 with dissolve
    jes "Por favor."
    jes "Volvamos nuestra atención al asunto que nos ocupa, ¿de acuerdo?"
    
    play music "bgs_medieval normal.mp3" volume 3.0 fadein 3.0
    "Asentí."
    "No quería agravar más la situación."
    "....."
    "Espera."
    "¿Desde cuándo estaba alcanzando el pomo de la puerta?"
    "Sólo quería mirar hacia adentro."
    "No recordaba haber decidido abrir la puerta."
    "Entonces, ¿por qué mi mano lo había estado alcanzando?"

    hide jes crownus room3 with dissolve


    jump chooseroom_day2  



label wizzyroom_day2:

    "Mi mirada se dirigió a la puerta naranja. La placa de identificación simplemente decía: «Mago»."
    "Si no recuerdo mal, el nombre del títere mago era Wizzy."
    "Estoy bastante seguro de que Jestyn mencionó ese nombre ayer. Bueno, supongo que intentaré conocerlo primero."
    "Señalé hacia la habitación de la marioneta mago."
    
    mc "Creo que me gustaría conocerlo."

    show jes happy2 with dissolve
    "La sonrisa de Jestyn se amplió."
    
    jes "Una elección acertada, Su Majestad."
    jes "Vamos."
    
    hide jes happy2 with dissolve
    "Jestyn me llevó hasta la puerta de la marioneta mago."

    scene bg_wizzydoor with dissolve
    "Puso una mano sobre mi hombro y me colocó directamente frente a ella."
    "Luego casualmente dio un paso hacia el lado izquierdo de la puerta."
    "... ¿Por qué estaba parado allí?"
    
    mc "Jestyn, ¿por qué estás parado así junto a la puerta?"
    mc "¿No estorbarás cuando se abra?"

    show jes normal2 with dissolve
    jes "Ese es el punto."
    mc "¿Por qué?"

    show jes happy2 with dissolve
    jes "... digamos simplemente..."
    jes "...Para sorpresa."
    
    "..."
    "Muy convincente."

    hide jes happy2 with dissolve
    "Una vez que Jestyn se aseguró de que estaba listo, llamó a la puerta de Wizzy."
    ".... No pasó nada durante unos segundos."
    "Entonces, escuché pasos acercándose desde el otro lado de la puerta."
    "Se acercaron..."
    "...y se detuvo justo enfrente de ella."
    "........"
    "Silencio."
    "¿Qué está haciendo?"

    play sound "opendoor.mp3"
    camera at camera_shake
    scene bg_puppetroom with dissolve
    stop music fadeout 2.0
    
    "La puerta se abrió de repente, revelando un títere vestido de mago."
    camera at reset
    "Estaba sosteniendo un bastón que se parecía al bastón de un mago, y-"
    "¡¿ME LO ESTABA Blandiendo?!"
    
    play music "bgs_silly medieval.mp3" volume 1.0 fadein 3.0
    camera at camera_shake
    show wiz angry
    wiz "JESTYN ¿DÓNDE ESTÁ MI-?"
    camera at reset
    pause 0.1
    camera at camera_shake
    show jes suprais at left
    jes "¡¡WIZZY, PARA!!"
    camera at reset
    
    "Jestyn inmediatamente intervino y atrapó el bastón de Wizzy antes de que pudiera golpearme."
    "Wizzy detuvo su movimiento en estado de shock."
    
    show wiz panic 
    wiz "¡¿QUÉ-?!"
    
    "Wizzy inmediatamente retiró su bastón y miró a Jestyn en estado de shock."
    "Un momento después, su atención se centró en mí."

    show wiz nosmile at center_to_right
    show jes unimpress2 
    with dissolve
    jes "¿Por qué de repente intentaste atacar a alguien así?"

    show wiz angry2 with dissolve
    wiz "¡PORQUE ESTABA INTENTANDO GOLPEARTE!"
    wiz "¡PENSÉ QUE ERA TÚ!"

    show wiz angry 
    wiz "¿DÓNDE ESTÁ LA POCIÓN QUE ACABO DE HACER?"
    
    show jes happy3 with dissolve
    "Jestyn simplemente se encogió de hombros."
    
    jes "¿Quién sabe~?"
    wiz "¡¡LA ACABABA DE HACER- UFF!!"
    
    show jes laugh2 with dissolve
    "Jestyn respondió a la indignación de Wizzy con nada más que su habitual risa maníaca."

    show wiz nosmile with dissolve
    "Finalmente, Wizzy se volvió hacia mí."
    "Cuando me vio, rápidamente se disculpó."
    
    show wiz nervous with dissolve
    wiz "¡Ah, lo siento! No sabía que había alguien más que Jestyn aquí."
    wiz "Lamento mucho el caos-"
    
    show wiz pout
    "Se detuvo a mitad de la frase."

    show wiz nosmile
    wiz "...Espera..."
    wiz "¿Quién eres...?"

    show jes normal2 with dissolve
    jes "Este es [player_name]."
    jes "Nuestro nuevo [title]. Del que te hablé esta mañana."
    
    "A pesar de que los ojos de Wizzy estaban ocultos debajo de la tela que los cubría, aún podía leer la sorpresa en su rostro por la forma en que abrió la boca."
    "Claramente no esperaba esto."

    show wiz nervous with dissolve
    wiz ".... E-Espera..."
    wiz "Eres... ¿nuestro nuevo [title]?"
    wiz "Uh-oh..."
    wiz "No esperaba conocerte tan pronto."
    wiz "Yo..."
    
    show wiz panic with dissolve
    "Wizzy miró nerviosamente hacia su habitación."
    
    show wiz nervous with dissolve
    wiz "M-Mi cuarto es un poco..."
    

    "Miró frenéticamente a su alrededor, como si buscara una excusa."
    "Luego volvió a Jestyn."

    play sound "movement.mp3" volume 3.0
    hide wiz nervous
    hide jes normal2
    camera at camera_shake
    show jeswiz_wizroomscene
    wiz "¡JESTYN! ¡Te perdonaré si me ayudas un minuto!"

    camera at reset
    "Jestyn miró a Wizzy con una mezcla de confusión y curiosidad."

    show jeswiz_wizroomscene2 with dissolve
    wiz "A-Jajajaja... Mis más sinceras disculpas, querida Majestad. Por favor, danos un segundo... quiero decir... un minuto. Jeje... jeje..."
    wiz "¡VOLVEREMOS EN UN MOMENTO!"
    
    play sound "doorslam.mp3"
    hide jeswiz_wizroomscene2
    camera at camera_shake
    scene bg_wizzydoor
    "Antes de que pudiera decir algo, Wizzy agarró a Jestyn por el brazo, lo arrastró hacia su habitación y cerró la puerta de golpe frente a mí."
    "Dejándome sola en el pasillo, completamente confundida."

    camera at reset
    "Aun así, todavía podía oírlos a los dos hablando en voz baja desde el interior de la habitación."
    
    wiz "Teletransporta todo esto."
    jes "¡¿Qué?! ¡Eso es demasiado!"
    wiz "¡Date prisa! [poss] ¡Majestad está esperando!"
    wiz "¡No quiero que se sientan incómodos!"
    jes "Ahora, querido mago... ¿no te dijo este magnífico bufón que ordenaras este espantoso desastre esta mañana?"
    wiz "¡Lo recuerdo! ¡Pero nunca dijiste que Su Majestad vendría esta noche!"
    jes "¿Ah? Entonces, ¿cuándo, dime, imaginabas que vendría [subj]? ¿El año que viene? ¡Desde luego que te lo dije esta mañana!"
    wiz "...... ¿Cuándo?"
    jes "¡Mientras te enterrabas en tus pequeños experimentos! Estaba parado JUSTO a tu lado."
    wiz "...Mentiroso. Siempre mientes."
    jes "¡Esta vez no! Quería que todo fuera absolutamente perfecto para Su Majestad, así que le dije que [subj] estaría de visita esta noche y que esta catástrofe de habitación tenía que desaparecer."
    wiz "........"
    jes "¡En verdad, eres imposible!"
    wiz "¡No empieces a hablarme en inglés antiguo! Ayúdame a limpiar este desastre."
    jes "Jeje ~ Vamos, Wizzy. Entonces seguramente unas cuantas pociones pequeñas son un precio justo por la ayuda del gran Jestyn, ¿eh?"
    wiz "¡¿Qué?! ¡No! yo-"
    wiz "....."
    wiz "...¡Bien! ¡Bien! ¡Pero sólo por una semana! ¡Ahora deja de estar parado! [poss] ¡Majestad está esperando!"

    play sound "snap.mp3" volume 3.0
    pause 0.3
    play sound "snap.mp3" volume 3.0
    pause 0.3
    play sound "snap.mp3" volume 3.0
    "Unos momentos más tarde, escuché varios chasquidos de dedos en rápida sucesión."
    "Entre los sonidos de los dedos chasqueando, escuché algunas discusiones entre Jestyn y Wizzy."
    "Luego silencio."

    camera at camera_shake
    scene bg_puppetroom
    play sound "opendoor.mp3" volume 2.0
    "Después de unos minutos la puerta se abrió y finalmente ambos salieron."
    camera at reset
    show wiz talk at right
    with dissolve

    show jes tired at left
    with dissolve
    wiz "¡Perdón por hacerte esperar, Su Majestad!"
    wiz "¡Todos los problemas finalmente desaparecieron! ¡Ahora, por favor, entra!"
    
    "La expresión nerviosa que Wizzy había tenido hace unos momentos había desaparecido por completo, reemplazada por una sonrisa brillante y acogedora."
    "Mientras tanto, Jestyn, que se había visto tan engreído apenas un minuto antes, ahora parecía tan pálido como alguien que había perdido toda la sangre de su cuerpo."
    "¿Qué le pasó?"
    "Decidí no pensar más en eso y simplemente entré a la habitación de Wizzy."

    hide jes tired with dissolve
    hide wiz talk with dissolve
    play sound "closedoor.mp3" volume 2.0
    scene bg_wizzyroom with dissolve
    "En el momento en que entré, el fuerte olor a productos químicos me hizo cosquillas en la nariz."
    "La habitación de Wizzy era sorprendentemente espaciosa y ordenada... al menos, por lo que pude ver a primera vista."
    "Las paredes estaban cubiertas de hojas de papel llenas de notas y fórmulas que ni siquiera podía empezar a entender."
    "Su cama estaba en el lado derecho de la habitación, con largas mesas al lado."
    "La mesa más cercana a la cama estaba repleta de papeles, libros, bolígrafos y diversos artículos de papelería. Supuse que es donde Wizzy escribió la mayor parte de sus escritos."
    "La otra mesa, en el lado izquierdo de la habitación, estaba llena de todo tipo de equipos utilizados para sus experimentos."
    "Y en el centro de la habitación había un gran caldero. Teniendo en cuenta su papel como títere mago del reino, no es exactamente sorprendente."

    show wiz nervous2 with dissolve
    wiz "...Uh... S-sí, sé que mi habitación huele un poco extraño. Sólo estaba realizando algunos experimentos... Mis disculpas, Su Majestad."

    "Parecía que me notó mirando alrededor de su habitación."

    wiz "Y-Y... Espero que mi habitación sea lo suficientemente cómoda para ti, Su Majestad. También espero que esté lo suficientemente ordenada... jeje."

    show wiz nervous at center_to_right
    show jes bitch2 with dissolve
    jes "Por supuesto que lo es. Esta habitación sería un completo desastre sin mí."

    show wiz angry 
    wiz "¡¡Shh!!"

    hide jes bitch2 with dissolve
    show wiz talk at center
    with dissolve
    wiz "¡Ah! ¿Por qué no tomas asiento primero, Su Majestad? Estar de pie debe de ser agotador."
    
    hide wiz talk with dissolve
    "Wizzy rápidamente agarró una silla y la colocó detrás de mí."
    "Jestyn, sin embargo, lo miró con evidente desaprobación y sacudió lentamente la cabeza."
    
    show jes nosmile2 at right 
    with dissolve
    show wiz normal at left
    with dissolve
    jes "Wizzy... ¿hablas en serio? ¿Vas a hacer que [poss] Majestad se siente en una silla de madera dura?"
    
    show wiz panic with dissolve
    "Sólo entonces Wizzy se dio cuenta de lo que había hecho. Inmediatamente se volvió hacia mí, nervioso."
    
    wiz "E-espera... ¡tienes razón! ¡Mis disculpas, Su Majestad! ¡Te buscaré una silla acolchada adecuada ahora mismo!"
    mc "N-Realmente no tienes que ir tan lejos, Wizzy..."
    
    "Quiero decir... estoy acostumbrado a sentarme en las viejas sillas de madera de mi apartamento..."

    mc "Puedes tratarme como-"
    
    "Antes de que pudiera terminar mi frase, Jestyn me interrumpió."

    show jes normal2 with dissolve
    jes "Tut, tut, tut~ Eso simplemente no vale, Su Majestad. Eres nuestro [title]. Nada menos que el mejor trato será suficiente para ti."
    wiz "¡Exactamente! ¡De hecho, esta vez estoy de acuerdo con Jestyn!"

    show jes unimpress2 with dissolve
    jes "... ¿Disculpe? ¿Esta vez? ¿Qué se supone que significa eso?"
    wiz "¡De todos modos! Iré a buscar un bonito sillón suave para Su Majestad."

    show jes normal2_2 
    jes "No hay necesidad."
    jes "¿Por qué molestarse con un cojín... cuando Su Majestad podría simplemente sentarse sobre mí?"
    stop music
    mc "...???"
    
    play music "bgs_silly medieval.mp3" volume 2.0 fadein 3.0
    show wiz pout with dissolve
    "Me quedé mirando a Jestyn con total confusión. Él sólo me mostró una amplia y descarada sonrisa, sus mejillas teñidas de rosa."
    "No es posible que mis oídos me hayan traicionado."

    show wiz nosmile 
    "Wizzy miró fijamente a Jestyn por un momento, con el rostro congelado por la incredulidad."

    show wiz nervous with dissolve
    "Cuando se giró para mirarme, sacudió sutilmente la cabeza, con cuidado de que Jestyn no notara que no estaba de acuerdo con la idea."
    "Sinceramente, no me importaba sentarme en una silla dura. De todos modos, estaba más que acostumbrado a ello."
    "Pero... ¿sentado sobre alguien? Quiero decir, ¿en una marioneta? Definitivamente fue la primera vez para mí."
    "Me encontré preguntándome qué opción sería la mejor."

    menu:
        "Siéntate en Jestyn":
            $ sit_on_jestyn = True
            jump sit_on_jestyn

        "Siéntate en la silla":
            $ sit_on_jestyn = False
            jump sit_chair

label sit_on_jestyn:
    "No podía creer que estaba a punto de decir esto."
    "Pero... estaba cansado de sentarme en sillas duras. Y sentarme en Jestyn... bueno, supuse que sería una experiencia nueva."
    
    mc "...Muy bien, Jestyn. Sé mi silla."
    
    show wiz panic with dissolve
    show jes freak with dissolve
    "En el momento en que las palabras salieron de mi boca, Wizzy me miró con total incredulidad. Honestamente... apenas podía creer que yo mismo hubiera dicho eso."
    "Jestyn, por otro lado, parecía absolutamente encantado. Su sonrisa se hizo aún más amplia y un sonrojo se deslizó por sus mejillas."
    
    hide wiz panic with dissolve
    show jes flush2 at center
    with dissolve
    jes "Con mucho gusto, Su Majestad..."
    
    hide jes flush2 with dissolve
    "Jestyn dio un paso detrás de mí antes de bajar al suelo. Plantando sus manos firmemente en el suelo, se puso a cuatro patas."
    
    jes "Su asiento le espera, Su Majestad~"
    
    show cg_jeschair with dissolve
    "Me acomodé con cuidado en la espalda de Jestyn."
    "En el instante en que lo hice, sentí su cuerpo temblar ligeramente."
    "También podía oírlo dejando escapar pequeños ruidos, haciendo todo lo posible para mantenerlos bajo control."
    "...Tenía la sensación de que Jestyn estaba disfrutando esto."
    "Wizzy miró entre Jestyn y yo. Parecía que quería decir algo... pero finalmente decidió no hacerlo."
    hide cg_jeschair with dissolve
    
    show wiz nosmile2 with dissolve
    wiz "E-Em... en ese caso... Espero que estés a gusto, Su Majestad..."

    jump wizzy_convo

label sit_chair:
    "Está bien. No estaba dispuesto a dejar que un títere bufón actuara como un completo bicho raro a mi alrededor todo el tiempo."
    
    mc "Me sentaré en la silla, Jestyn."
    
    show jes pout2 with dissolve
    show wiz talk with dissolve
    "Jestyn inmediatamente hizo un puchero."
    "Mientras tanto, a su lado, Wizzy dejó escapar un suspiro de alivio y me mostró el pulgar con disimulo."
    
    jes "Prometo que estoy mucho más cómodo que esa silla. Además... tú eres Su Majestad."
    mc "Y eso significa que puedo tener lo que quiero. Ahora quiero sentarme en la silla."
    
    "El puchero de Jestyn se hizo más profundo."
    
    jes "...Como Su Majestad desee."
    
    hide jes pout2 with dissolve
    hide wiz talk with dissolve
    "Finalmente tomé asiento en la silla."

    jump wizzy_convo


label wizzy_convo:
    show wiz normal with dissolve
    wiz "Muy bien... Supongo que finalmente podemos tener una conversación adecuada ahora."

    stop music fadeout 2.0
    show wiz pout with dissolve
    wiz "...."

    play music "bgs_medieval normal.mp3" volume 2.0 fadein 3.0
    show wiz nervous with dissolve
    wiz "Um... jaja... en realidad estoy muy nervioso. Todo esto es tan repentino... y completamente fuera de mi horario habitual."

    show wiz panic2 with dissolve
    wiz "¡P-Pero por favor no me malinterpretes, Su Majestad! ¡Realmente quiero hablar contigo!"
    
    show wiz nosmile with dissolve
    "Wizzy respiró hondo, intentando calmarse."
    
    $ voice_duck_start()
    show wiz talk 
    voice "WIZZY01_DAY2.ogg"
    wiz "No creo que nos hayamos presentado adecuadamente todavía, ¿verdad, Su Majestad? Mi nombre es Wizzy. Soy el títere que sirve al reino como mago. Es un honor conocerte."
    $ voice_duck_end()

    "Wizzy se inclinó respetuosamente ante mí."
    
    mc "Soy [player_call]. Es un placer conocerte también, Wizzy."

    show wiz talk with dissolve
    wiz "¡M-YO TAMBIÉN-! Quiero decir... el placer es mío también, Su Majestad."
    wiz "Estoy emocionado, majestad. Ha... pasado mucho tiempo desde la última vez que tuvimos un gobernante. ¿Cuántos años han pasado ahora...?"
    wiz "Desde que Cro-"
    
    show wiz nervous with dissolve
    "Wizzy se interrumpió abruptamente."
    
    wiz "Quiero decir... sí. Desde que falleció el rey."
    
    "El silencio se apoderó de la habitación. La atmósfera de repente se puso tensa."
    "Pero no por mucho tiempo, Wizzy aplaudió para romper el silencio."

    show wiz normal2 with dissolve
    wiz "Jestyn mencionó que traería a Su Majestad a conocerme."

    show wiz nervous2 with dissolve
    wiz "P-Pero... quedé tan atrapado en mis experimentos que... bueno... perdí completamente la noción del tiempo."

    show wiz talk with dissolve
    wiz "Jeje... Dado que el objetivo es que nos conozcamos, no dudes en preguntarme lo que quieras, Su Majestad."
    
    show wiz talk2 with dissolve
    wiz "¡Ah, ay! ¡Sólo un momento! ¡Debería haberte preparado algunos refrescos! ¡Ya vuelvo, Su Majestad!"
    
    "Wizzy corrió hacia un gabinete cercano y comenzó a buscar algo que ofrecerme."
    "Mientras Wizzy se ocupaba, mis ojos comenzaron a vagar por la habitación."

    hide wiz talk2 with dissolve

label examinewizzyroom_day2:
    if repeat_route < 2:
        $ wizzyroom_text = "Examina la esquina de la habitación."
        
    elif examinecornerwizzy == 0:
        $ wizzyroom_text = "{color=#FFC04C}¿No tienes curiosidad?{/color}"
        
    elif examinecornerwizzy == 1:
        $ wizzyroom_text = "{color=#FFC04C}Examínelo más de cerca..{/color}"
        
    else:
        $ wizzyroom_text = "{color=#FFC04C}Más cerca~{/color}"
    menu:
        "Examina los papeles.":
            jump examine_paper

        "[wizzyroom_text]" if examinecornerwizzy < 3:
            $ examinecornerwizzy += 1
            
            if examinecornerwizzy == 1:
                jump examine_corner1
                
            elif examinecornerwizzy == 2:
                jump examine_corner2
                
            elif examinecornerwizzy == 3:
                jump examine_corner3

        "Examina el estante de pociones de Wizzy.":
            jump examine_potion

        "eso es suficiente":
            jump wizzy_convo2

label examine_paper:
    "Mis ojos se sintieron atraídos por las innumerables hojas de papel clavadas en las paredes de la habitación de Wizzy."
    "Había muchísimos, cada uno cubierto de notas que ni siquiera podía empezar a entender."
    "Algunos parecían estar llenos de fórmulas químicas, mientras que otros estaban cubiertos de ecuaciones matemáticas."
    "A juzgar solo por estas notas, Wizzy debe haber sido increíblemente inteligente."
    "Continué mirando el resto de ellos."
    "Una hoja en particular me llamó la atención. A diferencia de las demás, no estaba llena solo de números y fórmulas. También tenía dibujos."
    "Hice lo mejor que pude para darle sentido, pero desafortunadamente, estaba completamente fuera de mi alcance."  

    jump examinewizzyroom_day2  

label examine_potion:
    "Mis ojos se dirigieron hacia un estante lleno de botellas de todas las formas y tamaños."
    "Variaban tanto en forma como en tamaño, pero lo que más destacaba era la gran variedad de colores."
    "Era increíblemente colorido."
    "Junto a las botellas llenas de líquidos vibrantes había otras que contenían ingredientes que ni siquiera reconocí."
    "En las películas, botellas como estas generalmente estaban llenas de ingredientes para preparar pociones."
    "Teniendo en cuenta el papel de Wizzy como títere mago del reino, supongo que tenía mucho sentido."  

    jump examinewizzyroom_day2         

label examine_corner1:
    "Mi mirada se desvió hacia la esquina de la habitación."
    "Varias fotografías enmarcadas descansaban tranquilamente en un rincón."
    "Desde donde estoy, no podía distinguir los detalles, pero parecían bastante antiguos."
    "Un cuadro, más grande que todos los demás, llamó inmediatamente mi atención."
    "Contenía una fotografía de un gran grupo de personas... aunque, lamentablemente, la imagen estaba rota."
    "...Me preguntaba si era una foto de los títeres."  

    jump examinewizzyroom_day2 

label examine_corner2:
    "Mi curiosidad se apoderó de mí."
    "Entrecerré los ojos, tratando de ver mejor la fotografía."
    "La mitad superior había sido arrancada, por lo que sólo quedaba la parte inferior."
    "Desafortunadamente, todavía estaba demasiado lejos para poder verlo con claridad." 

    jump examinewizzyroom_day2

label examine_corner3:
    $ crownus_secret_point += 1
    stop music fadeout 3.0
    play sound "buzzing ear.mp3" fadein 3.0 volume 1.0
    show photo_wizzy with dissolve
    "......"
    "...Quería saber."
    "Mi cuerpo se sentía extrañamente ligero cuando lentamente comencé a moverme." 

    jump wizzy_convo2

label wizzy_convo2:
    hide photo_wizzy with dissolve
    show wiz talk with dissolve
    wiz "¡Su Majestad, he vuelto! ¡Mira, traje unas galletas!"

    stop sound fadeout 3.0
    play music "bgs_medieval normal.mp3" fadein 3.0 volume 3.0
    wiz "No son nada lujosos, pero... espero que sean mejores que no tener nada en absoluto."

    "Wizzy me entregó un frasco de vidrio lleno de galletas de chocolate."

    show wiz nervous2 with dissolve
    wiz "De hecho, también quería servirte un poco de té... pero se me acabó. Tal vez podría preguntarle a alguno de los otros títeres si tiene alguno..."
    
    "Wizzy comenzó a levantarse de su asiento nuevamente."
    
    mc "¿Qué? No, de verdad. No es necesario."
    wiz "Pero... no creo que las galletas por sí solas sean suficientes para Su Majestad."
    mc "No, de verdad. Esto es más que suficiente."
    mc "El hecho de que te hayas tomado la molestia de servirme galletas ya es más de lo que podría pedir."
    mc "Realmente no necesitas hacer nada más que eso."
    
    show wiz talk with dissolve
    "La expresión de Wizzy se iluminó de inmediato."
    
    wiz "¿E-En serio...? Me alegra mucho que te sientas así, Su Majestad..."
    wiz "Jeje... Es usted muy amable, Su Majestad."
    
    "Con eso, Wizzy se recostó en su asiento."

    wiz "Adelante, prueba uno, Su Majestad. Están buenísimos. Siempre le pido a Jestyn que traiga más cuando sale."
    wiz "Las adoro absolutamente."

    show wiz normal with dissolve
    "Como Wizzy insistió, abrí el frasco y saqué una sola galleta."
    "En el momento en que la mordí, un rico sabor a chocolate me llenó la boca. Un bocado fue todo lo que necesité para darme cuenta de que eran galletas de alta calidad."
    "Fue una experiencia completamente nueva para alguien cuya dieta incluye principalmente alimentos instantáneos."
    
    mc "¡Mmm! ¡Están deliciosos!"
    wiz "¿Ves? Te dije. ¡Me alegra mucho que te gusten!"
    wiz "Ahora bien, mientras Su Majestad disfruta de las galletas, por fin podremos tener una agradable charla."

    show wiz talk with dissolve
    wiz "Su Majestad llegó al reino ayer, ¿no es así?"
    mc "Sí."
    wiz "Mmm... Bienvenido al Kingdom of Marionettes, Su Majestad."
    wiz "Espero que llegues a sentirte como en casa aquí... y poco a poco te vayas acostumbrando a todos los títeres que viven en el reino."

    show wiz nosmile 
    wiz "{size= 15}.... Bueno....tal vez no todos....{/size}"

    show wiz normal 
    wiz "Sólo llevas aquí dos días, pero... parece que te estás adaptando bastante bien."
    mc "En realidad... sí y no. No estoy realmente seguro. Ayer, Jestyn estuvo... bastante intenso. Me dejó una impresión tan fuerte que todavía no puedo dejar de pensar en ello."

    if sit_on_jestyn:
        camera at camera_shake
        show wiz angry 
        show jescg chair
        jes "Ooh ~ Por supuesto, Su Majestad. Después de todo, este pequeño y apasionado bufón es sencillamente inolvidable."
        jes "¿Te importaría revivir la experiencia?"
        mc "No, gracias."
        
        camera at reset
        "Al menos por ahora..."
        
        hide jescg chair with dissolve
        show wiz talk with dissolve
        wiz "Jeje... Sí, así es Jestyn."
        wiz "De hecho, ayer te estaba poniendo a prueba. Para ver si eras digno de convertirte en nuestro [title]."
        wiz "Siempre se ha hecho así. Se podría decir que es... una especie de ritual."
        
        show wiz normal2 with dissolve
        wiz "Y durante el ritual, cada títere permanece en su propia habitación..."
        
        "Hace una pausa."
        
        show wiz nosmile with dissolve
        wiz "...Bueno, la mayoría lo hace."
        
        camera at camera_shake
        show wiz pout 
        show jescg chair2 
        jes "Pero no se preocupe, Su Majestad. Todos pasan felizmente tiempo en sus propias habitaciones. No los mantendré encerrados como pájaros en una jaula."
        jes "Algunos están leyendo libros... otros están DURMIENDO."
        
        camera at reset
        "Wizzy frunció el ceño en el momento en que Jestyn enfatizó esa última palabra."
        
        hide wiz pout with dissolve
        show jescg chair with dissolve
        jes "Algunos están afilando sus espadas, rezando, cocinando, nadando, resolviendo acertijos, haciendo ejercicio, bailando, gritando, golpeándose la cabeza contra la pared... la la la la~♪"

    else:
        camera at camera_shake
        show wiz angry at left
        show jes happy2
        jes "Ooh ~ Por supuesto, Su Majestad. Después de todo, este pequeño y apasionado bufón es sencillamente inolvidable."
        jes "¿Te importaría revivir la experiencia?"
        mc "No, gracias."
        
        camera at reset
        "Al menos por ahora..."
        
        hide jes happy2 with dissolve
        show wiz talk at center
        with dissolve
        wiz "Jeje... Sí, así es Jestyn."
        wiz "De hecho, ayer te estaba poniendo a prueba. Para ver si eras digno de convertirte en nuestro [title]."
        wiz "Siempre se ha hecho así. Se podría decir que es... una especie de ritual."
        
        show wiz normal2 with dissolve
        wiz "Y durante el ritual, cada títere permanece en su propia habitación..."
        
        "Hace una pausa."
        
        show wiz nosmile with dissolve
        wiz "...Bueno, la mayoría lo hace."
        
        camera at camera_shake
        show wiz pout at left
        show jes happy2 
        jes "Pero no se preocupe, Su Majestad. Todos pasan felizmente tiempo en sus propias habitaciones. No los mantendré encerrados como pájaros en una jaula."
        jes "Algunos están leyendo libros... otros están DURMIENDO."
        
        camera at reset
        "Wizzy frunció el ceño en el momento en que Jestyn enfatizó esa última palabra."
        
        hide wiz pout with dissolve
        show jes normal2_2 with dissolve
        jes "Algunos están afilando sus espadas, rezando, cocinando, nadando, resolviendo acertijos, haciendo ejercicio, bailando, gritando, golpeándose la cabeza contra la pared... la la la la~♪"
    
    "Jestyn continuó divagando sin siquiera respirar."
    "Honestamente... ¿cómo se suponía que iba a conocer mejor a Wizzy si Jestyn seguía hablando así?"
    "Tal vez debería esperar a que termine..."
    "...O tal vez debería meterle algo en la boca."
    "Al menos, ese fue el pensamiento que cruzó por mi mente."

    menu:
        "Mete un paño en la boca de Jestyn.":
            $ jestyn_gagged = True

            if sit_on_jestyn:
                "No. Si quería conocer a Wizzy, Jestyn necesitaba estar callado."
                "Como mínimo, tenía que encontrar una manera de hacer que dejara de hablar."
                "Miré a mi alrededor, buscando algo que pudiera mantener callado a Jestyn. Luego metí la mano en el bolsillo y encontré un pañuelo."
                "Quizás esto funcione."
                "Sin pensarlo dos veces, metí suavemente el pañuelo en la boca de Jestyn."
                
                camera at camera_shake
                show jescg chair3
                jes "¡¿Hmph?!"
                mc "Jestyn, estoy intentando hablar con Wizzy. Así que, por favor, quédate callado."

                show jescg chair4 with dissolve
                jes "Mmm..."
                camera at reset
                "Jestyn asintió. Él entendió."
                "Mientras tanto, Wizzy hacía todo lo posible por contener la risa."

                hide jescg chair4 with dissolve
                show wiz nosmile2 with dissolve
                wiz "P-perdóname, Majestad... ¡ejem!"



            else:
                "No. Si quería conocer a Wizzy, Jestyn necesitaba estar callado."
                "Como mínimo, tenía que encontrar una manera de hacer que dejara de hablar."
                "Miré a mi alrededor, buscando algo que pudiera mantener callado a Jestyn. Luego metí la mano en el bolsillo y encontré un pañuelo."
                "Quizás esto funcione."
                "Sin pensarlo dos veces, metí suavemente el pañuelo en la boca de Jestyn."
                
                camera at camera_shake
                show jescg gagcrief
                jes "¡¿Hmph?!"
                mc "Jestyn, estoy intentando hablar con Wizzy. Así que, por favor, quédate callado."

                show jescg gagcrief2 with dissolve
                jes "Mmm..."
                
                "Jestyn asintió. Él entendió."
                "Mientras tanto, Wizzy hacía todo lo posible por contener la risa."

                hide jes normal2_2 with dissolve
                hide jescg gagcrief2 with dissolve
                show wiz nosmile2 with dissolve
                wiz "P-perdóname, Majestad... ¡ejem!"
            

        "déjalo en paz":
            $ jestyn_gagged = False

            if sit_on_jestyn:
                "... Pensándolo bien..."
                "No parecía correcto obligarlo a permanecer callado. Sentí como si lo estuviera silenciando."
                "Debería dejarlo hablar hasta que esté satisfecho."
                
                jes "Su Majestad debe preguntarse por qué mantuve a todos en sus habitaciones mientras yo... lo entretenía."
                jes "Bueno, seguramente Su Majestad estaría nerviosa con tantos títeres. Nada menos que títeres vivientes, que observan cada uno de tus movimientos."

                show jescg chair5 with dissolve
                jes "Conozco muy bien ese sentimiento. Cientos de ojos fijos en una sola persona. Cada mirada en la habitación sobre ti. Te conviertes en el centro de atención de todos, envuelto en un manto de abrumador y ansiedad tan grueso como la colcha de un hada madrina."
                jes "Y como este bufón es tan maravillosamente considerado... ¡se me ocurrió la solución perfecta! Me aseguré de que cada títere permaneciera en su habitación, dejando el escenario completamente vacío."

                show jescg chair6 with dissolve
                jes "Entonces seríamos solo nosotros dos... bailando bajo las brillantes luces del escenario... mientras los otros títeres simplemente se movían como las mareas del mar."
                mc "Ya veo..."
                mc "¿Ya terminaste?"

                show jescg chair2 with dissolve
                jes "Aaa y porque era mi oportunidad de tener a Su Majestad para mí solo, como un par de graciosos cisnes~"
                jes "Sí. Ya terminé."
                
                hide jescg chair2 with dissolve
                show wiz nervous2 with dissolve
                wiz "... Así es Jestyn, Su Majestad."
                wiz "A él realmente le encanta hablar... así que espero que lo perdones."

            else:
                "... Pensándolo bien..."
                "No parecía correcto obligarlo a permanecer callado. Sentí como si lo estuviera silenciando."
                "Debería dejarlo hablar hasta que esté satisfecho."
                
                show jes normal2 with dissolve
                jes "Su Majestad debe preguntarse por qué mantuve a todos en sus habitaciones mientras yo... lo entretenía."
                jes "Bueno, seguramente Su Majestad estaría nerviosa con tantos títeres. Nada menos que títeres vivientes, que observan cada uno de tus movimientos."

                show jes bow with dissolve
                jes "Conozco muy bien ese sentimiento. Cientos de ojos fijos en una sola persona. Cada mirada en la habitación sobre ti. Te conviertes en el centro de atención de todos, envuelto en un manto de abrumador y ansiedad tan grueso como la colcha de un hada madrina."
                jes "Y como este bufón es tan maravillosamente considerado... ¡se me ocurrió la solución perfecta! Me aseguré de que cada títere permaneciera en su habitación, dejando el escenario completamente vacío."

                show jes flush2 with dissolve
                jes "Entonces seríamos solo nosotros dos... bailando bajo las brillantes luces del escenario... mientras los otros títeres simplemente se movían como las mareas del mar."
                mc "Ya veo..."
                mc "¿Ya terminaste?"

                show jes happy2 with dissolve
                jes "Aaa y porque era mi oportunidad de tener a Su Majestad para mí solo, como un par de graciosos cisnes~"
                jes "Sí. Ya terminé."

                hide jes happy2 with dissolve
                show wiz nervous2 with dissolve
                wiz "... Así es Jestyn, Su Majestad."
                wiz "A él realmente le encanta hablar... así que espero que lo perdones."

    show wiz normal with dissolve
    wiz "En cuanto a mí... Sí, Jestyn no se equivoca. Dormí durante todo ayer."
    $ voice_duck_start()
    voice "WIZZY02_DAY2.ogg"
    wiz "Sin embargo, ese no suele ser el caso. Había estado despierto toda la noche realizando experimentos, así que estaba completamente agotado."
    $ voice_duck_end()
    mc "... ¿Alguien más ha venido alguna vez aquí... y ha pasado por ese ritual para convertirse en el próximo gobernante?"
    
    show wiz nosmile with dissolve
    "Wizzy se quedó en silencio por un momento. Sus dedos se entrelazaron mientras se movía nerviosamente."
    
    wiz "...Sí."
    wiz "Ha habido... algunos."
    mc "......"
    mc "Entonces... ya que estoy aquí..."
    mc "... ¿Tengo razón al suponer que el ritual no los eligió?"
    wiz "...Se podría decir eso, Su Majestad."

    "Mi mente comenzó a correr con innumerables posibilidades y una ola de ansiedad me invadió."
    "Sólo una pregunta permaneció en mi mente."
    "Si el ritual falló... ¿entonces qué pasó con la persona que trabajó aquí antes que yo?"
    "... ¿Era siquiera una pregunta segura?"
    
    mc "Si... el ritual falló... entonces, ¿qué...?"
    wiz "...Significa que esa persona tuvo que abandonar el reino. Al menos... eso es lo que dicen las reglas..."

    show wiz nervous with dissolve
    wiz "Las reglas de Jestyn... Más precisamente."
    
    "......"
    
    wiz "Por favor, no te preocupes tanto, Su Majestad. No hay por qué ponerse así."

    show wiz talk2 with dissolve
    wiz "¿Qué tal si me preguntas algo en su lugar? El objetivo de esta conversación es que conozcas mejor a tus sirvientes, ¿no es así?"
    wiz "Puedes preguntarme lo que quieras, Su Majestad."

    "Wizzy se quitó la capa y la dejó cuidadosamente sobre la cama antes de regresar a su asiento para continuar nuestra conversación."

    hide wiz talk2 with dissolve
    jump gettoknow_wizzy

label gettoknow_wizzy:
    show wizconvo normal with dissolve
    menu:
        "¿Qué haces en tu tiempo libre?":
            jump freetime_wizzy

        "Me encanta tu sombrero.":
            jump hat_wizzy

        "Quiero saber sobre tu relación con todos.":
            jump relationship_wizzy

        "¿Qué opinas del rey títere?" if examinecornerwizzy >= 3:
            $ examinecornerwizzy
            jump crownusask_wizzy

        "eso es todo":
            jump afterconvo_wizzy

label freetime_wizzy:
    mc "Tengo curiosidad... ¿Qué sueles hacer en tu tiempo libre?"
    
    show wizconvo happy with dissolve
    "La expresión de Wizzy se iluminó de inmediato."
    
    wiz "¡Ah! En realidad, bastantes."
    wiz "Tengo mucho tiempo libre todos los días porque... bueno... no hay mucho trabajo que realmente requiera mi atención."

    show wizconvo normal2 with dissolve
    wiz "Por eso suelo dedicar mi tiempo a escribir, leer... y mi favorito de todos, a realizar experimentos."
    wiz "Probablemente paso la mayor parte del tiempo experimentando."
    
    "Sí. Esta marioneta es definitivamente la más inteligente."
    
    mc "¿Sobre qué escribes?"

    show wizconvo nosmile3 with dissolve
    wiz "Todo tipo de cosas... Hmm, veamos..."
    
    hide wizconvo nosmile3 with dissolve
    "Wizzy se levanta y se acerca a su escritorio."
    "Abrió uno de los cajones y sacó una libreta marrón, gruesa y gastada."
    
    show wizconvo happy with dissolve
    wiz "¡Aquí está! Bastante grueso, ¿no? Bueno... escribo en él casi todos los días."
    wiz "También está lleno de notas de todos mis experimentos, así que... se podría decir que es principalmente un diario de experimentos."

    show wizconvo normal with dissolve
    "Wizzy abrió su diario y comenzó a hojear las páginas."
    
    wiz "Además de mis experimentos, también escribo todo lo que encuentro interesante."

    show wizconvo normal3 with dissolve
    wiz "Por ejemplo... una vez dediqué unas páginas a las rosas, ya que son mis flores favoritas."
    wiz "Las rosas vienen en todo tipo de colores. Rosa, blanco, negro..."
    wiz "Siempre me ha fascinado eso, así que decidí escribir sobre ellas aquí."

    show wizconvo suprais3 with dissolve
    $ voice_duck_start()
    voice "WIZZY03_DAY2.ogg"
    $ voice_duck_end()
    wiz "Después de leer varios libros sobre botánica, aprendí que el color de una rosa puede verse influenciado por el entorno en el que crece. ¿No es fascinante?"
    wiz "Por ejemplo, la acidez del suelo, la cantidad de luz solar, la temperatura… incluso la propia edad de la rosa pueden afectar a su color."
    
    show wizconvo happy2 with dissolve
    wiz "¡Ah! ¡Y también escribí el significado detrás de cada color de rosa!"
    wiz "Las rosas blancas simbolizan la pureza, la inocencia, el amor sincero... y los nuevos comienzos."
    wiz "Las rosas negras, por otro lado, suelen asociarse con el misterio, las despedidas y el dolor. Aunque... algunas personas también las ven como símbolos de fuerza interior, coraje y nuevos comienzos."
    
    show wizconvo suprais2 with dissolve
    wiz "¡Oh! Aquí hay un dato curioso sobre las rosas negras. Si no recuerdo mal... las rosas negras puras en realidad no existen en la naturaleza. Por lo general, son tonos muy oscuros de rojo o morado."
    
    show wizconvo normal with dissolve
    wiz "¿No es asombroso? Aunque sean la misma flor, algo tan simple como el color puede cambiar por completo lo que representan."
    mc "Entonces ¿cuál rosa es tu favorita?"

    show wizconvo normal3 with dissolve
    wiz "Rosas rojas."
    wiz "Creo que son encantadoras... especialmente porque simbolizan el amor verdadero y el romance profundo. Creo que es bastante lindo."
    wiz "¿Y tú, Su Majestad? Si pudieras elegir, ¿qué color de rosa sería tu favorito?"

    menu:
        "Rosa roja":
            wiz "¡¿Ah?! ¡Eso significa que tenemos el mismo gusto! ¡Jajaja!"

        "Rosa blanca":
            wiz "Pureza, inocencia, amor sincero y nuevos comienzos. Buena elección, Su Majestad."

        "Rosa negra":
            wiz "Misterio, despedidas y duelo. ¡Vaya, es usted tan misterioso, Su Majestad!"

        "Rosa rosa":
            wiz "Gentileza, gracia, gratitud y admiración. Buena elección, Su Majestad."

        "Rosa amarilla":
            wiz "Amistad cercana, alegría, felicidad y energía positiva. Vaya, buena elección, Su Majestad."

        "Rosa naranja":
            wiz "Entusiasmo, energía y admiración. Buena elección, Su Majestad."

        "Rosa morada":
            wiz "Encanto, amor a primera vista y elegancia. ¡Guau, esa es una buena elección, Su Majestad!"

    show wizconvo smirk3 with dissolve
    "Wiizy continuó contándome todo tipo de cosas que había escrito en su diario."
    "Plantas. Alimento. Compuestos de carbono. Química... y muchos otros temas."
    "Con solo escucharlo, era obvio que Wizzy tenía una mente increíblemente curiosa."
    "Finalmente mi mirada volvió al estante lleno de botellas llenas de líquidos coloridos e ingredientes extraños que no puedo reconocer."
    
    mc "Wizzy, dijiste que te gusta experimentar. ¿Todas las cosas en ese estante son creaciones tuyas?"
    
    show wizconvo suprais with dissolve
    "Señalé hacia el estante."
    
    wiz "¡Ah! ¡Sí! ¡Cada uno de ellos es el resultado de mis experimentos!"

    show wizconvo normal with dissolve
    wiz "Ven, querida Majestad. Déjame mostrarte."
    
    hide wizconvo normal with dissolve
    "Wizzy me hizo un gesto para que caminara adelante antes de seguirme."
    "Al acercarme, comencé a notar cuántas botellas diferentes había en los estantes."
    "Algunos contenían un líquido azul brillante. Otros eran rosas, negros, amarillos... y un sinfín de colores más."
    "En los estantes inferiores había frascos llenos de ingredientes extraños: ramitas, polvos que no pude identificar y todo tipo de materiales extraños."
    
    mc "Hmm... ¿Qué son todos estos líquidos?"

    show wiz talk2_2 with dissolve
    wiz "Ah... no son peligrosos. Bueno... algunos de ellos son venenosos, pero este..."
    
    "Wizzy tomó una botella llena de un líquido negro."

    show cg_wizpotion with dissolve
    
    wiz "Ésta es la medicina."
    wiz "Puedes beberlo siempre que tengas fiebre o resfriado. Sabe a jengibre y menta."
    wiz "Al principio pica un poco, por lo que puede resultar un poco desagradable. Pero una vez que te acostumbras, es bastante agradable. La menta ayuda a despejar las vías respiratorias cuando tienes la nariz congestionada."
    wiz "Si tienes curiosidad, Su Majestad, puedes olerlo. Es perfectamente seguro."
    
    "Acerqué la poción negra a mi cara y la olí cautelosamente."
    "En el momento en que lo hice, un fuerte olor a menta me picó en la nariz."
    
    mc "Uf... ese es un olor a menta muy fuerte..."
    wiz "Jaja, lo es."
    

    hide cg_wizpotion with dissolve
    "Wizzy volvió a colocar la botella negra en el estante antes de tomar otra llena de un líquido amarillo."
    
    show wiz normal2_2 with dissolve
    wiz "Ésta es una poción para dormir. Si alguna vez tienes problemas para conciliar el sueño, puedes beber esto."
    wiz "Sabe a naranja... aunque puede hacerte toser un poco ya que es bastante duro para la garganta."
    
    "Wizzy de repente se quedó en silencio."
    
    show wiz nosmile1_2 with dissolve
    wiz "...Esta poción es poderosa. Quizás... un poco demasiado poderosa..."
    
    "Ladeé la cabeza, desconcertada."
    
    mc "¿Qué quieres decir?"
    wiz "Una vez... Jestyn lo bebió sin mi permiso."

    show wiz nervous2_2 with dissolve
    wiz "Bueno... ciertamente funcionó. Lo puso a dormir..."
    wiz "...Durante un mes entero."
    
    "Mis ojos se abrieron como platos."
    "...¿Un mes entero? Eso es menos \"dormir\" y más \"hibernar\"."
    "Sí. Definitivamente no es seguro para los humanos."
    
    mc "¿Qué pasa con esos frascos con las ramitas, los polvos y todo lo demás?"

    show wiz normal1_2 with dissolve
    wiz "Oh, esos son sólo ingredientes para mis experimentos. A veces los agrego por capricho para ver qué pasa."
    wiz "Jestyn siempre los reúne para mí cada vez que sale del reino. Soy... un poco demasiado vago para irme solo."
    mc "Hmm... ¿Dónde aprendiste tanto sobre medicinas y pociones?"

    show wiz talk2_2 with dissolve
    wiz "Aprendí de libros de medicina escritos por humanos. De hecho, tengo una gran colección. Si alguna vez desea pedir prestado uno, Su Majestad, estaré encantado de prestárselo."
    mc "Eso es realmente impresionante."
    mc "¿Hay algo que te haya resultado especialmente difícil de aprender? ¿O tal vez el experimento que te causó más problemas?"
    
    show wiz nosmile1_2 with dissolve

    stop music fadeout 2.0 
    "La sonrisa en el rostro de Wizzy se desvaneció casi al instante."
    "Un silencio incómodo se apoderó de la habitación."
    "... ¿Dije algo mal?"
    
    wiz "...Sí."
    play music "bgs_mystery.mp3" fadein 3.0 
    wiz "Humanos."
    
    "......"
    "¿Humanos...? ¿Qué quiso decir con eso?"
    
    wiz "Una vez intenté aprender todo lo que pude sobre el cuerpo humano."
    wiz "Huesos. Carne. Órganos. Piel."
    wiz "Estudié cada parte que tienen los humanos... y nosotros no."
    mc "E-Entonces... ¿qué lo hizo tan difícil?"
    wiz "Estudié cada parte del cuerpo humano... porque quería intentar crear uno."
    mc "¡¿Qué?! ¿Por qué?"
    wiz "...Es una historia larga y complicada."
    wiz "Pero pensé... si podía tener éxito... podría convertirse en un nuevo camino a seguir para todos nosotros."
    wiz "Y tal vez... el reino no hubiera terminado así..."
    
    "Mi mente luchaba por darle sentido a lo que Wizzy intentaba decirme."
    "Quería preguntar más... pero de alguna manera, la atmósfera me dio demasiado miedo para seguir insistiendo."
    stop music fadeout 2.0
    "Al notar la expresión de mi rostro, Wizzy finalmente pareció salir de sus pensamientos."
    
    show wiz panic1_2 with dissolve
    wiz "¡Ah! M-Mis disculpas, Su Majestad. Es... no es nada, de verdad."
    play music "bgs_medieval normal.mp3" volume 3.0 fadein 3.0
    wiz "Mejor hablemos de otra cosa... jeje."
    hide wiz panic1_2 with dissolve

    jump gettoknow_wizzy

label hat_wizzy:
    "Mis ojos se dirigieron hacia el sombrero de Wizzy."
    "Es un sombrero de mago realmente genial. Sinceramente... tenía ganas de probármelo."
    
    mc "Wizzy... ¿puedo ser honesto contigo?"

    show wizconvo talk with dissolve
    wiz "¿Eh? Por supuesto..."

    show wizconvo nervous with dissolve
    wiz "¿Q-Qué pasa? ¿Fui aburrido? ¿Hablé demasiado? ¿No fui lo suficientemente interesante?"
    mc "¡¿Qué?! ¡No, en absoluto!"
    mc "Simplemente creo que tu sombrero se ve realmente genial."
    
    show wizconvo suprais with dissolve
    "La expresión de Wizzy se convirtió en sorpresa. Un leve sonrojo se extendió lentamente por sus mejillas."
    
    wiz "O-Oh... ¿De verdad lo crees?"
    
    show cg_wizhat with dissolve
    "Agarró suavemente su sombrero y distraídamente le pasó una mano por encima."
    
    wiz "Gracias, Su Majestad... Me alegra mucho que te guste."
    wiz "Se podría decir que este sombrero es muy valioso para mí. Nuestro creador... el que nos creó a todos... lo hizo él mismo."
    mc "¿Tu creador?"
    
    "...Eso es nuevo."
    
    wiz "Sí. El que nos creó... y todo el Kingdom of Marionettes."
    wiz "Me dijo que este sombrero se convertiría en mi fuerte identidad y en algo por lo que la gente siempre me reconocería. Y... bueno... creo que tenía razón."
    wiz "Es uno de los pocos recuerdos que todavía tengo de mi creador. Lo he atesorado desde entonces."
    
    "Wizzy mira su sombrero y recuerda en silencio los recuerdos que lleva consigo."
    
    mc "...¿Estaría bien si me lo probara?"

    hide cg_wizhat with dissolve
    show wizconvo suprais with dissolve
    wiz "¿Eh? ¿Quieres ponerte mi sombrero, majestad?"
    mc "Sí. Pero si no te sientes cómodo con eso, está completamente bien."

    show wizconvo nosmile3 with dissolve
    wiz "......"

    show wizconvo normal3 with dissolve
    wiz "Jeje... Por supuesto. Confío en ti, Su Majestad."

    camera at reset
    show wizconvo nosmile with dissolve
    wiz "A diferencia de... alguien que viste de rojo, amarillo, negro y blanco."
    
    "Wizzy se quitó el sombrero con cuidado, y yo mi corona, antes de colocármelo con suavidad en la cabeza."

    camera at camera_shake
    show wizconvo hat 
    "Desafortunadamente, era demasiado grande. El ala inmediatamente se deslizó hacia abajo y bloqueó toda mi vista."
    camera at reset
    mc "¡W-Wow-! ¡Es enorme! ¡No puedo ver nada!"
    wiz "¡Jaja! Lo sé. Es demasiado grande para ti."
    
    show wizconvo hat2 with dissolve
    "Riéndose suavemente, Wizzy levantó el ala lo suficiente para que yo pudiera ver de nuevo."
    
    show wizconvo hat3 with dissolve
    wiz "Ahí. Mucho mejor."
    
    "Se tomó un momento para mirarme."
    
    show wizconvo anim
    wiz "...Mmmm. En realidad te queda bastante lindo, Su Majestad."

    if sit_on_jestyn:
        if jestyn_gagged:
            camera at camera_shake
            show jescg chair8 
            jes "¡¡HMPHH!!"
            jes "¡Mmrrghhh!"
            
            camera at reset
            hide jescg chair8 with dissolve
            show wizconvo hat6 with dissolve
            wiz "¿Te gusta el sombrero?"
            mc "Sí. Es un sombrero realmente bonito."
            wiz "Jeje... También me gustó ver a Su Majestad usarlo. Quizás podría pedirle a alguien que haga otro igual."

            show wizconvo hat3 with dissolve
            wiz "Entonces nos pareceríamos aún más, ¿no?"
            mc "Estoy de acuerdo. Ja ja."
            jes "Mmmrrgh!!"

        else:
            camera at camera_shake
            show jescg chair7 with dissolve
            jes "Ejem!!"
            
            "Jestyn se aclara la garganta, haciéndonos saltar a ambos."
            
            wiz "¿Eh? ¿Qué ocurre?"
            jes "Nada en absoluto~ Sólo asegurándome de que ustedes dos no hagan nada... demasiado extraño."
            wiz "¡No estaba haciendo nada!"
            camera at reset
            hide jescg chair7 with dissolve

    else:
        if jestyn_gagged:
            camera at camera_shake
            show jescg gagcrief3 
            jes "¡¡HMPHH!!"
            jes "¡Mmrrghhh!"
            
            camera at reset
            hide jescg gagcrief3 with dissolve
            show wizconvo hat6 with dissolve
            wiz "¿Te gusta el sombrero?"
            mc "Sí. Es un sombrero realmente bonito."
            wiz "Jeje... También me gustó ver a Su Majestad usarlo. Quizás podría pedirle a alguien que haga otro igual."

            show wizconvo hat3 with dissolve
            wiz "Entonces nos pareceríamos aún más, ¿no?"
            mc "Estoy de acuerdo. Ja ja."
            jes "Mmmrrgh!!"

        else:
            hide wizconvo anim
            camera at camera_shake
            show jes creep2
            jes "Ejem!!"
            
            "Jestyn se aclara la garganta, haciéndonos saltar a ambos."
            
            show wiz panic1_2 at left
            with dissolve
            wiz "¿Eh? ¿Qué ocurre?"
            jes "Nada en absoluto~ Sólo asegurándome de que ustedes dos no hagan nada... demasiado extraño."
            wiz "¡No estaba haciendo nada!"
            camera at reset
            hide jes chair8 with dissolve
    
    hide wizconvo with dissolve
    show wiz smirk1_2 at center
    with dissolve
    "Wizzy recuperó su sombrero y luego me habló en un susurro."

    wiz "Quizás la próxima vez... podrías llevar mi sombrero más tiempo, Su Majestad..."

    "Sonreí y luego asentí con la cabeza."

    hide wiz smirk1_2 with dissolve
    jump gettoknow_wizzy

label relationship_wizzy:
    $ visited_wizzy = True
    $ prieston_route_point += 1
    
    mc "Tengo curiosidad. ¿Cómo es tu relación con los otros títeres?"

    show wizconvo nosmile3 with dissolve
    wiz "¿Oh? ¿Mi relación con todos los demás? Mmm..."
    wiz "A ver... Supongo que empezaré por el más cercano a nosotros..."

    show wizconvo pout with dissolve
    wiz "...Jestyn."
    
    "En el momento en que Wizzy dice su nombre, infló sus mejillas con molestia."
    
    wiz "Es un fastidio."
    
    "Miré a Jestyn. En lugar de parecer ofendido, lucía una sonrisa increíblemente engreída."
    "...Por supuesto que lo es."
    
    show wizconvo nosmile2 with dissolve
    wiz "¡Siempre me está gastando bromas! Me roba las botellas de pociones... ¡y hasta esconde mi sombrero!"
    wiz "Él también juega trucos con los otros títeres, ¡pero yo soy uno de sus objetivos favoritos! Uf..."
    wiz "......"

    show wizconvo nervous with dissolve
    wiz "...Pero aun así... en realidad es... una buena persona."

    if jestyn_gagged:
        jes "Hhhhmmmmmm~...."

    else:
        jes "¿Oh~? Soy una buena persona, ¿verdad~? Continúe entonces. Cuéntale a [poss] Majestad todo sobre esto."
    
    "Al verse obligado a felicitar a Jestyn justo en frente de él, Wizzy de repente pareció profundamente preocupado."
    
    wiz "H-Él... bueno..."
    wiz "...Suspiro... Por más molesto que sea... es como un hermano pequeño para mí."

    show wizconvo nosmile2 with dissolve
    wiz "Él me ayuda... y a los otros títeres... más a menudo de lo que jamás admitiría. Entonces..."
    wiz "Yo... entiendo por lo que ha pasado. Al menos... un poco."
    wiz "Supongo que eso es suficiente para perdonar... algunos de sus hábitos más exasperantes."
    wiz "....."

    show wizconvo pout with dissolve
    wiz "Pero sigue siendo molesto. ¡Fin de la discusión!"

    "Jestyn simplemente se ríe de la frustración de Wizzy. Con un suspiro, Wizzy decide ignorarlo y pasa al siguiente títere."
    
    show wizconvo nosmile3 with dissolve
    wiz "Ahora, ¿quién más...? Ah, Knighter. Es el caballero títere del reino."
    wiz "Él es... hmm... no es muy hablador, y puede parecer un poco de mal genio."
    wiz "Aunque, para ser justos, en realidad no es una persona enojada. Es solo que... Jestyn sigue molestándolo, así que... bueno... así es como suele terminar."

    show wizconvo normal2 with dissolve
    wiz "Pero es un buen títere. Se siente un poco incómodo con gente nueva, pero realmente trata de llevarse bien con ellos. En realidad es algo adorable."
    wiz "También viene a mí cada vez que necesita alguien con quien hablar. Siempre hago lo mejor que puedo para darle consejos. Él... no es del tipo que es bueno expresando sus sentimientos."

    show wizconvo happy2 with dissolve
    wiz "¡Ah! ¡Y le encantan las novelas! A menudo viene a mí para hablarme sobre lo que sea que haya estado leyendo."
    
    show wizconvo nosmile with dissolve
    "Wizzy de repente se quedó en silencio, mirándome durante un largo momento."
    
    mc "...Wizzy?"
    wiz "...Acabo de recordar algo."
    wiz "Ahora que es nuestro [title], Su Majestad... creo que debería tener cuidado con Knighter."
    mc "¿Eh? ¿Por qué?"
    wiz "Es realmente una persona amable, pero... Cro-"
    
    show wizconvo nervous
    "Se contuvo."
    
    wiz "Quiero decir... no ha aceptado del todo que alguien ocupe el lugar de nuestro antiguo rey. Todavía le es profundamente leal... Es... una situación complicada."

    show wizconvo talk 
    wiz "Existe la posibilidad de que intente hacerle daño, Su Majestad. Entonces... te aconsejo que tengas cuidado con él."
    
    "Wizzy miró hacia Jestyn por un momento."
    
    show wizconvo talk3 with dissolve
    wiz "...Aunque, con Jestyn siempre a tu lado, no creo que tenga mucho de qué preocuparme."
    
    "Miré a Jestyn. Como siempre, llevaba la misma sonrisa despreocupada."
    
    wiz "Knighter puede molestarse con Jestyn, sí... pero tiende a escucharlo. No sé por qué funciona."

    show wizconvo talk2 with dissolve
    wiz "Mientras Jestyn esté contigo, Su Majestad... estarás a salvo."

    show wizconvo talk3 with dissolve
    wiz "Ahora bien... hmm... ¿quién más...?"
    show wizconvo normal3 
    wiz "Ah, Prieston. Es el sacerdote títere del reino."
    wiz "Él es..."
    show wizconvo nosmile3 
    wiz "......"
    
    "Wizzy se quedó en silencio, luchando por encontrar las palabras adecuadas."
    
    mc "¿Qué ocurre?"

    show wizconvo talk3 with dissolve
    wiz "...Para ser honesto, no estoy muy seguro de cómo hablarte de Prieston, Su Majestad."
    wiz "Los dos hablamos bastante a menudo y yo diría que somos bastante cercanos."

    show wizconvo talk2 with dissolve
    wiz "Es sólo que... nunca sé realmente qué está pasando dentro de su cabeza. Es... bastante difícil de predecir."

    show wizconvo happy3 with dissolve
    wiz "Aun así, es tranquilo, reflexivo y sorprendentemente maduro... aunque es más joven que yo. Realmente lo admiro."

    show wizconvo talk3 with dissolve
    wiz "También siento que siempre hay algo escondido en él. Es bastante misterioso. Honestamente, si alguien logra ver a Prieston aunque sea una vez a la semana, lo consideraría afortunado."
    mc "¿Es tímido o algo así?"

    show wizconvo suprais2 with dissolve
    wiz "Oh, no. Todo lo contrario."
    wiz "Simplemente no le gustan las conversaciones ociosas. Por lo general, sólo sale de su habitación cuando hay un motivo para hacerlo."

    show wizconvo normal2 with dissolve
    wiz "...Aunque tal vez lo conozcas pronto, Su Majestad."

    jump gettoknow_wizzy

label crownusask_wizzy:
    $ crownus_wizzy = True
    $ crownus_secret_point += 1
    mc "Tengo curiosidad... ¿Cómo era el Rey Marioneta? ¿Qué opinas de él?"
    
    stop music fadeout 3.0
    show wizconvo nosmile with dissolve
    "En el instante en que Wizzy escuchó la pregunta, se quedó paralizado. Su expresión se volvió ilegible."
    "Entonces… lentamente apartó su rostro de mí."
    
    wiz "......"

    show wizconvo nervous with dissolve
    wiz "...¿Por qué quiere saber de él, Su Majestad?"
    
    "Sólo por su voz, me di cuenta de que el tema lo hacía sentir profundamente incómodo."
    "...Oh, no. No debería haber preguntado."
    
    mc "U-Um... Lo siento, Wizzy. Sólo tenía curiosidad."
    mc "Si no quieres hablar de eso, está bien."
    wiz "......"

    show wizconvo nosmile with dissolve
    wiz "No..."
    wiz "Creo que mereces saberlo."
    wiz "El Rey Marioneta... no era un buen rey."

    show wizconvo mad with dissolve
    voice "WIZZY04_DAY2.ogg"
    wiz "Era un mentiroso."
    voice "WIZZY05_DAY2.ogg"
    wiz "Un gran mentiroso."
    voice "WIZZY06_DAY2.ogg"
    wiz "Con nada más que dulces palabras, hechizó a los títeres... los cegó... les hizo creer cada mentira que decía."

    show wizconvo mad4 with dissolve
    wiz "QUIERO DECIR... ¡¿CÓMO PUDO HACER TODAS ESAS PROMESAS....Y DEJARNOS ASÍ?!"
    
    "Lentamente, un líquido espeso y negro comenzó a filtrarse por las grietas debajo de la venda de los ojos de Wizzy y por las comisuras de su boca."
    
    camera at camera_shake
    wiz "¡NO LE IMPORTÓ!"
    camera at reset
    wiz "¡NUNCA LE IMPORTAMOS NINGUNO DE NOSOTROS!"
    wiz "ERA TODO..."

    camera at camera_shake
    show wizconvo breakdown
    wiz "¡TODO FUE POR SÍ MISMO!"
    camera at reset
    mc "Wizzy, ¡cálmate!"
    
    "Rápidamente agarré el brazo de Wizzy, con la esperanza de sacarlo de allí."

    show wizconvo breakdown2 with dissolve
    "Afortunadamente, volvió en sí. Al darse cuenta de lo que acababa de suceder, rápidamente se limpió el líquido negro que se filtraba debajo de la venda de sus ojos y de las comisuras de su boca."
    
    wiz "Lo siento mucho, Su Majestad... Dejé que mis emociones se apoderaran de mí."
    mc "¿Qué te pasó? Ese líquido negro... salía de tus ojos y de tu boca."
    wiz "Está bien... Sólo sucede cuando mis emociones se salen de control."

    show wizconvo breakdown3 with dissolve
    wiz "Estaré bien... siempre y cuando no suceda muy a menudo."
    hide wizconvo breakdown3 with dissolve

    play music "bgs_medieval normal.mp3" fadein 2.0 volume 3.0
    "Wizzy se disculpó por un momento para limpiarse la cara con un paño."
    "Si sus emociones podían afectarlo tan profundamente... entonces, sea lo que sea que le haya sucedido, debe haberlo dejado con un profundo trauma."
    "Al regresar, dudó por un momento."
    
    show wizconvo nervous with dissolve
    wiz "...No me tienes miedo, ¿verdad, majestad?"

    menu:
        "Tengo miedo":
            wiz "¿Y-tú lo eres? Lo siento mucho, Su Majestad. Me aseguraré de que eso no vuelva a suceder."

        "No, no tengo miedo":
            show wizconvo talk with dissolve
            wiz "...Gracias a Dios."
            wiz "Lo siento mucho, Su Majestad..."
    
    show wizconvo nosmile with dissolve
    wiz "Pero... como dije antes... el Rey Marioneta no era un buen rey. A él sólo le importaba él mismo."
    wiz "...Me temo que eso es todo lo que puedo decir. No me siento cómodo hablando de él."
    mc "Está bien. Entiendo."

    jump gettoknow_wizzy

label afterconvo_wizzy:
    show wizconvo suprais with dissolve
    wiz "¿Ah? ¿Eso es todo?"

    show wizconvo happy with dissolve
    wiz "En ese caso... Espero que haya disfrutado nuestra conversación, Su Majestad."
    wiz "Porque... ciertamente lo hice."
    mc "Yo también, Wizzy. Disfruté mucho hablando contigo. Es muy fácil hablar contigo."

    show wizconvo blush with dissolve
    wiz "Ejeje... Me estás haciendo sonrojar."
    wiz "Ojalá pudiéramos hablar un poco más... pero imagino que Su Majestad tiene una agenda bastante ocupada."
    wiz "Quizás podamos volver a charlar en otro momento."
    
    hide wizconvo blush with dissolve
    "Asentí con la cabeza antes de ponerme de pie."
    
    mc "Me alegro de haberte conocido, Wizzy. Definitivamente hablaremos de nuevo."

    show wiz talk2_2 with dissolve
    wiz "¡Sí! ¡Sí! Siempre podrá llamar a mi puerta, Su Majestad. Estaré encantado de hablar contigo en cualquier momento."
    wiz "La próxima vez, me aseguraré de prepararnos té y un poco de pastel mientras charlamos."

    show wiz normal2_2 with dissolve
    wiz "Hasta entonces... ¡cuídate!"

    show wiz pout2_2 with dissolve
    wiz "¡Y Jestyn! ¡No le des demasiados problemas a [poss] Majestad!"

    show jes happy2 at left
    with dissolve
    jes "Hmm~ Claro, claro... sin promesas."

    show wiz angry2_2 with dissolve
    wiz "Caray..."
    
    hide jes happy2 at left
    hide wiz angry2_2 with dissolve
    "Wizzy se despidió con la mano mientras Jestyn me acompañaba fuera de su habitación."

    stop music fadeout 2.0
    wiz "Su Majestad...."

    "Mis pasos se detuvieron de repente."
    "La voz de Wizzy estaba justo al lado de mi oído, susurrada como si no quisiera que Jestyn lo escuchara."
    
    wiz "Ten cuidado..."
    
    "¿Qué...?"
    "Vi como Jestyn se alejaba, completamente inconsciente de lo que estaba sucediendo detrás de él."
    "¿Qué pasaría si se enterara?"
    "Ni siquiera me atreví a girar la cabeza hacia Wizzy."
    
    play music "bgs_medieval normal.mp3" volume 3.0 fadein 3.0
    show wiz normal2_2 with dissolve
    wiz "..... Hasta que nos volvamos a encontrar, Su Majestad."
    
    hide wiz normal2_2 with dissolve
    "....No entiendo..."
    scene bg_puppetroom with dissolve
    "Pero en general, Wizzy es amable, reflexivo e increíblemente inteligente."
    "Es... realmente maravilloso hablar con él."

    jump chooseroom_day2

#WIZZY ROOM -----------------------------------------------------WIZZY ROOM----------------------------------------------------------WIZZY ROOM



label knighterroom_day2:
    if met_knighter:
        "Mis ojos se posaron en la puerta con la placa «Caballero»."
        "El títere caballero."
        "El encuentro de ayer en el pasillo todavía estaba vivo en mi mente. El caballero títere se cernía sobre mí como un muro inamovible."
        "El escalofrío persistente aún recorría mi piel cada vez que lo recordaba."
        "Especialmente en el momento en que me di cuenta... que ese títere tenía toda la intención de matarme."
        "Y sin embargo... algo muy dentro de mí me impulsó a al menos intentar presentarme al caballero títere."

    else:
        "Mis ojos se posaron en la puerta con la placa «Caballero»."
        "El títere caballero."

    mc "Me gustaría conocer al títere caballero."
    show jes normal2 with dissolve
    jes "Por supuesto, Su Majestad. Por aquí~"
    
    hide jes normal2 with dissolve
    "Jestyn me lleva a la puerta del títere caballero."
    scene bg_knidoor with dissolve
    "Y en poco tiempo estábamos justo frente a él."
    show jes nosmile with dissolve
    jes "Antes de entrar, Su Majestad, hay algo que debe saber sobre nuestro querido caballero."
    jes "No es el títere con el que es más fácil llevarse bien. Es bastante impulsivo... especialmente con extraños."
    show jes nosmile2 with dissolve
    jes "Y no ha aceptado exactamente a Su Majestad como el nuevo [title] del Kingdom of Marionettes."
    
    "Tragué fuerte… Esto iba a ser difícil."
    
    jes "Entonces mi consejo es simple. Sigue burlándote de él."
    mc "Lo tengo."
    
    stop music
    "......"
    
    mc "...Espera, ¿qué?"
    
    play music "bgs_silly medieval.mp3" volume 1.0 fadein 3.0
    "Mientras intentaba cuestionar lo que acababa de escuchar, Jestyn simplemente me miró como si no hubiera dicho nada inusual."
    
    mc "¿Q-Qué quieres decir? ¿No debería hacer exactamente lo contrario?"
    show jes happy2 with dissolve
    jes "¿Mmm? ¿Por qué? Bromear con él es divertido~"
    jes "Además, no se preocupe, Su Majestad. No te pondrá un dedo encima. No mientras esté a tu lado."
    mc "¿Estás seguro...? Se siente mal molestar a alguien que nunca he conocido antes."
    show jes talk2 with dissolve
    jes "Créame, Su Majestad. Conozco a Knighter mejor que nadie. Si realmente quieres acercarte a él, entonces lo mejor que puedes hacer es..."
    kni "¿De verdad crees que no puedo oír todo lo que dices por ahí?"
    
    "La voz detrás de la puerta me sobresaltó."
    show jes happy2 with dissolve
    "Jestyn, por otro lado, simplemente se rió."
    
    jes "Lo sé~ Por eso lo dije lo suficientemente alto para que lo escuches."
    
    "Jestyn me guiñó un ojo juguetonamente y me mostró en silencio exactamente cómo trató con Knighter."
    
    kni "¿Qué quieres?"
    show jes normal2 with dissolve
    jes "Knighter, mi amado caballero. Hoy te he traído al invitado más importante de todo el reino."
    jes "[poss] Majestad desea tener una conversación con usted."
    
    "El silencio llena el pasillo por unos momentos."
    
    kni "No conozco a nadie con ese título."
    
    "... Vaya. Eso fue frío."
    
    show jes unimpress 
    jes "¡Ah! ¿Cómo pudiste decir algo tan grosero delante de [poss] Majestad? ¿Dónde están tus modales?"
    kni "Ya no hay gobernante en este reino. Fin de la discusión. Fuera."
    
    "Jestyn me dio una palmada en el hombro antes de inclinarse para susurrar."
    show jes happy
    jes "Intenta ordenarle ~ Di algo como... Knighter, como tu gobernante, te ordeno que abras esta puerta."
    hide jes happy with dissolve
    "Miré nerviosamente a Jestyn."
    "...No tenía idea si era una buena idea. Pero... tenía que intentarlo."
    
    mc "K-Knighter! Como tu [title]... ¡Te ordeno que abras la puerta!"
    kni "Dime algo así otra vez... y te atravesaré el corazón con mi espada."
    kni "Lo digo en serio."
    
    "Me quedé paralizado en el acto."
    show jes happy with dissolve
    "Mientras tanto, a mi lado, Jestyn luchaba por contener la risa. Ese idiota."
    "¿Entonces esto fue lo que obtuve por intentar ser valiente?"

    kni "Vete. Vosotros dos. No voy a abrir esta puerta."
    show jes normal with dissolve
    jes "Muy bien ~ Nos iremos."
    jes "Su Majestad... si nos disculpa."
    
    "Jestyn puso una mano sobre mi hombro y chasqueó los dedos."
    play sound "snap.mp3" 
    camera at camera_shake 
    scene bg_knighterroom
    "En un instante, los dos fuimos teletransportados a lo que sólo podía asumir que era la habitación de Knighter."
    camera at reset
    pause 0.5
    camera at camera_shake
    show kni mad
    kni "QUÉ-?!"
    camera at reset
    kni "¡¡DIJE SALIR!!"
    show kni mad at center_to_right
    show jes happy3 at left
    with dissolve
    jes "Te escuché~ Es exactamente por eso que salimos por la puerta principal... y en su lugar entramos a tu habitación."
    kni "¡Qué-TÚ-!"
    
    show kni annoy
    "Knighter se pasó una mano por el pelo con frustración."
    
    show kni hahh with dissolve
    kni "...... Hhhhhhhhhhaaaaaaaaaaaaaaaaaaaahhhhhhhhhhhhhhhhh......"
    kni "... Olvidé que podías hacer eso..."
    show jes bow with dissolve
    jes "Feliz de recordártelo."
    show jes talk2 with dissolve
    jes "Ahorawww, deja que este humilde bufón los presente a ambos."
    show kni normal2 with dissolve
    jes "Su Majestad, este es nuestro valiente y fuerte caballero, Sir Knighter."
    jes "Knighter cariño, este es nuestro amado, asombroso, lindo, adorable, hermoso, amable, gentil [title] [player_call]"
    jes "Ahora bien... tengamos una agradable charla. [poss] Majestad vino hasta aquí para hablar contigo."
    kni "....."
    kni "¿Sobre qué?"
    mc "En realidad, sólo una pequeña charla para conocerte mejor."
    show kni talkaway 
    kni "No me interesa eso."
    
    "Knighter me miró de arriba abajo con evidente irritación."
    
    stop music fadeout 3.0
    show kni normal2 with dissolve
    voice "KNIGHTER01_DAY2.ogg"
    kni "Intruso. Deja de fingir que eres el gobernante de este reino."
    voice "KNIGHTER02_DAY2.ogg"
    kni "No perteneces aquí."
    voice "KNIGHTER03_DAY2.ogg"
    kni "Tienes suerte de que el payaso esté a tu lado. De lo contrario, ya habría-"
    show jes creep
    jes "Knighter."
    
    "Jestyn pronunció su nombre."
    "Su voz era más baja de lo habitual… y todo rastro de su tono juguetón había desaparecido."
    
    jes "¿Qué te dije acerca de hablarle así a [poss] Majestad?"
    show kni annoy2 with dissolve
    kni "......"
    show kni normal2 
    "La expresión de Knighter no cambió."
    "Pero a juzgar por su lenguaje corporal... de repente parecía tenso."
    "... ¿Por qué? ¿Fue por Jestyn? ¿Le tenía... miedo?"
    
    jes "Si hablas así con [poss] Majestad una vez más..."
    kni "...Suficiente."
    show kni annoy with dissolve
    kni "...Lo entiendo."
    show jes happy3 with dissolve
    jes "¡Bien! Ahora... habla con [poss] Majestad correctamente. Ya te lo presenté, ahora inténtalo tú mismo."
    
    hide jes with dissolve
    hide kni with dissolve
    "Jestyn dio un paso atrás, dándonos a Knighter y a mí algo de espacio."
    
    show kni normal2 with dissolve
    kni "......"
    mc "......"
    
    "...Esto fue dolorosamente incómodo."
    "No tenía absolutamente ninguna idea de cómo iniciar una conversación con él."
    
    mc "...U-Um... hola."
    
    show kni mad2 with dissolve
    "En el momento en que la palabra salió de mi boca, la expresión de Knighter se endureció aún más."
    "... ¿Cómo se suponía que iba a tener una conversación con este títere si incluso decir \"hola\" parecía molestarlo?"
    
    show jes nosmile2 at right
    with dissolve
    jes "Suspiro... Está bien. Parece que tendré que ayudar después de todo."
    jes "Disculpe un momento, Su Majestad."
    
    play music "bgs_silly medieval.mp3" volume 1.0 fadein 3.0
    camera at camera_shake
    hide kni nosmile2 
    hide jes mad2 
    show jestynkni
    "De pie detrás de Knighter, Jestyn agarró su brazo y lo extendió hacia mí."
    camera at reset 
    "... ¿Qué estaba haciendo?"
    "Claramente irritado, Knighter inmediatamente intentó retirar su brazo."
    
    jes "Hola, Su Majestad. Soy Knighterrr~"
    kni "¡Suéltame! ¡¿Qué crees que estás haciendo?!"
    jes "Ayudándote a presentarte a [poss] Majestad, por supuesto. Ahora sé un buen caballero y coopera~"
    
    show jestynkni2 with dissolve
    pause 0.1
    hide jestynkni with dissolve
    "Knighter parecía listo para contraatacar antes de finalmente dejar escapar un suspiro de derrota."
    
    show jestynkni3 with dissolve
    pause 0.1
    hide jestynkni2 with dissolve
    jes "Su Majestad, Knighter quisiera estrecharle la mano~"
    mc "O-Oh... está bien."
    
    "Por muy incómodo que fuera, tomé la mano de Knighter y la estreché cortésmente."
    
    show jestynkni5 with dissolve
    pause 0.1
    hide jestynkni3 
    jes "Está bien, está bien ~ Ya basta de tomarse de la mano."
    mc "... ¿Está bien?"
    
    "Después de unos momentos, solté la mano de Knighter."
    
    show jestynkni4 with dissolve
    pause 0.1
    hide jestynkni5 
    jes "......"
    jes "¿Y bien? ¿Por qué estás tan callado, Knighter? Preséntate. ¿Cómo te llamas?"
    show jestynkni3 with dissolve
    pause 0.1
    hide jestynkni4 
    kni "...Uf... Knighter."
    show jestynkni4 with dissolve
    pause 0.1
    hide jestynkni3 
    jes "Knighter ¿quién~?"
    show jestynkni3 with dissolve
    pause 0.1
    hide jestynkni4 
    kni "...Knighter. El títere caballero."
    
    "...Por alguna razón, toda la situación era tan ridícula que tuve que contener la risa."
    
    mc "Ehe- Quiero decir... es un placer conocerte, Knighter. Soy [player_call]..."
    jes "[player_call] ¿quién, Su Majestad~?"
    mc "...[player_call], el nuevo [title] del Kingdom of Marionettes..."

    hide jestynkni3 with dissolve
    "Jestyn asintió con satisfacción antes de finalmente soltar el brazo de Knighter."
    show jes happy3 with dissolve
    jes "Ahí vamos ~ Ahora ambos habéis sido presentados correctamente."
    
    hide jes with dissolve
    "Jestyn trajo dos sillas y las colocó una al lado de la otra."
    
    show jes talk2 with dissolve
    jes "Ustedes dos, tomen asiento aquí ~"
    
    "Para mi sorpresa, Knighter realmente obedeció, aunque no sin quejarse en voz baja."
    "Vacilantemente me acerqué y tomé asiento justo al lado de Knighter."
    
    show jes unimpress with dissolve
    jes ".........."
    
    show jes normal 
    "Jestyn de repente deslizó mi silla un poco más lejos de Knighter."
    
    jes "Ahí vamos~ Por favor, toma asiento, Su Gracia~"
    
    hide jes with dissolve
    "¿Qué le pasa...?"
    "Me senté y traté de ponerme cómoda."
    "Knighter también tomó asiento a mi lado."
    "Tan pronto como se sentó, abrió su libro y comenzó a leer."
    stop music fadeout 3.0
    pause 2.0
    play music "bgs_medieval normla.mp3" volume 3.0 fadein 3.0
    "......"
    "Incluso después de todo eso, la atmósfera seguía siendo dolorosamente incómoda. Knighter ni siquiera intentó iniciar una conversación."
    "Realmente no podía culparlo. No le agrado ni un poquito."
    "Al final, decidí echar un vistazo a la habitación de Knighter."
    "La habitación de Knighter era bastante simple y no tenía tantos objetos."

    jump examineknighterroom_day2

label examineknighterroom_day2:

    if repeat_route < 2:
        $ knighterroom_text = "examina el escritorio"
        
    elif examinetableknighter == 0:
        $ knighterroom_text = "{color=#FFC04C}¿No tienes curiosidad?{/color}"
        
    elif examinetableknighter == 1:
        $ knighterroom_text = "{color=#FFC04C}Examínelo más de cerca..{/color}"
        
    else:
        $ knighterroom_text = "{color=#FFC04C}Más cerca~{/color}"

    menu:
        "Examina las decoraciones de las paredes.":
            jump examine_decoration

        "[knighterroom_text]" if examinetableknighter < 3:
            $ examinetableknighter += 1
            
            if examinetableknighter == 1:
                jump examine_table1
                
            elif examinetableknighter == 2:
                jump examine_table2
                
            elif examinetableknighter == 3:
                jump examine_table3

        "Examina la estantería de libros de Knighter.":
            jump examine_book

        "eso es suficiente":
            jump knighter_convo2

label examine_decoration:
    "Mis ojos vagaron hacia las paredes de la habitación."
    "Allí se exhibían varias decoraciones, aunque la mayoría eran escudos."
    "Había varios escudos montados en las paredes, cada uno con una forma y diseño diferente."
    "No pude evitar preguntarme si eran escudos reales o simplemente piezas decorativas."
    "Pero, de nuevo... ¿un títere necesitaría escudos reales? Incluso si fueran utilizados para una representación teatral."
    jump examineknighterroom_day2

label examine_book:
    "Mis ojos se dirigieron hacia la estantería al lado del escritorio."
    "No era muy grande, pero estaba lleno de libros."
    "Con solo mirarlo, ya me di cuenta de que Knighter era todo un ratón de biblioteca."
    "Me incliné un poco, tratando de ver mejor los tipos de libros que le gustaba leer."
    "Incluso desde donde estaba, reconocí algunas novelas que había leído o al menos visto antes."
    "También noté muchas otras novelas en los estantes... y la mayoría eran románticas."
    "......"
    "Entonces... ¿A Knighter le gusta leer novelas románticas...?"
    "Definitivamente no me esperaba eso."
    "Pero ya había visto este tipo de personajes antes en manga y otras historias de ficción."
    "El tipo que parece duro por fuera pero que en secreto tiene debilidad por las cosas dulces y románticas."
    jump examineknighterroom_day2

label examine_table1:
    "Mis ojos se posaron en el escritorio escondido en un rincón de la habitación."
    "Estaba cubierto de montones de libros, que supuse que eran novelas que había estado leyendo recientemente."
    "También había algunas hojas de papel, un bolígrafo y varios otros útiles de escritura esparcidos por el escritorio."
    jump examineknighterroom_day2

label examine_table2:
    "Mi mirada volvió al escritorio."
    "Eché otro vistazo a las cosas esparcidas por su superficie."
    "Fue entonces cuando noté una fotografía encima."
    "Era una foto de grupo, llena de gente."

    jump examineknighterroom_day2

label examine_table3:
    $ crownus_secret_point += 1
    stop music fadeout 3.0
    play sound "buzzing ear.mp3" fadein 3.0 volume 2.0
    show photo_knighter with dissolve
    "Mi curiosidad se apoderó de mí y mis ojos volvieron a la fotografía sobre el escritorio."
    "Esta vez, miré más de cerca."
    "En la foto, todos los títeres estaban reunidos para una foto grupal."
    "A juzgar únicamente por sus colores blanco y negro, la fotografía parecía bastante antigua."
    "El que está parado en el centro..."
    "¿Es ese Cro-?"

    jump knighter_convo2


label knighter_convo2:
    stop sound fadeout 3.0
    hide photo_knighter with dissolve
    show jes unimpress with dissolve
    jes "¿En serio se van a quedar sentados aquí en un silencio incómodo?"
    
    play music "bgs_silly medieval.mp3" fadein 1.0 volume 3.0
    "La voz de Jestyn finalmente rompió el silencio."
    
    show kni talkaway2 at right
    with dissolve
    kni "Ya te dije que no tengo tiempo para esto."
    show jes normal2 with dissolve
    jes "¿Ah? ¿Cuándo exactamente dijiste eso?"
    kni "Antes de que ustedes dos irrumpieran y arruinaran todo."
    jes "Todo lo que dijiste fue: 'Vete'."
    kni "Sí. Porque estaba ocupado."
    show jes happy2 with dissolve
    jes "Ocupado leyendo esos roma-"
    camera at camera_shake
    show kni flush
    show jes laugh2
    kni "¡¡CALLATE!!"
    camera at reset
    "La cara de Knighter instantáneamente se puso roja brillante cuando Jestyn estaba a punto de mencionar algo."
    
    show jes happy2 with dissolve
    jes "¿Y bien?"
    kni "......."
    show kni annoy with dissolve
    kni "Tsk... Bien. Hablaré con este humano."
    show kni convo normaldown with dissolve
    stop music fadeout 3.0
    kni "Entonces... ¿de qué querías hablar?"
    play music "bgs_medieval normal.mp3" fadein 3.0 volume 3.0
    show screen knibook with dissolve
    
    "Knighter finalmente habló conmigo, aunque su atención nunca abandonó el libro en sus manos."

    jump gettoknow_knighter


label gettoknow_knighter:
    show kni convo normaldown with dissolve
    menu:
        "¿Qué haces en tu tiempo libre?":
            jump freetime_knighter

        "Eres guapo.":
            jump compliment_knighter

        "Quiero saber sobre tu relación con todos.":
            jump relationship_knighter

        "Toca su mejilla":
            jump Poke_knighter

        "¿Qué opinas del rey títere?" if examinetableknighter >= 3:
            $ examinetableknighter
            jump crownusask_knighter

        "eso es todo":
            jump afterconvo_knighter

label freetime_knighter:
    "Quizás no estaría de más preguntarle qué hace habitualmente en su tiempo libre..."
    
    mc "Entonces... si no te importa que te pregunte, ¿qué sueles hacer en tu tiempo libre?"
    show kni convo talkdown
    kni "Leer."
    show kni convo normaldown
    mc "Ah... leyendo."
    mc "Qué lindo."
    mc "........."
    kni "......."
    
    "Y... ¡¿eso es todo?!"
    "Knighter ni siquiera estaba tratando de mantener la conversación."
    
    jes "Señor Knighter, el honorable caballero ~ Una conversación adecuada generalmente implica AL MENOS hacer un esfuerzo para mantenerla."
    jes "¿Qué tipo de conversación fue esa? Fue muy corta; casi tan breve como tus modales~"

    show kni convo close with dissolve
    "La expresión irritada de Knighter se profundizó por un momento antes de dejar escapar un suspiro silencioso y decidir no discutir más con Jestyn."
    "Sabía mejor que nadie que discutir con el bufón real no era más que una pérdida de tiempo."
    
    show kni convo talkdown with dissolve
    kni "...No hago mucho en mi tiempo libre."
    kni "Leo, limpio mi espada y ordeno mi habitación."
    
    show kni convo normaldown
    "Sentí cada vez más curiosidad por su rutina diaria."
    "Limpia su espada. Ordena su habitación..."
    "Knighter realmente era una persona disciplinada. Incluso su habitación estaba impecable y ordenada. Le sentaba perfecto."
    "Ver lo limpia y ordenada que estaba su habitación me recordó a mi propio apartamento."
    "......"
    "A diferencia de la habitación de Knighter, mi apartamento estaba... bastante desordenado."
    "En realidad, \"bastante desordenado\" podría ser quedarse corto. ¿Cuándo fue la última vez que lo limpié...? Ahora estaba un poco avergonzado."
    
    mc "Mmm... Te gusta mantener las cosas limpias. Eso es asombroso."
    mc "Quiero decir, la limpieza es importante."
    
    "Knighter no respondió. Simplemente siguió leyendo su libro."
    "Querido Dios... ¿de qué se suponía que debía hablar con él?"
    "Mis ojos vagaron por la habitación, buscando algo, cualquier cosa, que pudiera convertirse en tema de conversación."
    "O al menos algo lo suficientemente interesante como para mencionarlo."
    "Entonces mi mirada se posó en el libro que estaba leyendo."
    "Tirano del Amor*... Oh, pensé que había oído hablar de ese."
    "Es una novela sobre un director ejecutivo que no se detendrá ante nada para ganarse el corazón del protagonista."
    "Sinceramente... si fuera sincero, la historia era un poco cursi."
    "Pero Knighter parecía disfrutarlo. Parecía completamente absorto en ello."
    "Realmente disfruta de las historias románticas cursis... Tal vez podría usar eso para mantener la conversación."

    mc "...Parece que disfrutas leyendo novelas."
    
    show kni convo suprais
    "En el momento en que mencioné las novelas, sus ojos inmediatamente se dirigieron hacia mí."
    "Después de todo este tiempo, era la primera vez que realmente me miraba."
    "Premio mayor."

    kni "......."
    show kni convo annoy with dissolve
    kni "... ¿Qué te hace pensar eso? No puedes simplemente asumir que me gustan las novelas porque estoy leyendo una ahora mismo."
    mc "Porque noté todas las novelas en tu estantería."
    
    show kni convo suprais
    "Knighter se congeló y su mirada se dirigió lentamente hacia los estantes llenos de su colección."
    
    kni "...¿Se nota que son todas novelas...?"
    mc "La mayoría de ellos, sí. Yo mismo he leído algunos de ellos."
    mc "Y sé que todas son novelas románticas... incluida la que estás leyendo ahora mismo."
    
    camera at camera_shake
    hide screen knibook
    show kni convo flush
    "Knighter inmediatamente cerró su libro y lo escondió detrás de su espalda."
    camera at reset
    "Su rostro se puso rojo brillante en un instante."
    "Espera... ¿No me digas que en realidad le da vergüenza porque lee novelas románticas...?"
    
    mc "O-Oye, no es algo malo."
    kni "Tranquilo."
    kni "No te molestes en intentar hacerme sentir mejor..."
    mc "...Está bien..."
    show kni convo blush with dissolve
    show screen knihand with dissolve
    mc "............"
    mc "Entonces... ¿a quién apoyas en la novela que estás leyendo?"
    
    "Desde que leí la novela, decidí dirigir la conversación hacia la historia en sí, esperando que se sintiera un poco más cómodo hablando de ella."
    
    kni ".........."
    kni "...Edward. El segundo interés amoroso."
    
    "Respondió a mi pregunta, lo que tomé como luz verde para mantener la conversación."
    "En la novela, el protagonista estaba atrapado entre dos hombres: Jacob, el rico director ejecutivo y principal interés amoroso de la historia, y Edward, el amigo de la infancia del protagonista y el segundo interés amoroso."
    "Jacob estaba obsesivamente enamorado del protagonista y no se detendrá ante nada para deshacerse de Edward. Convencía constantemente al protagonista de que Edward no era un buen hombre..."
    "...afirmando que abrir una brecha entre ellos era por el bien del protagonista."
    "Lo hizo todo para ganarse el corazón del protagonista."
    "Por supuesto, cualquiera en su sano juicio podría darse cuenta de que Jacob era completamente el equivocado."
    
    mc "¿Verdad? Yo también lo pensé. Quiero decir... Jacob está loco."
    mc "Sigue pintando a Edward como el villano y abre una brecha entre él y el protagonista."
    
    show kni convo talkup with dissolve
    "Knighter asintió con la cabeza."
    
    kni "Exacto... cualquiera con dos dedos de frente puede ver lo despreciable que es eso."
    kni "Lo que más me irrita es cómo Jacob abusa de su posición como director ejecutivo de la empresa para inculpar a Edward de malversación de fondos de la empresa."
    show kni convo annoy with dissolve
    kni "No sólo intenta convencer al protagonista. También manipula a todos los que lo rodean, asegurándose de que la mayoría esté de su lado."
    kni "Escoria absoluta."
    
    "Me sorprendió la ira en la voz de Knighter. Estaba mucho más involucrado en la historia de lo que esperaba."
    
    mc "Sí... y lo más triste es que todos le creen. Incluso el protagonista cae en sus mentiras y Edward termina completamente aislado."
    mc "Pobre chico..."
    mc "Pero tengo algo de curiosidad... ¿Crees que Jacob realmente está equivocado? De hecho, hay personas a las que les gusta su personalidad obsesiva y dicen que es increíblemente leal y dulce con el protagonista."
    
    show kni convo close with dissolve
    hide screen knihand with dissolve
    "Knighter dejó escapar un profundo suspiro."
    
    kni "Ya sea ficción o realidad, ese tipo de comportamiento es peligroso."
    show kni convo annoy 
    kni "Manipula a la gente, abusa de la autoridad que tiene sobre Edward y es obsesivamente posesivo. No hay nada admirable en él."
    kni "Incluso si es leal y actúa dulcemente con el protagonista, eso no borra todas las cosas terribles que ha hecho para conseguir lo que quiere."
    kni "Entonces sí... creo que Jacob está equivocado."
    
    show kni convo normaldown with dissolve
    show screen knibook with dissolve
    "Knighter pareció recuperar la compostura y volvió a leer su novela."
    "Así que puede ser bastante hablador en las circunstancias adecuadas... Hablar con Knighter no es tan malo después de todo."
    
    mc "Jaja. En realidad es muy divertido hablar contigo."
    
    show kni convo suprais
    pause 1.5
    show kni convo blush with dissolve
    "Sus ojos se abrieron por una fracción de segundo antes de apartar la mirada rápidamente."
    "Aun así, todavía podía ver un leve sonrojo arrastrándose por sus mejillas."
    
    kni ".... No necesito tus elogios."

    jump gettoknow_knighter

label compliment_knighter:
    "Llevaba un tiempo mirando la cara de Knighter. Realmente parecía un príncipe sacado de un cuento de hadas."
    "La mayoría de las personas se alegran cuando alguien les felicita... creo."
    "Pero ¿qué pasa con Knighter?"
    "A juzgar por cómo ha estado actuando, parece del tipo al que no le importa nada."
    "Es muy probable que no reaccione incluso si lo felicito."
    "Aún así... no estaría de más intentarlo. Nunca lo sabré a menos que lo intente, ¿verdad...?"
    "Respiré profundamente, tratando de calmar mis nervios. En realidad estaba bastante ansioso."
    
    mc "Sabes... Creo que eres muy guapo."
    stop music
    show kni convo disgust with dissolve
    "......."
    play music "bgs_silly medieval.mp3" volume 1.0 fadein 3.0
    "Como era de esperar, me miró... pero en lugar de parecer indiferente, su rostro se torció en uno de puro disgusto."
    "Vaya... definitivamente no me esperaba eso. Eso fue un giro de la trama."
    "De repente, sentí una mano posarse suavemente sobre mi hombro desde atrás."
    
    jes "Su Majestad."
    
    "La voz de Jestyn estaba tan cerca que su susurro rozó mi oído."
    
    jes "Ahora bien... ¿qué le acabas de decir exactamente a Knighter, hm~?"
    
    hide kni convo disgust with dissolve
    hide screen knibook with dissolve
    "Miré hacia Jestyn que estaba detrás de mí."
    show jes creep with dissolve
    "Su expresión parecía... ¿irritada...?"
    
    mc "¿Q-qué? ¿Hice algo mal?"
    
    "Jestyn no respondió. Simplemente me miró fijamente con una mirada aguda e ilegible."
    "Sólo estaba tratando de felicitar a Knighter... ¿Está molesto por eso?"
    "......"
    "Espera... no me digas..."
    "Knighter y Jestyn..."
    hide jes creep with dissolve
    show kni convo disgust with dissolve
    "Mi mirada volvió a Knighter. Todavía tenía esa misma mirada de disgusto."

    "Su expresión irritada instantáneamente se convirtió en confusión y conmoción."
    
    kni "¿Qué diablos acabas de decir?"
    mc "Sólo estaba diciendo la verdad."
    
    "Sinceramente, no estaba seguro de si decir eso era una buena idea."
    
    show kni convo annoy with dissolve
    kni "Debe haber algo mal en tu cabeza."
    
    "¿Tal vez si sigo adelante, podría suavizarlo un poco?"
    
    mc "Por supuesto~ ¿Quién podría resistirse a una cara tan hermosa?"
    mc "Estoy seguro de que cualquiera que te vea por primera vez se volverá completamente loco por ti."
    
    show kni convo suprais
    "......."
    show kni convo smirk with dissolve
    "Sus labios lentamente se curvaron en una sonrisa."
    
    stop music fadeout 3.0
    kni "Ya veo... Entonces eso es lo que estás tratando de hacer."
    kni "Como no soy alguien que confíe fácilmente, has decidido coquetear conmigo."
    voice "KNIGHTER04_DAY2.ogg"
    kni "Felicitas mi apariencia... dime que soy guapo..."
    show kni convo annoy
    voice "KNIGHTER05_DAY2.ogg"
    kni "Todo para que baje la guardia. Y una vez que te acerques lo suficiente, te aprovecharás de mí... y me manipularás."
    
    "Knighter expuso cada una de sus sospechas sin dudarlo."
    "Nunca imaginé que sería tan desconfiado... al punto de pensar que estaba coqueteando con él."
    "No es así como esperaba que fuera esta conversación."
    
    mc "¡Eso no es todo! ¡Realmente lo dije como un cumplido!"
    show kni convo smirk
    kni "Je. En ese caso mereces morir."
    
    "Joder."
    camera at camera_shake
    show kni convo jes
    "Jestyn de repente se paró frente a mí y agarró el brazo de Knighter, deteniéndolo."
    camera at reset
    hide kni convo jes with dissolve
    show kni mad at right
    with dissolve
    kni "Uf-"

    show jes creep2 at left
    with dissolve
    jes "Knighter... si escucho esas palabras salir de tu boca una vez más-"
    kni "¿Por qué? No puedes seguir dándome órdenes."
    kni "No soy un niño."
    jes "Sí, sí, sí ~ Mi honorable señor Knighter. No recuerdo que esos hermosos labios míos dijeran alguna vez Pensé que eras un bebé aprendiendo a caminar~"
    jes "¡De hecho! Incluso es más fácil tratar con un bebé. Ahora mismo no eres más que un perro callejero abandonado por su dueño. Que trágico~"
    
    play sound "nyekek.mp3"
    camera at camera_shake
    hide jes creep2
    hide kni mad
    show knicg fight
    "Su ira finalmente se desbordó, Knighter agarró a Jestyn por el cuello."
    camera at reset
    show knicg fight2 with dissolve
    "Los dos se miraron a los ojos, mirándose el uno al otro."
    
    kni "Dime eso en la cara una vez más."
    show knicg fight3 with dissolve
    jes "¡Jajajaja~! Soy el títere bufón, cariño. Estos labios solo hablan del dulce sabor de la verdad. No del sabor amargo y agrio de las mentiras y el engaño."
    jes "Y si te ofreciera otra muestra de esa dulzura... ¿entonces qué? ¿Quieres revivir esos viejos tiempos MARAVILLOSOS, hm~?"
    show knicg fight4 with dissolve
    jes "No me importaría en absoluto. Déjame buscar mi hacha... y podemos empezar."

    "Mi pobre cerebro, incapaz de procesar las cosas rápidamente, trabajó horas extras tratando de darle sentido a la situación que de repente se había vuelto tan tensa."
    "¿¿Q-Qué diablos...?? ¿Están realmente a punto de pelear?"
    "¡¿Todo lo que hice fue felicitar a Knighter y de alguna manera se convirtió en esto?!"
    "No... Esto no puede estar pasando."
    
    mc "¡Está bien, ya es suficiente, los dos!"
    mc "Estamos aquí para hablar, no para pelear. ¿Entendido?"
    
    "No se movieron ni un centímetro, incluso después de que dije eso."
    "No pude leer la expresión de Jestyn en absoluto. ¿Estaba realmente enojado... o simplemente estaba bromeando como solía hacer?"
    "Cualquiera sea el caso, la atmósfera alrededor de Jestyn se sentía... inquietante."
    
    mc "Jestyn. Detente. Ya basta."
    jes "........"

    "Incluso Jestyn no se movió."
    "Me devané los sesos desesperadamente, tratando de descubrir cómo aligerar el estado de ánimo."
    "¿Quizás algo divertido...? ¿Algo gracioso...? Uf, soy terrible ideando temas de conversación."
    "......."
    "......Oh... Tal vez podría preguntar sobre eso."
    
    mc "Uh... en realidad me he estado preguntando sobre algo..."
    mc "¿Están ustedes dos como... saliendo?"
    show knicg fight5
    stop music
    jeskni "¿Eh?"

    "......Tal vez estaba completamente equivocado, a juzgar por sus reacciones."
    "Sin pensarlo dos veces, Knighter empujó a Jestyn."
    play music "bgs_silly medieval.mp3" volume 1.0 fadein 3.0
    camera at camera_shake
    hide knicg fight5
    show kni mad
    "Bueno... al menos logré evitar que pelearan."
    camera at reset
    
    kni "¡¿Todo lo que sale de tu boca tiene que ser una completa tontería?!"
    mc "...solo estaba preguntando."
    kni "No. Hoy no. Nunca. Preferiría atravesar mi corazón con mi propia espada que terminar con este bufón idiota."
    
    "... Vaya. Realmente quiere decir eso, ¿eh?"
    
    show kni mad at center_to_right
    show jes unimpress2 at left
    with dissolve
    jes "Su Majestad... ¿cómo se le ocurre pensar que estaría con este Sr. Gruñón con armadura? ¿Qué he hecho alguna vez para merecer tal acusación~?"
    mc "Nada... solo estaba adivinando..."
    mc "...Bueno, tal vez porque sigues burlándote de mí todo el tiempo."
    show jes pout2 with dissolve
    jes "Pero ese es simplemente mi deber como bufón real~"
    
    "Jestyn me miró con ojos muy abiertos y suplicantes de cachorrito."
    "¡¿Desde cuándo podría poner una cara así?! ¡Eso no es justo!"
    
    jes "......Así que el tiempo que pasamos juntos ayer no significó nada en absoluto para Su Majestad..."
    mc "N-no, ¡eso no es lo que quise decir! M-mira... volvamos a nuestra conversación, ¿vale?"
    mc "Sean cuales sean vuestros problemas, dejadlos fuera de esta conversación. ¿Entendido?"
    
    "Jestyn asintió levemente."
    
    show jes unimpress with dissolve
    jes "...Su Majestad realmente es muy amable... pero mi pobre corazón todavía está herido..."
    mc "Ahora, ¿qué tal si ustedes dos se reconcilian? Ya sabes... estrechar la mano."
    
    show jes glance 
    show kni glance
    "Jestyn y Knighter simplemente se miraron el uno al otro."
    show jes glance2 with dissolve
    show kni glance2 with dissolve
    "Antes de finalmente mirar hacia otro lado, ambos con expresiones de molestia."
    
    mc "Jaja... ¿De verdad tengo que guiaros a vosotros dos en una disculpa como a un par de niños?"
    mc "Dije, estrechar la mano. Esa es una orden."
    mc "Jestyn, extiende tu mano a Knighter."
    jes "........"
    
    "Jestyn obedeció como de costumbre y le tendió la mano a Knighter."
    
    mc "Knighter, tu turno. Extiende tu mano y estrecha la de Jestyn."
    kni "........"
    
    "Sorprendentemente, Knighter también obedeció y le tendió la mano. Los dos finalmente se dieron la mano."
    
    mc "¿Y luego? ¿Qué se supone que debes decir cuando has hecho algo mal?"
    jeskni "........."
    jeskni "...Lo lamento."

    mc "¿Ves? Eso no fue tan difícil, ¿verdad...?"
    
    "Después de unos momentos, finalmente se soltaron las manos."
    "Con un suspiro exageradamente abatido, Jestyn lentamente regresó a su lugar habitual detrás de mí."
    "Todo lo que quería era felicitar la apariencia de Knighter... Tal vez felicitarlo fue un error desde el principio..."
    stop music fadeout 3.0
    hide jes glance2 with dissolve
    hide kni glance2 with dissolve
    play music "bgs_medieval normal.mp3" volume 3.0 fadein 3.0

    jump gettoknow_knighter

label relationship_knighter:
    "Knighter parecía el tipo de títere al que le costaba llevarse bien con los demás. No pude evitar preguntarme cómo eran sus relaciones con el resto de los títeres."
    
    mc "¿Puedo preguntarte cómo es tu relación con los otros títeres?"
    
    show kni convo normalup with dissolve
    "Knighter me miró por un breve momento."
    
    show kni convo close with dissolve
    kni "Bien."
    
    show kni convo normaldown 
    "Luego inmediatamente volvió a su libro. ¿En serio?"
    
    mc "...¿Qué tan bien?"
    show kni convo talkdown
    kni "Muy bien."
    show kni convo normaldown 
    mc "Sabes que eso no es lo que quise decir."
    
    show kni convo close
    "Dejó escapar un largo suspiro."
    
    show kni convo talkup with dissolve
    kni "No sé exactamente qué quieres que te explique."
    
    show kni convo normalup
    "¿En serio tengo que explicarle todo a este títere?"
    
    mc "Está bien, bien."
    mc "Quiero que me cuentes cómo es tu relación con los demás títeres. ¿Qué tan bien te llevas con cada uno de ellos?"
    mc "Comencemos con Jestyn."
    
    "Jestyn infló su pecho con orgullo, luciendo más engreído que nunca."
    show kni convo annoy with dissolve
    show screen knihand with dissolve
    "Knighter, por otro lado, parecía como si acabara de morder algo amargo."
    
    kni "Quiero darle un puñetazo."
    jes "Qué grandes elogios de parte de mi noble caballero~ Mi pobre corazón está tan conmovido que prácticamente está partido."
    
    "Knighter respondió al sarcasmo de Jestyn con nada más que poner los ojos en blanco."
    
    show kni convo talkup 
    kni "No es más que una molestia. Un dolor de cabeza andante."
    show kni convo normaldown
    mc "¿Qué ha hecho exactamente para que te desagrade tanto?"
    show kni convo talkdown
    kni "Muchas cosas."
    show kni convo normaldown
    mc "¿Como qué?"
    show kni convo annoy
    kni "Bromas. Le encanta hacer bromas a la gente. Yo especialmente."
    mc "¿Son realmente tan malas las bromas que te hace Jestyn?"
    show kni convo talkdown
    kni "Júzgalo tú mismo."
    
    "Sí... creo que aceptaré su palabra."
    
    mc "Mmm... ¿Cuál es la broma más leve que te ha hecho?"
    
    show kni convo normalup with dissolve
    hide screen knihand with dissolve
    "Knighter hizo una pausa para pensar por un momento."
    
    show kni convo annoy with dissolve
    kni "Me arrojó un cubo de barro en la cabeza."
    
    "......"
    "¿Ese es el más leve...?"
    
    mc "E-Eh... vale... Entonces, ¿cuál fue la peor?"
    

    "El ceño de Knighter se frunció aún más. Su mandíbula se apretó cuando la irritación cruzó por su rostro."
    "Pase lo que pase… quedó claramente grabado en su memoria."

    kni "...Preferiría no recordarlo."
    camera at camera_shake
    hide kni convo annoy
    hide screen knibook 
    show jes happy2
    jes "Mis disculpas por interrumpir, Su Majestad~ Pero como mi querido amigo caballero parece estar luchando, permita que este humilde bufón cuente la historia en su nombre."
    
    camera at reset
    show kni mad at right
    with dissolve
    "Knighter le lanzó a Jestyn una mirada asesina. Todo su cuerpo se puso rígido."
    
    hide kni mad with dissolve
    show jes bow with dissolve
    jes "En una tarde brillante y hermosa~ Sir Knighter estaba disfrutando pacíficamente de una refrescante taza de café helado mientras leía una novela romántica que aún no había terminado."
    show jes unimpress2 with dissolve
    jes "Luego suspiró y dijo... 'Hahh... Hace tanto calor...'"
    camera at camera_shake
    show kni flush at right
    with dissolve
    kni "Jestyn, tú-"
    show jes normal2 with dissolve
    jes "Así que, naturalmente, este humilde bufón, con un corazón rebosante de bondad y una irresistible necesidad de ayudar, decidió acudir al rescate del honorable caballero."
    show jes nosmile2 with dissolve
    jes "Sin su conocimiento, por supuesto. La verdadera bondad no requiere reconocimiento. Actué por la pura bondad de mi corazón."
    show jes happy3 with dissolve
    jes "Una sola sonrisa de agradecimiento hubiera sido más que suficiente para mí. Entonces..." 
    jes "Este humilde bufón transformó su pesada, rígida, brillante, reluciente y espléndida armadura en algo suave, liviano y que garantizaba mantener a su portador agradable y fresco..."
    camera at camera_shake
    kni "¡¡JESTYN!!"
    camera at reset
    
    "Antes de que Knighter pudiera terminar, Jestyn instantáneamente se teletransportó detrás de él y se tapó la boca con una mano."
    "Knighter luchó furiosamente, tratando de apartar la mano de Jestyn."
    
    show jes laugh2
    jes "...¡Un bikini!"
    mc "........."
    mc "¿Convertiste la armadura de Knighter... en un bikini?"
    show jes happy3 with dissolve
    jes "¡BINGO~!"

    hide jes happy3
    hide kni flush with dissolve
    "Jestyn luego se teletransportó detrás de mí."
    show kni annoy2 with dissolve
    "Knighter, con el rostro todavía rojo brillante, lo miró con evidente irritación."
    "Pero en el momento en que se dio cuenta de que su secreto había salido a la luz, rápidamente apartó su rostro de mí."
    "Entonces Jestyn no se lo estaba inventando después de todo... Esa historia era realmente cierta."
    
    kni "...... Ahora lo sabes. No preguntes por los detalles."
    
    "Decidí no insistir más y pasé a preguntarle sobre su relación con los otros títeres."
    
    mc "En ese caso... ¿qué pasa con los otros títeres además de Jestyn?"
    hide kni annoy2 with dissolve
    show kni convo normalup with dissolve
    show screen knihand with dissolve
    kni "....."
    show kni convo talkup with dissolve
    kni "...Wizzy, supongo."
    kni "Me llevo bien con él. No tenemos ningún problema."
    show kni convo normalup
    mc "¿Ustedes dos hablan a menudo?"
    show kni convo talkup
    kni "Con bastante frecuencia."
    show kni convo talkdown
    kni "Normalmente solo hablamos de cosas al azar... o lo escucho mientras Wizzy parlotea sobre sus experimentos."
    kni "No hablo mucho. Principalmente solo escucho."
    
    show kni convo normaldown
    show screen knibook with dissolve
    "Asentí en comprensión."
    "Parecía que Knighter y Wizzy eran bastante cercanos. Por lo menos, tenía a alguien con quien realmente podía llevarse bien."
    
    mc "Muy bien entonces."
    mc "¿Qué pasa con los otros títeres?"
    
    "Knighter se puso a pensar profundamente."
    
    kni ".........."
    show kni convo talkdown with dissolve
    kni "La mayoría de ellos son sólo conocidos."
    kni "Farmin, Butley... todos son compañeros comunes y corrientes. Nos saludamos cortésmente cada vez que nos cruzamos."
    
    if visited_wizzy:
        $ prieston_route_point += 1
        show kni convo normaldown with dissolve
        mc "Ya veo..." 
        mc "Mmm... Antes estaba hablando con Wizzy y mencionó un sacerdote títere llamado Prieston. ¿Cómo es tu relación con él?"
        
        show kni convo suprais with dissolve
        "El ceño de Knighter se frunció casi de inmediato."
        
        kni ".....Él..."
        kni "............."
        
        "Hizo una pausa por un momento, aparentemente luchando por encontrar las palabras adecuadas."
        
        show kni convo normaldown 
        kni "Él es... confuso."
        mc "¿Qué quieres decir?"
        kni "No sé mucho sobre él. Nos saludamos cuando nos encontramos... pero ni siquiera eso sucede muy a menudo."
        kni "Rara vez sale de su habitación."
        kni "...Y..."
        kni "Sinceramente, no tengo idea de lo que está pasando dentro de su cabeza."
        kni "Realmente no confío en él."
        
    mc "...Muy bien, entonces..."
    mc "Tal vez-"
    kni "Creo que es suficiente por ahora. No hay nada particularmente interesante sobre este tema."
    hide screen knihand with dissolve

    jump gettoknow_knighter

label crownusask_knighter:
    $ crownus_secret_point += 1
    "Quería saber qué pensaba del Rey Marioneta. Quería saber qué clase de persona había sido."
    
    mc "Sabes... en realidad tengo mucha curiosidad sobre el Rey Marioneta."
    mc "Entonces... me gustaría saber qué piensas de él."
    
    show kni convo suprais with dissolve
    stop music
    "Knighter se congeló."
    "Luego me miró lentamente. Pero con una expresión completamente diferente."
    show kni convo sad with dissolve
    "Parecía... sorprendido. Y... ¿triste?"
    "¿Por qué?"
    
    mc "¿Knighter...?"
    kni "......Él..."
    
    "Knighter se quedó en silencio por un momento."
    
    voice "KNIGHTER06_DAY2.ogg"
    kni "...Crownus era... nuestro futuro... Él..."
    jes "Creo que terminaremos esta conversación aquí."
    
    "Jestyn interrumpió abruptamente a Knighter. Su voz sonaba tan juguetona como siempre, pero de alguna manera... la atmósfera a su alrededor de repente se sintió inquietante."
    
    mc "¿Eh? Pero yo sólo estaba-"
    jes "¿No crees que es una falta de respeto hablar de alguien que ya falleció? Su alma merece descansar en paz."
    show kni convo annoy
    jes "Así que dejémoslo en su eterno descanso para siempre. ¿Está bien~?"
    play music "bgs_medieval normal.mp3" volume 3.0 fadein 3.0

    jump gettoknow_knighter

label Poke_knighter:
    "......"
    "Por alguna razón, de repente sentí esta abrumadora necesidad de meterme con él."
    "Antes de que pudiera pensarlo dos veces, extendí la mano y toqué su mejilla."
    
    show screen knipoke
    show kni convo suprais
    kni "!!"
    
    "De hecho, podía sentir su piel debajo de mi dedo. Se sentía como piel humana... Qué extraño."
    
    kni "¿Qué crees que estás haciendo exactamente?"
    
    "Knighter me lanzó una mirada asesina, pero todo lo que hizo fue mirarme fijamente."
    hide screen knipoke with dissolve
    show kni convo annoy with dissolve
    kni "No te atrevas a tocarme otra vez, o yo..."
    jes "¡Ejem!"
    
    show kni convo close
    "Jestyn se aclaró la garganta con fuerza, interrumpiendo a Knighter antes de que pudiera terminar."
    "Knighter sólo pudo dejar escapar un suspiro de derrota."
    
    show kni convo talkdown with dissolve
    kni "Deja eso."
    
    show kni convo normaldown
    "Volvió a leer su libro."

    menu :
        "Tocarle la mejilla otra vez":
            "Ignoré su advertencia y volví a tocar su mejilla."
            show screen knipoke
            show kni convo suprais
            kni ".........."
            kni "¿Estás sordo?"
            jes "¿Mi querido amigo Knighter~?"
            show kni convo close
            kni ".........."
            show kni convo gentle with dissolve
            kni "¿Podrías dejar de tocarme la mejilla~?"
            kni "...O te mataré."
            hide screen knipoke with dissolve

        "Mejor parar":
            jump gettoknow_knighter
            
    menu :
        "Tocarle la mejilla otra vez.":
            show screen knipoke with dissolve
            "¡Toc!"
            
            camera at camera_shake
            hide screen knipoke
            hide screen knibook
            show kni convo cubit
            kni "¡¡TÚ!!"
            camera at reset
            kni "Voy a-"
            jes "¿Realmente tengo que repetirme?"
            
            show kni convo cubit2 with dissolve
            "Knighter luchó por controlar su temperamento."
            "Entonces..."
            
            camera at camera_shake
            show kni convo cubit3
            mc "¡¡Ay, ay, ay, ay!!"
            camera at reset
            "Knighter me pellizcó el brazo con fuerza en represalia."
            show kni convo annoy with dissolve
            "Inmediatamente retiré mi mano."
            
            kni "Haz eso de nuevo y no puedo prometerte que el próximo pellizco no te duela aún más."
            jes "¡¿Cómo te atreves a hacer daño a [poss] Majestad?!"
            show kni convo close
            show screen knibook
            kni "Fue sólo un pellizco. No seas tan dramático. Deberías estar agradecido de que no fui tan imprudente como para desenvainar mi espada."
            jump gettoknow_knighter

        "Mejor parar":
            jump gettoknow_knighter


label  afterconvo_knighter:
    hide jes happy2
    hide screen knibook with dissolve
    hide kni convo normaldown with dissolve
    show kni talkaway2 with dissolve
    kni "¿Hemos terminado?"
    
    "No se me ocurrió otro tema que mencionar, así que asentí, poniendo fin a la conversación."
    "Ya había aprendido suficiente por un día."
    "Y honestamente... Knighter parecía exhausto. Emocionalmente, más que nada."
    
    show kni normal with dissolve
    kni "Finalmente. Me he quedado completamente sin energía social al tratar con vosotros dos."
    kni "Entonces, ahora que he satisfecho su curiosidad, les ruego a ambos que abandonen mi habitación."
    kni "Ahora."

    hide kni normal with dissolve
    "Me levanté de mi silla."
    "Knighter también se levantó y nos observó mientras nos dirigíamos hacia la puerta."
    
    show jes happy2 at left 
    with dissolve
    show kni normal2 at right
    with dissolve
    jes "Gracias por tomarse el tiempo de hablar con [poss] Majestad, mi honorable caballero~"
    show jes bow 
    jes "En el fondo... realmente tienes un corazón noble."
    show kni hahh2 with dissolve
    kni "No sé si te estás burlando de mí o haciéndome un cumplido. Elegiré tomarlo como un cumplido, considerando que simplemente perdí un tiempo que, en primer lugar, nunca quise perder."
    show kni annoy2
    kni "Y recuerda esto, nunca quise hablar con ese humano. Me obligaste a hacerlo."
    
    show jes laugh2
    "Jestyn respondió con nada más que risas."
    
    show jes talk2 with dissolve
    jes "Bueno, al menos algunas cosas sobre ti nunca cambian~"
    show kni suprais with dissolve
    pause 1.5
    show kni sad2 with dissolve
    kni "...................."
    jes "En ese caso, hasta la próxima... ¡mi honorable señor Knighter~!"

    hide kni sad2 with dissolve
    hide jes talk2 with dissolve
    "Knighter simplemente puso los ojos en blanco en respuesta."
    "Jestyn luego me siguió fuera de la habitación de Knighter."
    scene bg_puppetroom with dissolve
    "En general, hablar con Knighter había sido bastante difícil. Era un títere muy reservado."
    "Si Jestyn no hubiera estado allí, probablemente habría sido aún más difícil. Sin embargo, sorprendentemente, Knighter realmente lo escuchó. Jestyn podría incluso presionarlo para que responda mis preguntas."
    "Aún así... creo que necesito acercarme a Knighter."
    "Aún no ha aprendido a confiar en mí."

    jump chooseroom_day2



