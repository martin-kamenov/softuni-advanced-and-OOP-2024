from project.peaks.base_peak import BasePeak
from project.climbers.base_climber import BaseClimber


class SummitClimber(BaseClimber):
    MINIMUM_STR_NEEDED = 75
    INITIAL_STR = 150

    def __init__(self, name: str):
        super().__init__(name, SummitClimber.INITIAL_STR)

    def can_climb(self) -> bool:
        return True if self.strength >= SummitClimber.MINIMUM_STR_NEEDED else False

    def climb(self, peak : BasePeak):
        self.strength = self.strength - 30 * 1.3 if peak.difficulty_level == "Advanced" else self.strength - 30 * 2.5
        self.conquered_peaks.append(peak.name)