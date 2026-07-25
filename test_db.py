from app.controllers.category_controller import CategoryController

controller = CategoryController()

categories = controller.get_all_categories()

for category in categories:
    print(category)