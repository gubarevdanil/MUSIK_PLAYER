import customtkinter as ctk
import modules.app_screen as m_app
import PIL
import modules.search_path as m_path
import modules.create_frame as m_frame
import modules.button_func as m_func

class Button(ctk.CTkButton):
    def __init__ (self, master, width, height, border_width, corner_radius, text, fg_color, command, **kwargs):
        super().__init__(master = master,
                         width = width,
                         height = height,
                         border_width = border_width,
                         corner_radius = corner_radius,
                         text = text,
                         fg_color = fg_color,
                         command = command,
                         **kwargs)
    


# Воспроизвести
button_1 = Button(master=m_app.screen_app, 
                  width=169, 
                  height=60, 
                  border_width=2, 
                  corner_radius=20,
                  text="",
                  fg_color="#bdbdbd",
                  image = ctk.CTkImage(dark_image = PIL.Image.open(m_path.path_search("images/play.png")), size = (43,43)),
                  command = m_func.play_music
                  )
button_1.place(x = 352.5, y = 115, anchor = ctk.CENTER)

# Вперед
button_2 = Button(master=m_app.screen_app, 
                  width=61, 
                  height=58, 
                  border_width=2, 
                  corner_radius=20,
                  text="",
                  fg_color="#bdbdbd",
                  image = ctk.CTkImage(dark_image = PIL.Image.open(m_path.path_search("images/forward.png")), size = (27,22)),
                  command = m_func.next_track
                  )
button_2.place(x = 298.5, y = 194, anchor=ctk.CENTER)

# Назад
button_3 = Button(master=m_app.screen_app, 
                  width=61, 
                  height=58, 
                  border_width=2, 
                  corner_radius=20,
                  text="",
                  fg_color="#bdbdbd",
                  image = ctk.CTkImage(dark_image = PIL.Image.open(m_path.path_search("images/back.png")), size = (27,22)),
                  command = m_func.past_track
                  )
button_3.place(x = 406.5, y = 194, anchor=ctk.CENTER)

# Пауза
button_4 = Button(master=m_app.screen_app, 
                  width=169, 
                  height=60, 
                  border_width=2, 
                  corner_radius=20,
                  text="",
                  fg_color="#bdbdbd",
                  image = ctk.CTkImage(dark_image = PIL.Image.open(m_path.path_search("images/pause.png")), size = (44,44)),
                  command = m_func.pause_music
                  )
button_4.place(x = 352.5, y = 273, anchor=ctk.CENTER)


# Остановить
button_5 = Button(master=m_app.screen_app, 
                  width=169, 
                  height=60, 
                  border_width=2, 
                  corner_radius=20,
                  text="",
                  fg_color="#bdbdbd",
                  image = ctk.CTkImage(dark_image = PIL.Image.open(m_path.path_search("images/stop.png")), size = (36,36)),
                  command = m_func.stop_music
                  )
button_5.place(x = 352.5, y = 353, anchor=ctk.CENTER)

# Звук -
button_6 = Button(master=m_app.screen_app, 
                  width=61, 
                  height=58, 
                  border_width=2, 
                  corner_radius=20,
                  text="",
                  fg_color="#bdbdbd",
                  image = ctk.CTkImage(dark_image = PIL.Image.open(m_path.path_search("images/volume_minus.png")), size = (33,34)),
                  command = m_func.volume_down
                  )
button_6.place(x = 399.5, y = 426, anchor=ctk.CENTER)

# Звук +
button_7 = Button(master=m_app.screen_app, 
                  width=61, 
                  height=58, 
                  border_width=2, 
                  corner_radius=20,
                  text="",
                  fg_color="#bdbdbd",
                  image = ctk.CTkImage(dark_image = PIL.Image.open(m_path.path_search("images/volume_plus.png")), size = (35,33)),
                  command = m_func.volume_up
                  )
button_7.place(x = 313.5, y = 426, anchor=ctk.CENTER)

# Рандом
button_8 = Button(master=m_app.screen_app, 
                  width=61, 
                  height=58, 
                  border_width=2, 
                  corner_radius=20,
                  text="",
                  fg_color="#bdbdbd",
                  image = ctk.CTkImage(dark_image = PIL.Image.open(m_path.path_search("images/random.png")), size = (37,33)),
                  command = m_func.random_tracks
                  )
button_8.place(x = 227.5, y = 426, anchor=ctk.CENTER)

# Удалить
button_9 = Button(master=m_app.screen_app, 
                  width=61, 
                  height=58, 
                  border_width=2, 
                  corner_radius=20,
                  text="",
                  fg_color="#bdbdbd",
                  image = ctk.CTkImage(dark_image = PIL.Image.open(m_path.path_search("images/delete.png")), size = (31,37)),
                  command = m_func.delete
                  )
button_9.place(x = 141.5, y = 426, anchor=ctk.CENTER)

# Добавить
button_10 = Button(master=m_app.screen_app, 
                  width=61, 
                  height=58, 
                  border_width=2, 
                  corner_radius=20,
                  text="",
                  fg_color="#bdbdbd",
                  image = ctk.CTkImage(dark_image = PIL.Image.open(m_path.path_search("images/plus.png")), size = (26,26)),
                  command = m_func.add_track
                  )
button_10.place(x = 55.5, y = 426, anchor=ctk.CENTER)


