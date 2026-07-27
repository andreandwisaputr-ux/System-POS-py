"""
Product View
"""

import customtkinter as ctk

from app.controllers.product_controller import ProductController

from app.views.product.components.product_header import ProductHeader
from app.views.product.components.product_toolbar import ProductToolbar
from app.views.product.components.product_table import ProductTable
from app.views.product.components.product_detail import ProductDetail
from app.views.product.dialogs.add_product_dialog import AddProductDialog


class ProductView(ctk.CTkFrame):
    """
    Main View Product Module.
    """

    def __init__(self, master) -> None:
        super().__init__(
            master,
            fg_color="transparent"
        )

        self.controller = ProductController()

        self.create_layout()

        self.load_products()

        self.detail.clear()

    # ==================================================
    # Layout
    # ==================================================

    def create_layout(self) -> None:

        self.grid_rowconfigure(2, weight=1)

        self.grid_columnconfigure(0, weight=3)

        self.grid_columnconfigure(1, weight=1)

        # Header
        self.header = ProductHeader(self)

        self.header.grid(
            row=0,
            column=0,
            columnspan=2,
            sticky="ew",
            padx=20,
            pady=(10, 10)
        )

        # Toolbar
        self.toolbar = ProductToolbar(
            self,
            on_add=self.open_add_dialog,
            on_edit=self.open_edit_dialog,
            on_delete=self.delete_product,
            on_search=self.search_products,
        )

        self.toolbar.grid(
            row=1,
            column=0,
            columnspan=2,
            sticky="ew",
            padx=20,
            pady=(0, 10)
        )

        # Product Table
        self.table = ProductTable(self)

        self.table.grid(
            row=2,
            column=0,
            sticky="nsew",
            padx=(20, 10),
            pady=(0, 20)
        )

        self.table.bind_select(
            self.on_product_selected
        )

        # Product Detail
        self.detail = ProductDetail(self)

        self.detail.grid(
            row=2,
            column=1,
            sticky="nsew",
            padx=(0, 20),
            pady=(0, 20)
        )

    # ==================================================
    # Load Data
    # ==================================================

    def load_products(self) -> None:

        products = self.controller.get_products()

        self.table.load(products)

    def search_products(self) -> None:
        """
        Live Search Product.
        """

        keyword = self.toolbar.get_search_keyword()

        products = self.controller.search_products(keyword)

        self.table.load(products)

        self.detail.clear()

    # ==================================================
    # Event
    # ==================================================

    def on_product_selected(self, event) -> None:

        product_id = self.table.get_selected_id()

        if product_id is None:

            self.detail.clear()

            return

        product = self.controller.get_product_by_id(
            product_id
        )

        if product:

            self.detail.show(product)

    # ==================================================
    # CRUD Event
    # ==================================================

    def open_add_dialog(self):
        AddProductDialog(
            self,
            self.controller,
            self.load_products
        )

    def open_edit_dialog(self) -> None:
        print("Edit Product")

    def delete_product(self) -> None:
        print("Delete Product")

