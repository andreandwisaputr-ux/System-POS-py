import customtkinter as ctk
from tkinter import ttk
from tkinter import messagebox
from app.controllers.supplier_controller import SupplierController



class SupplierView(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        self.controller = SupplierController()

        self.pack(fill="both", expand=True)

        # Layout utama Supplier View
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.create_header()
        self.create_toolbar()
        self.create_table()
        self.clear_table()
        self.refresh_table()
        

    def create_header(self):
            frame = ctk.CTkFrame(
                self,
                fg_color="transparent"
            )
            frame.grid(
                row=0,
                column=0,
                sticky="ew",
                padx=20,
                pady=(10, 10)
            )

            title = ctk.CTkLabel(
                frame,
                text="Manajemen Supplier",
                font=("Segoe UI", 24, "bold")
            )
            title.pack(anchor="w")

            subtitle = ctk.CTkLabel(
                frame,
                text="Kelola seluruh Supplier produk.",
                font=("Segoe UI", 14)
            )
            subtitle.pack(anchor="w")

    def create_toolbar(self):
        toolbar = ctk.CTkFrame(self)
        toolbar.grid(
            row=1,
            column=0,
            sticky="ew",
            padx=20,
            pady=10
        )

        add_button = ctk.CTkButton(
            toolbar,
            text="+ Tambah",
            command=self.open_add_dialog)
        add_button.pack(
            side="left",
            padx=10,
            pady=10
        )
        edit_button = ctk.CTkButton(
            toolbar,
            text="✏ Edit",
            command=self.open_edit_dialog
        )
        edit_button.pack(
            side="left",
            padx=(10, 0)
        )

        delete_button = ctk.CTkButton(
            toolbar,
            text="Hapus",
            command=self.delete_supplier
        )

        delete_button.pack(
            side="left",
            padx=(10,0)
        )

    def create_table(self):
        table_frame = ctk.CTkFrame(self)
        table_frame.grid(
            row=2,
            column=0,
            sticky="nsew",
            padx=20,
            pady=(0, 20)
        )
        self.tree = ttk.Treeview(
        table_frame,
        columns=(
            "id",
            "company_name",
            "contact_person",
            "phone",
            "email",
            "address",
            "description"
        ),
            show="headings"
        )
        self.tree.heading(
            "id",
            text="ID"
        )

        self.tree.heading(
            "company_name",
            text="Nama"
        )

        self.tree.heading(
            "contact_person",
            text="Nama Sales"
        )
        self.tree.heading(
            "phone",
            text="Nomor Ponsel"
        )
        self.tree.heading(
            "email",
            text="Email"
        )
        self.tree.heading(
            "address",
            text="Alamat"
        )
        self.tree.heading(
            "description",
            text="Deskripsi"
        )


        self.tree.column(
            "id",
            width=80,
            anchor="center"
        )

        self.tree.column(
            "company_name",
            width=220,
            anchor="center"
        )
        self.tree.column(
            "contact_person",
            width=220,
            anchor="center"
        )
        self.tree.column(
            "phone",
            width=220,
            anchor="center"
        )
        self.tree.column(
            "email",
            width=300,
            anchor="center"
        )
        self.tree.column(
            "address",
            width=220,
            anchor="center"
        )

        self.tree.column(
            "description",
            width=250,
            anchor="center"
        )

        self.tree.pack(
        fill="both",
        expand=True,
        padx=10,
        pady=10
    )

    def open_add_dialog(self):
        # Jika dialog masih terbuka
        if hasattr(self, "dialog") and self.dialog.winfo_exists():
            self.dialog.focus()
            return

        # Jika belum ada, buat dialog baru
        self.dialog = ctk.CTkToplevel(self)

        self.dialog.title("Tambah Supplier")
        self.dialog.geometry("450x550")
        self.dialog.grid_columnconfigure(0, weight=1)

        companyname_label = ctk.CTkLabel(self.dialog, text="Nama Company Supplier")
        companyname_label.grid(row=0,column=0,padx=20,pady=(20, 5),sticky="w")
        self.companyname_entry = ctk.CTkEntry(self.dialog)
        self.companyname_entry.grid(row=1,column=0,padx=20,sticky="ew")

        contactperson_label = ctk.CTkLabel(self.dialog, text="Contact Person")
        contactperson_label.grid(row=2,column=0,padx=20,pady=(20, 5),sticky="w")
        self.contactperson_entry = ctk.CTkEntry(self.dialog)
        self.contactperson_entry.grid(row=3,column=0,padx=20,sticky="ew")

        phone_label = ctk.CTkLabel(self.dialog, text="Phone")
        phone_label.grid(row=4,column=0,padx=20,pady=(20, 5),sticky="w")
        self.phone_entry = ctk.CTkEntry(self.dialog)
        self.phone_entry.grid(row=5,column=0,padx=20,sticky="ew")

        email_label = ctk.CTkLabel(self.dialog, text="Email")
        email_label.grid(row=6,column=0,padx=20,pady=(20, 5),sticky="w")
        self.email_entry = ctk.CTkEntry(self.dialog)
        self.email_entry.grid(row=7,column=0,padx=20,sticky="ew")

        address_label = ctk.CTkLabel(self.dialog, text="Address")
        address_label.grid(row=8, column=0, padx=20, pady=(20, 5), sticky="w")
        self.address_textbox = ctk.CTkTextbox(self.dialog, height=100)
        self.address_textbox.grid(row=9, column=0, padx=20, sticky="ew")

        description_label = ctk.CTkLabel(self.dialog,text="Deskripsi")
        description_label.grid(row=10,column=0,padx=20,pady=(15, 5),sticky="w")

        self.description_entry = ctk.CTkEntry(self.dialog)
        self.description_entry.grid(row=11,column=0,padx=20,sticky="ew")

        button_frame = ctk.CTkFrame(self.dialog,fg_color="transparent"
        )
        button_frame.grid(row=12,column=0, padx=20, pady=20,sticky="e"
        )

        save_button = ctk.CTkButton(button_frame,text="Simpan",command=self.save_supplier)
        save_button.pack(side="left",padx=(0, 10))

        cancel_button = ctk.CTkButton(button_frame,text="Batal",command=self.dialog.destroy)
        cancel_button.pack(side="left")


    def save_supplier(self):
        company_name = self.companyname_entry.get().strip()
        contact_person = self.contactperson_entry.get().strip()
        phone = self.phone_entry.get().strip()
        email = self.email_entry.get().strip()
        address = self.address_textbox.get("1.0", "end").strip()
        description = self.description_entry.get().strip()
        
        if not company_name:
            messagebox.showwarning(
                "Peringatan",
                "Nama Company tidak boleh kosong."
            )
            return

        try:

            self.controller.add_supplier(
                company_name,contact_person,phone,email,address,
                description
            )

        except ValueError as e:

            messagebox.showwarning(
                "Peringatan",
                str(e)
            )

            return
        self.refresh_table()

        messagebox.showinfo(
            "Berhasil",
            "Supplier berhasil disimpan."
        )

        self.dialog.destroy()

    def open_edit_dialog(self):

        selected_item = self.tree.selection()

        if not selected_item:
             messagebox.showwarning(
                "Peringatan",
                "Silakan pilih Supplier terlebih dahulu."
            )
             return
        item_id = selected_item[0]
        values = self.tree.item(item_id, "values")

        supplier_id = int(values[0])
        company_name =(values[1])
        contact_person = values[2]
        phone = values[3]
        email = values[4]
        address = values[5]
        description = values[6]

         # Simpan ID Supplier yang sedang diedit

        self.selected_supplier_id = supplier_id

        print(values)

          # Jika dialog masih terbuka
        if hasattr(self, "dialog") and self.dialog.winfo_exists():
            self.dialog.focus()
            return

        # Jika belum ada, buat dialog baru
        self.dialog = ctk.CTkToplevel(self)

        self.dialog.title("Edit Supplier")
        self.dialog.geometry("450x550")
        self.dialog.grid_columnconfigure(0, weight=1)

        companyname_label = ctk.CTkLabel(self.dialog,text="Nama Company Supplier")
        companyname_label.grid(row=0,column=0,padx=20,pady=(20, 5),sticky="w")
        self.companyname_entry = ctk.CTkEntry(self.dialog)
        self.companyname_entry.grid(row=1,column=0, padx=20,sticky="ew")
        self.companyname_entry.insert(0,company_name)

        contactperson_label = ctk.CTkLabel(self.dialog,text="Contact Person")
        contactperson_label.grid(row=2,column=0,padx=20,pady=(20, 5),sticky="w")
        self.contactperson_entry = ctk.CTkEntry(self.dialog)
        self.contactperson_entry.grid(row=3,column=0, padx=20,sticky="ew")
        self.contactperson_entry.insert(0,contact_person)

        phone_label = ctk.CTkLabel(self.dialog,text="Phone")
        phone_label.grid(row=4,column=0,padx=20,pady=(20, 5),sticky="w")
        self.phone_entry = ctk.CTkEntry(self.dialog)
        self.phone_entry.grid(row=5,column=0, padx=20,sticky="ew")
        self.phone_entry.insert(0,phone)

        email_label = ctk.CTkLabel(self.dialog,text="Email")
        email_label.grid(row=6,column=0,padx=20,pady=(20, 5),sticky="w")
        self.email_entry = ctk.CTkEntry(self.dialog)
        self.email_entry.grid(row=7,column=0, padx=20,sticky="ew")
        self.email_entry.insert(0,email)

        address_label = ctk.CTkLabel(self.dialog, text="Address")
        address_label.grid(row=8, column=0, padx=20, pady=(20, 5), sticky="w")
        self.address_textbox = ctk.CTkTextbox(self.dialog, height=100)
        self.address_textbox.grid(row=9, column=0, padx=20, sticky="ew")
        self.address_textbox.insert("1.0", address)
                
        description_label = ctk.CTkLabel(self.dialog,text="Deskripsi")
        description_label.grid(row=10,column=0,padx=20,pady=(15, 5),sticky="w")
        self.description_entry = ctk.CTkEntry(self.dialog)
        self.description_entry.grid(row=11,column=0,padx=20,sticky="ew")
        self.description_entry.insert(0,description)

        button_frame = ctk.CTkFrame(self.dialog,fg_color="transparent")
        button_frame.grid(row=12,column=0,padx=20, pady=20, sticky="e")

        save_button = ctk.CTkButton(button_frame,text="Simpan",command=self.update_supplier)
        save_button.pack( side="left",padx=(0, 10))

        cancel_button = ctk.CTkButton(button_frame,text="Batal",command=self.dialog.destroy)
        cancel_button.pack(side="left")

    def load_table(self):
        """
        Memuat seluruh data Supplier ke Treeview.
        """

        suppliers = self.controller.get_suppliers()

        for supplier in suppliers:
            self.tree.insert(
                "",
                "end",
                values=(
                    supplier.id,
                    supplier.company_name,
                    supplier.contact_person,
                    supplier.phone,
                    supplier.email,
                    supplier.address,
                    supplier.description
                )
            )

    def refresh_table(self):
        """
        Memuat ulang isi Treeview.
        """

        self.clear_table()

    def clear_table(self):
        """
        Menghapus seluruh baris pada Treeview.
        """

        for item in self.tree.get_children():
            self.tree.delete(item)

    def delete_supplier(self):

        selected_item = self.tree.selection()

        if not selected_item:
            messagebox.showwarning(
                "Peringatan",
                "Silakan pilih Supplier terlebih dahulu."
            )
            return


        item_id = selected_item[0]

        values = self.tree.item(
            item_id,
            "values"
        )

        supplier_id = int(values[0])
        supplier_company_name = values[1]


        confirm = messagebox.askyesno(
            "Konfirmasi Hapus",
            f"Apakah Anda yakin ingin menghapus Supplier '{supplier_company_name}'?"
        )


        if not confirm:
            return


        try:

            self.controller.delete_supplier(
                supplier_id
            )

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

            return


        self.refresh_table()

        messagebox.showinfo(
            "Berhasil",
            "Supplier berhasil dihapus."
        )