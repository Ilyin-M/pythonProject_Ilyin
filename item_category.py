from dataclasses import dataclass

@dataclass
class Item:
    name: str
    price: float
    rating: float

@dataclass
class Category:
    name_cat: str
    list_of_items: list