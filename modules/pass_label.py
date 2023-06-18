import customtkinter as ctk
import pygame

pass_text = ctk.CTkFont(
    family = 'Comic Sans MS',
    size = 20,
    text = "---------------------",
    text_color = "gray"
)

pass_lable = ctk.CTkLabel(
    text = pass_text,
    text_color = pass_text,
    fg_color = 'grey',
    bg_color = 'transparent'
)
