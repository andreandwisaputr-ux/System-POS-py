import customtkinter as ctk


class ProductHeader(ctk.CTkFrame):
    """
    Header Product Module.
    """

    def __init__(self, master):
        super().__init__(
            master,
            fg_color="transparent"
        )

        self.create_widgets()

    def create_widgets(self):

        title = ctk.CTkLabel(
            self,
            text="Manajemen Produk",
            font=("Segoe UI", 24, "bold")
        )

        title.pack(anchor="w")

        subtitle = ctk.CTkLabel(
            self,
            text="Kelola seluruh data produk yang tersedia.",
            font=("Segoe UI", 14)
        )

        subtitle.pack(anchor="w")