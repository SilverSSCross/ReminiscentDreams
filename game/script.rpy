# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

define th = Character("Therapist")
define mc = Character("You")
define np = Character("News of Helsinki")

# El juego comienza aquí.

label start:

    # Muestra una imagen de fondo: Aquí se usa un marcador de posición por
    # defecto. Es posible añadir un archivo en el directorio 'images' con el
    # nombre "bg room.png" or "bg room.jpg" para que se muestre aquí.

    #scene bg room

    # Muestra un personaje: Se usa un marcador de posición. Es posible
    # reemplazarlo añadiendo un archivo llamado "eileen happy.png" al directorio
    # 'images'.

    #show eileen happy

    # Presenta las líneas del diálogo.

    #e "Has creado un nuevo juego Ren'Py."

    #e "Añade una historia, imágenes y música, ¡y puedes presentarlo al mundo!"


    "Según la Teoría de las huellas Múltiples, cada vez que recuperamos un recuerdo, el registro de este mismo constituye otra memoria en sí."

    "La memoria como tal está estrechamente relacionada con las emociones de un individuo siendo que cuanto mayor impacto emocional mayor es la capacidad del recuerdo mismo."

    "Los recuerdos que más perduran en nuestro ser son aquellos que tienen que ver con emociones de mayores magnitudes, tales como la felicidad, la tristeza o el miedo."

    "Por otro lado, los traumas representan tanto amenazas en el bienestar de un individuo como a la consecuencia de estas sobre la estructura mental o la vida emocional de este mismo."

    "Los traumas emocionales a causa de sucesos ocurridos en la niñez, ya sea por estrés o miedo, pueden causar que el cerebro recuerde vívidamente estas memorias o que, por el contrario, se fragmenten o repriman para ayudar a una persona a salir hacia adelante."

    "Los individuos que sufren de traumas tienden a buscar ayuda de diversas formas. Aunque sobra decir que cada persona tiene sus propios demonios con los que luchar y que no todos son capaces de lograr la victoria frente a estos."

    "En los peores casos hablamos de problemas emocionales, dificultad en las relaciones y conductas autodestructivas que de no ser controladas pueden acompañar al individuo toda la vida……………"

    image red = "gui/red.jpg"
    
    scene red

    "{color=#732020}Fue tu culpa"

    scene black

    ""
    scene bg room

    show th

    th "¿Hoy hace bastante frio no? Incluso para esta zona de las montañas es una temperatura baja."

    mc "......"

    th "¿Quieres un poco de té para beber? Es bueno para la circulación y con este frio seguro que no sienta mal."

    mc "............"

    th "..."

    th "Has vuelto a tener pesadillas, ¿No es así?"

    mc "¿Acaso es alguna novedad?"

    th "¿De qué han sido esta vez?"

    mc "De aquel {color=#FF0000}{b}Sluagh{b}{/color}"

    th "¿Que pasaba en el sueño?"

    mc "Solo se quedaba mirándome desde la ventana mientras la arañaba y gruñía."

    th "Entonces sigue siendo ese {i}sueño recurrente{/i}."

    th "Si mal no recuerdo, estas últimas semanas han sido más constantes"

    mc "Si..."

    th "Llevas {color=#FF0000}años{/color} viniendo a mis consultas y sin embargo no siento que hayamos avanzado {color=#5F24B5}{i}nada{/i}{/color}."

    th "Reprimes tus memorias y revives los traumas que te atormentan, impidiendo que puedas superarlos."

    th "*Sigh*"

    th "Sabes, soy cliente habitual del bar de la esquina. La camarera y yo nos caemos bien. Me cuenta cosas que le pasan por allí."

    th "Cosas como que {i}Scott ha atropellado un ciervo{/i}, que {i}Lumi ha engañado a su marido con el nuevo vecino{/i}, o que {color=#FF0000}{b}TÚ{/b} le has estado dando a la bebida más de la cuenta últimamente{/color}, que ya es decir."

    mc "Métase en sus asuntos"

    th "Al principio me costaba entender el por qué seguías viniendo a mis consultas pese a lo reacio que te muestras a hablar sobre tu pasado."

    th "Ahora veo que usas la excusa de venir por terapia con tal de encontrar un pequeño momento de {color=#5CDBFF}paz{/color} en tu conciencia. Un pequeño campo {color=#5CDBFF}Eliseo{/color} dentro del {color=#5F24B5}zarzal envenenado{/color} de tu {color=#F9FF24}memoria{/color}."

    mc "..."

    th "En fin. Tenía que darte una noticia ahora que estas sobrio. Dentro de poco me jubilare y este viejo psicólogo tendrá que colgar la bata."

    mc "¿Va a abandonarme?"

    th "No puedo abandonar a un pájaro que se niega a salir de su {color=#5F24B5}jaula de espinas{/color}."

    mc "..."

    th "Te tiendo la mano una {b}última vez{/b}. Es decisión tuya si aceptarla e intentar hacer frente a aquello que lleva atormentándote desde niño"

    th "O, por el contrario, prefieres seguir viviendo en una jaula con olor a Kossu (licor finlandés con sabor a etanol puro) barato."

    menu:
        "Negarse a aceptar su mano":
            jump bad_ending
        "Aceptar su mano":
            jump new_beggining


    # Finaliza el juego:

    return

label bad_ending:
    th "Es una verdadera lástima la verdad. Eras un buen muchacho. De verdad."

    hide th
    with dissolve

    scene black
    with dissolve

    centered "Some days later...."
    with dissolve

    image news = "gui/newspaper.jpg"
    scene black
    scene news
    with dissolve

    np "Joven es encontrado en el callejón del bar del pueblo sin vida."

    np "El joven, aún sin identificar, ha sido encontrado sin vida en al lado de los contenedores de basura del bar OAKS."

    np "La policía ha declarado que el joven había sufrido un paro cardiaco causado por una sobredosis producto de numerosas sustancias entre las que se encuentran alcohol y varios estupefacientes."

    np "Los clientes habituales del bar comentan que era un borracho que frecuentaba el local a altas horas de la noche y causaba revueltas violentas."

    scene black
    with dissolve

    "A veces no es mala idea aceptar una mano ajena."

    hide narrator
    with dissolve

    centered "Bad ending 1 (The demon in the bottle)"
    with dissolve

    return
label new_beggining:
    th "Me alegra oír eso hijo."

    hide th
    with dissolve

    scene black
    with dissolve

    centered "{b}Two days Later{/b}"
    with dissolve

    scene bg room
    with dissolve

    show th
    with dissolve

    th "He traído un mapa del pueblo."

    th "Quiero que te concentres en los lugares que significaron algo para ti. Tanto los que avoquen {color=#5CDBFF}recuerdos felices{/color} como los que te inducen {color=#5F24B5}pesadillas{/color}."

    th "Vamos a intentar encontrar la raíz de tus {color=#5F24B5}males{/color} a través de tus {color=#F9FF24}recuerdos{/color}."

    th "Ahora bien."

    th "Comencemos."

    return








