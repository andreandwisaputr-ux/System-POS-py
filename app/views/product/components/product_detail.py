"""
Product Detail Component
"""

import customtkinter as ctk

from app.models.product import Product


class ProductDetail(ctk.CTkFrame):
    """
    Panel informasi detail produk.
    """

    def __init__(self, master):
        super().__init__(master)

        self.create_widgets()

    # ==================================================
    # UI
    # ==================================================

    def create_widgets(self):

        title = ctk.CTkLabel(
            self,
            text="Detail Produk",
            font=("Segoe UI", 18, "bold")
        )

        title.pack(
            anchor="w",
            padx=15,
            pady=(15,10)
        )

        self.labels = {}

        fields = [
            "Nama Produk",
            "Barcode",
            "Kategori",
            "Supplier",
            "Harga Beli",
            "Harga Jual",
            "Stok",
            "Minimum Stok",
            "Satuan",
            "Deskripsi",
        ]

        for field in fields:

            title = ctk.CTkLabel(
                self,
                text=field,
                font=("Segoe UI",11,"bold")
            )

            title.pack(
                anchor="w",
                padx=15,
                pady=(8,0)
            )

            value = ctk.CTkLabel(
                self,
                text="-",
                wraplength=260,
                justify="left"
            )

            value.pack(
                anchor="w",
                padx=25
            )

            self.labels[field] = value

    def show(
        self,
        product: Product
    ):

        self.labels["Nama Produk"].configure(
            text=product.product_name
        )

        self.labels["Barcode"].configure(
            text=product.barcode or "-"
        )

        self.labels["Kategori"].configure(
            text=product.category_name or "-"
        )

        self.labels["Supplier"].configure(
            text=product.supplier_name or "-"
        )

        self.labels["Harga Beli"].configure(
            text=f"Rp {product.purchase_price:,.0f}"
        )

        self.labels["Harga Jual"].configure(
            text=f"Rp {product.selling_price:,.0f}"
        )

        self.labels["Stok"].configure(
            text=str(product.stock)
        )

        self.labels["Minimum Stok"].configure(
            text=str(product.minimum_stock)
        )

        self.labels["Satuan"].configure(
            text=product.unit
        )

        self.labels["Deskripsi"].configure(
            text=product.description or "-"
        )

    def clear(self):

        for label in self.labels.values():

            label.configure(text="-")