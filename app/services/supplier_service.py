from app.models.supplier import Supplier
from app.repositories.supplier_repository import SupplierRepository
from app.database.database_manager import DatabaseManager


class SupplierService:
    def __init__(self) -> None:
        self.db: DatabaseManager = DatabaseManager()
        self.repo: SupplierRepository = SupplierRepository(self.db)

    def get_suppliers(self) -> list[Supplier]:
        return self.repo.get_all()

    def create_supplier(
        self,
        company_name: str,
        contact_person: str,
        phone: str,
        email: str,
        address: str,
        description: str
    ) -> Supplier:
        supplier: Supplier = Supplier(
            company_name=company_name,
            contact_person=contact_person,
            phone=phone,
            email=email,
            address=address,
            description=description
        )
        return self.repo.add(supplier)

    def update_supplier(
        self,
        supplier_id: int,
        company_name: str,
        contact_person: str,
        phone: str,
        email: str,
        address: str,
        description: str
    ) -> Supplier:
        supplier: Supplier = Supplier(
            id=supplier_id,
            company_name=company_name,
            contact_person=contact_person,
            phone=phone,
            email=email,
            address=address,
            description=description
        )
        return self.repo.update(supplier)

    def delete_supplier(self,supplier_id: int) -> bool:

        return self.repo.delete(supplier_id)