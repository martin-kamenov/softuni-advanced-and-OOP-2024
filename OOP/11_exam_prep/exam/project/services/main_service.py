from project.services.base_service import BaseService


class MainService(BaseService):
    CAPACITY = 30

    def __init__(self, name: str):
        super().__init__(name, MainService.CAPACITY)

    @property
    def type_of_service(self) -> str:
        return 'Main'