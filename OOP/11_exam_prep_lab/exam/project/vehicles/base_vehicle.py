from abc import ABC, abstractmethod


class BaseVehicle(ABC):
    INITIAL_BATTERY_LEVEL: int = 100

    def __init__(self, brand: str, model: str, license_plate_number: str, max_mileage: float):
        self.brand = brand
        self.model = model
        self.license_plate_number = license_plate_number
        self.max_mileage = max_mileage
        self.battery_level: int = self.INITIAL_BATTERY_LEVEL
        self.is_damaged: bool = False

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, value):
        if not value.strip():
            raise ValueError("Brand cannot be empty!")
        self.__brand = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if not value.strip():
            raise ValueError("Model cannot be empty!")
        self.__model = value

    @property
    def license_plate_number(self):
        return self.__license_plate_number

    @license_plate_number.setter
    def license_plate_number(self, value):
        if not value.strip():
            raise ValueError("License plate number is required!")
        self.__license_plate_number = value

    @abstractmethod
    def drive(self, mileage: float):
        ...

    def recharge(self):
        self.battery_level = self.INITIAL_BATTERY_LEVEL

    def change_status(self):
        self.is_damaged = not self.is_damaged

    def __str__(self):
        return (f"{self.brand} {self.model} License plate: {self.license_plate_number} "
                f"Battery: {self.battery_level}% Status: {'OK' if not self.is_damaged else 'Damaged'}")