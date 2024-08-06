from project.services.base_service import BaseService


class SecondaryService(BaseService):
    SERVICE_CAPACITY = 15

    def __init__(self, name: str):
        super().__init__(name, capacity=self.SERVICE_CAPACITY)

    @property
    def service_type(self) -> str:
        return 'Secondary'