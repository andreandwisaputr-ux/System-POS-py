import customtkinter as ctk

from app.widgets.stat_card import StatCard


class DashboardView(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(master)

        self.pack(fill="both", expand=True)

        self.grid_columnconfigure((0,1,2,3), weight=1)

        StatCard(self, "Produk", "120").grid(
            row=0,
            column=0,
            padx=10,
            pady=10,
            sticky="ew"
        )

        StatCard(self, "Supplier", "18").grid(
            row=0,
            column=1,
            padx=10,
            pady=10,
            sticky="ew"
        )

        StatCard(self, "Penjualan", "42").grid(
            row=0,
            column=2,
            padx=10,
            pady=10,
            sticky="ew"
        )

        StatCard(self, "Pendapatan", "Rp5.000.000").grid(
            row=0,
            column=3,
            padx=10,
            pady=10,
            sticky="ew"
        )