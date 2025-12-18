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
            jump bad_ending1
        "Accept the helping hand":
            jump new_beggining
    # Finaliza el juego:

    return

label bad_ending1:
    th "It's a real shame, honestly. You were a good kid. Truly."

    hide narrator

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

    #Llamar al mapa

    ##########call screen mapa_mundo#################

    return

#Bloque casa

screen casa():
    add "gui/House/Puzzle/Casa.jpg"

    imagebutton:
        idle "gui/House/Puzzle/Casa.jpg"
        hover "gui/House/Puzzle/Casa.jpg"
        action ShowMenu("empty")
    imagebutton:
        idle "gui/House/Puzzle/Ventana.png"
        hover "gui/House/Puzzle/Ventana_hover.png"
        xpos 0.341
        ypos 0.125
        action ShowMenu("ventana")
    imagebutton:
        idle "gui/House/Puzzle/Cuadro.png"
        hover "gui/House/Puzzle/Cuadro_hover.png"
        xpos 0.752
        ypos 0.216
        action ShowMenu("cuadro")
    imagebutton:
        idle "gui/House/Puzzle/Libro.png"
        hover "gui/House/Puzzle/Libro_hover.png"
        xpos 0.393
        ypos 0.809
        action ShowMenu("libro")
    imagebutton:
        at left 
        idle "gui/House/Puzzle/Silueta_padre.png" 
        hover "gui/House/Puzzle/Silueta_padre_hover.png" 
        action ShowMenu("padre")

label house_puzzle:

    mc "Im going home."

    scene black
    with dissolve

    show screen casa
    with dissolve

    image padre = "gui/House/Puzzle/Silueta_padre.png"

    show padre at left

    pause

    return

label cuadro:
    show screen casa
    "A strange painting for sure. \nA gentleman with a book and a pen, I think. He seems obsessed with finding something."
    jump house_puzzle

label ventana: 
    show screen casa
    "There is a snowstorm outside. \nI remember that one of the children from the village died in one not long ago."
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
    if Answer != Correct_Answer:
        show screen casa
        mc "No, I don't think that will do anything, gotta find more information. \nCould there be anything useful here?"
        jump house_puzzle
    if Answer == Correct_Answer:
        hide screen casa
        hide th
        hide TherapyBg
        hide padre
        scene black
        jump house_lore

label empty:
    show screen casa
    pause


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

    jump start

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

#Bloque bosque

label Bosque:

    image BosqueBg = "gui/BosqueBg.jpg"
    scene BosqueBg

    # FINAL MALO BOSQUE

    "A part of you tells you that you should keep digging into your past."

    "However, you decide not to listen to it."

    "You want to end this experience as soon as possible, so you venture deeper into the forest."

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

    "..."

    "..."

    "..."

    "You have no answer to these doubts."

    "You're not even aware of why you're suddenly asking yourself such profound questions out of nowhere."

    "¡¡WHAM!!"

    "You can't even get to the root of why you're having these thoughts in the first place."

    "A sharp, stabbing pain pierces your chest, and you collapse to the ground, unable to think any further."

    "The only thing you're able to do before the weak flame of your so-called life flickers out is to make out a subtle yellow silhouette."

    "Everything turns black."

    "..."

    "..."

    "..."

    "Are you still here?"

    "Well, I suppose you want to know what happened in reality."

    "You suffered an attack in the middle of the session."

    "The psychologist simply watched as, from one moment to the next, you began convulsing until you lay completely still on the floor."

    "The police arrived shortly after."

    "Your funeral was quite depressing."

    "The only person present was your psychologist, and he only stayed for a little while."

    "You also left no trace whatsoever of your time in this world."

    "You were simply someone who passed through without fanfare or glory."

    "Or well, isn't that the case for most people?"

    "You practically didn't even exist."

    "Your psychologist died a few years later, and the people you knew who are still alive have simply forgotten you."

    "You had no adult friends, you never met your parents, and those who once remembered you stopped doing so over time."

    "Can it even be said that you existed?"

    "..."

    "..."

    "Who am I?"

    "Who knows."

    "Maybe I'm God."

    "Maybe I'm the Devil."

    "Maybe I'm a being beyond comprehension, or perhaps I'm just your dying subconscious."

    "In any case."

    "Does it really matter?"

    "It's over."

    "That's all."

    "Goodbye, nameless one."

    "..."

    "..."

    "..."

    centered "BAD ENDING: THE NONEXISTENCE ABOUT THE YOU."



    #FINAL VERDADERO

    "Your memories converge into one."

    "You decide to venture into the depths of the forest."

    "Your steps are determined and agile."

    "One could even say that you are one with nature itself, seeing how naturally you delve deep into the woods."
    
    "You’re not aware of how much time has passed when you reach a cliff."
    
    "Standing just inches from the edge is the creature that has been watching you."
    
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

    "Olive steps closer to the edge of the precipice."

    "The cold wind blows."

    "Olive looks at you one last time, and the wind uncovers his hood."

    "Then he jumps."

    "The wind stops."

    "After gazing at the edge of the cliff for a few seconds, you take a deep breath."

    mc "It feels so good to be free."

    "As those words escape your lips, you breathe deeply again."

    "You count the seconds while feeling nature envelop you."

    "You hear the birds singing in your ears."

    "The gentle touch of moonlight."

    "And above everything else, you feel the cold ground running along your body, giving way to a warm sensation of hot blood spilling out from your body shattering against the cold granite."
    
    "..."

    "..."

    "..."

    "Life is a sigh in a corner,"

    "an echo that fades without reason,"

    "a lightning bolt that breaks in the blue,"

    "leaving only shadow at dawn."

    "One day we are breeze, we are light,"

    "the next, ashes and stillness."

    "The rose that blooms in its splendor"

    "soon loses its charm and virtue."

    "..."

    "..."

    "..."

    centered "Months later"

    "It all began quietly, almost imperceptibly."

    "A psychologist who had thrown himself out a window."

    "People thought that so much therapy had finally taken its toll."

    "Soon after, news began to spread that a woman from the town had killed her unfaithful husband."
    
    "Once again, it could pass as just another story."
    
    "However, shortly afterward, word came of a family that had committed suicide."
    
    "Then another murder."
    
    "And one after another."
    
    "Soon, people began leaving the town or simply disappearing."
    
    "Who knows."
    
    "The few who remained went from being a community to turning against one another."
    
    "No one did anything directly, but all it took was a small spark to ignite the flame."
    
    "And eventually, it happened."
    
    "It was a relatively small community, but the images seen after the “incident” suggested there had been many people, judging by the number of bodies."
    
    "No one knows what caused such a tragedy."
    
    "Some say the inhabitants were lunatics."
    
    "Others that the small tensions finally exploded because of some madman."
   
    "No one knows."
   
    "The strange thing is that on some of the walls of what remains of the houses, there are drawings of a yellow figure."
    
    "Isn’t it strange how manipulable people can be?"
    
    "The devil instigates, but it is the human hand that carries out his will."
   
    "Who is truly worse?"

    "..."

    "..."

    "..."

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
    
    "Everything that has happened and will happen in the life of the universe will be nothing more than a REMINISCENT DREAM at the end of time."
    
    centered "FINALE: A PARADOX ABOUT THE SOUL"

    return














