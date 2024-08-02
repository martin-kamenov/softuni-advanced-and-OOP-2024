from project.clients.base_client import BaseClient


class VIPClient(BaseClient):
    MEMBERSHIP_TYPE = 'VIP'

    def __init__(self, name: str):
        super().__init__(name, membership_type=VIPClient.MEMBERSHIP_TYPE)

    def earning_points(self, order_amount: float) -> int:
        points = int(order_amount / 5)
        self.points += points

        return points