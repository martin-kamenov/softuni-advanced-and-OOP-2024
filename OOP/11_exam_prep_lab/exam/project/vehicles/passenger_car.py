from project.vehicles.base_vehicle import BaseVehicle


class PassengerCar(BaseVehicle):
    MAX_MILEAGE: int = 450
    MAX_PERCENT: int = 100

    def __init__(self, brand: str, model: str, license_plate_number: str):
        super().__init__(brand, model, license_plate_number, max_mileage=self.MAX_MILEAGE)

    def drive(self, mileage: float):
        self.battery_level -= int(mileage / self.MAX_MILEAGE * self.MAX_PERCENT)