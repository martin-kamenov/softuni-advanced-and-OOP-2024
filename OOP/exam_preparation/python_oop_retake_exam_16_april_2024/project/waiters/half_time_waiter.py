from project.waiters.base_waiter import BaseWaiter


class HalfTimeWaiter(BaseWaiter):

    def __init__(self, name: str, hours_worked: int):
        super().__init__(name, hours_worked)

    @property
    def hour_wage(self) -> int:
        return 12

    @property
    def waiter_type(self) -> str:
        return 'half-time'