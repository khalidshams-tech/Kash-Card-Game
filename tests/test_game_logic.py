import unittest

from game_logic import check_loser, compute_round, determine_required, rotate_dealer


class KashGameLogicTests(unittest.TestCase):
    def test_determine_required_rotates_roles(self):
        players = ["Amina", "Ben", "Chris"]

        required = determine_required(players, 0)

        self.assertEqual(required, {"Amina": 3, "Ben": 8, "Chris": 5})

    def test_compute_round_adds_missing_tricks_to_scores(self):
        players = ["Amina", "Ben", "Chris"]
        scores = {player: 0 for player in players}
        required = {"Amina": 3, "Ben": 8, "Chris": 5}
        actual = {"Amina": 2, "Ben": 9, "Chris": 4}

        updated_scores, missing, pending_swaps = compute_round(scores, players, required, actual)

        self.assertEqual(updated_scores, {"Amina": 1, "Ben": 0, "Chris": 1})
        self.assertEqual(missing, {"Amina": 1, "Ben": 0, "Chris": 1})
        self.assertEqual(pending_swaps, {"Amina": {"Ben": 1}})

    def test_check_loser_returns_first_player_at_limit(self):
        self.assertEqual(check_loser({"Amina": 20, "Ben": 21}), "Ben")

    def test_rotate_dealer_wraps_after_third_player(self):
        self.assertEqual(rotate_dealer(0), 1)
        self.assertEqual(rotate_dealer(2), 0)


if __name__ == "__main__":
    unittest.main()
