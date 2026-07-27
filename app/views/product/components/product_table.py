"""
Product Table Component
"""

import customtkinter as ctk
from tkinter import ttk

from app.models.product import Product


class ProductTable(ctk.CTkFrame):
    """
    Komponen tabel Product.
    Bertugas menampilkan daftar produk.
    """

    def __init__(self, master):
        super().__init__(master)

        self.create_widgets()

    # ==================================================
    # UI
    # ==================================================

    def create_widgets(self) -> None:

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.tree = ttk.Treeview(
            self,
            columns=(
                "id",
                "product_name",
                "category",
                "supplier",
                "selling_price",
                "stock",
                "unit",
            ),
            show="headings",
        )

        # ==========================
        # Heading
        # ==========================

        self.tree.heading("id", text="ID")
        self.tree.heading("product_name", text="Nama Produk")
        self.tree.heading("category", text="Kategori")
        self.tree.heading("supplier", text="Supplier")
        self.tree.heading("selling_price", text="Harga Jual")
        self.tree.heading("stock", text="Stok")
        self.tree.heading("unit", text="Satuan")

        # ==========================
        # Column
        # ==========================

        self.tree.column(
            "id",
            width=60,
            anchor="center"
        )

        self.tree.column(
            "product_name",
            width=250,
            anchor="w"
        )

        self.tree.column(
            "category",
            width=180,
            anchor="center"
        )

        self.tree.column(
            "supplier",
            width=180,
            anchor="center"
        )

        self.tree.column(
            "selling_price",
            width=120,
            anchor="e"
        )

        self.tree.column(
            "stock",
            width=90,
            anchor="center"
        )

        self.tree.column(
            "unit",
            width=90,
            anchor="center"
        )

        self.tree.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        scrollbar = ttk.Scrollbar(
            self,
            orient="vertical",
            command=self.tree.yview
        )

        scrollbar.grid(
            row=0,
            column=1,
            sticky="ns"
        )

        self.tree.configure(
            yscrollcommand=scrollbar.set
        )

    # ==================================================
    # Public Method
    # ==================================================

    def load(
        self,
        products: list[Product]
    ) -> None:
        """
        Memuat data produk ke dalam Treeview.
        """

        self.clear()

        for product in products:

            self.tree.insert(
                "",
                "end",
                values=(
                    product.id,
                    product.product_name,
                    product.category_name,
                    product.supplier_name,
                    f"{product.selling_price:,.0f}",
                    product.stock,
                    product.unit,
                ),
            )

    def clear(self) -> None:
        """
        Menghapus seluruh isi Treeview.
        """

        for item in self.tree.get_children():
            self.tree.delete(item)

    def get_selected_id(self) -> int | None:
        """
        Mengambil ID produk yang dipilih.
        """

        selected = self.tree.selection()

        if not selected:
            return None

        values = self.tree.item(
            selected[0],
            "values"
        )

        return int(values[0])

    def get_selected_item(self):
        """
        Mengembalikan item Treeview yang sedang dipilih.
        """

        selected = self.tree.selection()

        if not selected:
            return None

        return selected[0]

    def bind_select(self,callback) -> None:
        """
        Event ketika baris dipilih.
        """

        self.tree.bind(
            "<<TreeviewSelect>>",
            callback
        )