from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak


class SummitClimber(BaseClimber):
    INITIAL_STRENGTH = 150
    MIN_NEEDED_STRENGTH = 75

    def __init__(self, name: str):
        super().__init__(name, strength=SummitClimber.INITIAL_STRENGTH)

    @property
    def min_needed_strength(self) -> int:
        return SummitClimber.MIN_NEEDED_STRENGTH

    def climb(self, peak: BasePeak):
        self.strength = self.strength - 30 * 1.3 if peak.difficulty_level == "Advanced" else self.strength - 30 * 2.5
        self.conquered_peaks.append(peak.name)