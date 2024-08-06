from project.robots.base_robot import BaseRobot


class FemaleRobot(BaseRobot):
    ROBOT_WEIGHT = 7
    WEIGHT_INCREASE = 1

    def __init__(self, name: str, kind: str, price: float):
        super().__init__(name, kind, price, weight=self.ROBOT_WEIGHT)

    @property
    def increase_kgs(self) -> int:
        return self.WEIGHT_INCREASE