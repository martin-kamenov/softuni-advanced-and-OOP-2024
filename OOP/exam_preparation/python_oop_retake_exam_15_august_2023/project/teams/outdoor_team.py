from project.teams.base_team import BaseTeam


class OutdoorTeam(BaseTeam):
    TEAM_BUDGET = 1000
    TEAM_ADVANTAGE_POINTS = 115

    def __init__(self, name: str, country: str, advantage: int):
        super().__init__(name, country, advantage, budget=OutdoorTeam.TEAM_BUDGET)

    @property
    def advantage_points(self) -> int:
        return OutdoorTeam.TEAM_ADVANTAGE_POINTS