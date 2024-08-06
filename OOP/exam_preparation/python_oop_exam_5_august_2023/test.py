from typing import List
from abc import ABC, abstractmethod


class BaseLoan(ABC):

    def __init__(self, interest_rate: float, amount: float):
        self.interest_rate = interest_rate
        self.amount = amount

    @abstractmethod
    def increase_interest_rate(self):
        ...

class MortgageLoan(BaseLoan):
    INTEREST_RATE = 3.5
    LOAN_AMOUNT = 50_000.0
    RATE_INCREMENT = 0.5
    LOAN_TYPE = 'MortgageLoan'

    def __init__(self):
        super().__init__(interest_rate=self.INTEREST_RATE, amount=self.LOAN_AMOUNT)

    def increase_interest_rate(self):
        self.interest_rate += self.RATE_INCREMENT

class StudentLoan(BaseLoan):
    INTEREST_RATE = 1.5
    LOAN_AMOUNT = 2_000.0
    RATE_INCREMENT = 0.2
    LOAN_TYPE = 'StudentLoan'

    def __init__(self):
        super().__init__(interest_rate=self.INTEREST_RATE, amount=self.LOAN_AMOUNT)

    def increase_interest_rate(self):
        self.interest_rate += self.RATE_INCREMENT

class BaseClient(ABC):

    def __init__(self, name: str, client_id: str, income: float, interest: float):
        self.name = name
        self.client_id = client_id
        self.income = income
        self.interest = interest
        self.loans: List = []

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str):
        if not value.strip():
            raise ValueError("Client name cannot be empty!")
        self.__name = value

    @property
    def client_id(self):
        return self.__client_id

    @client_id.setter
    def client_id(self, value):
        if len(value) != 10:
            raise ValueError("Client ID should be 10 symbols long!")
        self.__client_id = value

    @property
    def income(self):
        return self.__income

    @income.setter
    def income(self, value):
        if value <= 0.0:
            raise ValueError("Income must be greater than zero!")
        self.__income = value

    @abstractmethod
    def increase_clients_interest(self):
        ...

class Student(BaseClient):
    INITIAL_INTEREST = 2.0
    INCREASE_INTEREST = 1.0
    LOAN_TYPE = 'StudentLoan'

    def __init__(self, name: str, client_id: str, income: float):
        super().__init__(name, client_id, income, interest=self.INITIAL_INTEREST)

    def increase_clients_interest(self):
        self.interest += self.INCREASE_INTEREST

class Adult(BaseClient):
    INITIAL_INTEREST = 4.0
    INCREASE_INTEREST = 2.0
    LOAN_TYPE = 'MortgageLoan'


    def __init__(self, name: str, client_id: str, income: float):
        super().__init__(name, client_id, income, interest=self.INITIAL_INTEREST)

    def increase_clients_interest(self):
        self.interest += self.INCREASE_INTEREST

class BankApp:

    LOAN_TYPES = {
        'StudentLoan': StudentLoan,
        'MortgageLoan': MortgageLoan,
    }

    CLIENTS_TYPES = {
        'Student': Student,
        'Adult': Adult,
    }

    def __init__(self,capacity: int):
        self.capacity = capacity
        self.loans: List = []
        self.clients: List = []

    def add_loan(self, loan_type: str) -> str:
        if loan_type not in self.LOAN_TYPES:
            raise Exception("Invalid loan type!")

        loan = self.LOAN_TYPES[loan_type]
        self.loans.append(loan)

        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float) -> str:
        if client_type not in self.CLIENTS_TYPES:
            raise Exception("Invalid client type!")

        if self.capacity <= len(self.clients):
            return "Not enough bank capacity."

        client = self.CLIENTS_TYPES[client_type](client_name, client_id, income)
        self.clients.append(client)

        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str) -> str:
        client = self._get_client(client_id)
        loan = self._get_loan_type(loan_type)[0]

        if client.LOAN_TYPE != loan_type:
            raise Exception("Inappropriate loan type!")

        self.loans.remove(loan)
        client.loans.append(loan)

        return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."

    def remove_client(self, client_id: str) -> str:
        client = self._get_client(client_id)

        if not client:
            raise Exception("No such client!")

        if client.loans:
            raise Exception("The client has loans! Removal is impossible!")

        self.clients.remove(client)
        return f"Successfully removed {client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str) -> str:
        filtered_loans = self._get_loan_type(loan_type)
        [loan.increase_interest_rate() for loan in filtered_loans]

        return f"Successfully changed {len(filtered_loans)} loans."


    def increase_clients_interest(self, min_rate: float) -> str:
        clients = self._get_client_by_min_rate(min_rate)
        [c.increase_clients_interest() for c in clients]

        return f"Number of clients affected: {len(clients)}."

    def get_statistics(self) -> str:
        total_clients_income = sum(c.income for c in self.clients)
        loans_count_granted_to_clients = sum(len(c.loans) for c in self.clients)
        granted_sum = sum(sum(l.amount for l in c.loans) for c in self.clients)
        not_granted_sum = sum(l.amount for l in self.loans)
        avg_client_interest_rate = sum(c.interest for c in self.clients) / len(self.clients) if self.clients else 0

        return f"Active Clients: {len(self.clients)}\n" \
               f"Total Income: {total_clients_income}\n" \
               f"Granted Loans: {loans_count_granted_to_clients}, Total Sum: {granted_sum}\n" \
               f"Available Loans: {len(self.loans)}, Total Sum: {not_granted_sum}\n" \
               f"Average Client Interest Rate: {avg_client_interest_rate}"

    def _get_client(self, client_id):
        return next((c for c in self.clients if c.client_id == client_id))

    def _get_loan_type(self, loan_type) -> List:
        return [l for l in self.loans if l.LOAN_TYPE == loan_type]

    def _get_client_by_min_rate(self, min_rate) -> List:
        return [c for c in self.clients if c.interest < min_rate]

bank = BankApp(3)

print(bank.add_loan('StudentLoan'))
print(bank.add_loan('MortgageLoan'))
print(bank.add_loan('StudentLoan'))
print(bank.add_loan('MortgageLoan'))

print(bank.add_client('Student', 'Peter Simmons', '1234567891', 500))
print(bank.add_client('Adult', 'Samantha Peters', '1234567000', 1000))
print(bank.add_client('Student', 'Simon Mann', '1234567999', 700))
print(bank.add_client('Student', 'Tammy Smith', '1234567555', 700))

print(bank.grant_loan('StudentLoan', '1234567891'))
print(bank.grant_loan('MortgageLoan', '1234567000'))
print(bank.grant_loan('MortgageLoan', '1234567000'))

print(bank.remove_client('1234567999'))

print(bank.increase_loan_interest('StudentLoan'))
print(bank.increase_loan_interest('MortgageLoan'))

print(bank.increase_clients_interest(1.2))
print(bank.increase_clients_interest(3.5))

print(bank.get_statistics())

