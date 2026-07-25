# app/views/category/category_view.py

from tkinter import messagebox
import customtkinter as ctk
from app.controllers.category_controller import CategoryController
import tkinter.ttk as ttk

class CategoryView(ctk.CTkFrame):

    def __init__(self, master):
        # Set fg_color="transparent" agar menyatu dengan background content MainWindow
        super().__init__(master, fg_color="transparent")
        self.controller = CategoryController()

        # Layout utama CategoryView
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Buat komponen-komponen UI
        self.create_header()
        self.create_toolbar()
        self.create_table()
        self.load_table()
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
            text="Manajemen Kategori",
            font=("Segoe UI", 24, "bold")
        )
        title.pack(anchor="w")

        subtitle = ctk.CTkLabel(
            frame,
            text="Kelola seluruh kategori produk.",
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
            command=self.delete_category
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
            "name",
            "description"
        ),
            show="headings"
        )
        self.tree.heading(
            "id",
            text="ID"
        )

        self.tree.heading(
            "name",
            text="Nama"
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
            "name",
            width=220,
            anchor="center"
        )

        self.tree.column(
            "description",
            width=500,
            anchor="center"
        )

        self.tree.pack(
        fill="both",
        expand=True,
        padx=10,
        pady=10
)
        
    def load_table(self):
        """
        Memuat seluruh data kategori ke Treeview.
        """

        categories = self.controller.load_categories()

        for category in categories:
            self.tree.insert(
                "",
                "end",
                values=(
                    category.id,
                    category.name,
                    category.description
                )
            )
    def clear_table(self):
        """
        Menghapus seluruh baris pada Treeview.
        """

        for item in self.tree.get_children():
            self.tree.delete(item)

    def refresh_table(self):
        """
        Memuat ulang isi Treeview.
        """

        self.clear_table()
        self.load_table()
        
    def open_add_dialog(self):

        # Jika dialog masih terbuka
        if hasattr(self, "dialog") and self.dialog.winfo_exists():
            self.dialog.focus()
            return

        # Jika belum ada, buat dialog baru
        self.dialog = ctk.CTkToplevel(self)

        self.dialog.title("Tambah Kategori")
        self.dialog.geometry("400x250")
        self.dialog.grid_columnconfigure(0, weight=1)

        name_label = ctk.CTkLabel(
        self.dialog,
        text="Nama Kategori"
        )
        name_label.grid(
            row=0,
            column=0,
            padx=20,
            pady=(20, 5),
            sticky="w"
        )
        self.name_entry = ctk.CTkEntry(
        self.dialog
        )

        self.name_entry.grid(
            row=1,
            column=0,
            padx=20,
            sticky="ew"
        )


        description_label = ctk.CTkLabel(
        self.dialog,
            text="Deskripsi"
        )
        description_label.grid(
            row=2,
            column=0,
            padx=20,
            pady=(15, 5),
            sticky="w"
        )

        self.description_entry = ctk.CTkEntry(
        self.dialog
        )
        self.description_entry.grid(
        row=3,
        column=0,
        padx=20,
        sticky="ew"
        )

        button_frame = ctk.CTkFrame(
        self.dialog,
        fg_color="transparent"
        )

        button_frame.grid(
            row=4,
            column=0,
            padx=20,
            pady=20,
            sticky="e"
        )

        save_button = ctk.CTkButton(
        button_frame,
        text="Simpan",
        command=self.save_category
        )

        save_button.pack(
            side="left",
            padx=(0, 10)
        )


        cancel_button = ctk.CTkButton(
            button_frame,
            text="Batal",
            command=self.dialog.destroy
        )

        cancel_button.pack(
            side="left"
        )

    def save_category(self):

        name = self.name_entry.get().strip()
        description = self.description_entry.get().strip()

        if not name:
            messagebox.showwarning(
                "Peringatan",
                "Nama kategori tidak boleh kosong."
            )
            return

        try:

            self.controller.add_category(
                name,
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
            "Kategori berhasil disimpan."
        )

        self.dialog.destroy()

        
    def open_edit_dialog(self):

        selected_item = self.tree.selection()

        if not selected_item:
             messagebox.showwarning(
                "Peringatan",
                "Silakan pilih kategori terlebih dahulu."
            )
             return
        item_id = selected_item[0]
        values = self.tree.item(item_id, "values")

        category_id = int(values[0])
        name = values[1]
        description = values[2]
         # Simpan ID kategori yang sedang diedit
        self.selected_category_id = category_id

        print(values)

          # Jika dialog masih terbuka
        if hasattr(self, "dialog") and self.dialog.winfo_exists():
            self.dialog.focus()
            return

        # Jika belum ada, buat dialog baru
        self.dialog = ctk.CTkToplevel(self)

        self.dialog.title("Edit Kategori")
        self.dialog.geometry("400x250")
        self.dialog.grid_columnconfigure(0, weight=1)

        name_label = ctk.CTkLabel(
        self.dialog,
        text="Nama Kategori"
        )
        name_label.grid(
            row=0,column=0,padx=20,pady=(20, 5),sticky="w")
        self.name_entry = ctk.CTkEntry(self.dialog)
        self.name_entry.grid(row=1,column=0, padx=20,sticky="ew")
        self.name_entry.insert(0,name)
        
        description_label = ctk.CTkLabel(self.dialog,text="Deskripsi")
        description_label.grid(row=2,column=0,padx=20,pady=(15, 5),sticky="w")
        

        self.description_entry = ctk.CTkEntry(self.dialog)
        self.description_entry.grid(row=3,column=0,padx=20,sticky="ew")
        self.description_entry.insert(0,description)

        button_frame = ctk.CTkFrame(self.dialog,fg_color="transparent")
        button_frame.grid(row=4,column=0,padx=20, pady=20, sticky="e")

        save_button = ctk.CTkButton(button_frame,text="Simpan",command=self.update_category)
        save_button.pack( side="left",padx=(0, 10))

        cancel_button = ctk.CTkButton(button_frame,text="Batal",command=self.dialog.destroy)
        cancel_button.pack(side="left")


    def delete_category(self):

        selected_item = self.tree.selection()

        if not selected_item:
            messagebox.showwarning(
                "Peringatan",
                "Silakan pilih kategori terlebih dahulu."
            )
            return


        item_id = selected_item[0]

        values = self.tree.item(
            item_id,
            "values"
        )

        category_id = int(values[0])
        category_name = values[1]


        confirm = messagebox.askyesno(
            "Konfirmasi Hapus",
            f"Apakah Anda yakin ingin menghapus kategori '{category_name}'?"
        )


        if not confirm:
            return


        try:

            self.controller.delete_category(
                category_id
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
            "Kategori berhasil dihapus."
        )