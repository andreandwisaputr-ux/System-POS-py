"""
File    : category.py
Project : SMART POS

Model Category
"""

from dataclasses import dataclass
from typing import Optional


@dataclass(slots=True)
class Category:
    """
    Model data untuk kategori produk.
    """

    id: Optional[int] = None
    name: str = ""
    description: str = ""