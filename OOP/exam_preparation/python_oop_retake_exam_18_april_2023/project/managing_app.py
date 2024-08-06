from typing import List
from project.route import Route
from project.user import User
from project.vehicles.base_vehicle import BaseVehicle
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:

    VEHICLE_TYPES = {
        'PassengerCar': PassengerCar,
        'CargoVan': CargoVan
    }

    def __init__(self):
        self.users: List[User] = []
        self.vehicles: List[BaseVehicle] = []
        self.routes: List[Route] = []

    def register_user(self, first_name: str, last_name: str, driving_license_number: str) -> str:
        for user in self.users:
            if user.driving_license_number == driving_license_number:
                return f"{driving_license_number} has already been registered to our platform."

        new_user = User(first_name, last_name, driving_license_number)
        self.users.append(new_user)

        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str) -> str:
        if vehicle_type not in self.VEHICLE_TYPES:
            return f"Vehicle type {vehicle_type} is inaccessible."

        for vehicle in self.vehicles:
            if vehicle.license_plate_number == license_plate_number:
                return f"{license_plate_number} belongs to another vehicle."

        new_vehicle = self.VEHICLE_TYPES[vehicle_type](brand, model, license_plate_number)
        self.vehicles.append(new_vehicle)

        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float) -> str:
        route_id = len(self.routes) + 1
        filtered_route = self._find_route_with_start_and_end_point(start_point, end_point)

        if filtered_route:
            if filtered_route.length == length:
                return f"{start_point}/{end_point} - {length} km had already been added to our platform."

            if filtered_route.length < length:
                return f"{start_point}/{end_point} shorter route had already been added to our platform."

            if filtered_route.length > length:
                filtered_route.is_locked = True

        new_route = Route(start_point, end_point, length, route_id)
        self.routes.append(new_route)

        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,  is_accident_happened: bool) -> str:
        user = next(filter(lambda u: u.driving_license_number == driving_license_number, self.users))
        vehicle = next(filter(lambda v: v.license_plate_number == license_plate_number, self.vehicles))
        route = next(filter(lambda r: r.route_id == route_id, self.routes))

        if user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."

        if vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."

        if route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."

        vehicle.drive(route.length)

        if is_accident_happened:
            vehicle.change_status()
            user.decrease_rating()
        else:
            user.increase_rating()

        return f"{vehicle.brand} {vehicle.model} License plate: {vehicle.license_plate_number} " \
               f"Battery: {vehicle.battery_level}% Status: {'OK' if not vehicle.is_damaged else 'Damaged'}"

    def repair_vehicles(self, count: int) -> str:
        filtered_vehicles = [v for v in self.vehicles if v.is_damaged]
        sorted_vehicles = sorted(filtered_vehicles, key=lambda v: (v.brand[0], v.model[0]))

        if len(sorted_vehicles) > count:
            sorted_vehicles = sorted_vehicles[:count]

        for vehicle in sorted_vehicles:
            vehicle.change_status()
            vehicle.recharge()

        return f"{len(sorted_vehicles)} vehicles were successfully repaired!"

    def users_report(self) -> str:
        sorted_users = sorted(self.users, key=lambda u: -u.rating)

        result = "*** E-Drive-Rent ***\n"
        result += '\n'.join(str(u) for u in sorted_users)

        return result.strip()

    def _find_route_with_start_and_end_point(self, start_point: str, end_point: str):
        return next((r for r in self.routes if r.start_point == start_point and r.end_point == end_point), None)
