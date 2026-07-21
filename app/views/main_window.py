import customtkinter as ctk

from app.views.dashboard.dasboard_view import DashboardView
from app.views.product.product_view import ProductView
from app.views.category.category_view import CategoryView
from app.widgets.sidebar import Sidebar
from app.widgets.header import Header


class MainWindow(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.pack(fill="both", expand=True)

        # KUNCI PERBAIKAN 1: Daftarkan route menu ke view class-nya masing-masing di sini
        self.routes = {
            "Dashboard": {"view": DashboardView, "title": "Dashboard"},
            "Produk": {"view": ProductView, "title": "Manajemen Produk"},
            "Kategori": {"view": CategoryView, "title": "Manajemen Kategori"}
        }

        # Layout utama aplikasi
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Sidebar (Passing callback function self.show_menu)
        self.sidebar = Sidebar(self, self.show_menu)
        self.sidebar.grid(row=0, column=0, rowspan=2, sticky="ns")

        # Header
        self.header = Header(self)
        self.header.grid(row=0, column=1, sticky="ew")

        # Content Area (Wadah dinamis untuk berganti halaman)
        # Diubah fg_color="transparent" agar rapi mengikuti tema warna aplikasi
        self.content = ctk.CTkFrame(self, fg_color="transparent")
        self.content.grid(row=1, column=1, padx=20, pady=20, sticky="nsew")

        # Halaman default saat aplikasi pertama kali dibuka
        self.show_view(DashboardView, "Dashboard")

    # ======================================
    # Menghapus semua widget di Content Area
    # ======================================
    def clear_content(self):
        for widget in self.content.winfo_children():
            widget.destroy()

    # ======================================
    # Menampilkan sebuah View
    # ======================================
    def show_view(self, view_class, title):
        self.clear_content()
        self.header.set_title(title)
        
        # Instansiasi class view dan masukkan ke dalam self.content
        current_view = view_class(self.content)
        
        # KUNCI VISUAL: Pastikan view yang dipanggil otomatis memenuhi content area
        if hasattr(current_view, "grid"):
            current_view.grid(row=0, column=0, sticky="nsew")
        elif hasattr(current_view, "pack"):
            current_view.pack(fill="both", expand=True)

    # ======================================
    # KUNCI PERBAIKAN 2: Perbaikan Indentasi & Logika Routing
    # ======================================
    def show_menu(self, menu):
        route = self.routes.get(menu)
        if route:
            self.show_view(
                route["view"],
                route["title"]
            )