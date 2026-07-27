"""
File    : product.py
Project : SMART POS

Model Product
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class Product:
    category_id: int
    supplier_id: int
    purchase_price: float
    selling_price: float
    id: Optional[int] = None
    product_name: str = ""
    barcode: str = ""
    stock: int = 0
    minimum_stock: int = 0
    unit: str = ""
    description: str = ""

    # Field tambahan hasil JOIN dari repository
    category_name: Optional[str] = None
    supplier_name: Optional[str] = None