from project.equipment.base_equipment import BaseEquipment


class ElbowPad(BaseEquipment):
    PERCENT_TO_INCREASE = 1.10
    PRICE = 25
    PROTECTION = 90
    TYPE = 'ElbowPad'

    def __init__(self):
        super().__init__(protection=self.PROTECTION, price=self.PRICE)

    def increase_price(self):
        self.price *= self.PERCENT_TO_INCREASE