from project.teams.base_team import BaseTeam


class IndoorTeam(BaseTeam):
    TEAM_BUDGET = 500
    TEAM_ADVANTAGE_POINTS = 145


    def __init__(self, name: str, country: str, advantage: int):
        super().__init__(name, country, advantage, budget=IndoorTeam.TEAM_BUDGET)

    @property
    def advantage_points(self) -> int:
        return IndoorTeam.TEAM_ADVANTAGE_POINTS