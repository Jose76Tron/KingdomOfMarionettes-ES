# Traducción fan al español — Kingdom of Marionettes 2.0
# Fichero: character.rpy
# Nombres propios intactos. Roles genéricos traducidos.

define jes = Character("Jestyn", color="#d7343f")

define jespuppet = Character("Marioneta bufón", color="#d7343f")

define kni = Character("Knighter", color="#6a7eb1")

define wiz = Character("Wizzy", color="#ff892f")

define knipuppet = Character("Marioneta caballero", color="#6a7eb1")

define who = Character("???", color="#d8cebd")

define u = Character("Tú", color="#efba7e")

define farm = Character("Granjero", color="#efba7e")

define debt = Character("Cobrador", color="#efba7e")

define nara = Character("Narrador", color="#efba7e")

define puppet = Character("¿¿Marioneta??", color="#efba7e")

define maidy = Character("Maidy", color="#efba7e")

define maidra = Character("Maidra", color="#efba7e")

define maidelyn = Character("Maidelyn", color="#efba7e")

define maid = Character("Las Doncellas", color="#efba7e")

define jeskni = Character("Jestyn y Knighter", color="#efba7e")

define butpuppet = Character("Marioneta mayordomo", color="#efba7e")

define but = Character("Butley", color="#efba7e")

define pup1 = Character("Marioneta 1", color="#efba7e")

define pup2 = Character("Marioneta 2", color="#efba7e")

define pup3 = Character("Marioneta 3", color="#efba7e")

define pup4 = Character("Marioneta 4", color="#efba7e")

define pri = Character("Prieston", color="#a16fe0")

define everyone = Character("Todos", color="#efba7e")



default name_warning_count = 0
label ask_player_name:

    $ player_name = renpy.input("¿Cómo te llamas?", default="Seven")
    $ player_name = player_name.strip()

    if player_name == "":
        $ player_name = "Seven"

    $ name_check = player_name.lower()

    # default: character manggil pakai nama asli
    $ player_call = player_name

    if name_check == "jestyn":
        show jes happy2 with dissolve
        jes "Oh, tarta dulce y crema. ¡Tenemos el mismo nombre! Qué milagro tan maravilloso."
        show jes normal2
        jes "Mmm... en ese caso, llamarte por tu nombre sería un problema. Sería raro estar llamándome a mí mismo."
        jes "Así que, en su lugar, te otorgaré un apodo. ¡Sweetyn! ¿No suena delicioso? Dulce, como una tarta de fresa."
        show jes happy2
        jes "Y además, comparte las mismas letras finales. SweeTY, JesTYn. ¿No soy un genio?"
        mc "Esto... en realidad, le falta una «N»."
        show jes normal2
        jes "Entonces Sweetyn."
        "... Supongo que me vale."

        $ player_call = "Sweetyn"  # atau nickname khusus

    if name_check == "knighter":
        $ name_warning_count += 1

        if name_warning_count == 1:
            show jes happy2 with dissolve
            jes "¿¿Qué? ¿¡Knighter!? ¡Pfff! ¡Jajajajajaja! ¡Ay! ¿¡El cielo y la tierra intentan gastarme una broma!?"
            show jes talk with dissolve
            jes "Es un nombre con un sonido audaz y heroico, eso te lo concedo. Pero no puedo permitir que lo conserves."
            jes "Si el amo gruñón se enterara... ay, me horroriza imaginar en cuántos pedazos acabarías."
            show jes normal2 with dissolve
            jes "Así que te sugiero que elijas otro nombre."
            jump ask_player_name

        elif name_warning_count == 2:
            mc "Pero si mi nombre de verdad es Knighter..."
            show jes normal2_2
            jes "Y yo te digo que ya no puedes usar ese nombre."
            jes "O como dije hace unos segundos... no serías más que fragmentos esparcidos en un abrir y cerrar de ojos."
            show jes normal2
            jes "Así que te sugiero encarecidamente que elijas un nombre nuevo. Ahora mismo."
            jump ask_player_name

        elif name_warning_count >= 3:
            show jes nosmile with dissolve
            jes "Mmm... me pregunto, dulce humano."
            jes "¿Es que tus oídos no funcionan y no escuchaste lo que dije, o eres simplemente terco? Apenas hay diferencia."
            show jes bow with dissolve
            jes "Muy bien. Ya que insistes en ser tan obstinado, te daré yo mismo un nombre."
            show jes talk2 with dissolve
            jes "Desde este momento, tu nombre será... Stubbornelle."
            mc "Pero..."
            show jes normal2
            jes "Tatatatá~ Nada de quejas."

            $ player_call = "Stubornelle"



    if name_check == "wizzy":
        show jes happy3 with dissolve
        jes "¡Ay, por favor! ¿Wizzy? ¿Lo he oído bien?"
        show jes talk2 with dissolve
        jes "Qué adorable. Espera a que Wizzy, el mago real, se entere de esto."
        show jes normal2 with dissolve
        jes "Estoy seguro al mil y un por ciento de que su corazón brillará como una estrella cuando sepa que tiene un gemelo nuevo."

    if name_check == "crownus":

        $ cursed_route = True
        stop music
        show jes creep with dissolve
        show screen dark_effect with dissolve

        "{color=#FF2727}......{/color}"
        "{color=#FF2727}oh..... ¿de verdad...?{/color}"
        "{color=#FF2727}ja.... jaja....{/color}"
        scene black with dissolve
        camera at camera_shake
        "{color=#FF2727}{cps=220}JA JA JA JA JA JA JA JA JA JA JA JA JA JA JA JA JA JA JA JA JA JA JA JA JA JA JA JA JA JA JA JA JA JA JA JA JA JA JA JA JA JA JA JA JA JA JA JA JA JA JA JA JA JA JA JA JA JA JA JA JA JA JA JA JA JA JA JA JA JA JA JA JA JA JA JA JA JA JA JA JA JA JA JA JA JA JA JA JA JA JA JA{/cps}{/color}"

        "......"
        "........."
        camera at reset
        scene bg_theaterhall with dissolve
        play sound "jinglebell.mp3"
        show jes creep2 with dissolve
        play music "abandoned.mp3" volume 3.0 fadein 2.0
        jes "Ah... es un auténtico honor conocerte, [player_call]."
        hide screen dark_effect with dissolve

    return

define mc = DynamicCharacter("[player_call]", color="#efba7e")

# NOTA ES: subj/obj/poss/refl/title/gend ya van en español para que
# [poss] Majestad -> "su Majestad", [title] -> reina/rey/gobernante, etc.
default subj = "elle"   # ella / él / elle
default obj = "les"   # la / lo / les
default poss = "su"  # su / su / su
default refl = "sí misme"  # sí misma / sí mismo / sí misme
default title = "gobernante"
default gend = "peque"

label pronoun:
    menu:
        "Ella":
            $ subj = "ella"
            $ obj = "la"
            $ poss = "su"
            $ refl = "sí misma"
            $ title = "reina"
            $ gend = "niña"

        "Él":
            $ subj = "él"
            $ obj = "lo"
            $ poss = "su"
            $ refl = "sí mismo"
            $ title = "rey"
            $ gend = "niño"

        "Elle (neutro)":
            $ subj = "elle"
            $ obj = "les"
            $ poss = "su"
            $ refl = "sí misme"
            $ title = "gobernante"
            $ gend = "peque"

default affection = 0

label reset_chapter2:
    $ crownus_room = 0
    $ jestyn_location = 0
    $ found_jestyn = False
    $ crownus_secret_point = 0
    $ prieston_route_point = 0
    $ examinecornerwizzy = 0
    $ examinetableknighter = 0
    $ visited_wizzy = False
    $ mc_jealous = False
    $ crownus_wizzy = False
    $ jestyn_gagged = False
    $ sit_on_jestyn = False
    $ domjes = False
    $ subjes = False
