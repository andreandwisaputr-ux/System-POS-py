"""
Category Repository
"""

import sqlite3
from sqlite3 import IntegrityError  # <-- Di-import agar exception dapat tertangkap
from app.models.category import Category
from app.repositories.base_repository import BaseRepository


class CategoryRepository(BaseRepository):
    """
    Repository untuk mengelola tabel categories.
    """
    def add(self, category: Category) -> Category:
        try:
            # 1. Simpan cursor ke dalam variabel lokal!
            cursor = self.cursor

            # 2. Gunakan variabel cursor tersebut untuk execute
            cursor.execute(
                """
                INSERT INTO categories (
                    name,
                    description
                )
                VALUES (?, ?)
                """,
                (
                    category.name,
                    category.description,
                ),
            )

            # 3. Ambil lastrowid dari variabel cursor YANG SAMA
            category.id = cursor.lastrowid

            # 4. Baru lakukan commit
            self.commit()

            return category

        except IntegrityError:
            self.rollback()
            raise ValueError("Nama kategori sudah digunakan.")
  
    def create_table(self) -> None:
        """
        Membuat tabel categories jika belum ada.
        """
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS categories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE,
                description TEXT
            )
            """
        )

        self.commit()