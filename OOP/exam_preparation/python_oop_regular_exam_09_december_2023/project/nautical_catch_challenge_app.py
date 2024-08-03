from typing import List
from project.divers.free_diver import FreeDiver
from project.divers.scuba_diver import ScubaDiver
from project.fish.deep_sea_fish import DeepSeaFish
from project.fish.predatory_fish import PredatoryFish


class NauticalCatchChallengeApp:

    DIVER_TYPES = {
        'FreeDiver': FreeDiver,
        'ScubaDiver': ScubaDiver,
    }

    FISH_TYPES = {
        'PredatoryFish': PredatoryFish,
        'DeepSeaFish': DeepSeaFish,
    }

    def __init__(self):
        self.divers: List[FreeDiver or ScubaDiver] = []
        self.fish_list: List[DeepSeaFish or PredatoryFish] = []

    def dive_into_competition(self, diver_type: str, diver_name: str) -> str:
        if diver_type not in NauticalCatchChallengeApp.DIVER_TYPES:
            return f"{diver_type} is not allowed in our competition."

        if self._find_object(diver_name, self.divers):
            return f"{diver_name} is already a participant."

        diver = NauticalCatchChallengeApp.DIVER_TYPES[diver_type](diver_name)
        self.divers.append(diver)

        return f"{diver_name} is successfully registered for the competition as a {diver_type}."

    def swim_into_competition(self, fish_type: str, fish_name: str, points: float) -> str:
        if fish_type not in NauticalCatchChallengeApp.FISH_TYPES:
            return f"{fish_type} is forbidden for chasing in our competition."

        if self._find_object(fish_name, self.fish_list):
            return f"{fish_name} is already permitted."

        fish = NauticalCatchChallengeApp.FISH_TYPES[fish_type](fish_name, points)
        self.fish_list.append(fish)

        return f"{fish_name} is allowed for chasing as a {fish_type}."

    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool) -> str:
        diver = self._find_object(diver_name, self.divers)
        fish = self._find_object(fish_name, self.fish_list)

        if not diver:
            return f"{diver_name} is not registered for the competition."

        if not fish:
            return f"The {fish_name} is not allowed to be caught in this competition."

        if diver.has_health_issue:
            return f"{diver_name} will not be allowed to dive, due to health issues."

        if diver.oxygen_level < fish.time_to_catch:
            diver.miss(fish.time_to_catch)

            if diver.oxygen_level == 0:
                diver.update_health_status()

            return f"{diver_name} missed a good {fish_name}."

        elif diver.oxygen_level == fish.time_to_catch:
            if is_lucky:
                diver.hit(fish)

                if diver.oxygen_level == 0:
                    diver.update_health_status()

                return f"{diver_name} hits a {fish.points}pt. {fish_name}."

            else:
                diver.miss(fish.time_to_catch)

                if diver.oxygen_level == 0:
                    diver.update_health_status()

                return f"{diver_name} missed a good {fish_name}."

        else:
            diver.hit(fish)

            if diver.oxygen_level == 0:
                diver.update_health_status()

            return f"{diver_name} hits a {fish.points}pt. {fish_name}."

    def health_recovery(self) -> str:
        count = 0

        for diver in self.divers:
            if diver.has_health_issue:
                count += 1
                diver.update_health_status()
                diver.renew_oxy()

        return f"Divers recovered: {count}"

    def diver_catch_report(self, diver_name: str) -> str:
        diver = self._find_object(diver_name, self.divers)

        result = f"**{diver_name} Catch Report**\n"
        result += '\n'.join(fish.fish_details() for fish in diver.catch)

        return result

    def competition_statistics(self) -> str:
        healthy_divers = [diver for diver in self.divers if not diver.has_health_issue]
        sorted_divers = sorted(healthy_divers, key=lambda d: (-d.competition_points, -len(d.catch), d.name))

        result = "**Nautical Catch Challenge Statistics**\n"
        result += '\n'.join(str(d) for d in sorted_divers)

        return result

    @staticmethod
    def _find_object(object_name, collection):
        return next(filter(lambda o: o.name == object_name, collection), None)