from project.waiters.base_waiter import BaseWaiter


class HalfTimeWaiter(BaseWaiter):

    HOUR_WAGE = 12

    def calculate_earnings(self):
        return self.hours_worked * HalfTimeWaiter.HOUR_WAGE

    def report_shift(self):
        return f"{self.name} worked a half-time shift of {self.hours_worked} hours."