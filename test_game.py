import unittest
from unittest.mock import patch
import game


class TestGame(unittest.TestCase):
    def test_want_to_play_input(self):
        self.assertFalse(game.want_to_play_input("N"))
        self.assertFalse(game.want_to_play_input("No"))
        self.assertTrue(game.want_to_play_input("Y"))
        self.assertTrue(game.want_to_play_input("Yes"))
        self.assertIsNone(game.want_to_play_input("yes"))
        self.assertIsNone(game.want_to_play_input("c"))
        self.assertIsNone(game.want_to_play_input(""))

    def test_which_sign_input(self):
        self.assertEqual(game.which_sign_input("X"), "X")
        self.assertEqual(game.which_sign_input("x"), "X")
        self.assertEqual(game.which_sign_input("O"), "O")
        self.assertEqual(game.which_sign_input("o"), "O")
        self.assertIsNone(game.which_sign_input("XO"))
        self.assertIsNone(game.which_sign_input("1"))
        self.assertIsNone(game.which_sign_input("pod"))
        self.assertIsNone(game.which_sign_input(""))

    def test_other_player(self):
        self.assertEqual(game.other_player("X"), "O")
        self.assertEqual(game.other_player("O"), "X")

    def test_check_board(self):
        board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        self.assertTrue(game.check_board(1, board))
        self.assertTrue(game.check_board(4, board))
        self.assertTrue(game.check_board(9, board))
        board = ["X", " ", " ", "O", " ", " ", " ", "X", " "]
        self.assertTrue(game.check_board(2, board))
        self.assertFalse(game.check_board(4, board))
        self.assertFalse(game.check_board(8, board))
        self.assertTrue(game.check_board(3, board))

    def test_update_board(self):
        board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        self.assertEqual(game.update_board(1, "X", board, 1), ["X", " ", " ", " ", " ", " ", " ", " ", " "])
        board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        self.assertEqual(game.update_board(2, "X", board, 9), [" ", " ", " ", " ", " ", " ", " ", " ", "O"])
        board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        self.assertEqual(game.update_board(5, "O", board, 3), [" ", " ", "O", " ", " ", " ", " ", " ", " "])
        board = ["X", "O", "X", "O", " ", " ", " ", "X", " "]
        self.assertEqual(game.update_board(6, "X", board, 7), ["X", "O", "X", "O", " ", " ", "O", "X", " "])

    def test_check_for_game_over(self):
        board = ["X", "O", "X", "O", "X", "O", "O", "X", "O"]
        self.assertEqual(game.check_for_game_over(board), (True, None))
        board = ["X", "O", "X", "O", "X", "O", "O", "X", " "]
        self.assertEqual(game.check_for_game_over(board), (False, None))
        board = ["X", "X", "X", "O", " ", "O", "O", "X", " "]
        self.assertEqual(game.check_for_game_over(board), (True, "X"))
        board = ["X", " ", "X", "X", " ", "O", "O", "O", " "]
        self.assertEqual(game.check_for_game_over(board), (False, None))
        board = ["X", " ", "X", " ", "X", " ", "O", "O", "O"]
        self.assertEqual(game.check_for_game_over(board), (True, "O"))

    @patch("builtins.input", side_effect=["Yes", "Y", "No", "N"])
    def test_want_to_play(self, mock_input):
        self.assertTrue(game.want_to_play())
        self.assertTrue(game.want_to_play())
        self.assertFalse(game.want_to_play())
        self.assertFalse(game.want_to_play())

    @patch("builtins.input", side_effect=["X", "x", "O", "o"])
    def test_which_sign(self, mock_input):
        self.assertEqual(game.which_sign(),"X")
        self.assertEqual(game.which_sign(), "X")
        self.assertEqual(game.which_sign(), "O")
        self.assertEqual(game.which_sign(), "O")

    @patch("builtins.input", side_effect=["1", "4", "9"])
    def test_put_sign_where(self, mock_input):
        self.assertEqual(game.put_sign_where(),1)
        self.assertEqual(game.put_sign_where(), 4)
        self.assertEqual(game.put_sign_where(), 9)


if __name__ == "__main__":
    unittest.main()
