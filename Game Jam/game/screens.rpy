################################################################################
## Initialization
################################################################################

init offset = -1


################################################################################
## Styles
################################################################################

# Custom style for main menu buttons that rely on an image mapAdd commentMore actions
style start_button:
    # Set text color to fully transparent if your text is on the background image
    color "#00000000"
    hover_color "#00000000"
    selected_color "#00000000"
    insensitive_color "#00000000"

    # Make the button background completely invisible
    background None
    hover_background None
    selected_background None
    insensitive_background None
    idle_background None

    # Align text in the center of the hotspot area (relevant if text is visible)
    xalign 0.5
    yalign 0.5
    font gui.button_text_font
    size gui.button_text_size
#Add comment

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, 
    tile=gui.vslider_tile)


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"


    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

    adjust_spacing False

## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xanchor gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action


style choice_vbox is vbox
style choice_button is button
style choice_button_text:
    color gui.choice_button_text_idle_color
    hover_color gui.choice_button_text_hover_color
    selected_color gui.choice_button_text_hover_color
    insensitive_color gui.choice_button_text_insensitive_color
    outlines gui.button_text_outlines
    kerning gui.button_text_kerning
    xalign 0.5

style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.text_properties("choice_button")


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "standard"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") style "quick_button" action Rollback()

            # textbutton _("History") 
            #     style "quick_button"
            #     action ShowMenu('history')

            # textbutton _("Skip") 
            #     style "quick_button"
            #     action Skip() alternate Skip(fast=True, confirm=True)

            # textbutton _("Auto") 
            #     style "quick_button"
            #     action Preference("auto-forward", "toggle")

            # textbutton _("Save") 
            #     style "quick_button"
            #     action ShowMenu('save')

            # textbutton _("Q.Save") 
            #     style "quick_button"
            #     action QuickSave()

            # textbutton _("Q.Load") 
            #     style "quick_button"
            #     action QuickLoad()

            # textbutton _("Prefs") 
            #     style "quick_button"
            #     action ShowMenu('preferences')


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.text_properties("quick_button")


################################################################################
## Main and Game Menu Screens (Merged Storybook Look + Functional Tags)
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("Start") action Start()

        else:
            textbutton _("Options") action ShowMenu("preferences")

            textbutton _("Gallery") action ShowMenu("gallery")

            textbutton _("History") action ShowMenu("history")

            textbutton _("Save") action ShowMenu("save")

            textbutton _("Load") action ShowMenu("load")

            textbutton _("Preferences") action ShowMenu("preferences")

        if _in_replay:

            textbutton _("End Replay") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("Main Menu") action MainMenu()

            textbutton _("About") action ShowMenu("about")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## Help isn't necessary or relevant to mobile devices.
            textbutton _("Help") action ShowMenu("help")

        if renpy.variant("pc"):

            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.
            textbutton _("Quit") action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.text_properties("navigation_button")


## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    add gui.main_menu_background

    ## This empty frame darkens the main menu.
    frame:
        style "main_menu_frame"

    # Central functional buttons matching the background's theme
    # Adjusted positions: moved further right by 200 and lower by 50
    textbutton "":
        style "start_menu_button"
        xpos 1011
        ypos 385
        xsize 500
        ysize 80
        action Start()

    textbutton "":
        style "load_menu_button"
        xpos 1081
        ypos 500
        xsize 500
        ysize 80
        action ShowMenu("load")

    textbutton "":
        style "options_menu_button"
        xpos 1072
        ypos 555
        xsize 500
        ysize 80
        action ShowMenu("preferences")

    textbutton "":
        style "gallery_menu_button"
        xpos 1072
        ypos 610
        xsize 500
        ysize 80
        action ShowMenu("gallery")

    textbutton "":
        style "about_menu_button"
        xpos 1073
        ypos 665
        xsize 500
        ysize 80
        action ShowMenu("about")

    textbutton "":
        style "help_menu_button"
        xpos 1103
        ypos 720
        xsize 500
        ysize 80
        action ShowMenu("help")

    textbutton "":
        style "quit_menu_button"
        xpos 1101
        ypos 775
        xsize 500
        ysize 80
        action Quit(confirm=True)

    # Remove the display of the game title and version from the main menu
    # if gui.show_name:
    #     vbox:
    #         style "main_menu_vbox"
    #         text "[config.name!t]":
    #             style "main_menu_title"
    #         text "[config.version]":
    #             style "main_menu_version"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid".
## This screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None, yinitial=0.0, spacing=0):

    style_prefix "game_menu"

    add "gui/overlay/confirm.png"

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            spacing spacing

                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        spacing spacing

                        transclude

                else:

                    transclude

    use navigation

    textbutton _("Return"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45


## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():
    tag menu
    imagemap:
        ground 'gui/abouthistory/menu_idle.png'
        idle 'gui/abouthistory/menu_idle.png'
        hover 'gui/abouthistory/menu_hover.png'
        selected_idle 'gui/abouthistory/menu_hover.png'
        selected_hover 'gui/abouthistory/menu_hover.png'
        cache False
        hotspot (85, 263, 233, 90) action ShowMenu('history')
        hotspot (1584, 245, 239, 91) action ShowMenu('about')
        hotspot (1584, 411, 242, 98) action ShowMenu('help')
        hotspot (75, 613, 246, 88) action ShowMenu('preferences')
        hotspot (75, 483, 257, 91) action ShowMenu('load')
        hotspot (82, 366, 265, 90) action ShowMenu('save')
        hotspot (1584, 537, 254, 91) action MainMenu()
        hotspot (1601, 698, 229, 96) action Quit()
        hotspot (1448, 183, 64, 65) action Return()
    vbox:
        xpos 0.25
        ypos 0.23
        xmaximum 400
        text "[config.name!t]" style "about_label_text"
        text _(f"Version [config.version!t]\n") style "about_text"
        text _(f"Made with {{a=https://www.renpy.org/}}Ren'Py{{/a}} [renpy.version_only].\n\n[renpy.license!t]") style "about_text"
    vbox:
        xpos 0.55
        ypos 0.23
        xmaximum 400
        text _(f"Credits:\n-{{a=https://incompetech.filmmusic.io/song/4371-skye-cuillin/}}Skye Cuillin{{/a}} by Kevin MacLeod\nLicense: {{a=https://filmmusic.io/standard-license/}}https://filmmusic.io/standard-license{{/a}}") style "about_text"
        text _(f"\n-{{a=https://incompetech.filmmusic.io/song/4467-teller-of-the-tales/}}Teller of tales{{/a}} by Kevin MacLeod\nLicense: {{a=https://filmmusic.io/standard-license/}}https://filmmusic.io/standard-license{{/a}}") style "about_text"
        text _(f"\nTemplate created by Skolaztika") style "about_text"

style about_label_text:
    size gui.label_text_size
    font gui.interface_text_font
    color gui.text_color

style about_text:
    font gui.interface_text_font
    color gui.text_color


## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():
    tag menu
    add "gui/SaveLoad/saveload_ground.png"
    hbox:
        spacing 0
        # Left tab navigation
        vbox:
            spacing 10
            imagebutton idle "gui/abouthistory/menu_idle.png" hover "gui/abouthistory/menu_hover.png" action ShowMenu("history")
            imagebutton idle "gui/abouthistory/menu_idle.png" hover "gui/abouthistory/menu_hover.png" action ShowMenu("about")
            imagebutton idle "gui/abouthistory/menu_idle.png" hover "gui/abouthistory/menu_hover.png" action ShowMenu("help")
            imagebutton idle "gui/abouthistory/menu_idle.png" hover "gui/abouthistory/menu_hover.png" action ShowMenu("preferences")
            imagebutton idle "gui/abouthistory/menu_idle.png" hover "gui/abouthistory/menu_hover.png" action ShowMenu("load")
            imagebutton idle "gui/abouthistory/menu_idle.png" hover "gui/abouthistory/menu_hover.png" action ShowMenu("save")
            imagebutton idle "gui/abouthistory/menu_idle.png" hover "gui/abouthistory/menu_hover.png" action MainMenu()
            imagebutton idle "gui/abouthistory/menu_idle.png" hover "gui/abouthistory/menu_hover.png" action Quit()
        frame:
            style "storybook_options_frame"
            use file_slots(_("Save"))

screen load():
    tag menu
    add "gui/SaveLoad/saveload_ground.png"
    hbox:
        spacing 0
        # Left tab navigation
        vbox:
            spacing 10
            imagebutton idle "gui/abouthistory/menu_idle.png" hover "gui/abouthistory/menu_hover.png" action ShowMenu("history")
            imagebutton idle "gui/abouthistory/menu_idle.png" hover "gui/abouthistory/menu_hover.png" action ShowMenu("about")
            imagebutton idle "gui/abouthistory/menu_idle.png" hover "gui/abouthistory/menu_hover.png" action ShowMenu("help")
            imagebutton idle "gui/abouthistory/menu_idle.png" hover "gui/abouthistory/menu_hover.png" action ShowMenu("preferences")
            imagebutton idle "gui/abouthistory/menu_idle.png" hover "gui/abouthistory/menu_hover.png" action ShowMenu("load")
            imagebutton idle "gui/abouthistory/menu_idle.png" hover "gui/abouthistory/menu_hover.png" action ShowMenu("save")
            imagebutton idle "gui/abouthistory/menu_idle.png" hover "gui/abouthistory/menu_hover.png" action MainMenu()
            imagebutton idle "gui/abouthistory/menu_idle.png" hover "gui/abouthistory/menu_hover.png" action Quit()
        frame:
            style "storybook_options_frame"
            use file_slots(_("Load"))

screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):

        fixed:

            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True

            ## The page name, which can be edited by clicking on a button.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Buttons to access other pages.
            vbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                hbox:
                    xalign 0.5

                    spacing gui.page_spacing

                    textbutton _("<") action FilePagePrevious()
                    key "save_page_prev" action FilePagePrevious()

                    if config.has_autosave:
                        textbutton _("{#auto_page}A") action FilePage("auto")

                    if config.has_quicksave:
                        textbutton _("{#quick_page}Q") action FilePage("quick")

                    ## range(1, 10) gives the numbers from 1 to 9.
                    for page in range(1, 10):
                        textbutton "[page]" action FilePage(page)

                    textbutton _(">") action FilePageNext()
                    key "save_page_next" action FilePageNext()

                if config.has_sync:
                    if CurrentScreenName() == "save":
                        textbutton _("Upload Sync"):
                            action UploadSync()
                            xalign 0.5
                    else:
                        textbutton _("Download Sync"):
                            action DownloadSync()
                            xalign 0.5


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5

style page_label_text:
    textalign 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.text_properties("page_button")


## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():
    tag menu
    imagemap:
        ground 'gui/Config/config_ground.png'
        idle 'gui/Config/config_idle.png'
        hover 'gui/Config/config_hover.png'
        selected_idle 'gui/Config/config_sidle.png'
        selected_hover 'gui/Config/config_shover.png'
        cache False
        hotspot (547, 275, 201, 59) action Preference('display', 'fullscreen')
        hotspot (547, 347, 201, 53) action Preference('display', 'window')
        hotspot (547, 504, 126, 54) action Preference('skip', 'seen')
        hotspot (547, 574, 101, 54) action Preference('skip', 'all')
        hotspot (547, 718, 266, 59) action Preference('after choices', 'skip')
        hotspot (547, 794, 129, 55) action Preference('after choices', 'stop')
        hotbar (1053, 291, 372, 37) value Preference('text speed')
        hotbar (1053, 466, 372, 37) value Preference('music volume')
        hotbar (1053, 640, 372, 37) value Preference('sound volume')
        hotbar (1053, 816, 372, 37) value Preference('auto-forward time')
        hotspot (85, 263, 233, 90) action ShowMenu('history')
        hotspot (1584, 245, 239, 91) action ShowMenu('about')
        hotspot (1584, 411, 242, 98) action ShowMenu('help')
        hotspot (75, 613, 246, 88) action ShowMenu('preferences')
        hotspot (75, 483, 257, 91) action ShowMenu('load')
        hotspot (82, 366, 265, 90) action ShowMenu('save')
        hotspot (1584, 537, 254, 91) action MainMenu()
        hotspot (1601, 698, 229, 96) action Quit()
        hotspot (1448, 183, 64, 65) action Return()

style storybook_label:
    font "gui/font/MorrisRomanAlternate-Black.ttf"
    size 36
    color "#3a2a1a"

style storybook_button:
    font "gui/font/MorrisRomanAlternate-Black.ttf"
    size 30
    background None
    color "#3a2a1a"

style storybook_options_frame:
    background None
    padding (40, 40, 40, 40)

style storybook_slider is bar:
    left_bar "gui/slider/horizontal_idle_bar.png"
    right_bar "gui/slider/horizontal_hover_bar.png"
    thumb "gui/slider/horizontal_idle_thumb.png"
    ysize 38

style storybook_return_button:
    font "gui/font/MorrisRomanAlternate-Black.ttf"
    size 30
    background None
    color "#3a2a1a"
    xpos 0.05
    ypos 0.95
    xanchor 0.0
    yanchor 1.0


## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():
    tag menu
    imagemap:
        ground 'gui/abouthistory/menu_idle.png'
        idle 'gui/abouthistory/menu_idle.png'
        hover 'gui/abouthistory/menu_hover.png'
        selected_idle 'gui/abouthistory/menu_hover.png'
        selected_hover 'gui/abouthistory/menu_hover.png'
        cache False
        hotspot (85, 263, 233, 90) action ShowMenu('history')
        hotspot (1584, 245, 239, 91) action ShowMenu('about')
        hotspot (1584, 411, 242, 98) action ShowMenu('help')
        hotspot (75, 613, 246, 88) action ShowMenu('preferences')
        hotspot (75, 483, 257, 91) action ShowMenu('load')
        hotspot (82, 366, 265, 90) action ShowMenu('save')
        hotspot (1584, 537, 254, 91) action MainMenu()
        hotspot (1601, 698, 229, 96) action Quit()
        hotspot (1448, 183, 64, 65) action Return()
    vbox:
        xalign 0.3
        ypos 250
        viewport id "vpgrid":
            yinitial 1.0
            mousewheel True
            xmaximum 500
            ymaximum 620
            yfill True
            vbox:
                for h in _history_list:
                    $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                    text what:
                        substitute False
                    if h.who:
                        text "— " + h.who xalign 1.0 text_align 1.0
                    add "gui/abouthistory/divider.png" xalign 0.5
                if not _history_list:
                    label _("The dialogue history is empty.")


## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    textalign gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    textalign gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():
    tag menu
    add "gui/abouthistory/menu_idle.png"
    style_prefix "help"
    default device = "keyboard"
    hbox:
        spacing 0
        vbox:
            spacing 10
            imagebutton idle "gui/abouthistory/menu_idle.png" hover "gui/abouthistory/menu_hover.png" action ShowMenu("history")
            imagebutton idle "gui/abouthistory/menu_idle.png" hover "gui/abouthistory/menu_hover.png" action ShowMenu("about")
            imagebutton idle "gui/abouthistory/menu_idle.png" hover "gui/abouthistory/menu_hover.png" action ShowMenu("help")
            imagebutton idle "gui/abouthistory/menu_idle.png" hover "gui/abouthistory/menu_hover.png" action ShowMenu("preferences")
            imagebutton idle "gui/abouthistory/menu_idle.png" hover "gui/abouthistory/menu_hover.png" action ShowMenu("load")
            imagebutton idle "gui/abouthistory/menu_idle.png" hover "gui/abouthistory/menu_hover.png" action ShowMenu("save")
            imagebutton idle "gui/abouthistory/menu_idle.png" hover "gui/abouthistory/menu_hover.png" action MainMenu()
            imagebutton idle "gui/abouthistory/menu_idle.png" hover "gui/abouthistory/menu_hover.png" action Quit()
        frame:
            style "storybook_options_frame"
            vbox:
                spacing 20
                hbox:
                    imagebutton auto "gui/HelpButtons/keyboard_%s.png" focus_mask True action SetScreenVariable("device", "keyboard")
                    imagebutton auto "gui/HelpButtons/mouse_%s.png" focus_mask True action SetScreenVariable("device", "mouse")
                    if GamepadExists():
                        imagebutton auto "gui/HelpButtons/gamepad_%s.png" focus_mask True action SetScreenVariable("device", "gamepad")
                if device == "keyboard":
                    use keyboard_help
                elif device == "mouse":
                    use mouse_help
                elif device == "gamepad":
                    use gamepad_help

screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")

    hbox:
        label "Shift+A"
        text _("Opens the accessibility menu.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")

    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide, B/Right Button")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    textalign 1.0



################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action

    ## Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    textalign 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.text_properties("confirm_button")


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    textalign gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    textalign gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    textalign gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.text_properties("nvl_button")


## Bubble screen ###############################################################
##
## The bubble screen is used to display dialogue to the player when using speech
## bubbles. The bubble screen takes the same parameters as the say screen, must
## create a displayable with the id of "what", and can create displayables with
## the "namebox", "who", and "window" ids.
##
## https://www.renpy.org/doc/html/bubble.html#bubble-screen

screen bubble(who, what):
    style_prefix "bubble"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "bubble_namebox"

                text who:
                    id "who"

        text what:
            id "what"

style bubble_window is empty
style bubble_namebox is empty
style bubble_who is default
style bubble_what is default

style bubble_window:
    xpadding 30
    top_padding 5
    bottom_padding 5

style bubble_namebox:
    xalign 0.5

style bubble_who:
    xalign 0.5
    textalign 0.5
    color "#000"

style bubble_what:
    align (0.5, 0.5)
    text_align 0.5
    layout "subtitle"
    color "#000"

define bubble.frame = Frame("gui/bubble.png", 55, 55, 55, 95)
define bubble.thoughtframe = Frame("gui/thoughtbubble.png", 55, 55, 55, 55)

define bubble.properties = {
    "bottom_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "bottom_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "top_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "top_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "thought" : {
        "window_background" : bubble.thoughtframe,
    }
}

define bubble.expand_area = {
    "bottom_left" : (0, 0, 0, 22),
    "bottom_right" : (0, 0, 0, 22),
    "top_left" : (0, 22, 0, 0),
    "top_right" : (0, 22, 0, 0),
    "thought" : (0, 0, 0, 0),
}



################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Menu") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 900


## screens.rpy - This file defines the user interface screens for the supernatural dating sim.

################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input

# Gallery Screen
screen gallery():
    tag menu
    if renpy.loadable("gui/gallery.png"):
        add "gui/gallery.png"
    else:
        add Solid("#e7cfa0")
    # Top right red X button for return/close
    imagebutton idle "gui/abouthistory/close_idle.png" hover "gui/abouthistory/close_hover.png" xpos 1750 ypos 60 action Return()
    hbox:
        spacing 0
        # Left vertical category tabs
        vbox:
            spacing 20
            imagebutton idle "gui/gallery/tab_general_idle.png" hover "gui/gallery/tab_general_hover.png" action ShowMenu("galleryGeneral")
            imagebutton idle "gui/gallery/tab_yukionna_idle.png" hover "gui/gallery/tab_yukionna_hover.png" action ShowMenu("galleryYukiOnna")
            # Add more character tabs as needed, e.g.:
            # imagebutton idle "gui/gallery/tab_character_idle.png" hover "gui/gallery/tab_character_hover.png" action ShowMenu("galleryCharacter")
            imagebutton idle "gui/gallery/tab_return_idle.png" hover "gui/gallery/tab_return_hover.png" action Return()
        frame:
            style "storybook_options_frame"
            vbox:
                spacing 40
                text "Gallery" style "game_menu_label"
                # Placeholder for 3x3 grid of CG slots (locked state)
                grid 3 3:
                    spacing 30
                    for i in range(9):
                        frame:
                            xsize 200
                            ysize 120
                            vbox:
                                spacing 5
                                add "gui/gallery/locked_icon.png" xalign 0.5
                                text "Locked" xalign 0.5 style "storybook_gallery_button"

screen galleryGeneral():
    tag menu
    if renpy.loadable("gui/gallery.png"):
        add "gui/gallery.png"
    else:
        add Solid("#e7cfa0")
    imagebutton idle "gui/abouthistory/close_idle.png" hover "gui/abouthistory/close_hover.png" xpos 1750 ypos 60 action Return()
    hbox:
        spacing 0
        vbox:
            spacing 20
            imagebutton idle "gui/abouthistory/menu_idle.png" hover "gui/abouthistory/menu_hover.png" action ShowMenu("galleryGeneral")
            imagebutton idle "gui/abouthistory/menu_idle.png" hover "gui/abouthistory/menu_hover.png" action ShowMenu("galleryYukiOnna")
            # Add more character tabs as needed
            null height 40
            vbox:
                imagebutton idle "gui/abouthistory/menu_idle.png" hover "gui/abouthistory/menu_hover.png" action Return()
                text "Return" xalign 0.5
            vbox:
                imagebutton idle "gui/abouthistory/menu_idle.png" hover "gui/abouthistory/menu_hover.png" action MainMenu()
                text "Main Menu" xalign 0.5
        frame:
            style "storybook_options_frame"
            vbox:
                spacing 40
                text "General" style "game_menu_label"
                grid 3 3:
                    spacing 30
                    for i in range(1, 10):
                        $ unlocked = getattr(persistent, f'pg1_{i}', False)
                        if unlocked:
                            imagebutton idle f"images/CGs/preview/pg1_{i}.png" hover f"images/CGs/preview/pg1_{i}.png" action Show(f"cg images/CGs/Page1/{i}.png") xsize 200 ysize 120
                        else:
                            imagebutton idle "images/CGs/preview/locked.png" hover "images/CGs/preview/locked.png" action NullAction() xsize 200 ysize 120