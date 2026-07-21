import customtkinter as ctk


class LoginView(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        # Menempelkan main frame ke master (window utama)
        self.grid(row=0, column=0, sticky="nsew")

        # Konfigurasi master agar frame ini memenuhi layar
        master.grid_rowconfigure(0, weight=1)
        master.grid_columnconfigure(0, weight=1)

        # KUNCI PERBAIKAN: Mengatur row dan column weight agar panel kiri & kanan membagi layar 50:50
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)  # Panel Kiri
        self.grid_columnconfigure(1, weight=1)  # Panel Kanan

        self.create_left_panel()
        self.create_right_panel()

    def create_left_panel(self):
        # Gunakan corner_radius=0 agar menempel rapi di pojok kiri layar
        left = ctk.CTkFrame(self, corner_radius=0)
        left.grid(row=0, column=0, sticky="nsew")

        # Teks Judul SMART POS
        title = ctk.CTkLabel(
            left, text="SMART POS", font=("Segoe UI", 34, "bold")
        )
        title.place(relx=0.5, rely=0.45, anchor="center")

        # Teks Subjudul
        subtitle = ctk.CTkLabel(
            left, text="Desktop Point of Sales", font=("Segoe UI", 16)
        )
        subtitle.place(relx=0.5, rely=0.53, anchor="center")

    def create_right_panel(self):
        right = ctk.CTkFrame(self, fg_color="transparent")
        right.grid(row=0, column=1, sticky="nsew")

        # Konfigurasi grid di dalam panel kanan agar box login otomatis di tengah
        right.grid_rowconfigure(0, weight=1)
        right.grid_columnconfigure(0, weight=1)

        # Box Kontainer Login (diberi padding/tinggi otomatis dari elemen di dalamnya)
        frame = ctk.CTkFrame(right, width=380)
        frame.grid(row=0, column=0, padx=20, pady=20)
        # Mencegah frame menyusut agar properti width=380 tetap dipatuhi
        frame.grid_propagate(False)
        frame.configure(height=320)  # Menentukan tinggi box login agar proporsional

        # Judul Login
        title = ctk.CTkLabel(
            frame, text="Login", font=("Segoe UI", 26, "bold")
        )
        title.pack(pady=(30, 20))

        # Input Username
        username = ctk.CTkEntry(
            frame, width=280, placeholder_text="Username"
        )
        username.pack(pady=10)

        # Input Password
        password = ctk.CTkEntry(
            frame, width=280, placeholder_text="Password", show="*"
        )
        password.pack(pady=10)

        # Tombol Login
        login = ctk.CTkButton(
            frame, text="LOGIN", width=280, height=40, font=("Segoe UI", 14, "bold")
        )
        login.pack(pady=(25, 30))


# --- Kode untuk Test Run (Opsional) ---
if __name__ == "__main__":
    app = ctk.CTk()
    app.title("Smart POS - Login")
    app.geometry("900, 550")  # Ukuran standar layar login bimodal
    login_view = LoginView(app)
    app.mainloop()