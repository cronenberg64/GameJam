﻿################################################################################
## Initialization
################################################################################

init offset = -2

init python:
    gui.init(1920, 1080)

define config.check_conflicting_properties = True

################################################################################
## GUI Configuration Variables
################################################################################

## Colors ######################################################################
define gui.accent_color = '#000000'
define gui.idle_color = '#707070'
define gui.idle_small_color = '#606060'
define gui.hover_color = '#000000'
define gui.selected_color = '#555555'
define gui.insensitive_color = '#7070707f'
define gui.muted_color = '#666666'
define gui.hover_muted_color = '#999999'
define gui.text_color = '#404040'
define gui.interface_text_color = '#404040'

## Fonts and Font Sizes ########################################################
define gui.text_font = "DejaVuSans.ttf"
define gui.name_text_font = "DejaVuSans.ttf"
define gui.interface_text_font = "DejaVuSans.ttf"
define gui.text_size = 33
define gui.name_text_size = 45
define gui.interface_text_size = 33
define gui.label_text_size = 36
define gui.notify_text_size = 24
define gui.title_text_size = 75

## Main and Game Menus #########################################################
## Using your custom backgrounds
define gui.main_menu_background = "gui/main_menu.png"
define gui.game_menu_background = "gui/game_menu.png"

## Dialogue ####################################################################
## Using your custom textbox, namebox, and click-to-continue
define gui.textbox_background = "gui/textbox.png"
define gui.namebox_background = "gui/namebox.png"
define gui.ctc = "gui/ctc.png"
define gui.ctc_position = "nestled"

## Speech bubbles for character thoughts
define gui.thoughtbubble_background = "gui/thoughtbubble.png"
define gui.bubble_background = "gui/bubble.png"

define gui.textbox_height = 278
define gui.textbox_yalign = 1.0
define gui.name_xpos = 360
define gui.name_ypos = 0
define gui.name_xalign = 0.0
define gui.namebox_width = None
define gui.namebox_height = None
define gui.namebox_borders = Borders(5, 5, 5, 5)
define gui.namebox_tile = False
define gui.dialogue_xpos = 402
define gui.dialogue_ypos = 75
define gui.dialogue_width = 1116
define gui.dialogue_text_xalign = 0.0

## Buttons #####################################################################
## Using your custom button assets
define gui.button_width = None
define gui.button_height = None
define gui.button_borders = Borders(6, 6, 6, 6)
define gui.button_tile = False
define gui.button_text_font = gui.interface_text_font
define gui.button_text_size = gui.interface_text_size
define gui.button_text_idle_color = gui.idle_color
define gui.button_text_hover_color = gui.hover_color
define gui.button_text_selected_color = gui.selected_color
define gui.button_text_insensitive_color = gui.insensitive_color
define gui.button_text_xalign = 0.0

## Custom button backgrounds from your assets
define gui.button_background = "gui/button/button_idle.png"
define gui.button_hover_background = "gui/button/button_hover.png"
define gui.button_selected_background = "gui/button/button_selected.png"
define gui.button_insensitive_background = "gui/button/button_insensitive.png"

## Button variants
define gui.radio_button_borders = Borders(27, 6, 6, 6)
define gui.check_button_borders = Borders(27, 6, 6, 6)
define gui.confirm_button_text_xalign = 0.5
define gui.page_button_borders = Borders(15, 6, 15, 6)
define gui.quick_button_borders = Borders(15, 6, 15, 0)
define gui.quick_button_text_size = 21
define gui.quick_button_text_idle_color = gui.idle_small_color
define gui.quick_button_text_selected_color = gui.accent_color

## Choice Buttons using your assets - UPDATED FOR CONTRAST
define gui.choice_button_width = 1185
define gui.choice_button_height = None
define gui.choice_button_tile = False
define gui.choice_button_borders = Borders(150, 8, 150, 8)
define gui.choice_button_text_font = gui.text_font
define gui.choice_button_text_size = gui.text_size
define gui.choice_button_text_xalign = 0.5
define gui.choice_button_text_idle_color = '#B8860B'  # Dark goldenrod - supernatural theme
define gui.choice_button_text_hover_color = "#FFD700"  # Gold - bright contrast on hover
define gui.choice_button_text_insensitive_color = '#7070707f'
## New background colors for better contrast
define gui.choice_button_idle_background = "#1C1C1C"  # Very dark grey - mysterious
define gui.choice_button_hover_background = "#2F2F2F"  # Slightly lighter dark on hover

## File Slot Buttons ###########################################################
define gui.slot_button_width = 414
define gui.slot_button_height = 309
define gui.slot_button_borders = Borders(15, 15, 15, 15)
define gui.slot_button_text_size = 21
define gui.slot_button_text_xalign = 0.5
define gui.slot_button_text_idle_color = gui.idle_small_color
define gui.slot_button_text_selected_idle_color = gui.selected_color
define gui.slot_button_text_selected_hover_color = gui.hover_color

define config.thumbnail_width = 384
define config.thumbnail_height = 216
define gui.file_slot_cols = 3
define gui.file_slot_rows = 2

## Positioning and Spacing #####################################################
define gui.navigation_xpos = 60
define gui.skip_ypos = 15
define gui.notify_ypos = 68
define gui.choice_spacing = 33
define gui.navigation_spacing = 6
define gui.pref_spacing = 15
define gui.pref_button_spacing = 0
define gui.page_spacing = 0
define gui.slot_spacing = 15
define gui.main_menu_text_xalign = 1.0

## Frames using your frame.png ################################################
define gui.frame_background = "gui/frame.png"
define gui.frame_borders = Borders(6, 6, 6, 6)
define gui.confirm_frame_borders = Borders(60, 60, 60, 60)
define gui.skip_frame_borders = Borders(24, 8, 75, 8)
define gui.notify_frame_borders = Borders(24, 8, 60, 8)
define gui.frame_tile = False

## Bars, Scrollbars, and Sliders using your assets ###########################
define gui.bar_size = 38
define gui.scrollbar_size = 18
define gui.slider_size = 38
define gui.bar_tile = False
define gui.vbar_tile = False          # Added for consistency
define gui.scrollbar_tile = False
define gui.vscrollbar_tile = False    # Added for consistency
define gui.slider_tile = False
define gui.vslider_tile = False       # Added to fix the AttributeError

## Using your custom bar/scrollbar/slider assets (organized by folders)
## Note: You'll need to organize these into subfolders as shown in the directory structure
define gui.bar_left = "gui/bar/bar_left.png"
define gui.bar_right = "gui/bar/bar_right.png"
define gui.bar_full = "gui/bar/bar_full.png"
define gui.bar_empty = "gui/bar/bar_empty.png"

define gui.scrollbar_top = "gui/scrollbar/scrollbar_top.png"
define gui.scrollbar_bottom = "gui/scrollbar/scrollbar_bottom.png"
define gui.scrollbar_thumb = "gui/scrollbar/scrollbar_thumb.png"

define gui.slider_left = "gui/slider/slider_left.png"
define gui.slider_right = "gui/slider/slider_right.png"
define gui.slider_full = "gui/slider/slider_full.png"
define gui.slider_empty = "gui/slider/slider_empty.png"
define gui.slider_thumb = "gui/slider/slider_thumb.png"

define gui.bar_borders = Borders(6, 6, 6, 6)
define gui.scrollbar_borders = Borders(6, 6, 6, 6)
define gui.slider_borders = Borders(6, 6, 6, 6)
define gui.vbar_borders = Borders(6, 6, 6, 6)
define gui.vscrollbar_borders = Borders(6, 6, 6, 6)
define gui.vslider_borders = Borders(6, 6, 6, 6)

define gui.unscrollable = "hide"

## Skip indicator using your skip.png
define gui.skip_background = "gui/skip.png"

## Notify background using your notify.png
define gui.notify_background = "gui/notify.png"

## NVL Mode using your nvl.png ################################################
define gui.nvl_background = "gui/nvl.png"
define gui.nvl_borders = Borders(0, 15, 0, 30)
define gui.nvl_list_length = 6
define gui.nvl_height = 173
define gui.nvl_spacing = 15
define gui.nvl_name_xpos = 645
define gui.nvl_name_ypos = 0
define gui.nvl_name_width = 225
define gui.nvl_name_xalign = 1.0
define gui.nvl_text_xpos = 675
define gui.nvl_text_ypos = 12
define gui.nvl_text_width = 885
define gui.nvl_text_xalign = 0.0
define gui.nvl_thought_xpos = 360
define gui.nvl_thought_ypos = 0
define gui.nvl_thought_width = 1170
define gui.nvl_thought_xalign = 0.0
define gui.nvl_button_xpos = 675
define gui.nvl_button_xalign = 0.0

## History ####################################################################
define config.history_length = 250
define gui.history_height = 210
define gui.history_spacing = 0
define gui.history_name_xpos = 233
define gui.history_name_ypos = 0
define gui.history_name_width = 233
define gui.history_name_xalign = 1.0
define gui.history_text_xpos = 255
define gui.history_text_ypos = 3
define gui.history_text_width = 1110
define gui.history_text_xalign = 0.0

## Phone/Mobile variant assets
define gui.phone_background = "gui/phone.png"

## Overlay using your overlay assets ##########################################
define gui.overlay_background = "gui/overlay/overlay.png"

## Window icon using your window_icon.png #####################################
define config.window_icon = "gui/window_icon.png"

## Localization ###############################################################
define gui.language = "unicode"

################################################################################
## Mobile devices
################################################################################

init python:
    @gui.variant
    def touch():
        gui.quick_button_borders = Borders(60, 21, 60, 0)

    @gui.variant
    def small():
        gui.text_size = 45
        gui.name_text_size = 54
        gui.notify_text_size = 38
        gui.interface_text_size = 45
        gui.button_text_size = 45
        gui.label_text_size = 51
        gui.textbox_height = 360
        gui.name_xpos = 120
        gui.dialogue_xpos = 135
        gui.dialogue_width = 1650
        gui.slider_size = 54
        gui.choice_button_width = 1860
        gui.choice_button_text_size = 45
        gui.navigation_spacing = 30
        gui.pref_button_spacing = 15
        gui.history_height = 285
        gui.history_text_width = 1035
        gui.quick_button_text_size = 30
        gui.file_slot_cols = 2
        gui.file_slot_rows = 2
        gui.nvl_height = 255
        gui.nvl_name_width = 458
        gui.nvl_name_xpos = 488
        gui.nvl_text_width = 1373
        gui.nvl_text_xpos = 518
        gui.nvl_text_ypos = 8
        gui.nvl_thought_width = 1860
        gui.nvl_thought_xpos = 30
        gui.nvl_button_width = 1860
        gui.nvl_button_xpos = 30