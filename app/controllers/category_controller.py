from app.services.category_service import CategoryService


class CategoryController:

    def __init__(self):

        self.service = CategoryService()

    def load_categories(self):

        return self.service.get_categories()

    def add_category(
        self,name: str,description: str):

        return self.service.create_category(
            name,description)

    def get_all_categories(self):
        # PERBAIKAN: Panggil service, bukan self.repository
        return self.service.get_categories()
    

    def update_category(
        self,
        category_id: int,
        name: str,
        description: str):
        return self.service.update_category(
            category_id,
            name,
            description
        )
    
    
    def delete_category(self, category_id: int):

        return self.service.delete_category(
        category_id
    )