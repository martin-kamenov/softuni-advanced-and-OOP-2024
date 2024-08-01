from project.services.base_service import BaseService


class SecondaryService(BaseService):

    CAPACITY = 15

    def __init__(self, name: str):
        super().__init__(name, SecondaryService.CAPACITY)

    @property
    def type_of_service(self) -> str:
        return 'Secondary'