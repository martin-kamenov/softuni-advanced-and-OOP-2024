from typing import List
from pokemon import Pokemon


class Trainer:

    def __init__(self, name: str):
        self.name = name
        self.pokemons: List[Pokemon] = []

    def add_pokemon(self, pokemon_: Pokemon) -> str:
        if pokemon_ not in self.pokemons:
            self.pokemons.append(pokemon_)
            return f'Caught {pokemon_.pokemon_details()}'

        return f"This pokemon is already caught"

    def release_pokemon(self, pokemon_name: str) -> str:
        # Option 1 -> fast but long
        # pokemon = None
        #
        # for p in self.pokemons:
        #     if p.name == pokemon_name:
        #         pokemon = p
        #         break

        # Option 2 -> slow, but short
        # try:
        #     pokemon = [p for p in self.pokemons if p.name == pokemon_name][0]
        # except IndexError:
        #     return "Pokemon is not caught"

        # Option 3 -> fast and short
        try:
            pokemon_ = next(filter(lambda p: p.name == pokemon_name, self.pokemons))
        except StopIteration:
            return f"Pokemon is not caught"
        else:
            self.pokemons.remove(pokemon_)
            return f"You have released {pokemon_name}"

    def trainer_data(self) -> str:
        pokemons_data = '\n'.join(f"- {p.pokemon_details()}" for p in self.pokemons)

        return f"Pokemon Trainer {self.name}\n" \
               f"Pokemon count {len(self.pokemons)}\n" \
               f"{pokemons_data}"


pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())
