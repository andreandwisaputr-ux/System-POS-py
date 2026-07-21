import customtkinter as ctk


class Header(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(master, height=70)

        # Kolom tengah akan mengambil sisa ruang
        self.grid_columnconfigure(1, weight=1)

        # Judul halaman
        self.title_label = ctk.CTkLabel(
            self,
            text="Dashboard",
            font=("Segoe UI", 24, "bold")
        )

        self.title_label.grid(
            row=0,
            column=0,
            padx=20,
            pady=15,
            sticky="w"
        )

        # Nama pengguna
        self.user_label = ctk.CTkLabel(
            self,
            text="The Architecht"
        )

        self.user_label.grid(
            row=0,
            column=2,
            padx=20,
            sticky="e"
        )

    def set_title(self, title):
        """
        Mengubah judul yang tampil pada Header.
        """
        self.title_label.configure(text=title)