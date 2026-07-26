"""
Supplier Repository
"""


from sqlite3 import IntegrityError  # <-- Di-import agar exception dapat tertangkap
from app.models.supplier import Supplier
from app.repositories.base_repository import BaseRepository


class SupplierRepository(BaseRepository):

    
    """
    Repository untuk mengelola tabel Suppliers.
    """

    def create_table(self) -> None:
            """
            Membuat tabel suppliers jika belum ada.
            """
            cursor = self.cursor
    
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS suppliers (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    company_name TEXT NOT NULL UNIQUE,
                    contact_person TEXT,
                    phone TEXT,
                    email TEXT,
                    address TEXT,
                    description TEXT
                )
                """
                )
    
            self.commit()


    def add(self, supplier: Supplier) -> Supplier:
            try:
                # 1. Simpan cursor ke dalam variabel lokal!
                cursor = self.cursor
    
                # 2. Gunakan variabel cursor tersebut untuk execute
                cursor.execute(
                    """
                    INSERT INTO suppliers (
                        company_name,
                        contact_person,
                        phone,
                        email,
                        address,
                        description
                    )
                    VALUES (?, ?, ?, ?, ?, ?)
                    """,
                    (
                        supplier.company_name,
                        supplier.contact_person,
                        supplier.phone,
                        supplier.email,
                        supplier.address,
                        supplier.description,
                    ),
                )
    
                # 3. Ambil lastrowid dari variabel cursor YANG SAMA
                supplier.id = cursor.lastrowid
    
                # 4. Baru lakukan commit
                self.commit()
    
                return supplier
    
            except IntegrityError:
                self.rollback()
                raise ValueError("Nama Perusahaan sudah digunakan.")

            
    def get_all(self) -> list[Supplier]:
            """
            Mengambil seluruh data Supplier.
            """
            cursor = self.cursor
    
            cursor.execute("""
                SELECT
                    id,
                    company_name,
                    contact_person,
                    phone,
                    email,
                    address,
                    description
                FROM suppliers
                ORDER BY company_name
            """)
    
            rows = cursor.fetchall()
    
            # Konversi setiap sqlite3.Row menjadi instance Supplier

            suppliers = [
                Supplier(
                    id=row["id"],
                    company_name=row["company_name"],
                    contact_person=row["contact_person"],
                    phone=row["phone"],
                    email=row["email"],
                    address=row["address"],
                    description=row["description"]
    )
                for row in rows
            ]
    
            return suppliers
            
    def get_by_id(self, supplier_id: int) -> Supplier | None:
        """
        Mengambil satu supplier berdasarkan ID.
        """

        cursor = self.cursor

        cursor.execute(
            """
            SELECT
                id,
                company_name,
                contact_person,
                phone,
                email,
                address,
                description
            FROM suppliers
            WHERE id = ?
            """,
            (supplier_id,)
        )

        row = cursor.fetchone()

        if row is None:
            return None

        return Supplier(
            id=row["id"],
            company_name=row["company_name"],
            contact_person=row["contact_person"],
            phone=row["phone"],
            email=row["email"],
            address=row["address"],
            description=row["description"]
        )
    
    def update(self, supplier: Supplier) -> Supplier:
        """
        Memperbarui data Supplier.
        """

        cursor = self.cursor

        try:
            cursor.execute(
                """
                UPDATE suppliers
                SET
                    company_name = ?,
                    contact_person = ?,
                    phone = ?,
                    email = ?,
                    address = ?,
                    description = ?
                WHERE id = ?
                """,
                (
                    supplier.company_name,
                    supplier.contact_person,
                    supplier.phone,
                    supplier.email,
                    supplier.address,
                    supplier.description,
                    supplier.id,
                ),
            )

            self.commit()

            return supplier

        except IntegrityError:
            self.rollback()

            raise ValueError(
                "Nama Perusahaan sudah digunakan."
            )
        
    def delete(self, suppliers_id: int) -> bool:
        """
        Menghapus Supplier berdasarkan ID.
        """

        cursor = self.cursor

        cursor.execute(
            """
            DELETE FROM suppliers
            WHERE id = ?
            """,
            (suppliers_id,)
        )

        self.commit()

        return cursor.rowcount > 0