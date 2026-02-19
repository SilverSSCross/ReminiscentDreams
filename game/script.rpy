
# Coloca el código de tu juego en este archivo.
#Colores solidos personalizados
image dred = Solid("#420505")
# Declara los personajes usados en el juego como en el ejemplo:
default persistent.casaDesbloqueada = False
default persistent.escuelaDesbloqueada = False
default persistent.lagoDesbloqueado = False
default persistent.orfanatoDesbloqueado = False

#Bloque if para cada lore

#if persistent.casaDesbloqueada == False:
#    $persistent.casaDesbloqueada = True
#    call screen mapa 
#elif persistent.casaDesbloqueada == True:
#    return

#Fin Bloque if para cada lore

define th = Character("Therapist")
transform character_Base:
    xpos 0.3
    ypos 0.2
    xanchor 0.1
    yanchor 0.1
    zoom 3
transform down:
    xpos 0.4
    ypos 0.3
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
define stranger = Character("???")
define kid = Character("Student")
define Profe = Character("Teacher")
image unkown:
    "gui/Ojos1.jpg"
    pause 0.2

    "gui/Ojos2.jpg"
    pause 0.2

    "gui/Ojos3.jpg"
    pause 0.2

    "gui/Ojos4.jpg"
    pause 0.2

    "gui/Ojos5.jpg"
    pause 0.2

    "gui/Ojos6.jpg"
    pause 0.2

    "gui/Ojos7.jpg"
    pause 0.2

    "gui/Ojos8.jpg"
    pause 0.2

    "gui/Ojos9.jpg"
    pause 0.2

    "gui/Ojos10.jpg"
    pause 0.2

    repeat

define ol = Character("Olive")
define ft = Character("Father?")
define sl = Character("Sluagh")
image SluaghFrame1 = "gui/SluaghFrame1.png"

image SluaghFrame2 = "gui/SluaghFrame2.png"
define om = Character("Old Man")
image om:
    "gui/lago/Sprites/ImagenViejo.png"
define ym = Character("Young Man")
image ym:
    "gui/lago/Sprites/ImagenJoven2.png"
define kidA = Character("Kid 1")
define kidB = Character("Kid 2")
define kidC = Character("Kid 3")
# El juego comienza aquí.

label start:
    stop music 
    camera:
        perspective True 

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


    #Zona inicio pruebas
    jump orfanato
    ########################################


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

    play music reloj 

    th "It's quite cold today, isn't it? Even for this area of the mountains, it's a low temperature."

    mc "......"

    th "Would you like some tea? It's good for your circulation, and with this cold weather, it certainly won't do you any harm."

    mc "............"

    th "..."

    th "You've been having nightmares again, haven't you?"

    mc "Is that anything new at all?"

    th "What were they about this time?"

    mc "Of that {color=#FF0000}{b}Sluagh{/b}{/color}."

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
            jump bad_ending1
        "Accept the helping hand":
            jump new_beggining
    # Finaliza el juego:

    pause

    return

label bad_ending1:
    th "It's a real shame, honestly. You were a good kid. Truly."
    stop music

    hide narrator

    hide th
    with dissolve

    scene black
    with dissolve

    centered "Some days later...."
    with dissolve

    play sound sonidoperiodico
    play music undiamas

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

    stop music

    return

label new_beggining:
    th "I'm glad to hear that, son."
    stop music

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

    #Llamar al mapa
    play sound sonidoperiodico


    call screen mapa

    #return

#Bloque casa

screen casa():
    add "gui/House/Puzzle/Casa.jpg"

    imagebutton:
        idle "gui/House/Puzzle/Ventana.png"
        hover "gui/House/Puzzle/Ventana_hover.png"
        xpos 0.341
        ypos 0.125
        action Jump("ventana")
    imagebutton:
        idle "gui/House/Puzzle/Cuadro.png"
        hover "gui/House/Puzzle/Cuadro_hover.png"
        xpos 0.752
        ypos 0.216
        action Jump("cuadro")
        focus_mask True
    imagebutton:
        idle "gui/House/Puzzle/Libro.png"
        hover "gui/House/Puzzle/Libro_hover.png"
        xpos 0.393
        ypos 0.809
        action Jump("libro")
        focus_mask True
    imagebutton:
        at left 
        idle "gui/House/Puzzle/Silueta_padre.png" 
        hover "gui/House/Puzzle/Silueta_padre_hover.png" 
        action Jump("padre")
        focus_mask True

label house_puzzle:

    mc "Im going home."

    scene black
    with dissolve

    stop music
    stop audio
    stop sound

    play sound nieve loop
    label puzzle_loop:
        window hide
        call screen casa
        jump puzzle_loop

    



label cuadro:
    show screen casa
    window show
    "A strange painting for sure. \nA gentleman with a book and a pen, I think. He seems obsessed with finding something."
    jump puzzle_loop

label ventana: 
    show screen casa
    window show
    "There is a snowstorm outside. \nI remember that one of the children from the village died in one not long ago."
    jump puzzle_loop

label padre:
    show screen casa
    window show
    ft "I am the spirit that always denies. And I do so with full rights, for everything that is born deserves to be destroyed; it would be better, then, if it had never been born. Therefore, my true nature is what you call sin and destruction, in a word, Evil."
    jump puzzle_loop

label libro:
    $Correct_Answer = "Knowledge"
    show screen casa
    "It appears to have an inscription."
    $Answer = renpy.input("I am that which drives all thinking beings, even towards their own destruction. I am that which scholars covet and for which they would be willing to sell their souls to the devil. What am I?")
    if Answer != Correct_Answer:
        show screen casa
        mc "No, I don't think that will do anything, gotta find more information. \nCould there be anything useful here?"
        window hide
        jump puzzle_loop
    if Answer == Correct_Answer:
        hide screen casa
        hide th
        hide TherapyBg
        hide padre
        scene black
        stop sound
        jump house_lore


label house_lore:

    image escena1 = "gui/House/Lore/Frame_intro_cuento.jpg"
    image escena2 = "gui/House/Lore/Frame_jardines_cuento.jpg"
    image escena3 = "gui/House/Lore/Frame_intro_mefi.jpg"
    image escena4 = "gui/House/Lore/Frame_trato_mefi.jpg"
    image escena5 = "gui/House/Lore/Frame_jardines_cuento2.jpg"
    image escena6 = "gui/House/Lore/Frame_jardines_cuento3.jpg"
    image escena7 = "gui/House/Lore/Frame_jardines_cuento4.jpg"
    image finalMefi = "gui/House/Lore/Frame_final_mefi.jpg"

    scene black
    with dissolve

    stop music
    play music psalm loop

    centered "The man with the big nose and the man with the long eyes."
    with dissolve

    scene escena1
    with dissolve

    "Once upon a time there were two very different men."

    "One was a fat man with a large nose who lived a comfortable life." 
    
    "The other was a thin man with long eyes who lived in poverty."

    scene escena2

    hide escena1

    "Each of them owned a house with a garden where no flowers grew."

    scene escena3

    hide escena2

    "One day a devil named Mephi appeared and asked them:"

    mf "Do you want to make a deal? Your flowers will grow and the plants will sprout."

    scene escena4

    hide escena3

    "The man with the big nose accepted without a doubt, while the man with long eyes rejected him without hesitation."

    scene escena5

    hide escena4

    "Some time later, the garden of the man with the big nose burst into life like never before," 
    
    "and the garden of the man with the long eyes finally withered away."

    scene escena6

    hide escena5

    "The man with the long eyes wept incessantly because he was so poor that he didn't know what else to do."

    "On the other hand, the big-nosed man was ecstatic with joy as he looked at his large garden and satisfied his appetite with juicy apples that grew in it." 
    
    "That's why he didn't realize that his garden was beginning to die."

    scene escena7

    hide escena6

    "Once he realized it, all he could do was sob in a withered, lifeless garden."

    "The man with the big nose wished he had never made a pact with the devil."

    "Meanwhile, the man with the long eyes was starving." 
    
    "He wished he had made a pact with the devil back then."

    scene finalMefi

    hide escena7

    mf "I see, let's make a deal."
    
    "Said the devil."

    scene black
    with dissolve

    stop music

    hide finalMefi

    "Tell me. Would you have taken the deal?"

    menu:
        "Yes":
            pass
        "No":
            pass
    
    "It really is irrelevant."

    "We all end up regretting the things we don't do."

    "You come back to reality."

    call screen mapa

    #return

#Fin bloque casa


#bloque escuela

default Taquilla_Open = False 
default Armario_Open = False
default Profesora_tip = False

label school_puzzle:

    mc "I'm gonna check something in my old school"

    scene black
    with dissolve

    stop music
    stop audio
    stop sound
    
    
    label scene_escuela:
        window hide
        call screen escuela
        with dissolve
        jump scene_escuela
    
    label scene_pasillo:
        window hide
        call screen pasillo
        with dissolve
        jump scene_pasillo
    
    label scene_clase:
        hide screen interior_armario_puzzle
        window hide
        call screen clase
        with dissolve
        jump scene_clase
    
    label scene_salir:
        window hide
        call screen mapa
        with dissolve

label niño:
    show screen pasillo
    kid "Hey you. Wanna know something?"
    menu:
        "Yeah, sure":
            kid "Ralf told me that Eeli is getting a lot of great grades, it's weird coming from the laziest kid in the class."
            kid "So he followed him in the recess \nand he found out that the teacher gives him chores in her house in exchange of getting good grades."
            kid "Do you think i could do it too?"
            mc "I don't think you should, but you gave me an idea, now go kid."
            $Profesora_tip = True
            hide screen pasillo
            jump scene_pasillo
        "Get lost kid":
            hide screen pasillo
            jump scene_pasillo

label profesora:
    show screen clase
    Profe "What are you doing here? Shouldn't you be somewhere else wasting someone else time?"
    menu:
        "Not really. Why can't i unlock my locker? I want some stuff that I left there":
            Profe "It's not your locker anymore silly, besides, it's been inhabilitated and the code has been changed, \n I don't know what the hell you have in there for that, and I ain't giving you the code."
        "Sure, I don't even know why I'm talking to you":
            Profe "Jerk."
        "Like you waste the time of your students doing stuff\n you don't want to do in exchange for an easy A++?" if Profesora_tip == True:
            Profe "Wait. How do YOU know!?"
            Profe "Damn big mouth!"
            Profe "Ok ok, the locker's sheet code is in the cupboard at mi right"
            Profe "The code is 3516"
            Profe "Now go!\n AND DON'T YOU DARE TELL ANYONE WHAT WE KNOW OR YOU WILL REGRET IT!"
    hide screen clase
    jump scene_clase

label scene_armario:
    if Armario_Open == True:
        call screen armario_abierto
        with dissolve

        pause
    if Armario_Open == False:
        call screen armario_cerrado
        with dissolve

        pause

label scene_taquilla:
    if Taquilla_Open == True:
        call screen taquilla_abierta
        with dissolve

        pause
    if Taquilla_Open == False:
        call screen taquilla_cerrada
        with dissolve

        pause

label puzle_armario:
    show screen armario_cerrado

    mc "It needs a code"

    $ Answer = renpy.input("Code: ", length=4)
    if Answer == "3516":
        mc "Got it!"
        $ Armario_Open = True
    else:
        mc "Damn it! Maybe the code is somewhere else."
    hide screen armario_cerrado
    jump scene_armario 

label puzle_taquilla:
    show screen taquilla_cerrada
    
    mc "It needs a code"

    $Answer = renpy.input("Code: ")
    if Answer != "7531":
        show screen taquilla_cerrada
        mc "Damn it! \n maybe the code is somewhere around here."
        hide screen taquilla_cerrada
        jump scene_taquilla
        
        
    if Answer == "7531":
        show screen taquilla_abierta
        mc "Got it!"
        $Taquilla_Open = True
        hide screen taquilla_cerrada
        hide screen taquilla_abierta
        jump scene_taquilla    

label interior_armario:
    show screen interior_armario_puzzle
    with dissolve
    pause
    

label foto:
    mc "Wait a minute, this picture reminds me of something....."
    jump school_lore


screen escuela():
    add "gui/School/Puzzle/Entrada.jpg"

    imagebutton:
        xpos 0.797
        ypos 0.246
    
        idle "gui/School/Puzzle/pasillo.png"
        hover "gui/School/Puzzle/pasillo_hover.png"
        action Jump("scene_pasillo")
    imagebutton:
        xpos 0.45
        ypos 0.7
    
        idle "gui/School/Puzzle/FlechaAbajo.png"
        hover "gui/School/Puzzle/FlechaAbajo_hover.png"
        focus_mask True
        action Jump("scene_salir")


screen pasillo():
    add "gui/School/Puzzle/Pasillo.jpg"

    imagebutton:
        xpos 0.452
        ypos 0.435
        idle "gui/School/Puzzle/taquilla.png"
        hover "gui/School/Puzzle/taquilla_hover.png"
        action Jump("scene_taquilla")
    imagebutton:
        xpos 0.342
        ypos 0.299
        idle "gui/School/Puzzle/clase.png"
        hover "gui/School/Puzzle/clase_hover.png"
        action Jump("scene_clase")
    imagebutton:
        xpos 0.45
        ypos 0.7
    
        idle "gui/School/Puzzle/FlechaAbajo.png"
        hover "gui/School/Puzzle/FlechaAbajo_hover.png"
        focus_mask True
        action Jump("scene_escuela")
    imagebutton:
        xpos 0.7
        ypos 0.5
        focus_mask True
        idle Transform("gui/School/Puzzle/SiluetaNiño.png", zoom=0.75)
        hover Transform("gui/School/Puzzle/SiluetaNiño_hover.png", zoom=0.75)
        action Jump("niño")

screen taquilla_cerrada():
    add "gui/School/Puzzle/Taquilla_Cerrada.jpg"

    imagebutton:
        xpos 0.47
        idle "gui/School/Puzzle/PuertaTaquilla.png"
        hover "gui/School/Puzzle/PuertaTaquilla_hover.png"
        action Jump("puzle_taquilla")
    imagebutton:
        xpos 0.1
        ypos 0.4
    
        idle "gui/School/Puzzle/FlechaIzquierda.png"
        hover "gui/School/Puzzle/FlechaIzquierda_hover.png"
        focus_mask True
        action Jump("scene_pasillo")

screen taquilla_abierta():
    add "gui/School/Puzzle/Taquilla_Abierta.jpg"

    imagebutton:
        xpos 0.505
        ypos 0.4
        idle "gui/School/Puzzle/Imagen_lore.png"
        hover "gui/School/Puzzle/Imagen_Lore.png"
        focus_mask True
        action Jump("foto")
    imagebutton:
        xpos 0.1
        ypos 0.4
    
        idle "gui/School/Puzzle/FlechaIzquierda.png"
        hover "gui/School/Puzzle/FlechaIzquierda_hover.png"
        focus_mask True
        action Jump("scene_pasillo")

screen clase():
    add "gui/School/Puzzle/Clase.jpg"

    imagebutton:
        xpos 0.79
        ypos 0.22
        idle "gui/School/Puzzle/Armario.png"
        hover "gui/School/Puzzle/Armario_hover.png"
        action Jump("scene_armario")
    imagebutton:
        xpos 0.914
        ypos 0.197
        idle "gui/School/Puzzle/puerta.png"
        hover "gui/School/Puzzle/puerta_hover.png"
        action Jump("scene_pasillo")
    imagebutton:
        at left
        ysize 0.7
        idle "gui/School/Puzzle/SiluetaProfesora.png"
        hover "gui/School/Puzzle/SiluetaProfesora_hover.png"
        focus_mask True
        action Jump("profesora")

screen armario_cerrado():
    add "gui/School/Puzzle/Armario_Cerrado.jpg"

    imagebutton:
        xpos 0.307
        ypos 0.3521
        idle "gui/School/Puzzle/PuertaArmario.png"
        hover "gui/School/Puzzle/PuertaArmario_hover.png"
        action Jump("puzle_armario")
    imagebutton:
        xpos 0.8
        ypos 0.4
    
        idle "gui/School/Puzzle/FlechaDerecha.png"
        hover "gui/School/Puzzle/FlechaDerecha_hover.png"
        focus_mask True
        action Jump("scene_clase")

screen armario_abierto():
    add "gui/School/Puzzle/Armario_Abierto.jpg"

    imagebutton:
        xpos 0.315
        ypos 0.35
        idle "gui/School/Puzzle/InteriorArmario.png"
        hover "gui/School/Puzzle/InteriorArmario_hover.png"
        action Jump("interior_armario")
    imagebutton:
        xpos 0.8
        ypos 0.4
    
        idle "gui/School/Puzzle/FlechaDerecha.png"
        hover "gui/School/Puzzle/FlechaDerecha_hover.png"
        focus_mask True
        action Jump("scene_clase")

screen interior_armario_puzzle():
    add "gui/School/Puzzle/InteriorArmarioPuzzle.jpg"

    imagebutton:
        xpos 0.45
        ypos 0.7
    
        idle "gui/School/Puzzle/FlechaAbajo.png"
        hover "gui/School/Puzzle/FlechaAbajo_hover.png"
        focus_mask True
        action Jump("scene_clase")
    draggroup:
        drag:
            drag_name "pieza1"
            child Transform("gui/School/Puzzle/Pieza1.png", zoom=0.2)
            draggable True
            droppable False
            xpos 100 ypos 200
            focus_mask True
        drag:
            drag_name "pieza2"
            child Transform("gui/School/Puzzle/Pieza2.png", zoom=0.2)
            draggable True
            droppable False
            xpos 100 ypos 200
            focus_mask True
        drag:
            drag_name "pieza3"
            child Transform("gui/School/Puzzle/Pieza3.png", zoom=0.2)
            draggable True
            droppable False
            xpos 100 ypos 200
            focus_mask True
        drag:
            drag_name "pieza4"
            child Transform("gui/School/Puzzle/Pieza4.png", zoom=0.2)
            draggable True
            droppable False
            xpos 100 ypos 200
            focus_mask True
        drag:
            drag_name "pieza5"
            child Transform("gui/School/Puzzle/Pieza5.png", zoom=0.2)
            draggable True
            droppable False
            xpos 100 ypos 200
            focus_mask True
        drag:
            drag_name "pieza6"
            child Transform("gui/School/Puzzle/Pieza6.png", zoom=0.2)
            draggable True
            droppable False
            xpos 100 ypos 200
            focus_mask True

label school_lore:
    image bg_escuela = "gui/School/puzzle/Pasillo.jpg"
    scene bg_escuela
    with dissolve

    "You have a vague memory of this place."

    image stranger = "gui/School/puzzle/SiluetaNiño.png"
    show stranger at down
    with dissolve

    stranger "Are you daydreaming again?"

    stranger "Hey. I'm talking to you."
    
    "The voice comes from a boy your age."
    
    "It's your friend Olive."

    hide stranger

    image ol = "gui/School/Lore/SiluetaOlive.png"
    show ol at down
    
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
    
    ".."
    
    "..."

    scene bg_escuela

    "You calm down."
    
    "You don't understand what happened to you."
    
    "You whisper a melody that was stored in your subconscious."
    
    "(Insert melody that is the lake puzzle solution)"
    
    "The ripples of memory fade like waves in the water."

    "You return to reality."

    call screen mapa

#fin bloque escuela


###################################################################################################################################


#Bloque lago
#Backgrounds
#General
image bg lago_gen = "gui/lago/Imagenes/barco_final_pixel.png"
image cielo_recortado=Crop((0,0,200,150), "gui/lago/Imagenes/barco_final_pixel.png")
image bg lago_puzle_mview="gui/lago/Imagenes/puzle_view_pixel.png"
image bg lago_cielo="gui/Cielo.png"
#Puzle

#Lore
image bg pecho_sluagh = "gui/Pecho_Sluagh.png"
image bg coche_lore="gui/lago/coche_pixelado_2.jpg"
image bg nieve_lore="gui/lago/nieve_lore_pixelated.png"
image bg nieve_lore2="gui/lago/nieve_lore_pixelated2.png"
image bg habitacion_lago_lore="gui/lago/habitacion_lore_pixel.png"
image bg lore_sluagh_bg="gui/lago/presentacion_sluagh_lago_pixel.png"
image bg bad_ending_lago="gui/lago/BadEndingLago.jpg"
#Definir cualquier funcion que se quiera usar


label lago:
    play music "audio/Insectos.mp3" fadein 1.0
    scene bg lago_gen with fade:
        xsize config.screen_width
        ysize config.screen_height
        
    #Se añade la imagen de fondo del lago
    #Interactuable Cielo, Barcaza, lago (Puzle Musical)
    #Aprovecha que Jesus hizo algo similar en la casa para hacer los objetos interactuables
    call screen lago_main
        
    

label lago_cielo:
    #Imagen es la escena base de llegada a la zona
    "The sky is completely clear"
    "Blue like this rarely appears on the sky accentuating it's beauty"
    pause 1.5
    "It really makes me want to vomit"
    call screen lago_main

label lago_barcaza:
    #Imagen es la escena base de llegada a la zona
    "A small boat that they use on the town to take a stroll through the lake"
    "I remember one time that a teenager stole it to commit suicide"
    "It gave the place a picturesque touch to such a vulgar place"
    "I appreciate it"
    call screen lago_main

label lago_puzle_zona:
    #Imagen directamente mirando al lago
    scene bg lago_puzle_mview with fade:
        xsize config.screen_width
        ysize config.screen_height


    stop music
    stop audio
    stop sound

    
    "The waves that form on the lake resembles the cords of a medoly. I recall hearing this melody somewhere before..."
    #Se define la solucion del puzle musical
    $ lago_solution=["7","7","1","2","3","4","4"]
    #Se define lo que introduce el jugador
    $ lago_player_input=[]
    $ lago_player_visual=[]
        #Se inicializa un loop
    label .loop:
        call screen lago_puzle
        if lago_player_input == lago_solution:
            stop music fadeout 1.0
            jump lago_lore
        else:
            $ lago_player_input=[]
            jump .loop

label lago_lore:
    #Inicio Recuerdo
    #En negro todo esto probablemente
    scene black
    with fade


    #Audio de coche probablemente
    #Introduce como audio LluviaCoche
    play music "audio/LluviaCoche.mp3" fadein 1.0
    "A mechanic noise is heard. The noise of a car"
    "The noise that is heard when sitting inside of a car"
    "An elder and a man sit on the front seats"
    "No face was identifiable from the backseats"
    #Mediana edad
    # show ym at left
    ym "Think that this is a good one boss?"
    #Viejo    
    # show om at right
    om "Im sure. Now shut up, i don't pay you to talk"
    # hide ym
    # hide om

    "Silence filled the car, only interrupted with the ocasional groan that the elder made from coughing, 
    probably from a respiratory disease"
    "Or maybe it was simply from the age"
    "I guess that is irrelevant"
    "The route continued for a long time. It was long like the night on the north and heavy like the years that everybody goes through"

    "*CRUNCH*"
    #Tendria que poner una imagen aqui
    #Hay que hacer una CG de eso
    
    scene bg coche_lore with fade:
        xsize config.screen_width
        ysize config.screen_height


    #Mediana edad
    ym "Ah, you are finally awake" 
    "That was said by the young man with a joy that did not correlate with the somber expression he had" 
    #Son dialogos que no dice ninguno. Son narracion
    ym "From now on we will get along, okay?"
    "..."
    "..."
    "..."
    stop music fadeout 1.0
    #Aqui se corta la CG del coche y se pasa a fundido a negroo o bien al cielo o alguna cosa por el estilo para enfatizar el dialogo
    scene black with fade


    "The is no such thing as love"
    "Therefore there is no sadness"
    "Without love we avoid getting hurt..."
    "Why do we expose ourselves to suffering then?"

    "..."
    "..."
    "..."

    scene black
    with dissolve
    
    #Borroso?
    #O bien borroso o buscar alguna imagen de nieve y pixelarla
    play music "audio/nieve.mp3"
    play sound "audio/pasosnieve.mp3"
    scene bg nieve_lore with fade:
        xsize config.screen_width
        ysize config.screen_height

    "The ice chilled me to the bone preventing me from breathing right"
    "I don't know how long i walked without a specific direction on mind"
    "The only thing i remember is a word"
    "Move"
    "Move"
    "{b}MOVE!!!{/b}"
    stop sound fadeout 2.0
    
    "My legs wouldn't respond and my eyes began to redden due to blood clotting"
    "On the contrary of what it could look like, i felt warm and the soft touch of death whispering on my ear was kind"
    "I blacked out on that moment"
    
    scene black with fade

    "And a light appeared before me"

    scene bg nieve_lore2 with fade:
        xsize config.screen_width
        ysize config.screen_height
        
    "It was a small lamp, but for me it was as blinding as a supernova"
    stop music fadeout 3.0
    #Se prodria llegar a interpretar o busco otra?

    scene bg habitacion_lago_lore with fade:
        xsize config.screen_width
        ysize config.screen_height
    "An unkown ceiling was what i saw"
    "Moving my gaze i saw a man and a woman in front of me"

    "{b}IRRELEVANT{/b}"

    #Poner las siluetas de personas (recicla alguna existente)



    "I don't get to distinguish their faces"
    "I think they said the words 'look after'"
    
    "{b}IRRELEVANT{/b}"
    scene black with fade
    "Time passed. I don't know how much. Maybe a couple of months, maybe some years"
    "I guess people could say i was happy"

    "..."
    "..."
    "..."
    
    "Atleast, that's what people thought"
    "Happiness is a wrong concept"
    "How could someone be happy in such a cruel world where everything is destined to die?"

    "..."
    "..."
    "..."

    scene black
    with dissolve
    #Fin Recuerdo

    "Waves from the past are interrupted with and uproar"

    "{b}RETRIBUTION!!!{/b}"

    #Imagen de Sluagh
    scene bg lore_sluagh_bg with fade:
        xsize config.screen_width
        ysize config.screen_height

    "The birds stopped singing and the wind stopped blowing"
    #Para cualquier audio que este puesto
    stop music
    "Time feels as if it has stopped with no explanation"
    "You feel a pressure on the chest and hear an cacophony that felt both strange and familiar at the same time"
    "You see someone far away slowly getting out of the lake"
    #sonido 
    "Something so repulsive that the first thing that comes to mind is the image of the creature that you read about on irish mythology, a Sluagh, a cursed spirit that chases the living without rest"
    "Panic gets to you the moment you decypher what is infront of you"
    #Introduce al Sluagh, preferiblemente el segundo frame
    show SluaghFrame2
    "Their height was about two meters, and even then you weren't completley sure because of the limp and hump that this person...no, THAT creature"
    "It has a ripped yellow raincoat too short for the creature that revealed rotting flesh"
    "A piece of a tree bark impaled almos the whole body and through the chest it looked like something was coming out, although you could't distinguish what it was"
    "You hear a low voice, even if you couldn't tell that was voice, calling out for you"
    sl "Finale...hate...fault"
    "The creature muttered without order or meaning"
    "All your instincts tells you to run"
    "What are you doing?"

    menu:
        "Flee":
            jump lago_decision_flee
        "Stay":
            jump lago_decision_stay

label lago_decision_flee:
    "You aren't conscious how, but you are able to escape the creature"
    jump lago

label lago_decision_stay:
    "Your survival instinct displays its absence and going against every logic impulse that you didn't have, you stay in place while the creature got closer to you"
    "When the creature is just a couple centimiters away from your face you are able to distinguish an eye under the hood"
    "The creature starts to do sounds, that only could come from the darkest nightmares in existence, when suddenly it gets completley quiet"
    "You get to see on his beating chest an image that freezes your blood"
    #CG de pecho Sluagh
    scene bg pecho_sluagh with fade:
        xsize config.screen_width
        ysize config.screen_height

    "A kind of face buried on the chest"
    # No entiendo la frase "La criatura de dentro de la criatura araña el trozo de madera que tiene clavado atravesándolo y lo miró con una mirada que parecía juzgarlo."
    #Se refiere a literalmente eso, dentro del monstruo hay otro mas que araña el trozo de madera que lo atraviesa
    "A thought crosses your mind"
    scene bg lore_sluagh_bg:
        xsize config.screen_width
        ysize config.screen_height
    show SluaghFrame2
    #Player
    mc "What the hell is this? A matryoshka?"

    "A thought totaly out of line on the actual life or death situation"
    "Although not so strange"
    "He was on a situation of complete awareness"
    "His brain hardly could work properly"
    "It was correctly proven the moment he decide to stay in place"
    "Perhaps from fear"
    "Perhaps he was one of those people who, in moments of stress, would make unfunny jokes"
    "Perhaps..."
    "..."
    "..."
    #Introduce sonido de corte
    play sound "audio/corte.mp3"
    "That thought of process was cut violently like when pulling a weed from the garden"
    "The only thought that crossed his mind again was"
    #Player
    #Go/jo reference
    #No era la intencion

    #No queda muy bien aunque sea lore acurate probablemente una pantalla en negro baste
    #Lo guardo por si se considera
    #show SluaghFrame2:
    #    rotate 90
    #    xpos 1.160
    #    ypos 1.500
    scene black with fade
    mc "Huh, aren't those my legs?"

    "A fast cut from the creature's hands was all it was needed to separate the superior half of the boy from his inferior half"

    "He hardly felt any pain"
    "It was an almost instant death"
    "In a certain way it was a blessing, knowing averything that it was approaching"
    "The creature got closer to the boy's body kneeling beside him, in a strange way taking into account the wood fragment that impaled him,
    it proceed to bury his giant claws on the heart ripping it out"
    "Then the creature proceeded to devour it"
    #Introduce el audio de la criatura comiendo
    play sound "audio/MonstruoComiendo (Bad Ending Lago).mp3"
    "It was a disgusting sound. It made it sound like a pig was eating. Although that would be an insult to pigs"
    "After eating the creature only said one word"
    #Criatura
    sl "Empty..."
    
    #Puedes poner el sonido de bad ending
    scene bg bad_ending_lago:
        xsize config.screen_width
        ysize config.screen_height
    play sound "audio/SonidoCartelBadEnding.mp3"
    centered "BAD ENDING: INSATIABLE APPETITE."
    #{color=#732020}


#Bloque Orfanato
#Backgrounds
image bg orfanato_generalbg:
    "gui/orfanato/orfanato_general_pixel.png"
    xsize config.screen_width
    ysize config.screen_height

image bg orfanato_puzlebg:
    "gui/orfanato/orfanato_puzle_pixel.png"
    xsize config.screen_width
    ysize config.screen_height
#Lore
image bg orfanato_pasado:
    "gui/orfanato/lore/OrfanatoPast.jpg"
    xsize config.screen_width
    ysize config.screen_height
image bg orfanato_quemado:
    "gui/orfanato/lore/OrfanatoCG.jpg"
    xsize config.screen_width
    ysize config.screen_height
image static_effect_orfanato=Movie(play="gui/orfanato/static_effect.webm", loop=True)



#Codigo para que ambos sonidos del lore suenen
init python:
    renpy.music.register_channel("sfx1", mixer="sfx")
    renpy.music.register_channel("sfx2", mixer="sfx")

#Empiezael codigo
label orfanato:
    $contador_texto=False
    jump orfanato_gam

label orfanato_gam:
    scene bg orfanato_generalbg
    call screen orfanato_general

label orfanato_puzle:
    
    $solution_orfanato = "love"
    $answer_orfanato=""
    if(contador_texto==False):
        "You feel like something is watching you"
        $contador_texto=True
    scene bg orfanato_puzlebg
    call screen orfanato_puzle_screen
    $answer_orfanato=_return
    if solution_orfanato !=answer_orfanato.lower():
        "Maybe is not that"
        jump orfanato_puzle
    else:
        jump orfanato_lore

    

label orfanato_lore:
    "You feel a sharp pain on your head"
    "Your vision gets blurry"
    mc "Ahhhgggg!!!!!!!"
    "A pained scream escapes your throat and all you can see is red"
    #Poner fondo de la escena
    scene dred
    show SluaghFrame2 at center:
        matrixcolor TintMatrix("#000")
    "You barely see an outline getting near"
    
    #Escena usando el fuego
    scene expression Image("gui/Infierno.jpg")
    with fade
    "An abyss calls another abyss"
    "In the roar of your waterfalls"
    "All your waves and your waves they have rushed at me"

    scene black
    with fade

    "The people of the past should stay on the past"
    "Let the dead rest"

    #Flashback
    #Escena de una zona del orfanato sin derruir
    scene bg orfanato_pasado
    kidA "From now this will be your home"
    kidB "I hope you can adapt fast"
    kidC "Otherwise HE will get angry"

    #Flash blanco a temblor en la escena
    play sfx1 "audio/Incendio (orfanato pasado).mp3" fadein 2.0
    scene white
    pause 0.1
    #Escena del orfanato ardiendo
    scene bg orfanato_quemado
    play sfx2 "audio/GritosPanico(orfanato pasado).mp3" fadein 4.0
    kidA "Those who are not prepared to ascend to a superior plane need to be purged"
    kidB "The dirty hand of those who lied to us should be cut off, no?"
    kidC "Once you see death cross infront of you, you learn what is real beauty on this world"

    #Sonido de gente quemandose y del fuego
    #Lo pongo antes para que tenga sentido con la imagen

    "The noise is deafening"
    "The screaming doesn't stop no matter how hard you try"
    "You see dead people"
    "More precisely, you are seeing dead kids"
    "The smell to burnt flesh makes you want to vomit"
    "It is a hellish scene"
    "You distinguish a silhouette impaled on the wall" # Is this mf Dante? No era la intencion pero si
    "No..."
    "More exactly, you see half silhouette impaled on the wall"
    "The bottom half of the body remains on an unkown place"
    "The only thing left of this half are the guts hanging from the body"

    "Enough..."

    "You get to see a small kid lying on the floor"
    "The skin on her face has been cut"
    "The only reason you know the kid is a girl is because of her pigtails burning on the fire"

    "Enough!"

    #Audio tambien
    play sound "audio/caida.mp3"
    "PLAF!!!"

    "You turn your head to see the source of the noise"
    "Only to realize that it comes from a kid that jumped from a window"
    stop sfx1
    stop sfx2
    #Gabriel (Es por la coña. Se quita y ya)
    play audio "audio/orfanato/enough.mp3"
    "ENOUGH!!!"
    scene black
    "."
    ".."
    "..."
    
    "Your senses felt dampened after seeing such images"
    "You feel like vomiting"
    "However, that feeling doesn't come from the disgust from the atrocity"
    "You fell disgust because of how bland people is"
    "Disgust for how predictable is human behaviour is"
    "Although, what you feel the most is annoyance"
    "Annoyed that a fragment of charred wood gade you a burn on the side and splash of blood got on your shirt"
    "..."
    scene static_effect_orfanato
    "Definitely if hell existed it was this exact place"

    #Meter efecto RCT(televisor) y sonido
    #Puedes usar el q he puesto de Bad Ending ya que es estatica
    play sfx1 "audio/SonidoCartelBadEnding.mp3"
    "When the devil falls in love he also dreams of heaven"

    scene black
    with fade
    stop sfx1
    #Termina el flashback
    #Mostrar la escena general

    "You feel like the presence watching you gets more crushing"
    mc "I should get out of this place"
    
    #Se llama al mapa automaticamente
    call screen mapa

#Bloque bosque

label Bosque:

    image BosqueBg = "gui/BosqueBg.jpg"
    scene BosqueBg

    stop music
    stop audio
    stop sound

    play music bosquenieve loop

    "Sientes que este es un lugar al que solo deberias entrar con todos tus recuerdos"

    menu:
        "Entrar al bosque":
            jump eleccionFinal
        "Dar la vuelta":
            stop music
            call screen mapa

label eleccionFinal:

    menu:
        "Final Malo":
            jump Final1
        "Final Verdadero":
            jump Final2

    ###############
    #Contador para si ocurre un final u otro. Una vez estructurado el proyecto descomentar

    #default numero_recuerdos = 0

    #Cuando consigues un recuerdo

    #label buscar_recuerdos:
    #"Has recuperado una de tus memorias perdidas."
    #$ cantidad_recuerdos += 1
    #"Ahora tienes [cantidad_recuerdos] recuerdos."

    ###############

    #if cantidad_recuerdos < 4:

    # FINAL MALO BOSQUE########################################################################################################################


    label Final1:

    "A part of you tells you that you should keep digging into your past."

    "However, you decide not to listen to it."

    "You want to end this experience as soon as possible, so you venture deeper into the forest."

    play sound pasosnieve loop

    "You reflect on the decisions you've made throughout your life."

    "Though of course, you barely have any memories of that life."

    "Can a human be considered alive if their life has been ripped out entirely from their subconscious?"

    "Can you even consider that you've had a life?"

    "I mean, you're definitely alive."

    "The fact that you're alive is a completely objective and undeniable truth."

    "Despite this, what other proof of your life do you have beyond simply being here in the present?"

    "Without memories, you're nothing more than a vagabond wandering through this world until the day of your inevitable end."

    "In that case, what's the point of even living?"

    "We're all going to die one way or another."

    "The only thing that differentiates us is the path to that end."

    "But if you have no path, what sets you apart from someone who doesn't exist?"

    "."

    ".."

    "..."

    "You have no answer to these doubts."

    "You're not even aware of why you're suddenly asking yourself such profound questions out of nowhere."

    stop sound

    #Insertar sonido de corte/apuñalamiento

    image InfiernoBg = "gui/Infierno.jpg"
    scene InfiernoBg
    with vpunch

    play sound corte

    "¡¡WHAM!!"

    "You can't even get to the root of why you're having these thoughts in the first place."

    "A sharp, stabbing pain pierces your chest, and you collapse to the ground, unable to think any further."

    # show SluaghFrame2 (completamente en negro)

    show SluaghFrame2
    with fade

    "The only thing you're able to do before the weak flame of your so-called life flickers out is to make out a subtle yellow silhouette."

    "Everything turns black."

    hide SluaghFrame2

    scene black
    with fade

    "."

    ".."

    "..."

    stop music

    #Insertar musica piano clasica

    play music claire

    "Are you still here?"

    "Well, I suppose you want to know what happened in reality."

    "You suffered an attack in the middle of the session."

    "The psychologist simply watched as, from one moment to the next, you began convulsing until you lay completely still on the floor."

    image SirenaPoliciaBg = "gui/SirenaPolicia.jpg"
    scene SirenaPoliciaBg
    with dissolve
    
    "The police arrived shortly after."

    image CementerioBg = "gui/Cementerio.jpg"
    scene CementerioBg
    with dissolve

    "Your funeral was quite depressing."

    "The only person present was your psychologist, and he only stayed for a little while."

    "You also left no trace whatsoever of your time in this world."

    "You were simply someone who passed through without fanfare or glory."

    "Or well, isn't that the case for most people?"

    "You practically didn't even exist."

    "Your psychologist died a few years later, and the people you knew who are still alive have simply forgotten you."

    "You had no adult friends, you never met your parents, and those who once remembered you stopped doing so over time."

    "Can it even be said that you existed?"

    stop music

    scene black


    ".."

    "..."

    "Who am I?"

    "Who knows."

    play music daisy 

    show unkown 





    "Maybe I'm God."

    "Maybe I'm the Devil."

    "Maybe I'm a being beyond comprehension, or perhaps I'm just your dying subconscious."

    "In any case."

    "Does it really matter?"

    "It's over."

    "That's all."

    "Goodbye, nameless one."

    "."

    ".."

    "..."

    centered "BAD ENDING: THE NONEXISTENCE ABOUT THE YOU."

    stop music

    return

    #else:




    #FINAL VERDADERO##########################################################################

    label Final2:

    "Your memories converge into one."

    "You decide to venture into the depths of the forest."

    play sound pasosnieve loop

    "Your steps are determined and agile."

    "One could even say that you are one with nature itself, seeing how naturally you delve deep into the woods."
    
    "You’re not aware of how much time has passed when you reach a cliff."

    image AcantiladoBg = "gui/AcantiladoBg.jpg"

    scene AcantiladoBg
    with dissolve

    stop sound
    
    "Standing just inches from the edge is the creature that has been watching you."

    show SluaghFrame2
    with fade
    
    "Its yellow raincoat flutters in the wind in an almost orchestrated rhythm."
    
    "You approach slowly, but confidently."
    
    "You stop just a few steps away from the creature."
    
    "Though you shouldn’t keep calling it that anymore."
    
    "Should you?"

    mc "How are you, Olive?"

    "The creature known as Olive remains motionless."

    mc "You really surprised me back then."

    mc "I didn’t think you would actually jump."

    mc "I was just testing the limits of how much someone could endure."

    mc "Years ago I tried the same thing at that orphanage."

    mc "The result was pitiful."

    mc "It made me want to vomit. I still have that bad taste in my mouth."

    mc "What I can’t quite remember is precisely why it took me so long to recall it."

    mc "I suppose the monotony and disappointment from not finding what I was looking for made me lock myself in a bubble and never come out."
    
    mc "Well, look at me!"
   
    mc "I’m no longer bound by those chains, and here I am again, Olive."
   
    "Olive makes no movement at all."
    
    "He simply stares at you fixedly."

    mc "Hey, Olive."

    mc "Before we end all this, why don’t we reminisce about the old times?"

    hide SluaghFrame2

    show SluaghFrame1
    with dissolve

    "Olive tenses slightly."
   
    mc "We are born because we are loved."

    mc "Our birth has meaning because someone loved us."

    mc "We live because we are loved, because we are wanted."

    mc "But you… you were abandoned, Olive."

    mc "Maybe your mother loved you because she hated you."

    mc "There is nothing special about being born."

    mc "Most of the universe is dead."

    mc "In this cruel world we live in, the birth of a tiny, insignificant life in a corner of the cosmos means absolutely nothing."

    mc "Death is the norm."

    mc "So why live?"

    mc "Do you think you were wanted?"

    mc "Who loved you?"

    mc "If no one loved you, what is your reason for living at all?"

    play sound pasosnieve 
    

    hide SluaghFrame1
    with dissolve

    image Sluagh-Olive-S = "CG/Sluagh-Olive(S).jpg"

    scene Sluagh-Olive-S
    with dissolve

    "Olive steps closer to the edge of the precipice."

    "The cold wind blows."

    #CG de Olive sin capucha

    image Sluagh-Olive-O = "CG/Sluagh-Olive(O).jpg"

    scene Sluagh-Olive-O
    with dissolve

    "Olive looks at you one last time, and the wind uncovers his hood."

    "Then he jumps."

    "The wind stops."

    scene AcantiladoBg
    with dissolve


    stop music

    "After gazing at the edge of the cliff for a few seconds, you take a deep breath."

    mc "It feels so good to be free."

    "As those words escape your lips, you breathe deeply again."

    "You count the seconds while feeling nature envelop you."

    "You hear the birds singing in your ears."

    "The gentle touch of moonlight."

    scene black

    "And above everything else, you feel the cold ground running along your body, giving way to a warm sensation of hot blood spilling out from your body shattering against the cold granite."
    
    play sound caida

    scene InfiernoBg
    with vpunch


    "."

    ".."

    "..."

    #Tal vez poner imagen del cielo 

    image CieloBg = "gui/Cielo.jpg"

    scene CieloBg

    with dissolve

    play music vivaldi156

    "Life is a sigh in a corner,"

    "an echo that fades without reason,"

    "a lightning bolt that breaks in the blue,"

    "leaving only shadow at dawn."

    "One day we are breeze, we are light,"

    "the next, ashes and stillness."

    "The rose that blooms in its splendor"

    "soon loses its charm and virtue."

    "."

    ".."

    "..."

    scene black
    
    centered "Months later"

    #Escena de pueblo abandonado

    image PuebloAbandonadoBg = "gui/PuebloAbandonado.jpg"

    scene PuebloAbandonadoBg

    with dissolve

    "It all began quietly, almost imperceptibly."

    "A psychologist who had thrown himself out a window."

    "People thought that so much therapy had finally taken its toll."

    "Soon after, news began to spread that a woman from the town had killed her unfaithful husband."

    play sound sonidoperiodico

    scene news
    with dissolve

    "Once again, it could pass as just another story."
    
    "However, shortly afterward, word came of a family that had committed suicide."
    
    "Then another murder."
    
    "And one after another."
    
    "Soon, people began leaving the town or simply disappearing."
    
    "Who knows."

    scene PuebloAbandonadoBg 
    with dissolve
    
    "The few who remained went from being a community to turning against one another."
    
    "No one did anything directly, but all it took was a small spark to ignite the flame."
    
    "And eventually, it happened."
    
    "It was a relatively small community, but the images seen after the “incident” suggested there had been many people, judging by the number of bodies."
    
    "No one knows what caused such a tragedy."
    
    "Some say the inhabitants were lunatics."
    
    "Others that the small tensions finally exploded because of some madman."
   
    "No one knows."

    #Imagen mural Dibujo figura amarilla

    image ParedMonstruoBg = "gui/ParedMonstruo.jpg"

    scene ParedMonstruoBg

    with dissolve
   
    "The strange thing is that on some of the walls of what remains of the houses, there are drawings of a yellow figure."
    
    "Isn’t it strange how manipulable people can be?"

    #Imagen diablo

    image SatanBg = "gui/Satan.jpg"

    scene SatanBg

    with dissolve
    
    "The devil instigates, but it is the human hand that carries out his will."
   
    "Who is truly worse?"

    #Fundido a negro

    scene black

    stop music

    play sound vela loop


    "."

    ".."

    "..."


    #Pensando si poner una imagen de un libro, una silueta o algo tipo narrador omnisciente (musica o Daisy Daisy o algo similar)

    image NarradorBg = "gui/Narrador.jpg"

    scene NarradorBg

    with dissolve

    
    play music fever
    
    "Memory is a surprising thing, isn’t it?"

    "Memory is not an exact reproduction; we actively reconstruct memories based on pre-existing schemas, which can distort and “give weight” to certain aspects of an event depending on our perspective."
    
    "How would you consider a person with no memory of any kind?"
   
    "Inherently good or inherently evil?"
    
    "I’m talking about whether human beings are good or evil by nature."
    
    "We grow as people based on our childhood and the memories we hold."
    
    "It’s not completely accurate, but a turbulent childhood often leads to depressive, aggressive, or psychotic behavior…"
   
    "On the contrary, a joyful childhood full of affection usually forms more empathetic people."
   
    "But is it possible for a person to be born good and remain so despite everything bad that happens to them?"
    
    "This applies to the opposite case, of course."
   
    "Very well, now let’s consider a hypothetical."
    
    "A person is born as the very incarnation of evil, but at the same time completely loses their memory."
    
    "If you restored their memory, they would become a monster again; on the other hand, if you didn’t, you would be robbing them of their reason for living."
    
    "Do we all in this world truly have the same worth?"
    
    "Does the soul of a good person have the same value as that of a murderer?"
    
    "If heaven and hell exist, logic tells us that the wicked will be punished for all eternity."
   
    "But supposing neither heaven nor hell exists, what difference is there in our value as beings that exist?"
    
    "I have no objective answer to these dilemmas, and I could go on talking about the very concept of existence itself."
    
    "Though I suppose that’s not relevant here."
    
    "I am merely a narrator created by someone so that a reader like you can see their ideas and feelings brought to life."
   
    "In the end of the universe, none of this will matter."
    
    "Everything that has happened and will happen in the life of the universe will be nothing more than a REMINISCENT DREAM at the end of the times."

    stop sound

    
    scene black
    
    centered "FINALE: A PARADOX ABOUT THE SOUL"

    stop music



    return














