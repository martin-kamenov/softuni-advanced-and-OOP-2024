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
        self.climbers: List = []
        self.peaks: List = []

    def register_climber(self, climber_type: str, climber_name: str) -> str:
        try:
            climber = self.CLIMBER_TYPES[climber_type](climber_name)
        except KeyError:
            return f"{climber_type} doesn't exist in our register."

        try:
            next(filter(lambda c: c.name == climber_name, self.climbers))
            return f"{climber_name} has been already registered."
        except StopIteration:
            self.climbers.append(climber)

            return f"{climber_name} is successfully registered as a {climber_type}."

    def peak_wish_list(self, peak_type: str, peak_name: str, peak_elevation: int):
        try:
            peak = self.PEAK_TYPES[peak_type](peak_name, peak_elevation)
        except KeyError:
            return f"{peak_type} is an unknown type of peak."

        self.peaks.append(peak)

        return f"{peak_name} is successfully added to the wish list as a {peak_type}."

    def check_gear(self, climber_name: str, peak_name: str, gear: List[str]):
        peak = self._get_peak(peak_name)
        climber = self._get_climber(climber_name)

        if peak.get_recommended_gear() == gear:
            return f"{climber_name} is prepared to climb {peak_name}."

        climber.is_prepared = False
        missing_gear = [g for g in sorted(peak.get_recommended_gear()) if g not in gear]

        return f"{climber_name} is not prepared to climb {peak_name}. Missing gear: {', '.join(missing_gear)}."

    def perform_climbing(self, climber_name: str, peak_name: str):
        try:
            climber = self._get_climber(climber_name)
        except StopIteration:
            return f"Climber {climber_name} is not registered yet."

        try:
            peak = self._get_peak(peak_name)
        except StopIteration:
            return f"Peak {peak_name} is not part of the wish list."

        if not climber.is_prepared:
            return f"{climber_name} will need to be better prepared next time."

        if not climber.can_climb():
            climber.rest()
            return f"{climber_name} needs more strength to climb {peak_name} and is therefore taking some rest."

        climber.climb(peak)

        return f"{climber_name} conquered {peak_name} whose difficulty level is {peak.difficulty_level}."

    def get_statistics(self):
        climbers_that_can_climb = filter(lambda c: len(c.conquered_peaks) > 0, self.climbers)
        sorted_climbers = sorted(climbers_that_can_climb, key=lambda x: (-len(x.conquered_peaks), x.name[0]))

        total_climber_peaks = len({peak for climber in sorted_climbers for peak in climber.conquered_peaks})

        result = [f"Total climbed peaks: {total_climber_peaks}", "**Climber's statistics:**"]

        for climber in sorted_climbers:
            result.append(str(climber))

        return '\n'.join(result)

    def _get_climber(self, climber_name: str):
        return next((c for c in self.climbers if c.name == climber_name))

    def _get_peak(self, peak_name: str):
        return next((p for p in self.peaks if p.name == peak_name))