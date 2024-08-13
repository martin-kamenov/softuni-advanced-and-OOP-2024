from project.stores.base_store import BaseStore


class FurnitureStore(BaseStore):
    INITIAL_CAPACITY = 50

    def __init__(self, name: str, location: str):
        super().__init__(name, location, capacity=self.INITIAL_CAPACITY)

    @property
    def store_type(self) -> str:
        return 'FurnitureStore'

    #TODO logic might be incorrect
    def store_stats(self) -> str:
        sorted_furniture = sorted(self.products, key=lambda x: x.model)
        furniture_dict = {}

        for curr_furniture in sorted_furniture:
            if curr_furniture.model not in furniture_dict:
                furniture_dict[curr_furniture.model] = []
            furniture_dict[curr_furniture.model].append(curr_furniture.price)

        result = [
            f"Store: {self.name}, location: {self.location}, available capacity: {self.capacity}",
            self.get_estimated_profit(),
            "**Furniture for sale:"
        ]

        for fur_model, prices in furniture_dict.items():
            average_price_per_model = sum(prices) / len(prices)

            result.append(f"{fur_model}: {len(prices)}pcs, average price: {average_price_per_model:.2f}")

        return '\n'.join(result)