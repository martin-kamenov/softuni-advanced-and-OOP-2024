from typing import List
from project.equipment.knee_pad import KneePad
from project.equipment.elbow_pad import ElbowPad
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam


class Tournament:

    EQUIPMENT_TYPES = {
        "KneePad": KneePad,
        "ElbowPad": ElbowPad,
    }

    TEAM_TYPES = {
        "OutdoorTeam": OutdoorTeam,
        "IndoorTeam": IndoorTeam,
    }

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.equipment: List[KneePad or ElbowPad] = []
        self.teams: List[OutdoorTeam or IndoorTeam] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.isalnum():
            raise ValueError("Tournament name should contain letters and digits only!")
        self.__name = value

    def add_equipment(self, equipment_type: str) -> str:
        if equipment_type not in self.EQUIPMENT_TYPES:
            raise Exception("Invalid equipment type!")

        equipment = Tournament.EQUIPMENT_TYPES[equipment_type]()

        self.equipment.append(equipment)
        return f"{equipment_type} was successfully added."

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int) -> str:
        if team_type not in self.TEAM_TYPES:
            raise Exception("Invalid team type!")

        if self.capacity <= len(self.teams):
            return "Not enough tournament capacity."

        team = Tournament.TEAM_TYPES[team_type](team_name, country, advantage)
        self.teams.append(team)

        return f"{team_type} was successfully added."

    def sell_equipment(self, equipment_type: str, team_name: str) -> str:
        equipment = self._get_last_equipment_by_type(equipment_type)
        team = self._get_team(team_name)

        if team.budget < equipment.price:
            raise Exception("Budget is not enough!")

        self.equipment.remove(equipment)
        team.equipment.append(equipment)
        team.budget -= equipment.price

        return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name: str) -> str:
        try:
            team = self._get_team(team_name)
        except Exception:
            raise "No such team!"

        if team.wins:
            raise Exception(f"The team has {team.wins} wins! Removal is impossible!")

        self.teams.remove(team)
        return f"Successfully removed {team_name}."

    def increase_equipment_price(self, equipment_type: str) -> str:
        changed_equipment_pcs = len([e.increase_price() for e in self.equipment if e.TYPE == equipment_type])

        return f"Successfully changed {changed_equipment_pcs}pcs of equipment."

    def play(self, team_name1: str, team_name2: str) -> str:
        team1 = self._get_team(team_name1)
        team2 = self._get_team(team_name2)

        if not type(team1) == type(team2):
            raise Exception("Game cannot start! Team types mismatch!")

        team1_sum_points = team1.advantage + sum(e.protection for e in team1.equipment)
        team2_sum_points = team2.advantage + sum(e.protection for e in team2.equipment)

        if team1_sum_points > team2_sum_points:
            team1.win()
            return f"The winner is {team1.name}."

        if team1_sum_points < team2_sum_points:
            team2.win()
            return f"The winner is {team2.name}."

        return "No winner in this game."

    def get_statistics(self) -> str:
        sorted_teams = sorted(self.teams, key=lambda x: -x.wins)

        result = f"Tournament: {self.name}\nNumber of Teams: {len(self.teams)}\nTeams:\n"
        result += "\n".join(t.get_statistics() for t in sorted_teams)

        return result

    def _get_team(self, team_name):
        return next(filter(lambda t: t.name == team_name, self.teams), None)

    def _get_last_equipment_by_type(self, equipment_name):
        collection = [e for e in self.equipment if e.TYPE == equipment_name]
        return collection[-1] if collection else None