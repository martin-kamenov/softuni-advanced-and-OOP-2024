from typing import List
from project.clients.base_client import BaseClient
from project.clients.regular_client import RegularClient
from project.clients.vip_client import VIPClient
from project.waiters.base_waiter import BaseWaiter
from project.waiters.full_time_waiter import FullTimeWaiter
from project.waiters.half_time_waiter import HalfTimeWaiter


class SphereRestaurantApp:

    WAITERS_TYPE = {'FullTimeWaiter': FullTimeWaiter, 'HalfTimeWaiter': HalfTimeWaiter}
    CLIENTS_TYPE = {'RegularClient': RegularClient, 'VIPClient': VIPClient}

    def __init__(self):
        self.waiters: List[BaseWaiter] = []
        self.clients: List[BaseClient] = []

    def hire_waiter(self, waiter_type: str, waiter_name: str, hours_worked: int):
        if waiter_type not in self.WAITERS_TYPE:
            return f"{waiter_type} is not a recognized waiter type."

        waiter = self._get_waiter(waiter_name)

        if waiter is not None:
            return f"{waiter_name} is already on the staff."

        new_waiter = self.WAITERS_TYPE[waiter_type](waiter_name, hours_worked)
        self.waiters.append(new_waiter)

        return f"{waiter_name} is successfully hired as a {waiter_type}."


    def admit_client(self, client_type: str, client_name: str):
        if client_type not in self.CLIENTS_TYPE:
            return f"{client_type} is not a recognized client type."

        client = self._get_client(client_name)

        if client is not None:
            return f"{client_name} is already a client."

        new_client = self.CLIENTS_TYPE[client_type](client_name)
        self.clients.append(new_client)

        return f"{client_name} is successfully admitted as a {client_type}."

    def process_shifts(self, waiter_name: str):
        waiter = self._get_waiter(waiter_name)

        if waiter:
            return waiter.report_shift()

        return f"No waiter found with the name {waiter_name}."

    def process_client_order(self, client_name: str, order_amount: float):
        client = self._get_client(client_name)

        if client:
            earned_points = client.earning_points(order_amount)
            return f"{client_name} earned {earned_points} points from the order."

        return f"{client_name} is not a registered client."

    def apply_discount_to_client(self, client_name: str):
        client = self._get_client(client_name)

        if client is None:
            return f"{client_name} cannot get a discount because this client is not admitted!"

        discount_percentage, remaining_points = client.apply_discount()
        return f"{client_name} received a {discount_percentage}% discount. Remaining points {remaining_points}"

    def generate_report(self):
        sorted_waiters = sorted(self.waiters, key=lambda w: w.calculate_earnings(), reverse=True)

        waiter_info = "** Waiter Details **\n"
        for waiter in sorted_waiters:
            waiter_info += waiter.__str__() + "\n"

        total_earnings = sum(w.calculate_earnings() for w in self.waiters)
        total_points = sum(c.points for c in self.clients)
        total_clients = len(self.clients)

        report = "$$ Monthly Report $$\n"
        report += f"Total Earnings: ${total_earnings:.2f}\n"
        report += f"Total Clients Unused Points: {total_points}\n"
        report += f"Total Clients Count: {total_clients}\n"
        report += waiter_info

        return report.strip()

    def _get_waiter(self, waiter_name: str):
        waiter = next((w for w in self.waiters if w.name == waiter_name), None)

        return waiter

    def _get_client(self, client_name: str):
        client = next((w for w in self.clients if w.name == client_name), None)

        return client