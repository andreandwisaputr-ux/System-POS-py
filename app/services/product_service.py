from app.database.database_manager import DatabaseManager
from app.models.product import Product
from app.repositories.product_repository import ProductRepository
from app.repositories.category_repository import CategoryRepository
from app.repositories.supplier_repository import SupplierRepository


class ProductService:

    def __init__(self) -> None:
        self.db: DatabaseManager = DatabaseManager()
        self.repo: ProductRepository = ProductRepository(self.db)
        self.category_repository = CategoryRepository(self.db)

        self.supplier_repository = SupplierRepository(self.db)

    def get_products(self) -> list[Product]:
        """
        Mengambil seluruh data produk.
        """
        return self.repo.get_all()
    def get_categories(self):
        return self.category_repository.get_all()


    def get_suppliers(self):
        return self.supplier_repository.get_all()

    def create_product(
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
        """
        Menambahkan produk baru.
        """

        self._validate_product(
            product_name,
            purchase_price,
            selling_price,
            stock,
            minimum_stock,
        )

        product = Product(
            category_id=category_id,
            supplier_id=supplier_id,
            product_name=product_name,
            barcode=barcode,
            purchase_price=purchase_price,
            selling_price=selling_price,
            stock=stock,
            minimum_stock=minimum_stock,
            unit=unit,
            description=description,
        )

        return self.repo.add(product)

    
    def search_products(self,keyword: str) -> list[Product]:
        return self.repo.search(keyword)

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
        """
        Memperbarui data produk.
        """

        self._validate_product(
            product_name,
            purchase_price,
            selling_price,
            stock,
            minimum_stock,
        )

        product = Product(
            id=product_id,
            category_id=category_id,
            supplier_id=supplier_id,
            product_name=product_name,
            barcode=barcode,
            purchase_price=purchase_price,
            selling_price=selling_price,
            stock=stock,
            minimum_stock=minimum_stock,
            unit=unit,
            description=description,
        )

        return self.repo.update(product)

    def delete_product(self, product_id: int) -> bool:
        """
        Menghapus produk.
        """

        return self.repo.delete(product_id)

    # ==================================================
    # Private Method
    # ==================================================

    def _validate_product(
        self,
        product_name: str,
        purchase_price: float,
        selling_price: float,
        stock: int,
        minimum_stock: int,
    ) -> None:
        """
        Validasi data produk.
        """

        if not product_name.strip():
            raise ValueError(
                "Nama produk tidak boleh kosong."
            )

        if purchase_price < 0:
            raise ValueError(
                "Harga beli tidak boleh bernilai negatif."
            )

        if selling_price < 0:
            raise ValueError(
                "Harga jual tidak boleh bernilai negatif."
            )

        if selling_price < purchase_price:
            raise ValueError(
                "Harga jual tidak boleh lebih kecil dari harga beli."
            )

        if stock < 0:
            raise ValueError(
                "Stok tidak boleh bernilai negatif."
            )

        if minimum_stock < 0:
            raise ValueError(
                "Minimum stok tidak boleh bernilai negatif."
            )
        
        if minimum_stock > stock:
            raise ValueError(
            "Minimum stok tidak boleh lebih besar dari stok."
        )