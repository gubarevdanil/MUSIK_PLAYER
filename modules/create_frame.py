import customtkinter as ctk
import modules.app_screen as m_app
import modules.search_path as m_path
import os

track_names = ctk.CTkFont(
    family = 'Comic Sans MS',
    size = 20
)



# Создаем класс Frame
class Frame(ctk.CTkFrame):
    def __init__(self, width, height, fg_color, master, corner_radius, track_list, text, border_width, **kwargs):
        super().__init__(width = width, height = height, fg_color = fg_color, master = master, corner_radius = corner_radius, border_width = border_width, **kwargs)
        self.TRACK_LIST = self.track_names(text = track_list, text_color = 'black', fg_color = 'transparent', bg_color='transparent')
        self.TRACK_LIST.place(x = 24, y = 15)
        
    def track_names(self, text, text_color, fg_color, bg_color):
        return ctk.CTkLabel(
            master = m_app.screen_app.FRAME_TRACK,
            text = text,
            font = track_names,
            text_color = 'black',
            fg_color = 'transparent',
            bg_color = 'transparent'
        )

        


    
    

# Создаем фрейм для списка треков с помощью класса Frame


    
