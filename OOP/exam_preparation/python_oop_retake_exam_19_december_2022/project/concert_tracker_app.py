from typing import List
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.musician import Musician
from project.band import Band
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:

    MUSICIAN_TYPES = {
        'Guitarist': Guitarist,
        'Drummer': Drummer,
        'Singer': Singer
    }

    def __init__(self):
        self.bands: List[Band] = []
        self.musicians: List[Musician] = []
        self.concerts: List[Concert] = []

    def _find_musician(self, musician_name):
        return next(filter(lambda m: m.name == musician_name, self.musicians), None)

    def _find_band(self, band_name):
        return next(filter(lambda b: b.name == band_name, self.bands), None)

    def _find_concert_at_place(self, place):
        return next(filter(lambda c: c.place == place, self.concerts), None)

    def create_musician(self, musician_type: str, name: str, age: int) -> str:
        if musician_type not in self.MUSICIAN_TYPES:
            raise ValueError("Invalid musician type!")

        if self._find_musician(name):
            raise Exception(f"{name} is already a musician!")

        musician = self.MUSICIAN_TYPES[musician_type](name, age)
        self.musicians.append(musician)

        return f"{name} is now a {musician_type}."

    def create_band(self, name: str) -> str:
        if self._find_band(name):
            raise Exception(f"{name} band is already created!")

        band = Band(name)
        self.bands.append(band)

        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str) -> str:
        concert_rented_the_place = self._find_concert_at_place(place)
        if concert_rented_the_place:
            raise Exception(f"{place} is already registered for {concert_rented_the_place.genre} concert!")

        new_concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(new_concert)

        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str) -> str:
        musician = self._find_musician(musician_name)
        band = self._find_band(band_name)

        if not musician:
            raise Exception(f"{musician_name} isn't a musician!")

        if not band:
            raise Exception(f"{band_name} isn't a band!")

        band.members.append(musician)
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str) -> str:
        musician = self._find_musician(musician_name)
        band = self._find_band(band_name)

        if not band:
            raise Exception(f"{band_name} isn't a band!")

        if musician not in band.members:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        band.members.remove(musician)
        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str) -> str:
        concert = self._find_concert_at_place(concert_place)
        band = self._find_band(band_name)

        for musician_type in self.MUSICIAN_TYPES.keys():
            if not any(filter(lambda x: type(x).__name__ == musician_type, band.members)):
                raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        if concert.genre == 'Rock':
            for member in band.members:
                if type(member).__name__ == 'Drummer' and 'play the drums with drumsticks' not in member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if type(member).__name__ == 'Singer' and 'sing high pitch notes' not in member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if type(member).__name__ == 'Guitarist' and 'play rock' not in member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")

        if concert.genre == 'Metal':
            for member in band.members:
                if type(member).__name__ == 'Drummer' and 'play the drums with drumsticks' not in member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if type(member).__name__ == 'Singer' and 'sing low pitch notes' not in member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if type(member).__name__ == 'Guitarist' and 'play metal' not in member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")

        if concert.genre == 'Jazz':
            for member in band.members:
                if type(member).__name__ == 'Drummer' and 'play the drums with drum brushes' not in member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if type(member).__name__ == 'Singer' and 'sing high pitch notes and sing low pitch notes' not in member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if type(member).__name__ == 'Guitarist' and 'play jazz' not in member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")

        profit = (concert.audience * concert.ticket_price) - concert.expenses
        return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert_place}."
