from abc import ABC, abstractmethod


class Vehicle(ABC):

    def __init__(self, fuel_quantity: int, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance: int):
        ...

    @abstractmethod
    def refuel(self, fuel: int):
        ...


class Car(Vehicle):

    AIR_CONDITIONER_CONSUMPTION: float = 0.9

    def drive(self, distance: int):
        consumption_fuel = (self.fuel_consumption + Car.AIR_CONDITIONER_CONSUMPTION) * distance

        if consumption_fuel <= self.fuel_quantity:
            self.fuel_quantity -= consumption_fuel

    def refuel(self, fuel: int):
        self.fuel_quantity += fuel

class Truck(Vehicle):

    AIR_CONDITIONER_CONSUMPTION: float = 1.6
    TANK_WITH_HOLE = 0.95

    def drive(self, distance: int):
        consumption_fuel = (self.fuel_consumption + Truck.AIR_CONDITIONER_CONSUMPTION) * distance

        if consumption_fuel <= self.fuel_quantity:
            self.fuel_quantity -= consumption_fuel

    def refuel(self, fuel: int):
        self.fuel_quantity += fuel * Truck.TANK_WITH_HOLE


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)

truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
