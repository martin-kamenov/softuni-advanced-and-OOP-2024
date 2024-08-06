from project.equipment.base_equipment import BaseEquipment


class KneePad(BaseEquipment):
    PERCENT_TO_INCREASE = 1.2
    PRICE = 15
    PROTECTION = 120
    TYPE = 'KneePad'

    def __init__(self):
        super().__init__(protection=self.PROTECTION, price=self.PRICE)

    def increase_price(self):
        self.price *= self.PERCENT_TO_INCREASE