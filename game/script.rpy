# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:
define th = Character("Therapist")
transform character_Base:
    xpos 0.3
    ypos 0.2
    xanchor 0.1
    yanchor 0.1
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
define mf = Character("Mefi")
define unknown = Character("???")
define ol = Character("Olive")
define ft = Character("Father?")

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
            jump house_puzzle
        "Accept the helping hand":
            jump new_beggining


    # Finaliza el juego:

    return

label bad_ending1:
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

#Bloque casa

screen casa():
    add "gui/Casa.jpg"

    imagebutton:
        idle "gui/Ventana.png"
        hover "gui/Ventana_hover.png"
        xpos 1425
        ypos 150
        action ShowMenu("ventana")
    imagebutton:
        idle "gui/Cuadro.png"
        hover "gui/Cuadro_hover.png"
        xpos 675
        ypos 225
        action ShowMenu("cuadro")
    imagebutton:
        idle "gui/Libro.png"
        hover "gui/Libro_hover.png"
        xpos 300
        ypos 900
        action ShowMenu("libro")
    imagebutton:
        idle "gui/Casa.jpg"
        hover "gui/Casa.jpg"
        action ShowMenu("empty")
    imagebutton:
        at left 
        idle "gui/Silueta_padre.png" 
        hover "gui/Silueta_padre_hover.png" 
        action ShowMenu("padre")

label house_puzzle:

    show screen casa

    image padre = "gui/Silueta_padre.png"

    show padre at left

    pause

    return

label cuadro:
    show screen casa
    "A strange painting for sure." 
    "A gentleman with a book and a pen, I think. He seems obsessed with finding something."
    jump house_puzzle

label ventana: 
    show screen casa
    "There is a snowstorm outside." 
    "I remember that one of the children from the village died in one not long ago."
    jump house_puzzle

label padre:
    show screen casa
    ft "I am the spirit that always denies. And I do so with full rights, for everything that is born deserves to be destroyed; it would be better, then, if it had never been born. Therefore, my true nature is what you call sin and destruction, in a word, Evil."
    hide narrator
    jump house_puzzle

label libro:
    $Correct_Answer = "Knowledge"
    show screen casa
    "It appears to have an inscription."
    $Answer = renpy.input("I am that which drives all thinking beings, even towards their own destruction. I am that which scholars covet and for which they would be willing to sell their souls to the devil. What am I?")
    if Answer is None:
        show screen mapa
        jump house_puzzle
    if Answer.lower() == Correct_Answer:
        jump house_lore

label empty:
    show screen casa
    jump house_puzzle


label house_lore:
    scene black
    with dissolve

    centered "The man with the big nose and the man with the long eyes."
    with dissolve

    scene bg_cuento
    with dissolve

    "Once upon a time there were two very different men."

    "One was a fat man with a large nose who lived a comfortable life." 
    
    "The other was a thin man with long eyes who lived in poverty."

    "Each of them owned a house with a garden where no flowers grew."

    "One day a devil named Mephi appeared and asked them:"

    mf "Do you want to make a deal? Your flowers will grow and the plants will sprout."

    "The man with the big nose accepted without a doubt, while the man with long eyes rejected him without hesitation."

    "Some time later, the garden of the man with the big nose burst into life like never before," 
    
    "and the garden of the man with the long eyes finally withered away."

    "The man with the long eyes wept incessantly because he was so poor that he didn't know what else to do."

    "On the other hand, the big-nosed man was ecstatic with joy as he looked at his large garden and satisfied his appetite with juicy apples that grew in it." 
    
    "That's why he didn't realize that his garden was beginning to die."

    "Once he realized it, all he could do was sob in a withered, lifeless garden."

    "The man with the big nose wished he had never made a pact with the devil."

    "Meanwhile, the man with the long eyes was starving." 
    
    "He wished he had made a pact with the devil back then."

    mf "I see, let's make a deal."
    
    "Said the devil."

    scene black
    with dissolve

    "Tell me. Would you have taken the deal?"

    menu:
        "Yes":
            pass
        "No":
            pass
    
    "It really is irrelevant."

    "We all end up regretting the things we don't do."

    "You come back to reality."

    return

#Fin bloque casa

label school_lore:
    scene bg_escuela
    with dissolve

    "You have a vague memory of this place."

    show unknown
    with dissolve

    unknown "Are you daydreaming again?"

    unknown "Hey. I'm talking to you."
    
    "The voice comes from a boy your age."
    
    "It's your friend Olive."

    show ol
    
    "You nod your head and make a small grimace to let him know you're listening."

    ol "As I was saying..."

    ol "It's not very common for people to approach me."

    ol "That's because I was abandoned and stuff."

    ol "They treat me like I'm a pest."

    ol "But I plan to find my mother and we'll clear this up."

    ol "No mother would abandon her child."

    ol "I'm sure she had her reasons for just disappearing."
    
    "You don't know what expression to put on your face when you hear those words."
    
    "You're not sure whether to feel sorry for him or be happy that he still has hope inside him after everything that's happened in his life."

    ol "I'm sure it's nice to have a full table."

    hide ol

    scene black
    
    "..."

    scene red

    centered "*CRACK*"

    "..."

    "You feel as if something has broken."
    
    "Something in that sentence causes a deep discomfort within you."
    
    "There is apparently nothing wrong with Olive's sentence."
    
    "But something grates on your mind when you hear it."
    
    "You feel as if it burns you to hear it."
    
    "It irritates you, in fact."

    "Part of you wants to ⫣⊫⫣⊫⫣⊫⫣⊫⫣⊫⫣l͞⊫⫣⊫"

    scene black
    
    "..."
    
    "..."

    scene bg_escuela

    "You calm down."
    
    "You don't understand what happened to you."
    
    "You whisper a melody that was stored in your subconscious."
    
    "(Insert melody that is the lake puzzle solution)"
    
    "The ripples of memory fade like waves in the water."

    "You return to reality."

    return














