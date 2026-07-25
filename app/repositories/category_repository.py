"""
Category Repository
"""

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
        cursor = self.cursor

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS categories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE,
                description TEXT
            )
            """
            )

        self.commit()

    def get_all(self) -> list[Category]:
        """
        Mengambil seluruh data kategori.
        """
        cursor = self.cursor

        cursor.execute("""
            SELECT
                id,
                name,
                description
            FROM categories
            ORDER BY name
        """)

        rows = cursor.fetchall()

        # Konversi setiap sqlite3.Row menjadi instance Category
        categories = [
            Category(
                id=row["id"],
                name=row["name"],
                description=row["description"]
            )
            for row in rows
        ]

        return categories
        
    def get_by_id(self, category_id: int) -> Category | None:
        """
        Mengambil satu kategori berdasarkan ID.
        """

        cursor = self.cursor

        cursor.execute(
            """
            SELECT
                id,
                name,
                description
            FROM categories
            WHERE id = ?
            """,
            (category_id,)
        )

        row = cursor.fetchone()

        if row is None:
            return None

        return Category(
            id=row["id"],
            name=row["name"],
            description=row["description"]
        )
    
    def update(self, category: Category) -> Category:
        """
        Memperbarui data kategori.
        """

        cursor = self.cursor

        try:
            cursor.execute(
                """
                UPDATE categories
                SET
                    name = ?,
                    description = ?
                WHERE id = ?
                """,
                (
                    category.name,
                    category.description,
                    category.id,
                ),
            )

            self.commit()

            return category

        except IntegrityError:
            self.rollback()

            raise ValueError(
                "Nama kategori sudah digunakan."
            )
        
    def delete(self, category_id: int) -> bool:
        """
        Menghapus kategori berdasarkan ID.
        """

        cursor = self.cursor

        cursor.execute(
            """
            DELETE FROM categories
            WHERE id = ?
            """,
            (category_id,)
        )

        self.commit()

        return cursor.rowcount > 0