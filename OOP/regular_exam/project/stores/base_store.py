from abc import ABC, abstractmethod
from typing import List
from project.products.base_product import BaseProduct


class BaseStore(ABC):

    def __init__(self, name: str, location: str, capacity: int):
        self.name = name
        self.location = location
        self.capacity = capacity
        self.products: List[BaseProduct] = []

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str):
        if not value.strip():
            raise ValueError("Store name cannot be empty!")
        self.__name = value

    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, value: str):
        if len(value.strip()) != 3:
            raise ValueError("Store location must be 3 chars long!")
        self.__location = value

    @property
    def capacity(self) -> int:
        return self.__capacity

    @capacity.setter
    def capacity(self, value: int):
        if value < 0:
            raise ValueError("Store capacity must be a positive number or 0!")
        self.__capacity = value

    #TODO Check here, logic might be incorrect
    def get_estimated_profit(self) -> str:
        products_sum = sum(p.price for p in self.products)
        estimated_profit = products_sum * 0.1

        return f"Estimated future profit for {len(self.products)} products is {estimated_profit:.2f}"

    @property
    @abstractmethod
    def store_type(self):
        ...

    @abstractmethod
    def store_stats(self):
        ...