from app.database.database_manager import DatabaseManager
from app.repositories.supplier_repository import SupplierRepository


db = DatabaseManager()

repo = SupplierRepository(db)

repo.create_table()

print("Tabel suppliers berhasil dibuat.")

db.close()