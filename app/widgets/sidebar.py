import customtkinter as ctk


class Sidebar(ctk.CTkFrame):

    def __init__(self, master, menu_callback):

        super().__init__(
            master,
            width=220,
            corner_radius=0
        )

        # Simpan callback dari MainWindow
        self.menu_callback = menu_callback

        self.grid_rowconfigure(8, weight=1)

        title = ctk.CTkLabel(
            self,
            text="SMART POS",
            font=("Segoe UI", 22, "bold")
        )

        title.grid(
            row=0,
            column=0,
            padx=20,
            pady=(30, 40)
        )

        menus = [
            "Dashboard",
            "Produk",
            "Kategori",
            "Supplier",
            "Penjualan",
            "Pembelian",
            "Laporan"
        ]

        for i, menu in enumerate(menus):

            btn = ctk.CTkButton(
                self,
                text=menu,
                height=40,
                anchor="w",
                command=lambda m=menu: self.menu_callback(m)
            )

            btn.grid(
                row=i + 1,
                column=0,
                padx=15,
                pady=6,
                sticky="ew"
            )

        logout = ctk.CTkButton(
            self,
            text="Logout",
            fg_color="red"
        )

        logout.grid(
            row=9,
            column=0,
            padx=15,
            pady=20,
            sticky="ew"
        )