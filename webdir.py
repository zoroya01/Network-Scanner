import dearpygui.dearpygui as dpg
from fontsetup import setUp

def resize():
    width,height=dpg.get_viewport_width(),dpg.get_viewport_height()
    dpg.set_item_width("main_window",width)
    dpg.set_item_height("main_window",height)
    
    dpg.set_item_pos("ip_text",[(width/2)-150,(height/2)-40])
    dpg.set_item_pos("input",[(width/2)-10,(height/2)-40])
    dpg.set_item_pos("scan_button",[(width/2)-10,(height/2)+70])
    dpg.set_item_pos("ws_text",[(width/2)-150,(height/2)+10])
    dpg.set_item_pos("input_ws",[(width/2)-10,(height/2)+10])
    dpg.set_item_pos("browse_button",[(width/2)+200,(height/2)+10])
    dpg.set_item_pos("back_button",[(width/2)+260,(height/2)-290])
    
def hostlookupgui():
    with dpg.window(tag="main_window",label="Web Sub-directory Scanner",pos=(0,0),no_title_bar=True,no_resize=True,no_move=True):
        dpg.add_text("Web Sub-directory Scanner",tag="wss",color=(255,255,255,255))
        dpg.add_separator(tag="separator")
        dpg.add_text("Enter The URL Here:",tag="ip_text",color=(255,255,255,255))
        dpg.add_input_text(tag="input",height=30, width=200, multiline=True)
        dpg.add_text("Select Wordlist:",tag='ws_text',color=(255,255,255,255))
        dpg.add_input_text(tag="input_ws",height=30,width=200,multiline=True)
        dpg.add_button(label="Scan",tag="scan_button",pos=(0,0),width=100,height=30)
        dpg.add_button(label="Browse",tag="browse_button",pos=(0,0),width=100,height=30)
        dpg.add_button(label="Back",tag="back_button",pos=(0,0),width=100,height=30)
        
        

        with dpg.theme(tag="button_theme"):
                with dpg.theme_component(dpg.mvButton):
                    dpg.add_theme_color(dpg.mvThemeCol_Button, (22, 234, 147, 180))  # Background color
                    dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (0, 128, 0))  # Hover color
                    dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (66, 150, 250, 255))  # Active color
                    dpg.add_theme_color(dpg.mvThemeCol_Text, (255, 255, 255, 255))  # Text color
                    dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 5)  # Rounded corners
                    dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 10, 10)  # Padding
                    
        with dpg.theme(tag="input_theme"):
            with dpg.theme_component(dpg.mvInputText):
                dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (0, 128, 0))  # Dark green background
                dpg.add_theme_color(dpg.mvThemeCol_Text, (255, 255, 255))  # White text
                dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 5)  # Rounded corners
                
        with dpg.font_registry():
            heading_font = dpg.add_font("arialbd.ttf", 30)
                
        with dpg.font_registry():
            my_font = dpg.add_font("arialbd.ttf", 30)
        
        
                    
                    
    dpg.bind_item_theme("scan_button", "button_theme")
    dpg.bind_item_theme("input", "input_theme")
    dpg.bind_item_font("wss",setUp())
    dpg.bind_item_theme("input","my_font")
    dpg.bind_item_font("wss", heading_font)
    dpg.bind_item_theme("input_ws","my_font")
    dpg.bind_item_theme("browse_button","button_theme")
    dpg.bind_item_theme("back_button","button_theme")
    
    
    resize()
    dpg.set_viewport_resize_callback(lambda:resize())
if __name__=="__main__":
    dpg.create_context()
    dpg.create_viewport(title='Web Sub-directory Scanner',width=800,height=600)
    dpg.setup_dearpygui()
        
    hostlookupgui()
        
    dpg.show_viewport()
    dpg.start_dearpygui()
        
    dpg.destroy_context()