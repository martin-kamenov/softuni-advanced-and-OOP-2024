from abc import ABC, abstractmethod


class BaseWaiter(ABC):

    def __init__(self, name: str, hours_worked: int):
        self.name = name
        self.hours_worked = hours_worked

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        if len(name) < 3 or len(name) > 50:
            raise ValueError("Waiter name must be between 3 and 50 characters in length!")
        self.__name = name

    @property
    def hours_worked(self) -> int:
        return self.__hours_worked

    @hours_worked.setter
    def hours_worked(self, hours: int):
        if hours < 0:
            raise ValueError("Cannot have negative hours worked!")
        self.__hours_worked = hours

    @property
    @abstractmethod
    def hour_wage(self):
        ...

    def calculate_earnings(self) -> int:
        return self.hours_worked * self.hour_wage

    @property
    @abstractmethod
    def waiter_type(self):
        ...

    def report_shift(self) -> str:
        return f"{self.name} worked a {self.waiter_type} shift of {self.hours_worked} hours."

    def __str__(self):
        return f"Name: {self.name}, Total earnings: ${self.calculate_earnings():.2f}"