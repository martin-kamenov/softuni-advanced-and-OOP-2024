from typing import List

from project.climbers.arctic_climber import ArcticClimber
from project.climbers.summit_climber import SummitClimber
from project.peaks.arctic_peak import ArcticPeak
from project.peaks.summit_peak import SummitPeak


class SummitQuestManagerApp:

    CLIMBER_TYPES = {
        'ArcticClimber': ArcticClimber,
        'SummitClimber': SummitClimber,
    }

    PEAK_TYPES = {
        'ArcticPeak': ArcticPeak,
        'SummitPeak': SummitPeak,
    }

    def __init__(self):
        self.climbers: List[ArcticClimber or SummitClimber] = []
        self.peaks: List[ArcticPeak or SummitPeak] = []

    def register_climber(self, climber_type: str, climber_name: str) -> str:
        if climber_type not in SummitQuestManagerApp.CLIMBER_TYPES:
            return f"{climber_type} doesn't exist in our register."

        if self._get_object(climber_name, self.climbers):
            return f"{climber_name} has been already registered."

        climber = SummitQuestManagerApp.CLIMBER_TYPES[climber_type](climber_name)
        self.climbers.append(climber)

        return f"{climber_name} is successfully registered as a {climber_type}."

    def peak_wish_list(self, peak_type: str, peak_name: str, peak_elevation: int) -> str:
        if peak_type not in SummitQuestManagerApp.PEAK_TYPES:
            return f"{peak_type} is an unknown type of peak."

        peak = SummitQuestManagerApp.PEAK_TYPES[peak_type](peak_name, peak_elevation)
        self.peaks.append(peak)

        return f"{peak_name} is successfully added to the wish list as a {peak_type}."

    def check_gear(self, climber_name: str, peak_name: str, gear: List[str]) -> str:
        climber = self._get_object(climber_name, self.climbers)
        peak = self._get_object(peak_name, self.peaks)

        if gear == peak.get_recommended_gear():
            climber.can_climb()
            return f"{climber_name} is prepared to climb {peak_name}."

        # missing_gear = [g for g in sorted(peak.get_recommended_gear()) if g not in gear]
        missing_gear = set(peak.get_recommended_gear()) - set(gear)
        climber.is_prepared = False

        return (f"{climber_name} is not prepared to climb {peak_name}. "
                f"Missing gear: {', '.join(sorted(missing_gear))}.")

    def perform_climbing(self, climber_name: str, peak_name: str) -> str:
        climber = self._get_object(climber_name, self.climbers)
        peak = self._get_object(peak_name, self.peaks)

        if not climber:
            return f"Climber {climber_name} is not registered yet."

        if not peak:
            return f"Peak {peak_name} is not part of the wish list."

        if not climber.is_prepared:
            return f"{climber_name} will need to be better prepared next time."

        if not climber.can_climb():
            climber.rest()
            return f"{climber_name} needs more strength to climb {peak_name} and is therefore taking some rest."

        climber.climb(peak)
        return f"{climber_name} conquered {peak_name} whose difficulty level is {peak.difficulty_level}."

    def get_statistics(self) -> str:
        climbers_with_conquered_peaks = filter(lambda c: len(c.conquered_peaks) > 0, self.climbers)
        sorted_climbers = sorted(climbers_with_conquered_peaks, key=lambda c: (-len(c.conquered_peaks), c.name))

        # total_climbed_peaks = len(self.peaks)
        total_climbed_peaks = len({peak for climber in sorted_climbers for peak in climber.conquered_peaks})

        result = f"Total climbed peaks: {total_climbed_peaks}\n" \
                 f"**Climber's statistics:**\n"
        result += '\n'.join(str(c) for c in sorted_climbers)

        return result

    @staticmethod
    def _get_object(object_name, collection):
        return next(filter(lambda object_: object_.name == object_name, collection), None)