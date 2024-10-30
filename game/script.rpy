init python:
    import random
# Definición de personajes
define Ren = Character('Ren Edward', color='#75eeff')
define Yui = Character('Yui', color='#e175ff')
define Narrador = Character('Narrador', color='#ff2200')
define PersonajePrincipal = Character('Yo', color='#000000')

# Imágenes de los personajes
image RenImage = "sm1_sensei_angrylaugh.png"
image YuiImage = "sf1_outfit1_angrylaugh.png"

# Primera escena
label start:
    # Imágenes de fondo
    image City1 = 'Downtown 2 Afternoon.png'
    image City2 = 'Downtown 2 Day.png'

    scene City1
    Narrador "No esperes mucho de esta historia"
    Narrador "No siempre se puede todo"
    Narrador "Pero no te deprimas anda"
    Narrador "Haz lo que veas conveniente"

    # Segundo diálogo
    play music "audio/K-ON! OST - Happy languidness.mp3"
    with fade
    scene City2

    $ dialogs = [
        'Qué tal estás',
        'Hola, buenas tardes',
        'Qué día, ¿no?...',
        '¡Mucho gusto!',
        '¿Cómo te encuentras?'
    ]

    $ randomDialog = random.choice(dialogs)
    Ren "[randomDialog]"

    with fade
    show RenImage at right
    Ren "Soy Ren Edward"
    Ren "La oficina queda cruzando la calle"

    show YuiImage at left
    Yui "¡Hola Ren!"
    Yui "¿Hablabas con el nuevo?"
    Ren "Sí, preséntate ante él."
    Yui "Hola, mi nombre es Yui Mikura"
    Yui "Soy la asistente del PM en la oficina"
    Yui "Si tienes alguna duda, házmelo saber !!!!!!"
    stop music fadeout 1.0

    hide YuiImage
    with dissolve

    show RenImage at center
    Ren "Aca entre nos, ella es un poco molesta, a veces..."
    queue music "audio/Madoka The Cáncer Song (Official Music Vídeo).mp3"
    Ren "Pero venga, no digas más de esto, ¿vale?"
    PersonajePrincipal "(Que personas mas raras....)"
    Ren "Al parecer los que son de rh son unos desquiciados en muchos aspectos"
    Ren "Auqnue conozco a yui desde la primearia"
    Ren "la carrera de psicologia no le hizo bien...."
    Narrador "Hubo un silencion algo incomodo despues de esa oracion"
    Ren "en fin no hay que perder mas el tiempo"
    Ren "Sigueme que te presentare al jefe y el resto del equipo"
    Ren "Por cierto sosten esta hoja la usaras despues"
    play sound "audio/sonidos sfx/Papel (5).mp3"
    PersonajePrincipal "*Agarra el papel sin leer el contenido*"
    PersonajePrincipal "(algo me dice que tengo que ver este papel antes de que sea demasiado tarde)"
    Ren "Anda vamos!"

    Ren "Por cierto, ¿Te llamabas jorge o George?"
    menu:
        "Si es jorge":
            jump Jorge
        "No cabron es George":
            jump George
label George:
    Ren "Carajo Lo siento, te debo un cafe, no es normal que me equivoque te pido disculpas denuevo" 
    PersonajePrincipal "(Mejor mamame el huevo...)"
    Ren "Ya es tarde hay que irnos George"
    