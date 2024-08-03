from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak


class ArcticClimber(BaseClimber):
    INITIAL_STRENGTH = 200
    MIN_NEEDED_STRENGTH = 100

    def __init__(self, name: str):
        super().__init__(name, strength=ArcticClimber.INITIAL_STRENGTH)

    @property
    def min_needed_strength(self) -> int:
        return ArcticClimber.MIN_NEEDED_STRENGTH

    def climb(self, peak: BasePeak):
        self.strength = self.strength - 20 * 2 if peak.difficulty_level == 'Extreme' else self.strength - 20 * 1.5
        self.conquered_peaks.append(peak.name)