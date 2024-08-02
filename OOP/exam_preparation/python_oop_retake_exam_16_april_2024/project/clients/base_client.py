from abc import ABC, abstractmethod
from typing import Tuple


class BaseClient(ABC):

    def __init__(self, name: str, membership_type: str):
        self.name = name
        self.membership_type = membership_type
        self.points: int = 0

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str):
        if value.strip() == '':
            raise ValueError("Client name should be determined!")

        self.__name = value

    @property
    def membership_type(self) -> str:
        return self.__membership_type

    @membership_type.setter
    def membership_type(self, value: str):
        if value not in ['Regular', 'VIP']:
            raise ValueError("Invalid membership type. Allowed types: Regular, VIP.")

        self.__membership_type = value

    @abstractmethod
    def earning_points(self, order_amount: float):
        ...

    def apply_discount(self) -> Tuple[int, int]:
        discount = 0

        if self.points >= 100:
            discount = 10
            self.points -= 100

        elif 50 <= self.points < 100:
            discount = 5
            self.points -= 50

        return discount, self.points
