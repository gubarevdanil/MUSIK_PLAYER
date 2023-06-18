import customtkinter as ctk
# import modules.create_frame as m_frame

ctk.set_appearance_mode("dark")

app_width = 454
app_height = 469

class App(ctk.CTk):
    def __init__(self, app_width, app_height):
        super().__init__()
        self.APP_HEIGHT = app_height
        self.APP_WIDTH = app_width
        # self.SCREEN_HEIGHT = self.winfo_screenheight()
        # self.SCREEN_WIDTH = self.winfo_screenwidth()
        self.geometry("454x469")
        self.title("Player")
        self.resizable(False, False),
        self.FRAME_TRACK = ctk.CTkFrame(
            width = 233, 
            height = 367, 
            fg_color = "#bdbdbd",
            master = self, 
            corner_radius = 15, 
            border_width = 3)
        self.FRAME_TRACK.place(x = 130.5, y = 198.5, anchor = ctk.CENTER)
        
        self.TRACK_NAME = ctk.CTkFrame(
            width = 170,
            height = 55,
            master = self,
            fg_color = "#bdbdbd",
            corner_radius = 15, 
            border_width = 3)
        self.TRACK_NAME.place(x = 352.5, y = 15, anchor = ctk.N)


screen_app = App(app_width, app_height)

