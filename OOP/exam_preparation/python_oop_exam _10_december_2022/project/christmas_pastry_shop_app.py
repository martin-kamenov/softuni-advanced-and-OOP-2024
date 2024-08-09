from project.booths.booth import Booth
from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.delicacy import Delicacy
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    INITIAL_VALUE = 0.0
    DELICACY_TYPES = {
        'Gingerbread': Gingerbread,
        'Stolen': Stolen
    }
    BOOTH_TYPES = {
        'Open Booth': OpenBooth,
        'Private Booth': PrivateBooth
    }

    def __init__(self):
        self.booths: list[Booth] = []
        self.delicacies: list[Delicacy] = []
        self.income = self.INITIAL_VALUE

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        if self._get_delicacy(name):
            raise Exception(f"{name} already exists!")

        if type_delicacy not in self.DELICACY_TYPES:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        delicacy = self.DELICACY_TYPES[type_delicacy](name, price)
        self.delicacies.append(delicacy)

        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        if self._get_booth(booth_number):
            raise Exception(f"Booth number {booth_number} already exists!")

        if type_booth not in self.BOOTH_TYPES:
            raise Exception(f"{type_booth} is not a valid booth!")

        booth = self.BOOTH_TYPES[type_booth](booth_number, capacity)
        self.booths.append(booth)

        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        for booth in self.booths:
            if not booth.is_reserved and booth.capacity >= number_of_people:
                booth.reserve(number_of_people)
                return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."

        return f"No available booth for {number_of_people} people!"

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        booth = self._get_booth(booth_number)
        delicacy = self._get_delicacy(delicacy_name)

        if not booth:
            raise Exception(f"Could not find booth {booth_number}!")

        if not delicacy:
            raise Exception(f"No {delicacy_name} in the pastry shop!")

        booth.delicacy_orders.append(delicacy)
        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        booth = self._get_booth(booth_number)

        if booth:
            bill = booth.get_bill()
            self.income += bill
            booth.delicacy_orders = []
            booth.is_reserved = False
            booth.price_for_reservation = 0

            return f"Booth {booth_number}:\n" \
                   f"Bill: {bill:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."

    def _get_delicacy(self, name):
        return next((d for d in self.delicacies if d.name == name), None)

    def _get_booth(self, number):
        return next((b for b in self.booths if b.booth_number == number), None)