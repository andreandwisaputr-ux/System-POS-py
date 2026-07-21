from app.controllers.category_controller import CategoryController

controller = CategoryController()

controller.add_category("Makanan")
controller.add_category("Minuman")
controller.add_category("Snack")

for category in controller.load_categories():
    print(category.id, category.name)