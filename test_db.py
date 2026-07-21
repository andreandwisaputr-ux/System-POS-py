from app.database.database_manager import DatabaseManager
from app.models.category import Category
from app.repositories.category_repository import CategoryRepository

db = DatabaseManager()

repo = CategoryRepository(db)

repo.create_table()

category = Category(
    name="jajan",
    description="Semua jenis jajan"
)

saved = repo.add(category)

print(saved)

db.close()