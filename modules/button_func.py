import customtkinter as ctk
import modules.app_screen as m_app
import modules.create_frame as m_frame
import modules.search_path as m_path
#import modules.pass_label as p_l

# from tkinter import Listbox
import pygame
import os
import random


pygame.init()
pygame.mixer.init()

list_sounds = []
list_sounds1 = []

tracks_in_program = []
track_nume = False
lost = 5

def add_track():
    global lost
    global file_path
    global label
    global track_nume
    global peremeni
    file_path = ctk.filedialog.askopenfilename(initialdir="track/", filetypes=(("mp3", "*.mp3;*.wav"),))
    if file_path:
        list_sounds.append(file_path)
    file_path1 = os.path.splitext(os.path.basename(file_path))[0]
    update_tracks()
    if file_path1:
        list_sounds1.append(file_path1)
        update_tracks()
    if track_nume == True:
        label.destroy()
        
    # if list_sounds1 == list_sounds2:
    #     pass
  
def update_tracks():
    global label
    textx = 24
    texty = 15
    for widget in m_app.screen_app.FRAME_TRACK.winfo_children():
        widget.destroy()
    for widget in m_app.screen_app.TRACK_NAME.winfo_children():
        widget.destroy()
    for i, track in enumerate(list_sounds1):
        label = ctk.CTkLabel(
        master = m_app.screen_app.FRAME_TRACK, 
        text = f"{track}", 
        text_color = "black", 
        font = m_frame.track_names)
        label.place(x = textx, y = texty)
        texty = texty + 30

    # for i,track in enumerate(list_sounds1):
    #     label = ctk.CTkLabel(
    #     master = m_app.screen_app.TRACK_NAME, 
    #     text = f"{track}", 
    #     text_color = "black", 
    #     font = m_frame.track_names)
    #     label.place(x = textx, y = texty)
    #     texty = texty + 30

def play_music():
    global track_nume
    global label
    global peremeni
    pygame.mixer.music.load(list_sounds[peremeni])
    pygame.mixer.music.play(1)

    update_tracks()
    label = ctk.CTkLabel(master = m_app.screen_app.TRACK_NAME,
                         text = list_sounds1[peremeni],
                         text_color = "black",
                         font = m_frame.track_names)
    label.place(x = 10, y = 10) 
    track_nume == True

    
def delete():
    global list_sounds
    global peremeni
    global label
    global track_nume


    track_nume = False
    update_tracks()

    pygame.mixer.music.unload()
    list_sounds.pop(peremeni)
    list_sounds1.pop(peremeni)
    peremeni -= True
    update_tracks()

pause = True

def pause_music():
    global pause
    if pause:
        pygame.mixer.music.unpause()
        pause = False
    else:
        pygame.mixer.music.pause()
        pause = True

def stop_music():
    pygame.mixer.music.stop()
    
def volume_up():
    pelmne  = pygame.mixer.music.get_volume()
    pelmne += 0.055
    pygame.mixer.music.set_volume(pelmne)

def volume_down():
    pelmne  = pygame.mixer.music.get_volume()
    pelmne -= 0.055
    pygame.mixer.music.set_volume(pelmne)

peremeni = 0

def next_track():
    global peremeni
    global track_nume
    global label
    if peremeni >= len(list_sounds1):
        pass
    peremeni += True
    pygame.mixer.music.load(list_sounds[peremeni])
    pygame.mixer.music.play(1)


    update_tracks()
    label = ctk.CTkLabel(master = m_app.screen_app.TRACK_NAME,
                         text = list_sounds1[peremeni],
                         text_color = "black",
                         font = m_frame.track_names)
    label.place(x = 10, y = 10) 
    track_nume == True

def past_track():
    global peremeni
    global track_nume
    global label
    if peremeni <= False:
        pass
    peremeni -= True
    pygame.mixer.music.load(list_sounds[peremeni])
    pygame.mixer.music.play(1)


    update_tracks()
    label = ctk.CTkLabel(master = m_app.screen_app.TRACK_NAME,
                         text = list_sounds1[peremeni],
                         text_color = "black",
                         font = m_frame.track_names)
    label.place(x = 10, y = 10)
    track_nume == True 


def random_tracks():
    global peremeni
    global label
    global track_nume
    peremeni = random.randint(0, (len(list_sounds1)) - 1)
    pygame.mixer.music.load(list_sounds[peremeni])
    pygame.mixer.music.play(1)

    update_tracks()
    label = ctk.CTkLabel(master = m_app.screen_app.TRACK_NAME,
                         text = list_sounds1[peremeni],
                         text_color = "black",
                         font = m_frame.track_names)
    label.place(x = 10, y = 10) 
    track_nume == True
