from abc import ABC, abstractmethod
from typing import List


class Animal(ABC):
    def __init__(self, name: str):
        self.name = name

    @staticmethod
    @abstractmethod
    def make_sound():
        ...


class Cat(Animal):

    @staticmethod
    def make_sound():
        print('meow')


class Dog(Animal):

    @staticmethod
    def make_sound():
        print('woof-woof')

class Duck(Animal):

    @staticmethod
    def make_sound():
        print('kwak-kwak')

def animal_sound(animals: List[Animal]):
    for animal in animals:
        animal.make_sound()


animals = [Cat('Mara'), Dog('Gosho'), Duck('Pesho')]
animal_sound(animals)

## добавете ново животно и рефакторирайте кода да работи без да се налага да се правят промени по него
## при добавяне на нови животни
# 02_animals = [Animal('cat'), Animal('dog'), Animal('chicken')]
