from app.services.category_service import CategoryService


class CategoryController:

    def __init__(self):

        self.service = CategoryService()

    def load_categories(self):

        return self.service.get_categories()

    def add_category(self, name):

        return self.service.create_category(name)