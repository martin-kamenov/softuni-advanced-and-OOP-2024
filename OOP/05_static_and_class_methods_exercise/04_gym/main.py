from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.gym import Gym
from project.subscription import Subscription
from project.trainer import Trainer

customer = Customer("John", "Maple Street", "john.smith@gmail.com")
equipment = Equipment("Treadmill")
trainer = Trainer("Peter")
subscription = Subscription("14.05.2020", 1, 1, 1)
plan = ExercisePlan(1, 1, 20)

customer2 = Customer("Pavel", "Sofia", "pavel.smith@gmail.com")
equipment2 = Equipment("Weights")
trainer2 = Trainer("John")
subscription2 = Subscription("10.05.2022", 2, 2, 2)
plan2 = ExercisePlan(2, 2, 40)

gym = Gym()

gym.add_customer(customer)
gym.add_equipment(equipment)
gym.add_trainer(trainer)
gym.add_plan(plan)
gym.add_subscription(subscription)

print(Customer.get_next_id())

print(gym.subscription_info(1))


gym.add_customer(customer2)
gym.add_equipment(equipment2)
gym.add_trainer(trainer2)
gym.add_plan(plan2)
gym.add_subscription(subscription2)

print(Customer.get_next_id())

print(gym.subscription_info(2))
