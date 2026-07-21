"""
File    : application.py
Project : SMART POS

Application Container
Merakit seluruh dependency aplikasi.
"""

import customtkinter as ctk

from app.database.database_manager import DatabaseManager
from app.views.main_window import MainWindow


class Application:

    def __init__(self):

        # Membuat window utama
        self.window = ctk.CTk()

        self.window.title("POS SYSTEM")
        self.window.geometry("1400x800")

        # Database
        self.db = DatabaseManager()

        # Main Window
        self.main_window = MainWindow(self.window)

    def run(self):

        self.window.mainloop()