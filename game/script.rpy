# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:
define th = Character("Therapist")
transform character_Base:
    xpos 0.65
    ypos 0.87
    xanchor 1.0
    yanchor 1.0
    zoom 3
image th:
    "gui/PsicologoFrame1.png"
    pause 4

    "gui/PsicologoFrame2.png"
    pause 0.5

    "gui/PsicologoFrame1.png"
    pause 0.5

    repeat
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


    "According to the Multiple Trace Theory, every time we retrieve a memory, the record of that memory constitutes another memory in itself."

    "Memory is closely related to an individual's emotions, since the greater the emotional impact, the greater the capacity for recall itself."

    "The memories that linger longest in our minds are those associated with powerful emotions, such as happiness, sadness or fear."

    "On the other hand, traumas represent both threats to an individual's well-being and consequences for their mental structure or emotional life."

    "Emotional trauma caused by events that occurred in childhood, whether due to stress or fear, can cause the brain to vividly remember these memories or, conversely, to fragment or repress them to help a person move forward."

    "Individuals suffering from trauma tend to seek help in various ways. Needless to say, each person has their own demons to fight, and not everyone is capable of overcoming them."

    "In the worst cases, we are talking about emotional problems, relationship difficulties and self-destructive behaviours which, if left unchecked, can accompany the individual throughout their life……………"

    image red = "gui/red.jpg"
    
    scene red

    "{color=#732020}It was your fault"

    scene black

    ""

    image TherapyBg = "gui/TherapyBg.jpg"

    scene TherapyBg

    show th at character_Base

    th "It's quite cold today, isn't it? Even for this area of the mountains, it's a low temperature."

    mc "......"

    th "Would you like some tea? It's good for your circulation, and with this cold weather, it certainly won't do you any harm."

    mc "............"

    th "..."

    th "You've been having nightmares again, haven't you?"

    mc "Is that anything new at all?"

    th "What were they about this time?"

    mc "Of that {color=#FF0000}{b}Sluagh{b}{/color}."

    th "What happened in the dream?"

    mc "He just stood there watching me from the window while he scratched it and growled."

    th "So it's still that {i}recurring dream{/i}."

    th "If I remember correctly, these last few weeks have been more consistent."

    mc "Yeah..."

    th "You have been coming to my consultations for {color=#FF0000}years{/color}, and yet I don't feel that we have made {color=#5F24B5}{i}any progress at all{/i}{/color}."

    th "You repress your memories and relive the traumas that torment you, preventing you from overcoming them."

    th "*Sigh*"

    th "You know, I'm a regular at the bar on the corner. The barmaid and I get on well. She tells me things that happen there."

    th "Things like {i}Scott running over a deer{/i}, {i}Lumi cheating on her husband with the new neighbour{/i}, or {color=#FF0000}{b}YOU{/b} drinking more than you should lately{/color}, which is saying something."

    mc "Mind your own buisness."

    th "At first, I found it difficult to understand why you kept coming to my consultations despite your reluctance to talk about your past."

    th "Now I see that you use the excuse of coming for therapy in order to find a little moment of {color=#5CDBFF}peace{/color} in your conscience. A small {color=#5CDBFF}Elysian field{/color} within the {color=#5F24B5}poisoned brambles{/color} of your {color=#F9FF24}memory{/color}."

    mc "..."

    th "Anyway. I had to tell you this now that you're sober. I'll be retiring soon, and this old psychologist will have to hang up his coat."

    mc "Are you abandoning me?"

    th "I cannot abandon a bird that refuses to leave its {color=#5F24B5}cage of thorns{/color}."

    mc "..."

    th "I am extending my hand to you one last time."

    th "It is your decision whether to accept it and try to face what has been tormenting you since childhood."

    th "Or, on the contrary, would you rather continue living in a cage that smells like cheap Kossu? (a Finnish liqueur that tastes like pure ethanol)"

    menu:
        "Refuse to accept the therapy":
            jump bad_ending
        "Accept the helping hand":
            jump new_beggining


    # Finaliza el juego:

    return

label bad_ending:
    th "It's a real shame, honestly. You were a good kid. Truly."

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

    np "Young man found dead in the alley behind the village bar."

    np "The young man, who has not yet been identified, was found dead next to the rubbish bins outside the OAKS bar."

    np "The police have stated that the young man suffered a cardiac arrest caused by an overdose of numerous substances, including alcohol and various narcotics."

    np "Regular customers at the bar say he was a drunk who frequented the premises late at night and caused violent disturbances."

    scene black
    with dissolve

    "Sometimes it's not a bad idea to accept a helping hand."

    hide narrator
    with dissolve

    centered "Bad ending 1 (The demon in the bottle)"
    with dissolve

    return
label new_beggining:
    th "I'm glad to hear that, son."

    hide th
    with dissolve

    scene black
    with dissolve

    centered "{b}Two days Later{/b}"
    with dissolve

    scene TherapyBg
    with dissolve

    show th at character_Base
    with dissolve

    th "I have brought a map of the village."

    th "I want you to focus on the places that meant something to you. Both those that bring back {color=#5CDBFF}happy memories{/color} and those that induce {color=#5F24B5}nightmares{/color}."

    th "We will try to find the root of your {color=#5F24B5}problems{/color} through your {color=#F9FF24}memories{/color}."

    th "Alright then."

    th "Let's get this started."

    return








