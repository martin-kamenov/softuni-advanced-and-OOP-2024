from project.clients.base_client import BaseClient


class RegularClient(BaseClient):
    MEMBERSHIP_TYPE = 'Regular'

    def __init__(self, name: str):
        super().__init__(name, membership_type=RegularClient.MEMBERSHIP_TYPE)

    def earning_points(self, order_amount: float) -> int:
         points = int(order_amount / 10)
         self.points += points

         return points