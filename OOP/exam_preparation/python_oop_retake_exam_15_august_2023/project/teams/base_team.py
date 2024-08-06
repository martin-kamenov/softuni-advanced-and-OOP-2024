from abc import ABC, abstractmethod
from typing import List
from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad


class BaseTeam(ABC):

    def __init__(self, name: str, country: str, advantage: int, budget: float):
        self.name = name
        self.country = country
        self.advantage = advantage
        self.budget = budget
        self.wins = 0
        self.equipment: List[KneePad or ElbowPad] = []

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value:str):
        if value.strip() == '':
            raise ValueError("Team name cannot be empty!")
        self.__name = value

    @property
    def country(self) -> str:
        return self.__country

    @country.setter
    def country(self, value: str):
        if len(value.strip()) < 2:
            raise ValueError("Team country should be at least 2 symbols long!")
        self.__country = value

    @property
    def advantage(self) -> int:
        return self.__advantage

    @advantage.setter
    def advantage(self, value: int):
        if value <= 0:
            raise ValueError("Advantage must be greater than zero!")
        self.__advantage = value

    @property
    @abstractmethod
    def advantage_points(self):
        ...

    def win(self):
        self.wins += 1
        self.advantage += self.advantage_points

    def get_statistics(self) -> str:
        return f"Name: {self.name}\n" \
               f"Country: {self.country}\n" \
               f"Advantage: {self.advantage} points\n" \
               f"Budget: {self.budget:.2f}EUR\n" \
               f"Wins: {self.wins}\n" \
               f"Total Equipment Price: {sum(e.price for e in self.equipment):.2f}\n" \
               f"Average Protection: {sum(e.protection for e in self.equipment) / len(self.equipment) if self.equipment else 0:.0f}"
