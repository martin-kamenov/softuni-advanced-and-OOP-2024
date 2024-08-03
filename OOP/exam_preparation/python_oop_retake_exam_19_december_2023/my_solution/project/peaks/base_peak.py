from abc import ABC, abstractmethod


class BasePeak(ABC):

    MINIMUM_ELEVATION_PEAK = 1500

    def __init__(self, name: str, elevation: int):
        self.name = name
        self.elevation = elevation
        self.difficulty_level = self.calculate_difficulty_level()

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str):
        if not len(value) >= 2:
            raise ValueError("Peak name cannot be less than 2 symbols!")
        self.__name = value

    @property
    def elevation(self) -> int:
        return self.__elevation

    @elevation.setter
    def elevation(self, value: int):
        if not value > BasePeak.MINIMUM_ELEVATION_PEAK:
            raise ValueError(f"Peak elevation cannot be below {BasePeak.MINIMUM_ELEVATION_PEAK}m.")
        self.__elevation = value

    @abstractmethod
    def get_recommended_gear(self):
        ...

    @abstractmethod
    def calculate_difficulty_level(self):
        ...