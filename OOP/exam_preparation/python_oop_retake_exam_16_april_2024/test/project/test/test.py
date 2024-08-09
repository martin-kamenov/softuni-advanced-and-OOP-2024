from unittest import TestCase, main
from project.restaurant import Restaurant


class RestaurantTests(TestCase):

    def setUp(self):
        self.restaurant = Restaurant('Name', 50)

    def test_correct_init(self):
        self.assertEqual(self.restaurant.name, 'Name')
        self.assertEqual(self.restaurant.capacity, 50)
        self.assertEqual(self.restaurant.waiters, [])

    def test_incorrect_name_with_empty_value_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.restaurant.name = ''

        self.assertEqual(str(ve.exception), "Invalid name!")

    def test_capacity_under_zero_raise_exception(self):
        with self.assertRaises(ValueError) as ve:
            self.restaurant.capacity = -1

        self.assertEqual(str(ve.exception), "Invalid capacity!")

    def test_get_waiters_expect_empty(self):
        expect = []
        self.assertEqual(self.restaurant.get_waiters(), expect)

    def test_get_waiters_expect_waiter(self):
        self.restaurant.add_waiter('Gosho')
        expected = [{'name': 'Gosho'}]

        self.assertEqual(self.restaurant.get_waiters(), expected)

    def test_get_waiters_expect_waiters_with_min_earnings(self):
        self.restaurant.add_waiter('Gosho')
        self.restaurant.add_waiter('Kolio')

        self.restaurant.waiters[0]['total_earnings'] = 2
        self.restaurant.waiters[1]['total_earnings'] = 7

        expected = [{'name': 'Kolio', 'total_earnings': 7}]

        self.assertEqual(self.restaurant.get_waiters(min_earnings=3), expected)

    def test_get_waiters_expect_waiters_with_max_earnings(self):
        self.restaurant.add_waiter('Gosho')
        self.restaurant.add_waiter('Kolio')

        self.restaurant.waiters[0]['total_earnings'] = 2
        self.restaurant.waiters[1]['total_earnings'] = 7

        expected = [{'name': 'Gosho', 'total_earnings': 2}]

        self.assertEqual(self.restaurant.get_waiters(max_earnings=4), expected)

    def test_get_waiters_expect_waiter_wit_min_max_earnings(self):
        self.restaurant.add_waiter('Gosho')
        self.restaurant.add_waiter('Kolio')
        self.restaurant.add_waiter('Pacho')

        self.restaurant.waiters[0]['total_earnings'] = 2
        self.restaurant.waiters[1]['total_earnings'] = 4
        self.restaurant.waiters[2]['total_earnings'] = 7

        expected = [{'name': 'Kolio', 'total_earnings': 4}]

        self.assertEqual(
            self.restaurant.get_waiters(min_earnings=3, max_earnings=6),
            expected
        )

    def test_add_waiter_when_no_capacity_with_no_success(self):
        self.restaurant.capacity = 0

        self.assertEqual(
            self.restaurant.add_waiter('Pesho'),
            'No more places!'
        )

    def test_add_waiter_when_waiter_already_exists_in_restaurant(self):
        self.restaurant.add_waiter('Pesho')

        expected_result = self.restaurant.add_waiter('Pesho')

        self.assertEqual(expected_result, "The waiter Pesho already exists!")

    def test_add_waiter_to_waiters_expect_success(self):
        self.assertEqual(
            self.restaurant.add_waiter('Gosho'),
            "The waiter Gosho has been added."
        )

    def test_remove_waiter_expect_success(self):
        self.restaurant.add_waiter('Gosho')

        self.assertEqual(
            self.restaurant.remove_waiter('Gosho'),
            "The waiter Gosho has been removed."
        )

    def test_remove_waiter_with_no_success(self):
        self.assertEqual(
            self.restaurant.remove_waiter('Gosho'),
            "No waiter found with the name Gosho."
        )

    def test_get_total_earnings_expect_no_waiter(self):
        self.assertEqual(
            self.restaurant.get_total_earnings(),
            0
        )

    def test_get_total_earning_for_one_waiter(self):
        self.restaurant.add_waiter('Gosho')
        self.restaurant.waiters[0]['total_earnings'] = 20

        self.assertEqual(
            self.restaurant.get_total_earnings(),
            20
        )

    def test_get_total_earnings_for_two_waiters(self):
        self.restaurant.add_waiter('Gosho')
        self.restaurant.add_waiter('Kolio')

        self.restaurant.waiters[0]['total_earnings'] = 10
        self.restaurant.waiters[1]['total_earnings'] = 20

        self.assertEqual(
            self.restaurant.get_total_earnings(),
            30
        )

if __name__ == '__main__':
    main()