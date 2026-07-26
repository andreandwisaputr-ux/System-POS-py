from app.services.supplier_service import SupplierService
from app.models.supplier import Supplier




class SupplierController:


    def __init__(self) -> None:

        self.service: SupplierService = SupplierService()

    def add_supplier(
        self,company_name: str, contact_person: str, phone : str, 
            email: str, address: str, description: str) -> Supplier:

        return self.service.create_supplier(
            company_name,contact_person,phone,email,address,description)

    def get_suppliers(self) -> list[Supplier]:

        # PERBAIKAN: Panggil service, bukan self.repository

        return self.service.get_suppliers()
    

    def update_supplier(
        self,
        supplier_id: int,
        company_name: str,
        contact_person: str, 
        phone : str, 
        email: str, 
        address: str,
        description: str)-> Supplier:

        return self.service.update_supplier(
            supplier_id,
            company_name,contact_person,
            phone,email,address,
            description
        )
    

    def delete_supplier(self, supplier_id: int)-> bool:

        return self.service.delete_(    
        supplier_id
    )