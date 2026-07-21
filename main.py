import customtkinter as ctk

from app.views.main_window import MainWindow


ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

app = ctk.CTk()

app.title("SMART POS")

app.geometry("1400x800")

MainWindow(app)

app.mainloop()