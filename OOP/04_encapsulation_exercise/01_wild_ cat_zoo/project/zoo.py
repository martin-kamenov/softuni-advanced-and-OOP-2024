from typing import List, Union
from project.animal import Animal
from project.worker import Worker


class Zoo:

    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: List[Animal] = []
        self.workers: List[Worker] = []

    def add_animal(self, animal: Animal, price: int) -> str:
        if len(self.animals) == self.__animal_capacity:
            return "Not enough space for animal"

        if self.__budget < price:
            return "Not enough budget"

        self.animals.append(animal)
        self.__budget -= price

        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker) -> str:
        if len(self.workers) == self.__workers_capacity:
            return "Not enough space for worker"

        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name: str) -> str:
        try:
            worker = next(filter(lambda w: w.name == worker_name, self.workers))
        except StopIteration:
            return f"There is no {worker_name} in the zoo"

        self.workers.remove(worker)
        return f"{worker_name} fired successfully"

    def pay_workers(self) -> str:
        salaries = sum(w.salary for w in self.workers)

        if self.__budget < salaries:
            return "You have no budget to pay your workers. They are unhappy"

        self.__budget -= salaries
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self) -> str:
        care_money = sum(a.money_for_care for a in self.animals)

        if self.__budget < care_money:
            return f"You have no budget to tend the animals. They are unhappy."

        self.__budget -= care_money
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount: int) -> None:
        self.__budget += amount

    def animals_status(self) -> str:
        # 2nd way
        #
        # lions = list(filter(lambda a: a.__class__.__name__ == 'Lion', self.02_animals))
        # tigers = list(filter(lambda a: a.__class__.__name__ == 'Tiger', self.02_animals))
        # cheetahs = list(filter(lambda a: a.__class__.__name__ == 'Cheetah', self.02_animals))


        # 1st way
        #
        # lions = []
        # tigers = []
        # cheetahs = []
        #
        # for animal in self.02_animals:
        #     if animal.__class__.__name__ == 'Lion':
        #         lions.append(repr(animal))
        #
        #     if animal.__class__.__name__ == 'Tiger':
        #         tigers.append(repr(animal))
        #
        #     if animal.__class__.__name__ == 'Cheetah':
        #         cheetahs.append(repr(animal))

        # result = [
        #     f"You have {len(self.02_animals)} 02_animals",
        #     f"----- {len(lions)} Lions:"
        # ]
        #
        # ------------------------------------------------------------
        #
        # result.extend(lions)
        #
        # result.append(f"----- {len(tigers)} Tigers:")
        # result.extend(tigers)
        #
        # result.append(f"----- {len(cheetahs)} Cheetahs:")
        # result.extend(cheetahs)
        #
        # return "\n".join(result)


        # 3rd way

        return self.__print_status(self.animals, 'Lion', 'Tiger', 'Cheetah')

    def workers_status(self) -> str:
        return self.__print_status(self.workers, 'Keeper', 'Caretaker', 'Vet')

    @staticmethod
    def __print_status(category: List[Union[Animal,Worker]], *args) -> str:
        elements = {arg: [] for arg in args}

        for object_ in category:
            elements[object_.__class__.__name__].append(repr(object_))

        result = [f'You have {len(category)} {str(category[0].__class__.__bases__[0].__name__).lower()}s']

        for key in args:
            value = elements[key]

            result.append(f'----- {len(value)} {key}s:')
            result.extend(value)

        return "\n".join(result)