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
# image yuki neutral = "yuki_onna_default.png"
# image yuki happy = "yuki_onna_default.png"
# image yuki scary = "yuki_onna_scary.png"

# image sadako neutral = "sadako_default.png"
# image sadako shy = "sadako_default.png"
# image sadako scary = "sadako_scary.png"

# image oni neutral = "oni_default.png"
# image oni playful = "oni_default.png"
# image oni scary = "oni_scary.png"

# image kitsune neutral = "kitsune_default.png"
# image kitsune mischievous = "kitsune_default.png"
# image kitsune scary = "kitsune_scary.png"

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
    play music "assets/music/bg/ambient_summer.mp3" fadein 1.0 loop
    
    narrator "Summer vacation has finally arrived, and you've been planning this hiking trip for months."
    narrator "The weather forecast shows perfect conditions, and you're eager to escape the city heat."
    narrator "You've narrowed down your destination to two famous mountains, each with their own legends and mysteries."
    
    menu:
        "Where should I go hiking?"
        
        "Akagi Mountain - Known for its ancient caves and mysterious fog":
            #sfx
            $ mountain_choice = "akagi"
            stop music fadeout 1.0
            jump akagi_path
            
        "Oeyama Mountain - Famous for oni legends and sudden weather changes":
            #sfx
            $ mountain_choice = "oeyama"
            stop music fadeout 1.0
            jump oeyama_path

label akagi_path:
    scene bg forest
    play music "assets/music/bg/ambient_forest.mp3" fadein 1.0 loop #change
    
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
            stop music fadeout 1.0
            jump tv_encounter
            
        "Leave the cabin and continue exploring":
            $ cabin_choice = "explore"
            stop music fadeout 1.0
            jump cave_encounter

label oeyama_path:
    scene bg forest
    play music "assets/music/bg/ambient_forest.mp3" fadein 1.0 loop
    
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
            stop music fadeout 1.0
            jump tv_encounter
            
        "Leave the cabin and continue exploring":
            $ cabin_choice = "explore"
            stop music fadeout 1.0
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
        stop music fadeout 1.0
        jump sadako_route
    else:
        stop music fadeout 1.0
        jump oni_route

# Cave/Weather Encounter
label cave_encounter:
    play music "assets/music/bg/ambient_forest.mp3" fadein 1.0 loop #change
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
    stop music fadeout 1.0
    jump yuki_route

label weather_encounter:
    play music "assets/music/bg/ambient_forest.mp3" fadein 1.0 loop #change
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
    stop music fadeout 1.0
    jump kitsune_route

# Character Routes - Each approximately 5 minutes of content

label yuki_route:
    scene bg cave
    show yuki neutral
    with fade
    
    play music "assets/music/bg/mystery_melody.mp3" fadein 1.0 loop
    
    narrator "You awaken in a strange cave, but something feels different about this place."
    narrator "The air is thick with magic, and the walls seem to pulse with an otherworldly energy."
    
    YukiOnna "You're not supposed to be here, human."
    YukiOnna "This is the demon world, and your presence here is... problematic."
    
    menu:
        "Where am I? What happened?":
            $ yuki_affection += 1
            YukiOnna "The mountain's magic must have pulled you through a rift between worlds."
            YukiOnna "Humans aren't meant to be here. The demon lords would execute you on sight."
            
        "Are you going to turn me in?":
            $ yuki_affection -= 1
            YukiOnna "That would be the proper thing to do..."
            YukiOnna "But something about you makes me hesitate."
            
        "Can you help me get back?":
            $ yuki_affection += 2
            YukiOnna "Help you? That would be treason against the demon lords."
            YukiOnna "But... I've always been different from other demons."
    
    narrator "She looks around cautiously, as if expecting someone to appear at any moment."
    
    if yuki_affection < 0:
        YukiOnna "Your fear and suspicion are clouding your judgment."
        YukiOnna "But perhaps there's still time to change your fate."
    else:
        YukiOnna "I've been watching the human world for centuries, fascinated by its warmth and life."
        YukiOnna "Maybe helping you is my chance to do something good."
    
    menu:
        "I trust you to help me.":
            $ yuki_affection += 2
            YukiOnna "Your trust... it's been so long since anyone trusted me."
            YukiOnna "I'll help you find a way back, but we must be careful."
            
        "How do I know you won't betray me?":
            $ yuki_affection -= 1
            YukiOnna "You don't. But what choice do you have?"
            YukiOnna "The demon lords will find you eventually if you stay here alone."
            
        "What's in it for you?":
            YukiOnna "Perhaps I'm tired of the eternal winter of the demon world."
            YukiOnna "Or perhaps I just want to believe there's still good in this world."
    
    narrator "She leads you through winding tunnels, her ice magic creating a path through the darkness."
    narrator "Suddenly, you hear voices echoing from ahead."
    
    YukiOnna "The demon guards are patrolling. We need to hide."
    
    menu:
        "Follow her lead":
            $ yuki_affection += 1
            YukiOnna "Good. Trust is essential if we're to survive this."
            
        "Try to run":
            $ yuki_affection -= 2
            show yuki scary
            YukiOnna "Fool! You'll get us both killed!"
            YukiOnna "The demon lords will show no mercy to traitors."
            narrator "Before you can react, Yuki-onna's hand strikes your temple."
            narrator "The last thing you see is her cold, determined expression as darkness claims you."
            jump yuki_death
    
    if yuki_affection >= 3:
        stop music fadeout 1.0
        jump yuki_marriage
    else:
        stop music fadeout 1.0
        jump yuki_death

label sadako_route:
    scene bg cabin
    show sadako neutral
    with fade
    
    play music "assets/music/bg/haunting_piano.mp3" fadein 1.0 loop
    
    narrator "The television's static clears to reveal a dark, otherworldly realm."
    narrator "Through the screen, a woman with long dark hair reaches out to you."
    
    Sadako "O-oh... a human? In the demon world?"
    Sadako "I... I didn't mean to pull you through. The television sometimes... acts on its own."
    
    menu:
        "How did this happen?":
            $ sadako_affection += 1
            Sadako "W-well... the television acts as a gateway between worlds."
            Sadako "But it's not supposed to pull humans through... I'm so sorry..."
            
        "Are you going to turn me in?":
            $ sadako_affection -= 1
            show sadako scary
            Sadako "T-turn you in? I... I should, but..."
            Sadako "I've always been different from other demons. Too... too soft, they say."
            
        "Can you help me get back?":
            $ sadako_affection += 2
            Sadako "H-help you? That would be treason against the demon lords..."
            Sadako "But... I've always been fascinated by the human world. Maybe I could..."
    
    narrator "She fidgets nervously, her hair swaying as she looks around."
    
    if sadako_affection < 0:
        Sadako "Y-your suspicion is understandable... but dangerous here."
        Sadako "In this world, trust is the only currency that matters."
        show sadako scary
    else:
        Sadako "I... I've been watching your world through the television for so long."
        Sadako "Maybe helping you is my chance to do something... meaningful."
        show sadako neutral
    
    menu:
        "I trust you to help me.":
            $ sadako_affection += 2
            Sadako "Y-you trust me? It's been so long since anyone..."
            Sadako "I'll help you find a way back, but we must be careful."
            
        "How do I know you won't betray me?":
            $ sadako_affection -= 1
            show sadako scary
            Sadako "Y-you don't... but what choice do you have?"
            Sadako "The demon lords will find you eventually if you stay here alone."
            
        "What's in it for you?":
            Sadako "I... I'm tired of being just a watcher in the shadows."
            Sadako "Or perhaps I just want to believe there's still good in this world."
    
    narrator "Suddenly, the sound of demon guards echoes through the corridors."
    
    Sadako "O-oh no! The guards are coming! They'll take you to the demon lords!"
    
    menu:
        "Follow her lead":
            $ sadako_affection += 1
            Sadako "G-good. Trust is essential if we're to survive this."
            
        "Try to run":
            $ sadako_affection -= 2
            show sadako scary
            Sadako "N-no! You'll get us both killed!"
            Sadako "The demon lords will show no mercy to traitors."
    
    if sadako_affection >= 3:
        stop music fadeout 1.0
        jump sadako_marriage
    else:
        stop music fadeout 1.0
        jump sadako_death

label oni_route:
    scene bg cabin
    show oni neutral
    with fade
    
    play music "assets/music/bg/energetic_drums.mp3" fadein 1.0 loop
    
    narrator "The cabin door bursts open, revealing a massive figure silhouetted against the demon world's crimson sky."
    narrator "A powerful oni warrior stands before you, his horns casting long shadows in the dim light."
    
    Oni "Oho! What do we have here? A little human lost in the demon world?"
    Oni "This is going to be fun! The demon lords will be so surprised!"
    
    menu:
        "I don't want any trouble":
            $ oni_affection += 1
            Oni "Trouble? Ha! You're already in it, little one!"
            Oni "But don't worry, I'll make sure it's the fun kind of trouble!"
            
        "I can handle myself":
            $ oni_affection -= 1
            show oni scary
            Oni "Bold words for someone so tiny! I like your spirit!"
            Oni "But maybe you should save that courage for when you really need it!"
            
        "I need help getting back to my world":
            $ oni_affection += 2
            Oni "Help? An oni helping a human? That would be a first!"
            Oni "But you know what? I've always wanted to try something new!"
    
    narrator "The oni circles around you, his eyes sparkling with excitement."
    
    if oni_affection < 0:
        Oni "Your bravado is cute, but dangerous in this world."
        Oni "The demon lords don't play nice with humans who think they're tough."
        show oni scary
    else:
        Oni "You know, humans are usually so... boring."
        Oni "But you, you might actually be fun to play with!"
        show oni neutral
    
    menu:
        "I'll help you if you help me":
            $ oni_affection += 2
            Oni "A deal? Now that's what I call a good game!"
            Oni "But what could a little human possibly offer an oni warrior?"
            
        "Please, I just want to go home":
            $ oni_affection -= 1
            show oni scary
            Oni "Aw, don't be such a scaredy-cat!"
            Oni "Where's your sense of adventure?"
            
        "I can prove my worth":
            Oni "Prove your worth? Now that's what I like to hear!"
            Oni "Let's make a game of it!"
    
    narrator "Suddenly, the ground trembles as demon guards approach."
    
    Oni "Oho! The guards are coming! This is getting exciting!"
    
    menu:
        "Fight alongside the oni":
            $ oni_affection += 2
            Oni "That's the spirit! Let's show them what we're made of!"
            
        "Try to hide":
            $ oni_affection -= 2
            show oni scary
            Oni "Hiding? Where's the fun in that?"
            Oni "The demon lords will make an example of you."
    
    if oni_affection >= 3:
        stop music fadeout 1.0
        jump oni_marriage
    else:
        stop music fadeout 1.0
        jump oni_death

label kitsune_route:
    scene bg cabin
    show kitsune neutral
    with fade
    
    play music "assets/music/bg/mystical_flute.mp3" fadein 1.0 loop #more playful
    
    narrator "A swirl of foxfire illuminates the cabin, revealing a beautiful woman with fox ears and multiple tails."
    narrator "She materializes from the flames, her golden eyes studying you with amusement."
    
    Kitsune "My, my, what do we have here? A little human lost in the demon world?"
    Kitsune "How delightfully unexpected! The demon lords will be so... entertained."
    
    menu:
        "Who are you?":
            $ kitsune_affection += 1
            Kitsune "Me? I'm just a humble fox spirit who loves to play games."
            Kitsune "And you, my dear human, have just become my newest plaything~"
            
        "Are you going to turn me in?":
            $ kitsune_affection -= 1
            show kitsune scary
            Kitsune "Turn you in? Now where's the fun in that?"
            Kitsune "I much prefer to play with my prey before deciding their fate~"
            
        "Can you help me get back to my world?":
            $ kitsune_affection += 2
            Kitsune "Help you? That would be... interesting."
            Kitsune "But what would you offer in return for such a favor? I do love making deals~"
    
    narrator "She circles around you, her tails swishing with barely contained energy."
    
    if kitsune_affection < 0:
        Kitsune "Your suspicion is wise, but perhaps misplaced."
        Kitsune "In this world, sometimes the greatest danger comes from those you trust least~"
        show kitsune scary
    else:
        Kitsune "You know, humans are usually so... predictable."
        Kitsune "But you, you're different. I wonder what games we could play together~"
        show kitsune neutral
    
    menu:
        "I'll make a deal with you":
            $ kitsune_affection += 2
            Kitsune "A deal? Now you're speaking my language!"
            Kitsune "But be careful what you wish for, little human~"
            
        "I don't trust you":
            $ kitsune_affection -= 1
            show kitsune scary
            Kitsune "Smart, but perhaps too smart for your own good."
            Kitsune "The demon lords don't take kindly to humans who think they're clever~"
            
        "What do you want from me?":
            Kitsune "What do I want? Perhaps I just want to see how this story unfolds."
            Kitsune "Or perhaps I'm bored of the usual games in the demon world~"
    
    narrator "Suddenly, the sound of demon guards echoes through the corridors."
    
    Kitsune "Oho! The guards are coming! This is getting interesting~"
    
    menu:
        "Trust the kitsune's plan":
            $ kitsune_affection += 2
            Kitsune "Good choice. Let's make this interesting~"
            
        "Try to escape alone":
            $ kitsune_affection -= 2
            show kitsune scary
            Kitsune "Running? How predictable. And how... disappointing."
            Kitsune "The demon lords will make an example of you~"
    
    if kitsune_affection >= 3:
        stop music fadeout 1.0
        jump kitsune_marriage
    else:
        stop music fadeout 1.0
        jump kitsune_death

# Marriage and Death Endings - Two per character

label yuki_marriage:
    scene bg cave
    show yuki neutral
    with fade
    
    YukiOnna "I've found a way to open a portal to your world."
    YukiOnna "But I can't stay here anymore. The demon lords will hunt me for helping you."
    
    narrator "She takes your hand, and together you step through the portal."
    narrator "The warmth of the human world welcomes you both."
    
    scene bg black
    with fade
    
    centered "ONE YEAR LATER{w=2.0}{nw}"
    
    scene bg modern_city
    show yuki happy
    with fade
    
    YukiOnna "It's been a year since we escaped the demon world."
    YukiOnna "I never thought I'd find happiness in the human world, but you showed me the way."
    
    narrator "She takes your hand, a gentle smile on her face."
    
    YukiOnna "Will you spend the rest of your life with me?"
    YukiOnna "I promise to keep you warm, even in the coldest winters."
    
    scene bg black
    with fade
    
    centered "YUKI-ONNA MARRIAGE ENDING{w=2.0}{nw}"
    centered "You have found eternal love in the warmth of winter."
    
    jump credit

label yuki_death:
    scene bg cave
    show yuki scary
    with fade
    
    YukiOnna "I'm sorry, but I can't risk my position for someone who doesn't trust me."
    YukiOnna "The demon lords will decide your fate."
    
    narrator "She leads you deeper into the cave, her hand cold against yours."
    narrator "The temperature drops further as you enter a secluded chamber."
    
    YukiOnna "This is where I bring those who disappoint me."
    YukiOnna "Your warmth will sustain me through the long winter."
    
    narrator "Before you can react, her hand strikes your temple."
    narrator "The last thing you see is her cold, determined expression as darkness claims you."
    narrator "When you wake up, you're in a secluded ice cave, Yuki-onna watching over you."
    
    scene bg black
    with fade
    
    centered "YUKI-ONNA DEATH ENDING{w=2.0}{nw}"
    centered "Your warmth has become her eternal feast."
    
    jump credit

label sadako_marriage:
    scene bg cabin
    show sadako neutral
    with fade
    
    Sadako "I've found a way to open a portal to your world."
    Sadako "But I can't stay here anymore. The demon lords will hunt me for helping you."
    
    narrator "She takes your hand, and together you step through the television screen."
    narrator "The familiar warmth of your world welcomes you both."
    
    scene bg black
    with fade
    
    centered "ONE YEAR LATER{w=2.0}{nw}"
    
    scene bg modern_city
    show sadako shy
    with fade
    
    Sadako "It's been a year since we escaped the demon world."
    Sadako "I never thought I'd find someone who could see past my... unusual nature."
    
    narrator "She looks at you with a gentle smile, her hair no longer obscuring her face."
    
    Sadako "Will you spend the rest of your life with me?"
    Sadako "I promise to keep the darkness at bay, as long as you're by my side."
    
    scene bg black
    with fade
    
    centered "SADAKO MARRIAGE ENDING{w=2.0}{nw}"
    centered "You have found love in the space between worlds."
    
    jump credit

label sadako_death:
    scene bg cabin
    show sadako scary
    with fade
    
    Sadako "I'm sorry, but I can't risk my position for someone who doesn't trust me."
    Sadako "The demon lords will decide your fate."
    
    narrator "She leads you deeper into the cabin, her hand cold against yours."
    narrator "The television static grows louder as you enter a secluded room."
    
    Sadako "This is where I bring those who disappoint me."
    Sadako "Your life force will sustain me through the long years."
    
    narrator "Before you can react, her hand reaches through the television screen."
    narrator "The last thing you see is her cold, determined expression as darkness claims you."
    narrator "When you wake up, you're trapped in the television, Sadako watching over you."
    
    scene bg black
    with fade
    
    centered "SADAKO DEATH ENDING{w=2.0}{nw}"
    centered "Your life has become her eternal entertainment."
    
    jump credit

label oni_marriage:
    scene bg cabin
    show oni neutral
    with fade
    
    Oni "I've found a way to open a portal to your world."
    Oni "But I can't stay here anymore. The demon lords will hunt me for helping you."
    
    narrator "He takes your hand, and together you step through the portal."
    narrator "The familiar warmth of your world welcomes you both."
    
    scene bg black
    with fade
    
    centered "ONE YEAR LATER{w=2.0}{nw}"
    
    scene bg modern_city
    show oni playful
    with fade
    
    Oni "It's been a year since we escaped the demon world."
    Oni "I never thought I'd find someone who could match my strength and spirit."
    
    narrator "He looks at you with a proud smile, his horns now hidden under a stylish hat."
    
    Oni "Will you spend the rest of your life with me?"
    Oni "I promise to protect you with all my strength, as long as you stand by my side."
    
    scene bg black
    with fade
    
    centered "ONI MARRIAGE ENDING{w=2.0}{nw}"
    centered "You have found love in the strength of your bond."
    
    jump credit

label oni_death:
    scene bg cabin
    show oni scary
    with fade
    
    Oni "I'm sorry, but I can't risk my position for someone who doesn't trust me."
    Oni "The demon lords will decide your fate."
    
    narrator "He leads you deeper into the cabin, his grip firm on your arm."
    narrator "The air grows thick with demonic energy as you enter a secluded chamber."
    
    Oni "This is where I bring those who disappoint me."
    Oni "Your strength will sustain me through the long battles to come."
    
    narrator "Before you can react, his massive fist strikes your temple."
    narrator "The last thing you see is his cold, determined expression as darkness claims you."
    narrator "When you wake up, you're in a secluded training ground, the Oni watching over you."
    
    scene bg black
    with fade
    
    centered "ONI DEATH ENDING{w=2.0}{nw}"
    centered "Your strength has become his eternal power."
    
    jump credit

label kitsune_marriage:
    scene bg cabin
    show kitsune neutral
    with fade
    
    Kitsune "I've found a way to open a portal to your world."
    Kitsune "But I can't stay here anymore. The demon lords will hunt me for helping you."
    
    narrator "She takes your hand, and together you step through the portal."
    narrator "The familiar warmth of your world welcomes you both."
    
    scene bg black
    with fade
    
    centered "ONE YEAR LATER{w=2.0}{nw}"
    
    scene bg modern_city
    show kitsune mischievous
    with fade
    
    Kitsune "It's been a year since we escaped the demon world."
    Kitsune "I never thought I'd find someone who could keep up with my tricks and games."
    
    narrator "She looks at you with a playful smile, her tails now hidden under a stylish coat."
    
    Kitsune "Will you spend the rest of your life with me?"
    Kitsune "I promise to keep life interesting, as long as you play along with my games."
    
    scene bg black
    with fade
    
    centered "KITSUNE MARRIAGE ENDING{w=2.0}{nw}"
    centered "You have found love in the joy of eternal play."
    
    jump credit

label kitsune_death:
    scene bg cabin
    show kitsune scary
    with fade
    
    Kitsune "I'm sorry, but I can't risk my position for someone who doesn't trust me."
    Kitsune "The demon lords will decide your fate."
    
    narrator "She leads you deeper into the cabin, her hand deceptively gentle on yours."
    narrator "The air grows thick with foxfire as you enter a secluded chamber."
    
    Kitsune "This is where I bring those who disappoint me."
    Kitsune "Your life force will sustain me through the long years of games to come."
    
    narrator "Before you can react, her tails wrap around you, draining your energy."
    narrator "The last thing you see is her cold, determined expression as darkness claims you."
    narrator "When you wake up, you're in a secluded shrine, the Kitsune watching over you."
    
    scene bg black
    with fade
    
    centered "KITSUNE DEATH ENDING{w=2.0}{nw}"
    centered "Your life has become her eternal plaything."
    
    jump credit

label neutral_ending:
    scene bg forest
    with fade
    
    play music "assets/music/bg/ambient_forest.mp3" fadein 2.0 loop #change
    
    narrator "You make your way back down the mountain, the strange encounters fading like a dream."
    narrator "The sun is beginning to set, casting long shadows through the trees."
    
    narrator "As you reach the base of the mountain, you look back one last time."
    narrator "Was it all real? Or just your imagination playing tricks on you?"
    
    narrator "Either way, you've survived your adventure, wiser for the experience."
    narrator "The city lights welcome you back to the familiar world of the living."
    
    scene bg black
    with fade
    
    centered "NEUTRAL ENDING{w=2.0}{nw}"
    centered "You have returned home, carrying the memories of your supernatural encounter."
    
    jump credit

label credit:
    scene bg black
    with fade
    
    centered "CREDITS{w=2.0}{nw}"
    centered "Game Development{w=1.0}{nw}"
    centered "Game Mechanics: Faiq and Jonathan{w=1.0}{nw}"
    centered "Story: Faiq{w=1.0}{nw}"
    centered "GUI: Jonathan{w=1.0}{nw}"
    
    centered "Art & Graphics{w=1.0}{nw}"
    centered "Illustrator: Ren{w=1.0}{nw}"
    
    centered "Music & Sound{w=1.0}{nw}"
    centered "SFX & Background Music: Chad{w=1.0}{nw}"
    
    centered "Special Thanks{w=1.0}{nw}"
    centered "Ren'Py Engine{w=1.0}{nw}"
    centered "All our team members{w=1.0}{nw}"
    centered "And you, for playing our game!{w=2.0}{nw}"

    centered "Third-Party Sources{w=1.0}{nw}"
    centered "Musics{w=1.0}{nw}"
    
    return