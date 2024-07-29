from project.peaks.base_peak import BasePeak
from project.climbers.base_climber import BaseClimber


class ArcticClimber(BaseClimber):
    MINIMUM_STR_NEEDED = 100
    INITIAL_STR = 200

    def __init__(self, name: str):
        super().__init__(name, ArcticClimber.INITIAL_STR)

    def can_climb(self) -> bool:
        return True if self.strength >= ArcticClimber.MINIMUM_STR_NEEDED else False


    def climb(self, peak : BasePeak):
        self.strength = self.strength - 20 * 2 if peak.difficulty_level == "Extreme" else self.strength - 20 * 1.5
        self.conquered_peaks.append(peak.name)
