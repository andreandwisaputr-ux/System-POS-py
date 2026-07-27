from app.database.database_manager import DatabaseManager
from app.repositories.product_repository import ProductRepository


db = DatabaseManager()

repo = ProductRepository(db)

repo.create_table()

print("Tabel products berhasil dibuat.")

db.close()