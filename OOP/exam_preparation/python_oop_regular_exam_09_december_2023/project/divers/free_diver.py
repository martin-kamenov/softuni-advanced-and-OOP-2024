from project.divers.base_diver import BaseDiver


class FreeDiver(BaseDiver):

    OXYGEN_LEVEL = 120
    OXYGEN_PERCENT = 0.6

    def __init__(self, name: str):
        super().__init__(name, oxygen_level=FreeDiver.OXYGEN_LEVEL)

    @property
    def oxygen_percent(self) -> float:
        return FreeDiver.OXYGEN_PERCENT

    @property
    def initial_oxygen_level(self) -> float:
        return FreeDiver.OXYGEN_LEVEL
