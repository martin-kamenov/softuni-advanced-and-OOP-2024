from typing import List

from project.drink import Drink
from project.food import Food

class ProductRepository:

    def __init__(self):
        self.products: List[Food, Drink] = []

    def add(self, product: Food or Drink):
        self.products.append(product)

    def find(self, product_name: str) -> str:
        product = next((p for p in self.products if p.name == product_name), None)

        if product:
            return product

    def remove(self, product_name: str) -> None:
        product = self.find(product_name)

        if product:
            self.products.remove(product)

    def __repr__(self):
        return "\n".join(f"{p.name}: {p.quantity}"for p in self.products)