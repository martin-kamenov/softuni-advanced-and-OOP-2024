from typing import List
from project.clients.adult import Adult
from project.clients.student import Student
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan


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

        loan = self.LOAN_TYPES[loan_type]()
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
               f"Total Income: {total_clients_income:.2f}\n" \
               f"Granted Loans: {loans_count_granted_to_clients}, Total Sum: {granted_sum:.2f}\n" \
               f"Available Loans: {len(self.loans)}, Total Sum: {not_granted_sum:.2f}\n" \
               f"Average Client Interest Rate: {avg_client_interest_rate:.2f}"

    def _get_client(self, client_id):
        return next((c for c in self.clients if c.client_id == client_id))

    def _get_loan_type(self, loan_type) -> List:
        return [l for l in self.loans if l.LOAN_TYPE == loan_type]

    def _get_client_by_min_rate(self, min_rate) -> List:
        return [c for c in self.clients if c.interest < min_rate]