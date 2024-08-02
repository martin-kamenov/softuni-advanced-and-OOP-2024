from typing import List

from project.clients.base_client import BaseClient
from project.clients.regular_client import RegularClient
from project.clients.vip_client import VIPClient
from project.waiters.base_waiter import BaseWaiter
from project.waiters.full_time_waiter import FullTimeWaiter
from project.waiters.half_time_waiter import HalfTimeWaiter


class SphereRestaurantApp:

    WAITER_TYPES = {
        'FullTimeWaiter': FullTimeWaiter,
        'HalfTimeWaiter': HalfTimeWaiter,
    }

    CLIENT_TYPES = {
        'RegularClient': RegularClient,
        'VIPClient': VIPClient
    }

    def __init__(self):
        self.waiters: List[BaseWaiter] = []
        self.clients: List[BaseClient] = []

    def hire_waiter(self, waiter_type: str, waiter_name: str, hours_worked: int) -> str:
        if waiter_type not in SphereRestaurantApp.WAITER_TYPES:
            return f"{waiter_type} is not a recognized waiter type."

        if self._get_object(waiter_name, self.waiters):
            return f"{waiter_name} is already on the staff."

        waiter = self.WAITER_TYPES[waiter_type](waiter_name, hours_worked)
        self.waiters.append(waiter)

        return f"{waiter_name} is successfully hired as a {waiter_type}."

    def admit_client(self, client_type: str, client_name: str) -> str:
        if client_type not in SphereRestaurantApp.CLIENT_TYPES:
            return f"{client_type} is not a recognized client type."

        if self._get_object(client_name, self.clients):
            return f"{client_name} is already a client."

        client = self.CLIENT_TYPES[client_type](client_name)
        self.clients.append(client)

        return f"{client_name} is successfully admitted as a {client_type}."

    def process_shifts(self, waiter_name: str) -> str:
        waiter = self._get_object(waiter_name, self.waiters)

        if waiter:
           return waiter.report_shift()

        return f"No waiter found with the name {waiter_name}."

    def process_client_order(self, client_name: str, order_amount: float) -> str:
        client = self._get_object(client_name, self.clients)

        if client:
            earned_points = client.earning_points(order_amount)
            return f"{client_name} earned {earned_points} points from the order."

        return f"{client_name} is not a registered client."

    def apply_discount_to_client(self, client_name: str) -> str:
        client = self._get_object(client_name, self.clients)

        if client:
            discount_percentage, remaining_points = client.apply_discount()
            return f"{client_name} received a {discount_percentage}% discount. Remaining points {remaining_points}"

        return f"{client_name} cannot get a discount because this client is not admitted!"

    def generate_report(self) -> str:
        sorted_waiters = sorted(self.waiters, key=lambda x: x.calculate_earnings(), reverse=True)

        waiter_details = '** Waiter Details **\n'
        waiter_details += '\n'.join(str(waiter) for waiter in sorted_waiters)

        total_earnings = sum(w.calculate_earnings() for w in self.waiters)
        total_client_points = sum(c.points for c in self.clients)
        clients_count = len(self.clients)

        result = "$$ Monthly Report $$\n"
        result += f"Total Earnings: ${total_earnings:.2f}\n"
        result += f"Total Clients Unused Points: {total_client_points}\n"
        result += f"Total Clients Count: {clients_count}\n"
        result += waiter_details

        return result

    @staticmethod
    def _get_object(object_name, collection):
        return next(filter(lambda x: x.name == object_name,collection), None)