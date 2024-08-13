from unittest import TestCase, main
from project.soccer_player import SoccerPlayer


class SoccerPlayerTests(TestCase):

    def setUp(self):
        self.player1 = SoccerPlayer("Tester1", 20, 3, "Barcelona")
        self.player2 = SoccerPlayer('Tester2', 21, 10, "Juventus")

    def test_correct_init(self):
        self.assertEqual(self.player1.name, 'Tester1')
        self.assertEqual(self.player1.age, 20)
        self.assertEqual(self.player1.goals, 3)
        self.assertEqual(self.player1.team, 'Barcelona')
        self.assertEqual(self.player1.achievements, {})

    def test_name_with_less_symbols_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.player1.name = 'Test'

        self.assertEqual(str(ve.exception), "Name should be more than 5 symbols!")

    def test_age_under_allowed_age_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.player1.age = 15

        self.assertEqual(str(ve.exception), "Players must be at least 16 years of age!")

    def test_goals_when_under_zero_returns_to_zero(self):
        self.player1.goals = -5

        self.assertEqual(self.player1.goals, 0)

    def test_team_when_is_not_from_allowed_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.player1.team = 'Test'

        self.assertEqual(
            str(ve.exception),
            f"Team must be one of the following: {', '.join(SoccerPlayer._VALID_TEAMS)}!"
        )

    def test_change_team_with_not_valid_team_expect_no_success(self):
        result = self.player1.change_team('CSKA')

        self.assertEqual(result, "Invalid team name!")
        self.assertEqual(self.player1.team, 'Barcelona')

    def test_change_team_with_valid_team_expect_success(self):
        result = self.player1.change_team('Juventus')

        self.assertEqual(result, "Team successfully changed!")
        self.assertEqual(self.player1.team, 'Juventus')

    def test_add_new_achievements_to_player(self):
        result = self.player1.add_new_achievement('Test')

        self.assertEqual(result, f"Test has been successfully added to the achievements collection!")
        self.assertEqual(self.player1.achievements['Test'], 1)

        result = self.player1.add_new_achievement('Test')

        self.assertEqual(result, f"Test has been successfully added to the achievements collection!")
        self.assertEqual(self.player1.achievements['Test'], 2)

    def test__lt_second_player_is_better_than_first_player(self):
        result = self.player1 < self.player2

        self.assertEqual(
            result,
            f"{self.player2.name} is a top goal scorer! S/he scored more than {self.player1.name}."
        )

    def test__lt_first_player_is_better_than_second_player(self):
        self.player1.goals = 15

        result = self.player1 < self.player2

        self.assertEqual(
            result,
            f"{self.player1.name} is a better goal scorer than {self.player2.name}."
        )

if __name__ == "__main__":
    main()