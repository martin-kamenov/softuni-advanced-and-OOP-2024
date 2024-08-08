from unittest import TestCase, main
from given_codes.car_manager import Car


class CarTest(TestCase):
    def setUp(self):


        self.car = Car('Porsche', 'Carrera', 10, 50)

    def test_init_is_correct(self):
        self.assertEqual('Porsche', self.car.make)
        self.assertEqual('Carrera', self.car.model)
        self.assertEqual(10, self.car.fuel_consumption)
        self.assertEqual(50, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_make_if_value_is_empty_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ''

        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_model_when_empty_value_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ''

        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_fuel_consumption_when_value_is_zero_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_when_value_is_zero_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_amount_when_value_is_less_than_zero_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -1

        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_refuel_with_zero_value_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)

        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_if_add_fuel_and_controls_to_not_go_over_capacity(self):
        self.car.fuel_capacity = 50
        self.car.refuel(70)

        self.assertEqual(50, self.car.fuel_amount)

    def test_drive_car_without_enough_fuel_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(100)

        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_drive_car_with_fuel_decreases_fuel(self):
        self.car.refuel(300)
        self.car.drive(10)
        self.assertEqual(49, self.car.fuel_amount)

if __name__ == '__main__':
    main()