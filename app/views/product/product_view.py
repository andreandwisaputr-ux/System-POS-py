import customtkinter as ctk


class ProductView(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(master)

        self.pack(fill="both", expand=True)

        title = ctk.CTkLabel(
            self,
            text="Halaman Produk",
            font=("Segoe UI", 28, "bold")
        )

        title.pack(expand=True)