import customtkinter as ctk

from app.application.application import Application

ctk.set_appearance_mode("white")
ctk.set_default_color_theme("green")


app = Application()

app.run()