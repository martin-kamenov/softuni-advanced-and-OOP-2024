import unittest
from project.toy_store import ToyStore


class ToyStoreTest(unittest.TestCase):

    def setUp(self):
        self.toy_store = ToyStore()

    def test_correct_init(self):
        self.assertEqual(
            self.toy_store.toy_shelf,
            {
                "A": None,
                "B": None,
                "C": None,
                "D": None,
                "E": None,
                "F": None,
                "G": None,
            }
        )

    def test_add_toy_with_incorrect_shelf_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy('W', 'doll')

        self.assertEqual(
            str(ex.exception),
            "Shelf doesn't exist!"
        )

    def test_add_the_same_toy_on_the_same_shelf_raise_exception(self):
        self.toy_store.add_toy('A', 'doll')

        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy('A', 'doll')

        self.assertEqual(
            str(ex.exception),
            "Toy is already in shelf!"
        )

    def test_add_toy_on_already_taken_shelf_raise_exception(self):
        self.toy_store.add_toy('A', 'doll')

        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy('A', 'toy_car')

        self.assertEqual(
            str(ex.exception),
            "Shelf is already taken!"
        )

    def test_add_toy_adds_toy_expect_success(self):
        expected_result = self.toy_store.add_toy('A', 'doll')

        self.assertEqual(
            f"Toy:doll placed successfully!",
            expected_result
        )
        self.assertEqual(
            self.toy_store.toy_shelf,
            {
                "A": 'doll',
                "B": None,
                "C": None,
                "D": None,
                "E": None,
                "F": None,
                "G": None,
            }
        )

    def test_remove_toy_from_non_existing_shelf_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.toy_store.remove_toy('R', 'doll')

        self.assertEqual(
            str(ex.exception),
            "Shelf doesn't exist!"
        )

    def test_remove_toy_from_shelf_where_toy_is_not_on_that_shelf_raise_exception(self):
        self.toy_store.add_toy('A', 'doll')

        with self.assertRaises(Exception) as ex:
            self.toy_store.remove_toy('A', 'bear')

        self.assertEqual(
            str(ex.exception),
            "Toy in that shelf doesn't exists!"
        )

    def test_remove_toy_successfully_from_shelf(self):
        self.toy_store.add_toy('A', 'doll')
        result = self.toy_store.remove_toy('A', 'doll')

        self.assertEqual(
            result,
            f"Remove toy:doll successfully!"
        )
        self.assertEqual(
            self.toy_store.toy_shelf,
            {
                "A": None,
                "B": None,
                "C": None,
                "D": None,
                "E": None,
                "F": None,
                "G": None,
            }
        )

if __name__ == '__main__':
    unittest.main()