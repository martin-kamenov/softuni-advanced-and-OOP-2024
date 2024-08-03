from project.fish.base_fish import BaseFish

class DeepSeaFish(BaseFish):
    TIME_TO_CATCH = 180

    def __init__(self, name: str, points: float):
        super().__init__(name, points, time_to_catch=DeepSeaFish.TIME_TO_CATCH)

    @property
    def time_to_catch_fish(self) -> int:
        return DeepSeaFish.TIME_TO_CATCH