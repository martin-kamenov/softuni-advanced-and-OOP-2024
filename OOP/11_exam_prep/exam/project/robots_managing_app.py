from typing import List
from project.robots.base_robot import BaseRobot
from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.base_service import BaseService
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:

    TYPE_OF_ROBOTS = {'FemaleRobot': FemaleRobot, 'MaleRobot': MaleRobot}
    TYPE_OF_SERVICES = {'MainService': MainService, 'SecondaryService': SecondaryService}

    def __init__(self):
        self.robots: List[BaseRobot] = []
        self.services: List[BaseService] = []

    def add_service(self, service_type: str, name: str) -> str:
        if service_type not in RobotsManagingApp.TYPE_OF_SERVICES:
            raise Exception("Invalid service type!")

        service = RobotsManagingApp.TYPE_OF_SERVICES[service_type](name)
        self.services.append(service)

        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float) -> str:
        try:
            robot = RobotsManagingApp.TYPE_OF_ROBOTS[robot_type](name, kind, price)
        except Exception:
            raise "Invalid robot type!"

        self.robots.append(robot)

        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str) -> str:
        robot = self._get_object(robot_name, self.robots)
        service = self._get_object(service_name, self.services)

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
        service = self._get_object(service_name, self.services)
        robot = self._get_object(robot_name, service.robots)

        if robot not in service.robots:
            raise Exception("No such robot in this service!")

        service.robots.remove(robot)
        self.robots.append(robot)

        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str) -> str:
        service = self._get_object(service_name, self.services)

        for robot in service.robots:
            robot.eating()

        return f"Robots fed: {len(service.robots)}."

    def service_price(self, service_name: str) -> str:
        service = self._get_object(service_name, self.services)
        total_price = sum(r.price for r in service.robots)

        return f"The value of service {service_name} is {total_price:.2f}."

    @staticmethod
    def _get_object(object_name: str, collection: List):
        result = next(filter(lambda x: x.name == object_name, collection), None)
        return result

    def __str__(self):
        return '\n'.join(s.details() for s in self.services)
