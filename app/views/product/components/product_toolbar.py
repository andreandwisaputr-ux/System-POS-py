"""
Product Toolbar Component
"""

import customtkinter as ctk


class ProductToolbar(ctk.CTkFrame):
    """
    Toolbar Product Module.
    """

    def __init__(
        self,
        master,
        on_add=None,
        on_edit=None,
        on_delete=None,
        on_search=None,
    ) -> None:
        super().__init__(master)

        self.on_add = on_add
        self.on_edit = on_edit
        self.on_delete = on_delete
        self.on_search = on_search

        self.create_widgets()

    # ==================================================
    # UI
    # ==================================================

    def create_widgets(self) -> None:

        self.grid_columnconfigure(3, weight=1)

        # -----------------------------
        # Add Button
        # -----------------------------
        add_button = ctk.CTkButton(
            self,
            text="+ Tambah",
            command=self.on_add
        )

        add_button.grid(
            row=0,
            column=0,
            padx=(10, 5),
            pady=10
        )

        # -----------------------------
        # Edit Button
        # -----------------------------
        edit_button = ctk.CTkButton(
            self,
            text="✏ Edit",
            command=self.on_edit
        )

        edit_button.grid(
            row=0,
            column=1,
            padx=5,
            pady=10
        )

        # -----------------------------
        # Delete Button
        # -----------------------------
        delete_button = ctk.CTkButton(
            self,
            text="🗑 Hapus",
            command=self.on_delete
        )

        delete_button.grid(
            row=0,
            column=2,
            padx=5,
            pady=10
        )

        # -----------------------------
        # Search Entry
        # -----------------------------
        self.search_entry = ctk.CTkEntry(
            self,
            width=250,
            placeholder_text="Cari produk..."
        )

        self.search_entry.grid(
            row=0,
            column=4,
            padx=10,
            pady=10,
            sticky="e"
        )

        self.search_entry.bind(
            "<KeyRelease>",
            self._on_search
        )

    # ==================================================
    # Event
    # ==================================================

    def _on_search(self, event) -> None:
        """
        Dipanggil setiap user mengetik pada Search Entry.
        """

        if self.on_search:
            self.on_search()

    # ==================================================
    # Public Method
    # ==================================================

    def get_search_keyword(self) -> str:
        """
        Mengambil keyword pencarian.
        """

        return self.search_entry.get().strip()

    def clear_search(self) -> None:
        """
        Mengosongkan Search Entry.
        """

        self.search_entry.delete(0, "end")