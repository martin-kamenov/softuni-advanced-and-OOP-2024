from typing import List
from project.products.base_product import BaseProduct
from project.products.chair import Chair
from project.products.hobby_horse import HobbyHorse
from project.stores.base_store import BaseStore
from project.stores.furniture_store import FurnitureStore
from project.stores.toy_store import ToyStore


class FactoryManager:

    PRODUCT_TYPES = {
        'Chair': Chair,
        'HobbyHorse': HobbyHorse
    }

    STORE_TYPES = {
        'FurnitureStore': FurnitureStore,
        'ToyStore': ToyStore
    }

    def __init__(self, name: str):
        self.name = name
        self.income: float = 0
        self.products: List[BaseProduct] = []
        self.stores: List[BaseStore] = []

    def produce_item(self, product_type: str, model: str, price: float) -> str:
        if product_type not in self.PRODUCT_TYPES:
            raise Exception("Invalid product type!")

        product = self.PRODUCT_TYPES[product_type](model, price)
        self.products.append(product)

        return f"A product of sub-type {product.sub_type} was produced."

    def register_new_store(self, store_type: str, name: str, location: str) -> str:
        if store_type not in self.STORE_TYPES:
            raise Exception(f"{store_type} is an invalid type of store!")

        store = self.STORE_TYPES[store_type](name, location)
        self.stores.append(store)

        return f"A new {store_type} was successfully registered."

    def sell_products_to_store(self, store: BaseStore, *products: BaseProduct) -> str:
        if store.capacity < len(products):
            return f"Store {self.name} has no capacity for this purchase."


        if store.store_type == 'FurnitureStore':
            allowed_products = [p for p in products if p.sub_type == 'Furniture']

        elif store.store_type == 'ToyStore':
            allowed_products = [p for p in products if p.sub_type == 'Toys']

        else:
            return "Products do not match in type. Nothing sold."

        if not allowed_products:
            return "Products do not match in type. Nothing sold."

        purchased_products = 0

        for product in allowed_products:
            store.products.append(product)
            self.products.remove(product)
            store.capacity -= 1
            self.income += product.price
            purchased_products += 1

        return f"Store {store.name} successfully purchased {purchased_products} items."

    def unregister_store(self, store_name: str) -> str:
        store = self._get_store(store_name)

        if store is None:
            raise Exception("No such store!")

        if store.products:
            return "The store is still having products in stock! Unregistering is inadvisable."

        self.stores.remove(store)

        return f"Successfully unregistered store {store_name}, location: {store.location}."

    def discount_products(self, product_model: str) -> str:
        discounted_products = 0

        for product in self.products:
            if product.model == product_model:
                product.discount()
                discounted_products += 1

        return f"Discount applied to {discounted_products} products with model: {product_model}"

    def request_store_stats(self, store_name: str) -> str:
        store = self._get_store(store_name)

        if store is None:
            return "There is no store registered under this name!"

        return store.store_stats()

    def statistics(self) -> str:
        result = [
            f"Factory: {self.name}",
            f"Income: {self.income:.2f}",
            f"***Products Statistics***",
        ]


        if self.products:
            sorted_unsold_products = sorted(self.products, key=lambda p: p.model)
            result.append(f"Unsold Products: {len(sorted_unsold_products)}. "
                          f"Total net price: {sum(p.price for p in sorted_unsold_products):.2f}")

            for product in sorted_unsold_products:
                result.append(f'{product.model}: {len(product.sub_type)}')

        if self.stores:
            sorted_stores = sorted(self.stores, key=lambda s: s.name)
            result.append(f"***Partner Stores: {len(sorted_stores)}***")

            [result.append(store.name) for store in self.stores]

        return '\n'.join(result)

    def _get_store(self, store_name):
        return next((store for store in self.stores if store.name == store_name), None)