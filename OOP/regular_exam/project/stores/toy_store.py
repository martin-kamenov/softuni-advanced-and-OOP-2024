from project.stores.base_store import BaseStore


class ToyStore(BaseStore):
    INITIAL_CAPACITY = 100

    def __init__(self, name: str, location: str):
        super().__init__(name, location, capacity=self.INITIAL_CAPACITY)

    @property
    def store_type(self) -> str:
        return "ToyStore"

    #TODO logic might be incorrect
    def store_stats(self) -> str:
        sorted_toys = sorted(self.products, key=lambda x: x.model)
        toys_dict = {}

        for curr_toy in sorted_toys:
            if curr_toy.model not in toys_dict:
                toys_dict[curr_toy.model] = []
            toys_dict[curr_toy.model].append(curr_toy.price)

        result = [
            f"Store: {self.name}, location: {self.location}, available capacity: {self.capacity}",
            self.get_estimated_profit(),
            "**Toys for sale:"
        ]

        for toy_model, prices in toys_dict.items():
            average_price_per_model = sum(prices) / len(prices)

            result.append(f"{toy_model}: {len(prices)}pcs, average price: {average_price_per_model:.2f}")

        return '\n'.join(result)