import customtkinter as ctk


class StatCard(ctk.CTkFrame):

    def __init__(self, master, title, value):

        super().__init__(
            master,
            corner_radius=12,
            height=130
        )

        self.grid_propagate(False)

        self.grid_columnconfigure(0, weight=1)

        title_label = ctk.CTkLabel(
            self,
            text=title,
            font=("Segoe UI", 15)
        )

        title_label.grid(
            row=0,
            column=0,
            pady=(20, 5)
        )

        value_label = ctk.CTkLabel(
            self,
            text=value,
            font=("Segoe UI", 28, "bold")
        )

        value_label.grid(
            row=1,
            column=0
        )