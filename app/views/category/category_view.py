import customtkinter as ctk


class CategoryView(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(master)

        self.pack(fill="both", expand=True)

        title = ctk.CTkLabel(
            self,
            text="Halaman Kategori",
            font=("Segoe UI", 28, "bold")
        )

        title.pack(expand=True)