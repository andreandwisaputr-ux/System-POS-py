from app.repositories.category_repository import CategoryRepository


class CategoryService:

    def __init__(self):

        self.repo = CategoryRepository()

    def get_categories(self):

        return self.repo.get_all()

    def create_category(self, name):

        name = name.strip()

        if not name:

            raise ValueError("Nama kategori tidak boleh kosong.")

        return self.repo.create(name)