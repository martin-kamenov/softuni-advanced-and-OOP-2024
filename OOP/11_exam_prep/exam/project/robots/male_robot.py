from project.robots.base_robot import BaseRobot


class MaleRobot(BaseRobot):

    MALE_KGS = 9

    def __init__(self, name: str, kind: str, price: float):
        super().__init__(name, kind, price, MaleRobot.MALE_KGS)

    def eating(self):
        self.weight += 3