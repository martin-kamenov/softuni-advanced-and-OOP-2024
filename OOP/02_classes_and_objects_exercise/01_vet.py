from typing import List


class Vet:
    animals: List = []
    space = 5

    def __init__(self, name: str):
        self.name = name
        self.animals: List = []

    def register_animal(self, animal_name: str) -> str:
        if Vet.space > 0:
            Vet.animals.append(animal_name)
            self.animals.append(animal_name)

            Vet.space -= 1

            return f"{animal_name} registered in the clinic"

        return f"Not enough space"

    def unregister_animal(self, animal_name: str) -> str:
        if animal_name not in Vet.animals:
            return f"{animal_name} not in the clinic"

        Vet.animals.remove(animal_name)
        self.animals.remove(animal_name)

        Vet.space += 1

        return f"{animal_name} unregistered successfully"

    def info(self) -> str:
        return f"{self.name} has {len(self.animals)} animals. {Vet.space} space left in clinic"


peter = Vet("Peter")
george = Vet("George")
print(peter.register_animal("Tom"))
print(george.register_animal("Cory"))
print(peter.register_animal("Fishy"))
print(peter.register_animal("Bobby"))
print(george.register_animal("Kay"))
print(george.unregister_animal("Cory"))
print(peter.register_animal("Silky"))
print(peter.unregister_animal("Molly"))
print(peter.unregister_animal("Tom"))
print(peter.info())
print(george.info())
