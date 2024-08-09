from unittest import TestCase, main
from project.robot import Robot


class RobotTests(TestCase):
    ROBOT_ALLOWED_CATEGORIES = ['Military', 'Education', 'Entertainment', 'Humanoids']

    def setUp(self):
        self.robot = Robot('Test', 'Military', 20, 100)

    def test_correct_init(self):
        self.assertEqual(self.robot.robot_id,'Test')
        self.assertEqual(self.robot.category, 'Military')
        self.assertEqual(self.robot.available_capacity, 20)
        self.assertEqual(self.robot.price, 100)
        self.assertEqual(self.robot.hardware_upgrades, [])
        self.assertEqual(self.robot.software_updates, [])

    def test_category_is_not_from_allowed_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.category = 'Kitchen'

        self.assertEqual(
            str(ve.exception),
            f"Category should be one of '{self.ROBOT_ALLOWED_CATEGORIES}'",
        )
        
    def test_price_is_not_positive_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.price = -1

        self.assertEqual(str(ve.exception), "Price cannot be negative!")

    def test_robot_not_upgraded_as_already_have_the_hardware(self):
        self.robot.hardware_upgrades = ['RAM']
        result = self.robot.upgrade('RAM', 50)

        self.assertEqual(result, f"Robot {self.robot.robot_id} was not upgraded.")
        self.assertEqual(self.robot.hardware_upgrades,['RAM'])

    def test_robot_upgrade_expect_success_increase_price_append_hardware_to_hardware_list(self):
        result = self.robot.upgrade('RAM', 50)

        self.assertEqual(self.robot.hardware_upgrades, ['RAM'])
        self.assertEqual(
            result,
            f'Robot {self.robot.robot_id} was upgraded with RAM.'
        )

    def test_robot_upgrade_expect_success_increase_price(self):
        expected_price = self.robot.price + (self.robot.PRICE_INCREMENT * 50)

        self.robot.upgrade('RAM', 50)
        self.assertEqual(self.robot.price, expected_price)

    def test_robot_update_non_existing_version_and_enough_capacity_should_update_successfully(self):
        result = self.robot.update(1.1, 20)

        self.assertEqual(self.robot.software_updates, [1.1])
        self.assertEqual(self.robot.available_capacity, 0)
        self.assertEqual(
            f'Robot {self.robot.robot_id} was updated to version 1.1.',
            result
        )

    def test_robot_update_with_existing_version_and_enough_capacity_should_not_update(self):
        self.robot.software_updates = [1.5]
        result = self.robot.update(1.5, 10)

        self.assertEqual(f"Robot {self.robot.robot_id} was not updated.", result)
        self.assertEqual(self.robot.software_updates, [1.5])
        self.assertEqual(self.robot.available_capacity, 20)

    def test_robot_update_with_version_and_enough_capacity_should_not_update(self):
        self.robot.software_updates = [1.5]
        result = self.robot.update(1.3, 5)

        self.assertEqual(f"Robot {self.robot.robot_id} was not updated.", result)
        self.assertEqual(self.robot.software_updates, [1.5])
        self.assertEqual(self.robot.available_capacity, 20)

    def test_gt_should_return_first_robot_is_more_expensive(self):
        self.robot_2 = Robot('Test_2', 'Education', 15, 50)

        result = self.robot > self.robot_2

        self.assertEqual(
            result,
            f'Robot with ID {self.robot.robot_id} is more expensive than '
            f'Robot with ID {self.robot_2.robot_id}.'
        )

    def test_gt_should_return_other_robot_is_more_expensive(self):
        self.robot_2 = Robot('Test_2', 'Education', 15, 150)

        result  = self.robot > self.robot_2

        self.assertEqual(
            result,
            f'Robot with ID {self.robot.robot_id} is cheaper than '
            f'Robot with ID {self.robot_2.robot_id}.'
        )

    def test_gt_should_return_robots_are_equal(self):
        self.robot_2 = Robot('Test_2', 'Education', 15, 100)

        result = self.robot > self.robot_2

        self.assertEqual(
            result,
            f'Robot with ID {self.robot.robot_id} costs equal to '
            f'Robot with ID {self.robot_2.robot_id}.'
        )

if __name__ == '__main__':
    main()