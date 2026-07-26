"""
File    : supplier.py
Project : SMART POS

Model Supplier
"""



from dataclasses import dataclass


@dataclass
class Supplier:

    id: int | None = None

    company_name: str = ""

    contact_person: str = ""

    phone: str = ""

    email: str = ""

    address: str = ""

    description: str = ""