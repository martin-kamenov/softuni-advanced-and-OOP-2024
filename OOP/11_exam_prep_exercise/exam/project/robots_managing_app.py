from typing import List
from project.robots.base_robot import BaseRobot
from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.base_service import BaseService
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:

    ROBOT_TYPES = {
        'MaleRobot': MaleRobot,
        'FemaleRobot': FemaleRobot
    }

    SERVICE_TYPES = {
        'MainService': MainService,
        'SecondaryService': SecondaryService
    }

    def __init__(self):
        self.robots: List[BaseRobot] = []
        self.services: List[BaseService] = []

    def add_service(self, service_type: str, name: str) -> str:
        if service_type not in self.SERVICE_TYPES:
            raise Exception("Invalid service type!")

        service = self.SERVICE_TYPES[service_type](name)
        self.services.append(service)

        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float) -> str:
        if robot_type not in self.ROBOT_TYPES:
            raise Exception("Invalid robot type!")

        robot = self.ROBOT_TYPES[robot_type](name, kind, price)
        self.robots.append(robot)

        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str) -> str:
        robot = self._find_object(robot_name, self.robots)
        service = self._find_object(service_name, self.services)

        if isinstance(robot, MaleRobot) and not isinstance(service, MainService):
            return "Unsuitable service."

        if isinstance(robot, FemaleRobot) and not isinstance(service, SecondaryService):
            return "Unsuitable service."

        if service.capacity <= len(service.robots):
            raise Exception("Not enough capacity for this robot!")

        self.robots.remove(robot)
        service.robots.append(robot)

        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str) -> str:
        service = self._find_object(service_name, self.services)
        robot = self._find_object(robot_name, service.robots)

        if not robot:
            raise Exception("No such robot in this service!")

        service.robots.remove(robot)
        self.robots.append(robot)

        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str) -> str:
        service = self._find_object(service_name, self.services)

        fed_robots = [robot.eating() for robot in service.robots]

        return f"Robots fed: {len(fed_robots)}."

    def service_price(self, service_name: str) -> str:
        service = self._find_object(service_name, self.services)

        total_price = sum(r.price for r in service.robots)

        return f"The value of service {service_name} is {total_price:.2f}."

    def __str__(self):
        return '\n'.join(service.details() for service in self.services)

    @staticmethod
    def _find_object(object_name, collection):
        return next(filter(lambda o: o.name == object_name, collection))