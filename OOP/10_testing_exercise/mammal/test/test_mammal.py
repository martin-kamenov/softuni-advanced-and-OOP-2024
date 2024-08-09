from unittest import TestCase, main
from project.mammal import Mammal


class MammalTests(TestCase):

    def setUp(self):
        self.mammal = Mammal('Gosho', 'duck', 'kwak')

    def test_correct_init(self):
        self.assertEqual('Gosho', self.mammal.name)
        self.assertEqual('duck', self.mammal.type)
        self.assertEqual('kwak', self.mammal.sound)
        self.assertEqual('animals', self.mammal._Mammal__kingdom)

    def test_make_sound_returns_correct_string(self):
        self.assertEqual("Gosho makes kwak", self.mammal.make_sound())

    def test_get_kingdom_returns_correct_kingdom(self):
        self.assertEqual('animals', self.mammal.get_kingdom())

    def test_info_returns_correct_string(self):
        self.assertEqual("Gosho is of type duck", self.mammal.info())


if __name__ == '__main__':
    main()