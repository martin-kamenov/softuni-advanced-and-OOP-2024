from typing import List
from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.id_mixin import IDMixin
from project.subscription import Subscription
from project.trainer import Trainer


class Gym(IDMixin):

    def __init__(self):
        self.customers: List[Customer] = []
        self.trainers: List[Trainer] = []
        self.equipment: List[Equipment] = []
        self.plans: List[ExercisePlan] = []
        self.subscriptions: List[Subscription] = []

    def add_customer(self, customer: Customer):
        return self.__add_method(customer, self.customers)

    def add_trainer(self, trainer: Trainer):
        return self.__add_method(trainer, self.trainers)

    def add_equipment(self, equipment: Equipment):
        return self.__add_method(equipment, self.equipment)

    def add_plan(self, plan: ExercisePlan):
        return self.__add_method(plan, self.plans)

    def add_subscription(self, subscription: Subscription):
        return self.__add_method(subscription, self.subscriptions)

    def subscription_info(self, subscription_id: int) -> str:
        # subscription = next(filter(lambda x: x.id == subscription_id, self.subscriptions), None)
        subscription = next((s for s in self.subscriptions if s.id == subscription_id), None)
        customer = next((c for c in self.customers if c.id == subscription.customer_id), None)
        trainer = next((t for t in self.trainers if t.id == subscription.trainer_id), None)
        plan = next((p for p in self.plans if p.id == subscription.exercise_id), None)
        equipment = next((e for e in self.equipment if e.id == plan.equipment_id), None)

        # return f'{str(subscription)}\n{str(customer)}\n{str(trainer)}\n{str(equipment)}\n{str(plan)}\n'

        return '\n'.join([subscription.__repr__(),
                          customer.__repr__(),
                          trainer.__repr__(),
                          equipment.__repr__(),
                          plan.__repr__()
        ])

    @staticmethod
    def __add_method(object__: object, collection: List[object]) -> None:
        if object__ not in collection:
            collection.append(object__)

