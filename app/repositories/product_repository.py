"""
Product Repository
"""


from sqlite3 import IntegrityError  # <-- Di-import agar exception dapat tertangkap
from app.models.product import Product
from sqlite3 import Row
from app.repositories.base_repository import BaseRepository


class ProductRepository(BaseRepository):

    
    """
    Repository untuk mengelola tabel Product.
    """

    def create_table(self) -> None:
        """
        Membuat tabel products jika belum ada.
        """

        cursor = self.cursor

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                category_id INTEGER NOT NULL,
                supplier_id INTEGER NOT NULL,
                product_name TEXT NOT NULL,
                barcode TEXT UNIQUE,
                purchase_price REAL NOT NULL,
                selling_price REAL NOT NULL,
                stock INTEGER DEFAULT 0,
                minimum_stock INTEGER DEFAULT 0,
                unit TEXT,
                description TEXT
            )
            """
        )

        self.commit()


    def search(self,keyword: str) -> list[Product]:
        """
        Mencari produk berdasarkan nama produk atau barcode.
        """

        cursor = self.cursor

        cursor.execute(
            """
            SELECT
                p.id,
                p.category_id,
                p.supplier_id,
                p.product_name,
                p.barcode,
                p.purchase_price,
                p.selling_price,
                p.stock,
                p.minimum_stock,
                p.unit,
                p.description,
                c.name AS category_name,
                s.company_name AS supplier_name
            FROM products p
            LEFT JOIN categories c
                ON p.category_id = c.id
            LEFT JOIN suppliers s
                ON p.supplier_id = s.id
            WHERE
                p.product_name LIKE ?
                OR
                p.barcode LIKE ?
            ORDER BY
                p.product_name
            """,
            (
                f"%{keyword}%",
                f"%{keyword}%"
            ),
        )

        rows = cursor.fetchall()

        return [
            self._build_product(row)
            for row in rows
        ]

    


    def add(self, product: Product) -> Product:
        """
        Menambahkan data produk baru.
        """

        try:
            cursor = self.cursor

            cursor.execute(
                """
                INSERT INTO products (
                    category_id,
                    supplier_id,
                    product_name,
                    barcode,
                    purchase_price,
                    selling_price,
                    stock,
                    minimum_stock,
                    unit,
                    description
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    product.category_id,
                    product.supplier_id,
                    product.product_name,
                    product.barcode,
                    product.purchase_price,
                    product.selling_price,
                    product.stock,
                    product.minimum_stock,
                    product.unit,
                    product.description,
                ),
            )

            product.id = cursor.lastrowid

            self.commit()

            return product

        except IntegrityError:
            self.rollback()
            raise ValueError(
                "Barcode produk sudah digunakan."
            )
            
        
    def update(self, product: Product) -> Product:
        """
        Memperbarui data produk.
        """

        cursor = self.cursor

        try:
            cursor.execute(
                """
                UPDATE products
                SET
                    category_id = ?,
                    supplier_id = ?,
                    product_name = ?,
                    barcode = ?,
                    purchase_price = ?,
                    selling_price = ?,
                    stock = ?,
                    minimum_stock = ?,
                    unit = ?,
                    description = ?
                WHERE id = ?
                """,
                (
                    product.category_id,
                    product.supplier_id,
                    product.product_name,
                    product.barcode,
                    product.purchase_price,
                    product.selling_price,
                    product.stock,
                    product.minimum_stock,
                    product.unit,
                    product.description,
                    product.id,
                ),
            )

            self.commit()

            return product

        except IntegrityError:
            self.rollback()
            raise ValueError(
                "Barcode produk sudah digunakan."
            )
        
    def delete(self, product_id: int) -> bool:
        """
        Menghapus produk berdasarkan ID.
        """

        cursor = self.cursor

        cursor.execute(
            """
            DELETE FROM products
            WHERE id = ?
            """,
            (product_id,),
        )

        self.commit()

        return cursor.rowcount > 0


    def get_all(self) -> list[Product]:
        """
        Mengambil seluruh data produk beserta nama kategori dan supplier.
        """

        cursor = self.cursor

        cursor.execute(
            """
            SELECT
                p.id,
                p.category_id,
                p.supplier_id,
                p.product_name,
                p.barcode,
                p.purchase_price,
                p.selling_price,
                p.stock,
                p.minimum_stock,
                p.unit,
                p.description,
                c.name AS category_name,
                s.company_name AS supplier_name
            FROM products p
            LEFT JOIN categories c
                ON p.category_id = c.id
            LEFT JOIN suppliers s
                ON p.supplier_id = s.id
            ORDER BY p.product_name
            """
        )

        rows = cursor.fetchall()

        return [
            self._build_product(row)
            for row in rows
        ]

    def get_by_id(self, product_id: int) -> Product | None:
        """
        Mengambil satu produk berdasarkan ID.
        """

        cursor = self.cursor

        cursor.execute(
            """
            SELECT
                p.id,
                p.category_id,
                p.supplier_id,
                p.product_name,
                p.barcode,
                p.purchase_price,
                p.selling_price,
                p.stock,
                p.minimum_stock,
                p.unit,
                p.description,
                c.name AS category_name,
                s.company_name AS supplier_name
            FROM products p
            LEFT JOIN categories c
                ON p.category_id = c.id
            LEFT JOIN suppliers s
                ON p.supplier_id = s.id
            WHERE p.id = ?
            """,
            (product_id,),
        )

        row = cursor.fetchone()

        if row is None:
            return None

        return self._build_product(row)

    def get_by_barcode(self, barcode: str) -> Product | None:
        """
        Mengambil satu produk berdasarkan barcode.
        Digunakan pada modul Kasir / Barcode Scanner.
        """

        cursor = self.cursor

        cursor.execute(
            """
            SELECT
                p.id,
                p.category_id,
                p.supplier_id,
                p.product_name,
                p.barcode,
                p.purchase_price,
                p.selling_price,
                p.stock,
                p.minimum_stock,
                p.unit,
                p.description,
                c.name AS category_name,
                s.company_name AS supplier_name
            FROM products p
            LEFT JOIN categories c
                ON p.category_id = c.id
            LEFT JOIN suppliers s
                ON p.supplier_id = s.id
            WHERE p.barcode = ?
            """,
            (barcode,),
        )

        row = cursor.fetchone()

        if row is None:
            return None

        return self._build_product(row)

    def exists_barcode(self,barcode: str,exclude_id: int | None = None) -> bool:
        """
        Mengecek apakah barcode sudah digunakan.

        exclude_id digunakan saat update produk agar
        barcode milik produk yang sedang diedit tidak dianggap duplikat.
        """

        cursor = self.cursor

        if exclude_id is not None:

            cursor.execute(
                """
                SELECT 1
                FROM products
                WHERE barcode = ?
                AND id != ?
                LIMIT 1
                """,
                (barcode, exclude_id),
            )

        else:

            cursor.execute(
                """
                SELECT 1
                FROM products
                WHERE barcode = ?
                LIMIT 1
                """,
                (barcode,),
            )

        return cursor.fetchone() is not None
    

    def _build_product(self, row: Row) -> Product:
        """
        Mengubah sqlite3.Row menjadi object Product.
        """

        return Product(
            id=row["id"],
            category_id=row["category_id"],
            supplier_id=row["supplier_id"],
            product_name=row["product_name"],
            barcode=row["barcode"],
            purchase_price=row["purchase_price"],
            selling_price=row["selling_price"],
            stock=row["stock"],
            minimum_stock=row["minimum_stock"],
            unit=row["unit"],
            description=row["description"],
            category_name=row["category_name"],
            supplier_name=row["supplier_name"],
        )