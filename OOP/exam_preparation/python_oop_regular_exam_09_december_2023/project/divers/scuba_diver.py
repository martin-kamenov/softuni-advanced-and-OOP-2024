from project.divers.base_diver import BaseDiver


class ScubaDiver(BaseDiver):
    OXYGEN_LEVEL = 540
    OXYGEN_PERCENT = 0.3

    def __init__(self, name: str):
        super().__init__(name, oxygen_level=ScubaDiver.OXYGEN_LEVEL)

    @property
    def oxygen_percent(self) -> float:
        return ScubaDiver.OXYGEN_PERCENT

    @property
    def initial_oxygen_level(self) -> int:
        return ScubaDiver.OXYGEN_LEVEL


