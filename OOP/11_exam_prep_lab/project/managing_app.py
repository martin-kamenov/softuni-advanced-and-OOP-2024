from typing import List
from project.route import Route
from project.user import User
from project.vehicles.base_vehicle import BaseVehicle
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:

    VEHICLE_TYPES = {
        'PassengerCar': PassengerCar,
        'CargoVan': CargoVan,
    }

    def __init__(self):
        self.users: List[User] = []
        self.vehicles: List[BaseVehicle] = []
        self.routes: List[Route] = []

    @property
    def _find_next_route_id(self) -> int:
        return len(self.routes) + 1

    def _find_route_by_id(self, route_id) -> Route:
        find_route = [route for route in self.routes if route.route_id == route_id]
        return find_route[0] if self.routes else None

    def _find_user_by_driving_license_number(self, driving_license_number: str) -> User:
        return next((user for user in self.users if user.driving_license_number == driving_license_number), None)

    def _find_vehicle_by_license_plate_number(self, license_plate_number: str) -> BaseVehicle:
        return next((vehicle for vehicle in self.vehicles if vehicle.license_plate_number == license_plate_number), None)

    def _find_route_by_start_and_end_point(self, start_point: str, end_point: str) -> Route:
        return next((route for route in self.routes if route.start_point == start_point and route.end_point == end_point), None)

    def register_user(self, first_name: str, last_name: str, driving_license_number: str) -> str:
        if self._find_user_by_driving_license_number(driving_license_number):
            return f"{driving_license_number} has already been registered to our platform."

        user = User(first_name, last_name, driving_license_number)
        self.users.append(user)

        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str) -> str:
        if vehicle_type not in self.VEHICLE_TYPES:
            return f"Vehicle type {vehicle_type} is inaccessible."

        if self._find_vehicle_by_license_plate_number(license_plate_number):
            return f"{license_plate_number} belongs to another vehicle."

        vehicle = self.VEHICLE_TYPES[vehicle_type](brand, model, license_plate_number)
        self.vehicles.append(vehicle)

        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float) -> str:
        route = self._find_route_by_start_and_end_point(start_point, end_point)

        if route:
            if route.length == length:
                return f"{start_point}/{end_point} - {length} km had already been added to our platform."

            if route.length < length:
                return f"{start_point}/{end_point} shorter route had already been added to our platform."

            if route.length > length:
                route.is_locked = True

        route_id = self._find_next_route_id
        new_route = Route(start_point, end_point, length, route_id)
        self.routes.append(new_route)

        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,  is_accident_happened: bool) -> str:
        user = self._find_user_by_driving_license_number(driving_license_number)
        vehicle = self._find_vehicle_by_license_plate_number(license_plate_number)
        route = self._find_route_by_id(route_id)

        if user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."

        if vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."

        if route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."

        vehicle.drive(route.length)

        if is_accident_happened:
            vehicle.is_damaged = True
            user.decrease_rating()
        else:
            user.increase_rating()

        return str(vehicle)

    def repair_vehicles(self, count: int) -> str:
        damaged_vehicles = [vehicle for vehicle in self.vehicles if vehicle.is_damaged]
        ordered_damage_vehicles = sorted(damaged_vehicles, key=lambda v: (v.brand, v.model))[:count]

        for vehicle in ordered_damage_vehicles:
            vehicle.recharge()
            vehicle.change_status()

        return f"{len(ordered_damage_vehicles)} vehicles were successfully repaired!"

    def users_report(self) -> str:
        result = "*** E-Drive-Rent ***\n"
        ordered_users = sorted(self.users, key=lambda u: -u.rating)
        result += '\n'.join(str(u) for u in ordered_users)

        return result