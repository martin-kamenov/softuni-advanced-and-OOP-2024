from project.services.base_service import BaseService


class MainService(BaseService):
    SERVICE_CAPACITY = 30


    def __init__(self, name: str):
        super().__init__(name, capacity=self.SERVICE_CAPACITY)

    @property
    def service_type(self) -> str:
        return 'Main'