from app.models.product import Product
from app.services.product_service import ProductService


class ProductController:

    def __init__(self) -> None:
        self.service: ProductService = ProductService()
        

    def get_products(self) -> list[Product]:
        return self.service.get_products()
    
    def get_categories(self):
        """
        Mengambil semua kategori
        untuk ComboBox Product.
        """
        return self.service.get_categories()


    def get_suppliers(self):
        """
        Mengambil semua supplier
        untuk ComboBox Product.
        """

        return self.service.get_suppliers()

    def add_product(
        self,
        category_id: int,
        supplier_id: int,
        product_name: str,
        barcode: str,
        purchase_price: float,
        selling_price: float,
        stock: int,
        minimum_stock: int,
        unit: str,
        description: str,
    ) -> Product:

        return self.service.create_product(
            category_id,
            supplier_id,
            product_name,
            barcode,
            purchase_price,
            selling_price,
            stock,
            minimum_stock,
            unit,
            description,
        )

    def update_product(
        self,
        product_id: int,
        category_id: int,
        supplier_id: int,
        product_name: str,
        barcode: str,
        purchase_price: float,
        selling_price: float,
        stock: int,
        minimum_stock: int,
        unit: str,
        description: str,
    ) -> Product:

        return self.service.update_product(
            product_id,
            category_id,
            supplier_id,
            product_name,
            barcode,
            purchase_price,
            selling_price,
            stock,
            minimum_stock,
            unit,
            description,
        )

    def delete_product(self, product_id: int) -> bool:
        return self.service.delete_product(product_id)

    def search_products(self,keyword: str) -> list[Product]:
        return self.service.search_products(
            keyword
        )