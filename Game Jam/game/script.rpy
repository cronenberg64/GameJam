# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define YukiOnna = Character("Yuki-onna (ゆき女)", color="#c8ffc8")

define Sadako = Character("Sadako (佐渡子)", color="#c8c8ff")

define Oni = Character("Oni (鬼)", color="#ffc8c8")

image YukiOnna default = "yuki_onna_default.png"
image YukiOnna scary = "yuki_onna_scary.png"
image Sadako default = "sadako_default.png"
image Sadako scary = "sadako_scary.png"
image Oni default = "oni_default.png"
image Oni scary = "oni_scary.png"


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
