from unittest import TestCase, main
from given_codes.extended_list import IntegerList

class IntegerListTests(TestCase):

    def setUp(self):
        self.integer_list = IntegerList(1, 2, 3, 4.5, 'five')

    def test_correct_init_ignor_non_integer(self):
        self.assertEqual([1, 2, 3], self.integer_list.get_data())

    def test_add_non_integer_value_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.integer_list.add(4.5)

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_add_integer_adds_integer_to_the_list(self):
        expected_list = self.integer_list.get_data() + [4]

        self.integer_list.add(4)

        self.assertEqual(expected_list, self.integer_list.get_data())

    def test_remove_index_with_out_of_range_raises_error(self):
        with self.assertRaises(IndexError) as ie:
            self.integer_list.remove_index(20)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_remove_index_with_valid_index(self):
        self.integer_list.remove_index(1)

        self.assertEqual([1, 3], self.integer_list.get_data())

    def test_get_index_with_index_out_of_range_raises_value_error(self):
        with self.assertRaises(IndexError) as ie:
            self.integer_list.get(50)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_get_index_with_valid_index(self):
        desired_index = self.integer_list.get(1)

        self.assertEqual(2, desired_index)

    def test_insert_with_index_out_of_range_raises_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.integer_list.insert(20, 3)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_insert_with_valid_index_with_non_integer_value_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.integer_list.insert(1, 5.5)

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_insert_integer_value_on_valid_index(self):
        expected_list = self.integer_list.get_data().copy()

        expected_list.insert(1, 5)
        self.integer_list.insert(1, 5)

        self.assertEqual(expected_list, self.integer_list.get_data())

    def test_get_biggest_number(self):
        result = self.integer_list.get_biggest()

        self.assertEqual(3, result)

    def test_get_index_on_valid_index(self):
        result = self.integer_list.get_index(2)

        self.assertEqual(1, result)

if __name__ == '__main__':
    main()
