################################################################################
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
define gui.button_background = "gui/button/gallerybutton_idle_blank.png"
define gui.button_hover_background = "gui/button/gallerybutton_selecthover_blank.png"
define gui.button_selected_background = "gui/button/gallerybutton_selecthover_blank.png"
define gui.button_insensitive_background = "gui/button/gallerybutton_selecthover_blank.png"

define gui.quick_button_background = "gui/button/gallerybutton_idle_blank.png"
define gui.quick_button_hover_background = "gui/button/gallerybutton_selecthover_blank.png"
define gui.quick_button_selected_background = "gui/button/gallerybutton_selecthover_blank.png"
define gui.quick_button_insensitive_background = "gui/button/gallerybutton_selecthover_blank.png"

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
define gui.choice_button_text_idle_color = '#fff7d6'  # Light cream for readabilityAdd commentMore actions
define gui.choice_button_text_hover_color = '#000000'  # Lighter cream on hover
define gui.choice_button_text_insensitive_color = '#7070707f'
## New background colors for better contrast
define gui.choice_button_idle_background = '#7c4a03'  # Dark brownAdd commentMore actions
define gui.choice_button_hover_background = '#a86c1d'  # Lighter brown
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
define gui.scrollbar_tile = False
define gui.slider_tile = False

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

################################################################################
## Button Synchronization - Add these to your gui.rpy
################################################################################

## Base Button Style Template (add after your existing button definitions)
define gui.button_text_outlines = [(2, "#000000", 0, 0)]  # Text outline for readability
define gui.button_text_kerning = 0.0  # Letter spacing

## Standardized Button Colors for All Types
define gui.standard_idle_color = '#707070'
define gui.standard_hover_color = '#000000' 
define gui.standard_selected_color = '#555555'
define gui.standard_insensitive_color = '#7070707f'

## Menu Navigation Buttons (to match your custom buttons)
define gui.navigation_button_width = None
define gui.navigation_button_height = None
define gui.navigation_button_tile = False
define gui.navigation_button_borders = Borders(6, 6, 6, 6)
define gui.navigation_button_text_font = gui.interface_text_font
define gui.navigation_button_text_size = gui.interface_text_size
define gui.navigation_button_text_idle_color = gui.standard_idle_color
define gui.navigation_button_text_hover_color = gui.standard_hover_color
define gui.navigation_button_text_selected_color = gui.standard_selected_color

## Quick Menu Sync (already partially defined, ensure consistency)
define gui.quick_button_text_font = gui.interface_text_font
define gui.quick_button_text_hover_color = gui.standard_hover_color

## Preference Buttons
define gui.pref_button_borders = Borders(6, 6, 6, 6)
define gui.pref_button_text_font = gui.interface_text_font
define gui.pref_button_text_size = gui.interface_text_size
define gui.pref_button_text_idle_color = gui.standard_idle_color
define gui.pref_button_text_hover_color = gui.standard_hover_color

## History Screen Buttons
define gui.history_button_borders = Borders(6, 6, 6, 6)
define gui.history_button_text_font = gui.interface_text_font

## Return/Back Buttons
define gui.return_button_borders = Borders(6, 6, 6, 6)
define gui.return_button_text_font = gui.interface_text_font
define gui.return_button_text_size = gui.interface_text_size

################################################################################
## Custom Style Application Function
################################################################################

init python:
    def apply_button_style(button_style):
        """
        Function to apply consistent styling to dynamically created buttons
        Usage: apply_button_style("choice") or apply_button_style("navigation")
        """
        styles = {
            "choice": {
                "background": gui.choice_button_idle_background,
                "hover_background": gui.choice_button_hover_background,
                "text_color": gui.choice_button_text_idle_color,
                "hover_text_color": gui.choice_button_text_hover_color,
                "borders": gui.choice_button_borders,
                "text_size": gui.choice_button_text_size,
                "text_font": gui.choice_button_text_font
            },
            "navigation": {
                "background": gui.button_background,
                "hover_background": gui.button_hover_background,
                "text_color": gui.button_text_idle_color,
                "hover_text_color": gui.button_text_hover_color,
                "borders": gui.button_borders,
                "text_size": gui.button_text_size,
                "text_font": gui.button_text_font
            },
            "standard": {
                "background": gui.button_background,
                "hover_background": gui.button_hover_background,
                "text_color": gui.standard_idle_color,
                "hover_text_color": gui.standard_hover_color,
                "borders": gui.button_borders,
                "text_size": gui.interface_text_size,
                "text_font": gui.interface_text_font
            },
        }
        return styles.get(button_style, styles["standard"])

################################################################################
## Screen Template for Consistent Buttons
################################################################################

## Example of how to use consistent styling in screens
screen example_menu():
    style_prefix "navigation"
    
    vbox:
        spacing gui.navigation_spacing
        
        textbutton _("Start Game"):
            style "navigation_button"
            action Start()
            
        textbutton _("Load Game"):
            style "navigation_button" 
            action ShowMenu("load")
            
        textbutton _("Preferences"):
            style "navigation_button"
            action ShowMenu("preferences")

## Style definitions to match your custom assets
style navigation_button:
    properties gui.button_properties("navigation_button")
    
style navigation_button_text:
    properties gui.text_properties("navigation_button")
    
## Choice button style override to use your custom colors
style choice_button:
    background gui.choice_button_idle_background
    hover_background gui.choice_button_hover_background
    selected_background gui.choice_button_hover_background
    
style choice_button_text:
    color gui.choice_button_text_idle_color
    hover_color gui.choice_button_text_hover_color
    selected_color gui.choice_button_text_hover_color

################################################################################
## Dynamic Button Creation Helper
################################################################################

init python:
    def create_synced_button(text, action, button_type="standard", **kwargs):
        """
        Create a button with synchronized styling
        Usage in screens: use create_synced_button("Button Text", SomeAction(), "choice")
        """
        style_props = apply_button_style(button_type)
        
        button_kwargs = {
            "background": style_props["background"],
            "hover_background": style_props["hover_background"], 
            "text_color": style_props["text_color"],
            "text_hover_color": style_props["hover_text_color"],
            "text_size": style_props["text_size"],
            "text_font": style_props["text_font"]
        }
        
        button_kwargs.update(kwargs)  # Allow override of any property
        
        return button_kwargs

# Main menu button styles using custom diamond/polygonal images
style start_menu_button is default:
    background "gui/main_menu/buttons/start_idle.png"
    hover_background "gui/main_menu/buttons/start_hover.png"
    xsize 500
    ysize 80
    xalign 0.5
    yalign 0.5
    padding (0, 0, 0, 0)
    foreground None

style load_menu_button is default:
    background "gui/main_menu/buttons/load_idle.png"
    hover_background "gui/main_menu/buttons/load_hover.png"
    xsize 500
    ysize 80
    xalign 0.5
    yalign 0.5
    padding (0, 0, 0, 0)
    foreground None

style options_menu_button is default:
    background "gui/main_menu/buttons/options_idle.png"
    hover_background "gui/main_menu/buttons/options_hover.png"
    xsize 500
    ysize 80
    xalign 0.5
    yalign 0.5
    padding (0, 0, 0, 0)
    foreground None

style gallery_menu_button is default:
    background "gui/main_menu/buttons/gallery_idle.png"
    hover_background "gui/main_menu/buttons/gallery_hover.png"
    xsize 500
    ysize 80
    xalign 0.5
    yalign 0.5
    padding (0, 0, 0, 0)
    foreground None

style about_menu_button is default:
    background "gui/main_menu/buttons/about_idle.png"
    hover_background "gui/main_menu/buttons/about_hover.png"
    xsize 500
    ysize 80
    xalign 0.5
    yalign 0.5
    padding (0, 0, 0, 0)
    foreground None

style help_menu_button is default:
    background "gui/main_menu/buttons/help_idle.png"
    hover_background "gui/main_menu/buttons/help_hover.png"
    xsize 500
    ysize 80
    xalign 0.5
    yalign 0.5
    padding (0, 0, 0, 0)
    foreground None

style quit_menu_button is default:
    background "gui/main_menu/buttons/quit_idle.png"
    hover_background "gui/main_menu/buttons/quit_hover.png"
    xsize 500
    ysize 80
    xalign 0.5
    yalign 0.5
    padding (0, 0, 0, 0)
    foreground None