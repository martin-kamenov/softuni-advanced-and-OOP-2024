from unittest import TestCase, main
from project.vehicle import Vehicle


class TestVehicle(TestCase):

    def setUp(self):
        self.vehicle = Vehicle(50.0, 250.0)

    def test_correct_init(self):
        self.assertEqual(50.0, self.vehicle.fuel)
        self.assertEqual(50.0, self.vehicle.capacity)
        self.assertEqual(250.0, self.vehicle.horse_power)
        self.assertEqual(1.25, self.vehicle.fuel_consumption)

    def test_drive_when_fuel_is_not_enough_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(1000)

        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_have_enough_fuel_and_reduce_with_the_consumed_fuel(self):
        self.vehicle.fuel = 100
        self.vehicle.drive(40)

        self.assertEqual(50, self.vehicle.fuel)

    def test_refuel_when_refueled_fuel_over_capacity_raise_error(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(100)

        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_with_enough_fuel_not_over_capacity(self):
        self.vehicle.capacity = 100
        self.vehicle.fuel = 50
        expected_fuel = self.vehicle.fuel + 20

        self.vehicle.refuel(20)

        self.assertEqual(expected_fuel, self.vehicle.fuel)

    def test_str_returns_correct_info_with_values(self):
        expected_result = f"The vehicle has 250.0 horse power with 50.0 fuel left and 1.25 fuel consumption"

        self.assertEqual(expected_result, self.vehicle.__str__())


if __name__ == '__main__':
    main()