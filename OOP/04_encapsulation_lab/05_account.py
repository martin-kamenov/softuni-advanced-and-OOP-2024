class Account:

    def __init__(self, id_: int, balance: int, pin: int):
        self.__id = id_
        self.balance = balance
        self.__pin = pin

    def get_id(self, pin: int) -> str or int:
        if pin != self.__pin:
            return f'Wrong pin'

        return self.__id

    def change_pin(self, old_pint: int, new_pin: int):
        if old_pint != self.__pin:
            return f"Wrong pin"

        self.__pin = new_pin
        return f"Pin changed"


account = Account(8827312, 100, 3421)
print(account.get_id(1111))
print(account.get_id(3421))
print(account.balance)
print(account.change_pin(2212, 4321))
print(account.change_pin(3421, 1234))
