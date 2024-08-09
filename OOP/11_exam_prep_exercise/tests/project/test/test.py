from project.tennis_player import TennisPlayer
from unittest import TestCase, main

class TennisPlayersTests(TestCase):

    def setUp(self):
        self.tennis_player = TennisPlayer('Test', 20, 200)
        self.tennis_player_2 = TennisPlayer('Test2', 25, 150)

    def test_correct_init(self):
        self.assertEqual('Test', self.tennis_player.name)
        self.assertEqual(20, self.tennis_player.age)
        self.assertEqual(200, self.tennis_player.points)
        self.assertEqual([], self.tennis_player.wins)

    def test_name_if_two_chars_or_less_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.tennis_player.name = 'Te'

        self.assertEqual("Name should be more than 2 symbols!", str(ve.exception))

    def test_age_when_under_eighteen_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.tennis_player.age = 10

        self.assertEqual("Players must be at least 18 years of age!", str(ve.exception))

    def test_add_new_win_append_tournament_to_win_list_expect_success(self):
        self.tennis_player.add_new_win('Tournament')

        self.assertEqual(['Tournament'], self.tennis_player.wins)

    def test_add_the_same_win_to_wins_list_with_no_success(self):
        self.tennis_player.add_new_win('Tournament')
        result = self.tennis_player.add_new_win('Tournament')

        self.assertEqual("Tournament has been already added to the list of wins!", result)
        self.assertEqual(['Tournament'], self.tennis_player.wins)

    def test_lt_should_return_first_player_is_better(self):
        result = self.tennis_player < self.tennis_player_2

        self.assertEqual(
            f'{self.tennis_player.name} is a better player than {self.tennis_player_2.name}',
            result
         )

    def test_lt_returns_other_player_is_better(self):
        self.tennis_player_2.points = 300
        result = self.tennis_player < self.tennis_player_2

        self.assertEqual(
            f'{self.tennis_player_2.name} is a top seeded player and he/she is better than {self.tennis_player.name}',
            result
        )

    def test_correct_str_without_wins(self):
        result = f"Tennis Player: {self.tennis_player.name}\n" \
               f"Age: {self.tennis_player.age}\n" \
               f"Points: {self.tennis_player.points:.1f}\n" \
               f"Tournaments won: "

        self.assertEqual(result, self.tennis_player.__str__())

    def test_correct_str_with_win(self):
        self.tennis_player.add_new_win('Tournament')

        result = f"Tennis Player: {self.tennis_player.name}\n" \
               f"Age: {self.tennis_player.age}\n" \
               f"Points: {self.tennis_player.points:.1f}\n" \
               f"Tournaments won: Tournament"

        self.assertEqual(result, self.tennis_player.__str__())

    def test_correct_str_with_two_wins(self):
        self.tennis_player.add_new_win('Tournament')
        self.tennis_player.add_new_win('Tournament2')


        result = f"Tennis Player: {self.tennis_player.name}\n" \
               f"Age: {self.tennis_player.age}\n" \
               f"Points: {self.tennis_player.points:.1f}\n" \
               f"Tournaments won: Tournament, Tournament2"

        self.assertEqual(result, self.tennis_player.__str__())

if __name__ == '__main__':
    main()