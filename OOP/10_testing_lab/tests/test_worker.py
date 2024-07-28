from unittest import TestCase, main
# from given_codes.worker import Worker

class WorkerTests(TestCase):

    def setUp(self):
        self.worker = Worker('Ivan', 1000, 50)

    def test_correct_init(self):
        self.assertEqual('Ivan', self.worker.name)
        self.assertEqual(1000, self.worker.salary)
        self.assertEqual(50, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_work_when_worker_has_enough_energy_expect_money_increase_and_energy_decrease(self):
        expected_money = self.worker.salary * 2
        expected_energy = self.worker.energy - 2

        self.worker.work()
        self.worker.work()

        self.assertEqual(expected_money, self.worker.money)
        self.assertEqual(expected_energy, self.worker.energy)

    def test_work_when_energy_is_zero_raise_exception(self):
        self.worker.energy = 0

        with self.assertRaises(Exception) as ex:
            self.worker.work()

        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_work_when_energy_is_negative_value_raise_exception(self):
        self.worker.energy = -1

        with self.assertRaises(Exception) as ex:
            self.worker.work()

        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_rest_increases_rest_with_one(self):
        expected_energy = self.worker.energy + 1

        self.worker.rest()

        self.assertEqual(expected_energy, self.worker.energy)

    def test_get_info_returns_correct_string(self):
        self.assertEqual('Ivan has saved 0 money.', self.worker.get_info())


if __name__ == "__main__":
    main()