from project.robots.base_robot import BaseRobot

class FemaleRobot(BaseRobot):

    FEMALE_KGS = 7

    def __init__(self, name: str, kind: str, price: float):
        super().__init__(name, kind, price, FemaleRobot.FEMALE_KGS)

    def eating(self):
        self.weight += 1