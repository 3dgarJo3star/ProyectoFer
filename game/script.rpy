init python:
    import random

# primer personaje 
define Ren = Character('Ren Edward', color='#75eeff')
image RenImage = "sm1_sensei_angrylaugh.png"

# segundo personaje
define Yui = Character('Yui', color='#e175ff')
image YuiImage = "sf1_outfit1_angrylaugh.png"

# narrador
define Narrador = Character('Narrador', color='#ff2200')

# primera escena 
label start:
    image City1 = 'Downtown 2 Afternoon.png'
    scene City1
    Narrador "No esperes mucho de esta historia"
    Narrador "No siempre se puede todo"
    Narrador "Pero no te deprimas anda"
    Narrador "Haz lo que veas conveniente"

    # segundo dialogo
    with fade
    image City2 = 'Downtown 2 Day.png'
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
    show RenImage
    Ren "Soy Ren Edward"
    Ren "La oficina queda cruzando la calle"

    hide RenImage
    with dissolve
    show YuiImage
    Yui "¡Hola Ren!"
    Yui "¿Hablabas con el nuevo?"

    hide YuiImage
    with dissolve
    show RenImage
    Ren "Sí, preséntate ante él."

    hide RenImage
    with dissolve
    show YuiImage
    Yui "Hola mi nombre es Yui Mikura"
    Yui "soy la asistente del PM en la oficina"
    Yui "Si tienes alguna duda, hasmelo saber !!!!!!"


    