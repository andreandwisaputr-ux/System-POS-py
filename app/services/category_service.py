from app.repositories.category_repository import CategoryRepository
from app.database.database_manager import DatabaseManager
from app.models.category import Category


class CategoryService:

    def __init__(self):
        # 1. Buat instance database manager
        self.db = DatabaseManager()
        # 2. Oper db ke CategoryRepository
        self.repo = CategoryRepository(self.db)

    def get_categories(self):
            return self.repo.get_all()

    def create_category(
        self,
        name: str,
        description: str
    ):

        category = Category(
            name=name,
            description=description
        )

        return self.repo.add(category)
    

    def update_category(
        self,
        category_id: int,
        name: str,
        description: str
    ):

        category = Category(
            id=category_id,
            name=name,
            description=description
        )

        return self.repo.update(category)
    
    def delete_category(self, category_id: int):

        return self.repo.delete(
            category_id
        )