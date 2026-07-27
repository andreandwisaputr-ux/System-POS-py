"""
Add Product Dialog
"""

import customtkinter as ctk
from app.models.product import Product
from tkinter import messagebox


class AddProductDialog(ctk.CTkToplevel):
    """
    Dialog untuk menambah produk baru.
    """

    def __init__(
        self,
        master,
        controller,
        on_success=None,
    ) -> None:
        super().__init__(master)

        self.controller = controller
        self.on_success = on_success
        self.categories = {}
        self.suppliers = {}

        self.title("Tambah Produk")

        self.geometry("700x900")

        self.resizable(False, False)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(13, weight=1)

        self.create_widgets()
        self.load_categories()
        self.load_suppliers()

    def create_widgets(self) -> None:
        """
        Membuat seluruh komponen dialog.
        """

        # ==================================================
        # Title
        # ==================================================

        title = ctk.CTkLabel(
            self,
            text="Tambah Produk",
            font=("Segoe UI", 22, "bold")
        )

        title.grid(
            row=0,
            column=0,
            columnspan=2,
            pady=(20, 25)
        )
        # ==================================================
        # Nama Produk
        # ==================================================

        product_name_label = ctk.CTkLabel(
            self,
            text="Nama Produk"
        )

        product_name_label.grid(
            row=1,
            column=0,
            sticky="w",
            padx=(20, 10)
        )

        self.product_name_entry = ctk.CTkEntry(
            self,
            width=280
        )

        self.product_name_entry.grid(
            row=2,
            column=0,
            padx=(20, 10),
            sticky="ew"
        )
        # ==================================================
        # Barcode
        # ==================================================

        barcode_label = ctk.CTkLabel(
            self,
            text="Barcode"
        )

        barcode_label.grid(
            row=1,
            column=1,
            sticky="w",
            padx=(10, 20)
        )

        self.barcode_entry = ctk.CTkEntry(
            self,
            width=280
        )

        self.barcode_entry.grid(
            row=2,
            column=1,
            padx=(10, 20),
            sticky="ew"
        )
        # ==================================================
        # Category
        # ==================================================

        category_label = ctk.CTkLabel(
            self,
            text="Kategori"
        )

        category_label.grid(
            row=3,
            column=0,
            padx=(20, 10),
            pady=(15, 5),
            sticky="w"
        )

        self.category_combobox = ctk.CTkComboBox(
            self,
            width=280,
            values=[]
        )

        self.category_combobox.grid(
            row=4,
            column=0,
            padx=(20, 10),
            sticky="ew"
        )
        # ==================================================
        # Supplier
        # ==================================================

        supplier_label = ctk.CTkLabel(
            self,
            text="Supplier"
        )

        supplier_label.grid(
            row=3,
            column=1,
            padx=(10, 20),
            pady=(15, 5),
            sticky="w"
        )

        self.supplier_combobox = ctk.CTkComboBox(
            self,
            width=280,
            values=[]
        )

        self.supplier_combobox.grid(
            row=4,
            column=1,
            padx=(10, 20),
            sticky="ew"
        )
        # ==================================================
        # Purchase Price
        # ==================================================

        purchase_price_label = ctk.CTkLabel(
            self,
            text="Harga Beli"
        )

        purchase_price_label.grid(
            row=5,
            column=0,
            padx=(20, 10),
            pady=(15, 5),
            sticky="w"
        )


        self.purchase_price_entry = ctk.CTkEntry(
            self,
            placeholder_text="Contoh: 5000"
        )

        self.purchase_price_entry.grid(
            row=6,
            column=0,
            padx=(20, 10),
            sticky="ew"
        )

        # ==================================================
        # Selling Price
        # ==================================================

        selling_price_label = ctk.CTkLabel(
            self,
            text="Harga Jual"
        )

        selling_price_label.grid(
            row=5,
            column=1,
            padx=(10, 20),
            pady=(15, 5),
            sticky="w"
        )


        self.selling_price_entry = ctk.CTkEntry(
            self,
            placeholder_text="Contoh: 7000"
        )

        self.selling_price_entry.grid(
            row=6,
            column=1,
            padx=(10, 20),
            sticky="ew"
        )

        # ==================================================
        # Stock
        # ==================================================

        stock_label = ctk.CTkLabel(
            self,
            text="Stock Awal"
        )

        stock_label.grid(
            row=7,
            column=0,
            padx=(20, 10),
            pady=(15, 5),
            sticky="w"
        )


        self.stock_entry = ctk.CTkEntry(
            self,
            placeholder_text="Contoh: 100"
        )

        self.stock_entry.grid(
            row=8,
            column=0,
            padx=(20, 10),
            sticky="ew"
        )

        # ==================================================
        # Minimum Stock
        # ==================================================

        minimum_stock_label = ctk.CTkLabel(
            self,
            text="Minimum Stock"
        )

        minimum_stock_label.grid(
            row=7,
            column=1,
            padx=(10, 20),
            pady=(15, 5),
            sticky="w"
        )


        self.minimum_stock_entry = ctk.CTkEntry(
            self,
            placeholder_text="Contoh: 10"
        )

        self.minimum_stock_entry.grid(
            row=8,
            column=1,
            padx=(10, 20),
            sticky="ew"
        )
        # ==================================================
        # Unit
        # ==================================================

        unit_label = ctk.CTkLabel(
            self,
            text="Satuan"
        )

        unit_label.grid(
            row=9,
            column=0,
            padx=(20, 10),
            pady=(15, 5),
            sticky="w"
        )


        self.unit_combobox = ctk.CTkComboBox(
            self,
            values=[
                "Pcs",
                "Box",
                "Pack",
                "Botol",
                "Dus",
                "Kg",
                "Gram",
                "Liter",
                "Ml"
            ]
        )

        self.unit_combobox.grid(
            row=10,
            column=0,
            padx=(20, 10),
            sticky="ew"
        )

        # ==================================================
        # Description
        # ==================================================

        description_label = ctk.CTkLabel(
            self,
            text="Deskripsi"
        )

        description_label.grid(
            row=11,
            column=0,
            columnspan=2,
            padx=20,
            pady=(15, 5),
            sticky="w"
        )


        self.description_textbox = ctk.CTkTextbox(
            self,
            height=100
        )

        self.description_textbox.grid(
            row=12,
            column=0,
            columnspan=2,
            padx=20,
            sticky="ew"
        )

        # ==================================================
        # Button
        # ==================================================

        button_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        button_frame.grid(
            row=13,
            column=0,
            columnspan=2,
            pady=20,
            padx=20,
            sticky="e"
        )


        save_button = ctk.CTkButton(
            button_frame,
            text="Simpan",
            command=self.save_product
        )

        save_button.pack(
            side="left",
            padx=(0,10)
        )


        cancel_button = ctk.CTkButton(
            button_frame,
            text="Batal",
            command=self.destroy
        )

        cancel_button.pack(
            side="left"
        )


    def load_categories(self):
        """
        Mengambil data kategori
        untuk ComboBox.
        """

        categories = self.controller.get_categories()

        values = []

        for category in categories:
            values.append(category.name)

            self.categories[category.name] = category.id


        self.category_combobox.configure(
            values=values
        )


        if values:
            self.category_combobox.set(
                values[0]
        )

            
    def load_suppliers(self):
        """
        Mengambil data supplier
        untuk ComboBox.
        """

        suppliers = self.controller.get_suppliers()

        values = []

        for supplier in suppliers:
            values.append(supplier.company_name)

            self.suppliers[supplier.company_name] = supplier.id


        self.supplier_combobox.configure(
            values=values
        )


        if values:
            self.supplier_combobox.set(
                values[0]
            )

    def save_product(self) -> None:
        """
        Menyimpan produk baru.
        """

        try:

            # ==========================================
            # Ambil Category
            # ==========================================

            category_name = self.category_combobox.get()

            category_id = self.categories.get(
                category_name
            )

            if category_id is None:
                raise ValueError(
                    "Kategori belum dipilih."
                )


            # ==========================================
            # Ambil Supplier
            # ==========================================

            supplier_name = self.supplier_combobox.get()

            supplier_id = self.suppliers.get(
                supplier_name
            )

            if supplier_id is None:
                raise ValueError(
                    "Supplier belum dipilih."
                )


            # ==========================================
            # Ambil Data Form
            # ==========================================

            product_name = (
                self.product_name_entry.get()
                .strip()
            )

            barcode = (
                self.barcode_entry.get()
                .strip()
            )

            unit = (
                self.unit_combobox.get()
                .strip()
            )


            description = (
                self.description_textbox
                .get("0.0", "end")
                .strip()
            )


            try:
                purchase_price = float(
                    self.purchase_price_entry.get()
                )

                selling_price = float(
                    self.selling_price_entry.get()
                )

                stock = int(
                    self.stock_entry.get()
                )

                minimum_stock = int(
                    self.minimum_stock_entry.get()
                )

            except ValueError:

                raise ValueError(
                    "Harga dan stok harus berupa angka."
                )

            selling_price = float(
                self.selling_price_entry.get()
            )


            stock = int(
                self.stock_entry.get()
            )


            minimum_stock = int(
                self.minimum_stock_entry.get()
            )


            # ==========================================
            # Kirim ke Controller
            # ==========================================

            product = self.controller.add_product(
                category_id,
                supplier_id,
                product_name,
                barcode,
                purchase_price,
                selling_price,
                stock,
                minimum_stock,
                unit,
                description,
            )


            print(
                "Produk berhasil:",
                product
            )


            # ==========================================
            # Refresh ProductView
            # ==========================================

            if self.on_success:
                self.on_success()


            self.destroy()


        except ValueError as e:

            messagebox.showwarning(
                "Validasi Produk",
                str(e),
                parent=self
            )


        except Exception as e:

            messagebox.showerror(
                "Error",
                f"Terjadi kesalahan:\n{e}",
                parent=self
            )