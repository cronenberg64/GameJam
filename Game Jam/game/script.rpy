# script.rpy - Main story script for supernatural dating sim
# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define YukiOnna = Character("Yuki-onna", color="#a8d8ea")
define Sadako = Character("Sadako", color="#aa96da") 
define Oni = Character("Oni", color="#ff9a9e")
define Kitsune = Character("Kitsune", color="#feca57")
define narrator = Character(None, color="#ffffff")

# Character image definitions
image yuki default = "yuki_onna_default.png"
image yuki scary = "yuki_onna_scary.png"
image yuki happy = "yuki_onna_happy.png"

image sadako default = "sadako_default.png"
image sadako scary = "sadako_scary.png"
image sadako shy = "sadako_shy.png"

image oni default = "oni_default.png"
image oni scary = "oni_scary.png"
image oni playful = "oni_playful.png"

image kitsune default = "kitsune_default.png"
image kitsune scary = "kitsune_scary.png"
image kitsune mischievous = "kitsune_mischievous.png"

# Background definitions
image bg room = "bg_room.png"
image bg forest = "bg_forest.png"
image bg cabin = "bg_cabin.png"
image bg cave = "bg_cave.png"
image bg snowy_path = "bg_snowy_path.png"
image bg tv_static = "bg_tv_static.png"
image bg black = "#000000"

# Variables to track choices
default mountain_choice = ""
default cabin_choice = ""

# Character affection levels
default yuki_affection = 0
default sadako_affection = 0
default oni_affection = 0
default kitsune_affection = 0

# The game starts here.
label start:
    scene bg room
    play music "ambient_summer.ogg" fadein 2.0
    
    narrator "Summer vacation has finally arrived, and you've been planning this hiking trip for months."
    narrator "The weather forecast shows perfect conditions, and you're eager to escape the city heat."
    narrator "You've narrowed down your destination to two famous mountains, each with their own legends and mysteries."
    
    menu:
        "Where should I go hiking?"
        
        "Akagi Mountain - Known for its ancient caves and mysterious fog":
            $ mountain_choice = "akagi"
            jump akagi_path
            
        "Oeyama Mountain - Famous for oni legends and sudden weather changes":
            $ mountain_choice = "oeyama"
            jump oeyama_path

label akagi_path:
    scene bg forest
    play music "forest_ambience.ogg" fadein 2.0
    
    narrator "You arrive at Akagi Mountain as the morning mist still clings to the trees."
    narrator "The trail is well-marked, but something feels different about this place."
    narrator "After hiking for an hour, you spot an old wooden cabin through the trees."
    
    scene bg cabin
    narrator "The cabin looks abandoned but well-preserved, as if someone left just yesterday."
    narrator "The door creaks open at your touch, revealing a simple interior with just a couch and an old television."
    
    menu:
        "What should I do?"
        
        "Turn on the television":
            $ cabin_choice = "tv"
            jump tv_encounter
            
        "Leave the cabin and continue exploring":
            $ cabin_choice = "explore"
            jump cave_encounter

label oeyama_path:
    scene bg forest
    play music "forest_ambience.ogg" fadein 2.0
    
    narrator "Oeyama Mountain greets you with dense forests and winding paths."
    narrator "Local legends speak of oni who once ruled these peaks, but surely those are just stories..."
    narrator "After hiking for an hour, you discover the same mysterious cabin."
    
    scene bg cabin
    narrator "Inside, you find the same sparse furnishing - a couch and an old television."
    narrator "But something feels different here, more charged with energy."
    
    menu:
        "What should I do?"
        
        "Turn on the television":
            $ cabin_choice = "tv"
            jump tv_encounter
            
        "Leave the cabin and continue exploring":
            $ cabin_choice = "explore"
            jump weather_encounter

# TV Encounter - leads to Sadako route
label tv_encounter:
    scene bg tv_static
    play sound "tv_static.wav"
    
    narrator "The old television flickers to life with a burst of static."
    narrator "Through the white noise, a shadowy figure begins to take shape."
    narrator "Your heart races as the figure becomes clearer... it's a woman with long, dark hair."
    
    scene bg black
    with fade
    
    narrator "The world fades to black..."
    
    # Determine which character appears based on mountain choice
    if mountain_choice == "akagi":
        jump sadako_route
    else:
        jump oni_route

# Cave/Weather Encounter
label cave_encounter:
    scene bg forest
    narrator "You leave the cabin behind and continue deeper into Akagi Mountain."
    narrator "The path becomes steeper, and you notice the temperature dropping."
    narrator "Ahead, you spot a cave entrance partially hidden by hanging vines."
    
    scene bg cave
    narrator "The cave is surprisingly deep, with an otherworldly blue glow emanating from within."
    narrator "As you step inside, your breath becomes visible in the suddenly frigid air."
    
    scene bg black
    with fade
    
    narrator "Everything goes dark..."
    jump yuki_route

label weather_encounter:
    scene bg forest
    narrator "You decide to continue exploring Oeyama Mountain."
    narrator "Suddenly, the sunny sky darkens, and snow begins to fall despite it being summer."
    narrator "The temperature drops rapidly, and an eerie silence fills the forest."
    
    scene bg snowy_path
    narrator "The snowfall intensifies, creating an almost magical winter wonderland."
    narrator "Through the swirling snow, you glimpse a graceful figure moving between the trees."
    
    scene bg black
    with fade
    
    narrator "The cold overwhelms you..."
    jump kitsune_route

# Character Routes - Each approximately 5 minutes of content

label yuki_route:
    scene bg cave
    show yuki default
    with fade
    
    play music "mysterious_melody.ogg" fadein 2.0
    
    narrator "You awaken in the cave, but it's transformed into an ice palace of sorts."
    narrator "Before you stands a beautiful woman with pale skin and flowing white hair."
    
    YukiOnna "You've wandered far from the warm world above, traveler."
    YukiOnna "I am Yuki-onna, guardian of the eternal winter that sleeps within this mountain."
    
    menu:
        "Are you going to hurt me?":
            $ yuki_affection += 1
            YukiOnna "Hurt you? No... I sense no malice in your heart."
            YukiOnna "But why do you seek the cold embrace of the mountain?"
            
        "This place is incredible!":
            $ yuki_affection += 2
            show yuki happy
            YukiOnna "You appreciate beauty even in the harsh cold. How... refreshing."
            YukiOnna "Most humans flee when they feel winter's touch."
    
    narrator "She glides closer, and you notice her breath doesn't mist in the cold air."
    
    YukiOnna "I have been alone here for centuries, watching the seasons change above."
    YukiOnna "But summer grows stronger each year, and my domain shrinks."
    
    menu:
        "That must be lonely.":
            $ yuki_affection += 2
            show yuki happy
            YukiOnna "You... understand loneliness?"
            YukiOnna "Perhaps that's why the mountain brought you to me."
            
        "Why don't you leave this place?":
            $ yuki_affection += 1
            YukiOnna "I am bound to winter itself. Where it goes, I must follow."
            YukiOnna "But in places like this, winter never truly dies."
    
    narrator "She extends a pale hand toward you."
    
    YukiOnna "Would you stay with me, just for a while?"
    YukiOnna "I could show you wonders hidden in ice and snow that no human has ever seen."
    
    menu:
        "I'd like that very much.":
            $ yuki_affection += 3
            show yuki happy
            YukiOnna "Then let me share with you the secret beauty of eternal winter."
            jump yuki_ending
            
        "I need to return to my world.":
            $ yuki_affection += 1
            YukiOnna "I understand. The warm world calls to you."
            YukiOnna "But know that you will always have a place here, should you choose to return."
            jump neutral_ending

label sadako_route:
    scene bg cabin
    show sadako default
    with fade
    
    play music "haunting_piano.ogg" fadein 2.0
    
    narrator "You find yourself back in the cabin, but the atmosphere has changed completely."
    narrator "The woman from the television stands before you, her long hair partially obscuring her face."
    
    Sadako "You... you actually turned on the television."
    Sadako "Most people sense something wrong and leave immediately."
    
    narrator "She moves closer, and you notice her movements are graceful yet unsettling."
    narrator "The air around her seems to shimmer with otherworldly energy."
    
    Sadako "I am Sadako. Once, I had powers that others couldn't understand."
    Sadako "They called me cursed, dangerous. So I found refuge in the space between worlds."
    
    narrator "She gestures to the television, which now shows swirling darkness."
    
    Sadako "Through this window, I've watched the world change, but I've been so... alone."
    Sadako "You're the first person to stay and speak with me instead of running in terror."
    
    narrator "Her eyes meet yours, and you feel a chill run down your spine."
    
    Sadako "I could share my world with you... but the choice comes with consequences."
    Sadako "Will you accept my gift and stay with me forever?"
    
    menu:
        "Yes, I want to be with you.":
            jump sadako_marriage
            
        "No, this is too frightening.":
            jump sadako_death

label oni_route:
    scene bg cabin
    show oni default
    with fade
    
    play music "energetic_drums.ogg" fadein 2.0
    
    narrator "The cabin shakes as a powerful presence makes itself known."
    narrator "A tall, striking woman with small horns and vibrant red hair appears before you."
    
    Oni "Ha! You've got guts, human! Most people run screaming when they feel my presence."
    Oni "I'm Oni, and I've been stuck on this boring mountain for way too long!"
    
    narrator "She flexes her impressive muscles and grins, showing sharp canine teeth."
    narrator "Despite her intimidating appearance, there's something almost playful about her demeanor."
    
    Oni "I used to be the terror of these mountains, you know!"
    Oni "But what's the point of being feared if nobody comes around to be afraid?"
    
    narrator "She looks at you with a predatory gleam in her eyes."
    
    Oni "You climbed all the way up here, found this weird cabin, and you're still not running."
    Oni "That's either very brave... or very stupid."
    
    narrator "She steps closer, her presence both threatening and magnetic."
    
    Oni "I'll make you a deal, little human. Prove you're worthy of my respect..."
    Oni "And I might just let you become my eternal companion. Refuse, and... well."
    
    menu:
        "I accept your challenge!":
            jump oni_marriage
            
        "I don't want to fight you.":
            jump oni_death

label kitsune_route:
    scene bg snowy_path
    show kitsune default
    with fade
    
    play music "mystical_flute.ogg" fadein 2.0
    
    narrator "Through the supernatural snowfall, a fox-eared woman with golden hair approaches."
    narrator "Her multiple tails sway hypnotically as she moves with fluid grace."
    
    Kitsune "My, my... what have we here? A human who doesn't flee from a little magical weather?"
    Kitsune "I am Kitsune, and I confess, I may have been testing you."
    
    narrator "She circles around you playfully, but there's something predatory in her movements."
    narrator "Her golden eyes gleam with an otherworldly intelligence."
    
    Kitsune "I've been watching travelers on this mountain for decades."
    Kitsune "Most are so boring, so predictable. But you... you're different."
    
    narrator "She stops in front of you, her tails swishing behind her."
    
    Kitsune "You see, I've grown quite lonely up here. Fox spirits need... companionship."
    Kitsune "But humans are so fragile, so short-lived. It's quite the problem."
    
    narrator "Her smile becomes both beautiful and unsettling."
    
    Kitsune "I could solve that problem, though. Make you like me - eternal, magical."
    Kitsune "But the transformation is... irreversible. What do you say?"
    
    menu:
        "I want to become like you.":
            jump kitsune_marriage
            
        "I want to stay human.":
            jump kitsune_death

# Marriage and Death Endings - Two per character

label yuki_marriage:
    scene bg cave
    show yuki happy
    with fade
    
    YukiOnna "Your acceptance of my world fills my heart with warmth I thought I'd never feel again."
    YukiOnna "Then stay with me, and become part of the eternal winter."
    
    narrator "She extends her hand, and as you take it, you feel a wonderful coldness spread through your body."
    narrator "Your breath becomes visible, but you no longer feel the chill."
    
    YukiOnna "Now you are like me - eternal, bound to winter's beauty."
    YukiOnna "We will rule over the ice and snow together, forever."
    
    narrator "You feel your humanity slipping away, replaced by something magical and timeless."
    narrator "Together, you and Yuki-onna become the guardians of eternal winter."
    
    scene bg black
    with fade
    
    centered "YUKI-ONNA MARRIAGE ENDING{w=2.0}{nw}"
    centered "You have become one with the winter itself."
    
    return

label yuki_death:
    scene bg cave
    show yuki scary
    with fade
    
    YukiOnna "Fear... yes, I can smell it on you now."
    YukiOnna "How disappointing. I thought you might be different."
    
    narrator "Her beautiful features become sharp and menacing."
    narrator "The temperature drops drastically, and ice begins to form on your skin."
    
    YukiOnna "Those who reject winter's embrace must face winter's wrath."
    YukiOnna "Your warmth will be mine, and your body will become part of my frozen domain."
    
    narrator "You try to run, but the cold has already seeped into your bones."
    narrator "As consciousness fades, you feel yourself becoming one with the ice..."
    
    scene bg black
    with fade
    
    centered "YUKI-ONNA DEATH ENDING{w=2.0}{nw}"
    centered "You have become a frozen statue in her ice palace."
    
    return

label sadako_marriage:
    scene bg cabin
    show sadako shy
    with fade
    
    Sadako "You... you truly accept me? Even knowing what I am?"
    Sadako "Then let us be together beyond the veil of life and death."
    
    narrator "She reaches out to you, and as her fingers touch yours, you feel a strange tingling."
    narrator "The world around you begins to shift and blur."
    
    Sadako "Now you can see the world as I do - between reality and dreams."
    Sadako "We will exist together in the spaces between worlds."
    
    narrator "Your vision changes, and you realize you're no longer fully alive, but not dead either."
    narrator "You and Sadako exist in a realm between worlds, together for eternity."
    
    scene bg black
    with fade
    
    centered "SADAKO MARRIAGE ENDING{w=2.0}{nw}"
    centered "You have joined her in the realm between life and death."
    
    return

label sadako_death:
    scene bg cabin
    show sadako scary
    with fade
    
    Sadako "Fear... just like all the others. How naive I was to hope."
    Sadako "You reject me, just as everyone else has."
    
    narrator "Her hair falls across her face, and the temperature in the room drops."
    narrator "The television screen begins to glow with an ominous light."
    
    Sadako "Then you will share the fate of all who have seen me and turned away."
    Sadako "Seven days... but for you, it will be much sooner."
    
    narrator "Images of death and decay flash across the television screen."
    narrator "You feel your life force being drained away as her curse takes hold."
    
    scene bg black
    with fade
    
    centered "SADAKO DEATH ENDING{w=2.0}{nw}"
    centered "Her curse has claimed another victim."
    
    return

label oni_marriage:
    scene bg cabin
    show oni playful
    with fade
    
    Oni "Hah! Now THAT'S the spirit I was looking for!"
    Oni "You're not just brave, you're as fierce as I am!"
    
    narrator "She laughs heartily and claps you on the back with enough force to knock you forward."
    narrator "But instead of pain, you feel a surge of incredible strength."
    
    Oni "I'm going to make you like me - strong, eternal, and ready for any adventure!"
    Oni "Together we'll rule these mountains and beyond!"
    
    narrator "You feel your body changing, becoming stronger and more powerful."
    narrator "Small horns begin to grow from your head as your transformation completes."
    
    scene bg black
    with fade
    
    centered "ONI MARRIAGE ENDING{w=2.0}{nw}"
    centered "You have become an oni and will adventure together forever."
    
    return

label oni_death:
    scene bg cabin
    show oni scary
    with fade
    
    Oni "Coward! You're just like all the rest - no backbone!"
    Oni "I offer you strength and power, and you cower like a weakling!"
    
    narrator "Her playful demeanor vanishes, replaced by terrifying rage."
    narrator "Her muscles bulge and her eyes glow with fury."
    
    Oni "Weaklings have no place in my domain!"
    Oni "I'll crush you like the pathetic insect you are!"
    
    narrator "She raises her massive fist, and you realize there's no escape."
    narrator "The last thing you see is her terrible smile before everything goes dark."
    
    scene bg black
    with fade
    
    centered "ONI DEATH ENDING{w=2.0}{nw}"
    centered "Your cowardice has sealed your fate."
    
    return

label kitsune_marriage:
    scene bg snowy_path
    show kitsune mischievous
    with fade
    
    Kitsune "Excellent choice! I knew you had the wisdom to see beyond mortal limitations."
    Kitsune "Now, hold still while I work my magic on you."
    
    narrator "She begins to glow with golden light, and you feel a warm tingling throughout your body."
    narrator "Your senses sharpen, and you can suddenly perceive magic in the air around you."
    
    Kitsune "Welcome to immortality, my dear. You now have the power of a fox spirit."
    Kitsune "We'll spend eternity together, playing tricks and exploring the magical world."
    
    narrator "You feel your own fox tail beginning to grow as the transformation completes."
    narrator "Together, you and the kitsune will roam the world, eternal and free."
    
    scene bg black
    with fade
    
    centered "KITSUNE MARRIAGE ENDING{w=2.0}{nw}"
    centered "You have become a fox spirit and gained immortality."
    
    return

label kitsune_death:
    scene bg snowy_path
    show kitsune scary
    with fade
    
    Kitsune "How disappointing. I offer you eternity, and you choose to remain... mundane."
    Kitsune "Well, if you won't join me willingly, you'll serve me in another way."
    
    narrator "Her playful demeanor disappears, replaced by cold calculation."
    narrator "Her tails begin to glow with ominous energy."
    
    Kitsune "Your life force will sustain me for decades. Consider it... payment for wasting my time."
    Kitsune "Don't worry, it will be over quickly."
    
    narrator "You try to run, but fox-fire surrounds you, draining your energy."
    narrator "As your vision fades, you realize you've become her next meal."
    
    scene bg black
    with fade
    
    centered "KITSUNE DEATH ENDING{w=2.0}{nw}"
    centered "Your refusal has cost you your life."
    
    return