from unittest import TestCase

import autopy

from board import get_position, NotVisible
from screen import get_current_grid
from tactics import get_scoring_moves, get_swapped_position, get_grid_after_move


class BoardDetectionTest(TestCase):
    def test_basic_detection(self):
        bitmap = autopy.bitmap.Bitmap.open("sample_images/board1.png")
        x, y = get_position(bitmap) # throws board.NotVisible if no position

        # since the board positioning is imprecise, we just assert a range
        self.assertGreater(x, 268)
        self.assertLess(x, 272)

        self.assertGreater(y, 100)
        self.assertLess(y, 105)

    def test_darker_board_detection(self):
        bitmap = autopy.bitmap.Bitmap.open("sample_images/board_dark_background.png")
        get_position(bitmap) # throws board.NotVisible if no position

    def test_snow_board_detection(self):
        bitmap = autopy.bitmap.Bitmap.open("sample_images/board_snow.png")
        get_position(bitmap) # throws board.NotVisible if no position

    def test_part_board(self):
        """If we can only see part of the board, we shouldn't say we
        can detect it.

        """
        bitmap = autopy.bitmap.Bitmap.open("sample_images/board_part.png")
        self.assertRaises(NotVisible, get_position, bitmap)

    def test_side_board(self):
        """If we can only see one side of the board, we shouldn't say
        we can detect it.

        """
        bitmap = autopy.bitmap.Bitmap.open("sample_images/board_left_part.png")
        self.assertRaises(NotVisible, get_position, bitmap)


class JewelDetectionTest(TestCase):
    def test_purple(self):
        bitmap = autopy.bitmap.Bitmap.open("sample_images/board1.png")
        grid = get_current_grid(bitmap)
        self.assertEqual(grid[0][4], 'purple')

    def test_green(self):
        bitmap = autopy.bitmap.Bitmap.open("sample_images/board1.png")
        grid = get_current_grid(bitmap)
        self.assertEqual(grid[0][0], 'green')

    def test_blue(self):
        bitmap = autopy.bitmap.Bitmap.open("sample_images/board1.png")
        grid = get_current_grid(bitmap)
        self.assertEqual(grid[0][1], 'blue')

    def test_yellow(self):
        bitmap = autopy.bitmap.Bitmap.open("sample_images/board1.png")
        grid = get_current_grid(bitmap)
        self.assertEqual(grid[0][5], 'yellow')

    def test_orange(self):
        bitmap = autopy.bitmap.Bitmap.open("sample_images/board1.png")
        grid = get_current_grid(bitmap)
        self.assertEqual(grid[0][3], 'orange')

    def test_red(self):
        bitmap = autopy.bitmap.Bitmap.open("sample_images/board1.png")
        grid = get_current_grid(bitmap)
        self.assertEqual(grid[1][1], 'red')

    def test_white(self):
        bitmap = autopy.bitmap.Bitmap.open("sample_images/board1.png")
        grid = get_current_grid(bitmap)
        self.assertEqual(grid[1][4], 'white')


class CrossJewelDetectionTest(TestCase):
    def test_yellow_cross(self):
        bitmap = autopy.bitmap.Bitmap.open("sample_images/board_with_glowing_yellow.png")
        grid = get_current_grid(bitmap)
        # todo: check it's special
        self.assertEqual(grid[2][5], 'yellow')

    def test_green_cross(self):
        bitmap = autopy.bitmap.Bitmap.open("sample_images/board_with_green_cross.png")
        grid = get_current_grid(bitmap)
        # todo: check it's special
        self.assertEqual(grid[2][7], 'green')

    def test_purple_cross(self):
        bitmap = autopy.bitmap.Bitmap.open("sample_images/board_with_purple_cross.png")
        grid = get_current_grid(bitmap)
        # todo: check it's special
        self.assertEqual(grid[7][3], 'purple')

    def test_orange_cross(self):
        bitmap = autopy.bitmap.Bitmap.open("sample_images/board_with_orange_cross.png")
        grid = get_current_grid(bitmap)
        # todo: check it's special
        self.assertEqual(grid[3][2], 'orange')


class FireJewelDetectionTest(TestCase):
    def test_red_fire(self):
        bitmap = autopy.bitmap.Bitmap.open("sample_images/board_with_red_fire.png")
        grid = get_current_grid(bitmap)
        # todo: check it's special
        self.assertEqual(grid[6][3], 'red')

    def test_white_fire(self):
        bitmap = autopy.bitmap.Bitmap.open("sample_images/board_with_white_fire.png")
        grid = get_current_grid(bitmap)
        # todo: check it's special
        self.assertEqual(grid[3][6], 'white')

    def test_blue_fire(self):
        bitmap = autopy.bitmap.Bitmap.open("sample_images/board_with_blue_fire.png")
        grid = get_current_grid(bitmap)
        # todo: check it's special
        self.assertEqual(grid[0][3], 'blue')

    def test_purple_fire(self):
        bitmap = autopy.bitmap.Bitmap.open("sample_images/board_with_purple_fire.png")
        grid = get_current_grid(bitmap)
        # todo: check it's special
        self.assertEqual(grid[5][6], 'purple')

    def test_yellow_fire(self):
        bitmap = autopy.bitmap.Bitmap.open("sample_images/board_with_yellow_green_fire.png")
        grid = get_current_grid(bitmap)
        # todo: check it's special
        self.assertEqual(grid[3][6], 'yellow')

    def test_green_fire(self):
        bitmap = autopy.bitmap.Bitmap.open("sample_images/board_with_yellow_green_fire.png")
        grid = get_current_grid(bitmap)
        # todo: check it's special
        self.assertEqual(grid[4][6], 'green')


class WildcardJewelDetectionTest(TestCase):
    def test_wildcard(self):
        bitmap = autopy.bitmap.Bitmap.open("sample_images/board_with_wildcard.png")
        grid = get_current_grid(bitmap)
        self.assertEqual(grid[5][5], 'wildcard')

        # since the wildcard gem rotates, we have two images to test with
        bitmap = autopy.bitmap.Bitmap.open("sample_images/board_with_wildcard2.png")
        grid = get_current_grid(bitmap)
        self.assertEqual(grid[5][5], 'wildcard')


class MovesTest(TestCase):
    def test_valid_moves(self):
        bitmap = autopy.bitmap.Bitmap.open("sample_images/board2.png")
        grid = get_current_grid(bitmap)
        scoring_moves = get_scoring_moves(grid)

        expected_moves = [((6,2), (7,2)), ((6, 3), (7, 3))]

        # check we found all the expected moves
        for move in expected_moves:
            self.assertIn(move, scoring_moves)

        # check there are no other moves found
        self.assertEqual(len(scoring_moves), len(expected_moves))

    def test_move_outcome(self):
        bitmap = autopy.bitmap.Bitmap.open("sample_images/board2.png")
        grid = get_current_grid(bitmap)

        grid = get_swapped_position(grid, (6, 2), (7, 2))
        final_grid = get_grid_after_move(grid)

        expected_final_grid = [
            ['purple', 'green', 'green', 'yellow', 'white', 'blue', None, 'yellow'],
            ['white', 'blue', 'red', 'blue', 'purple', 'orange', None, 'white'],
            ['purple', 'purple', 'orange', 'yellow', 'white', 'blue', None, 'orange'],
            ['red', 'green', 'blue', 'purple', 'red', 'yellow', 'purple', 'blue'],
            ['blue', 'yellow', 'blue', 'yellow', 'orange', 'white', 'green', 'red'],
            ['orange', 'yellow', 'red', 'green', 'red', 'yellow', 'yellow', 'purple'],
            ['purple', 'green', 'white', 'blue', 'orange', 'orange', 'blue', 'purple'],
            ['blue', 'red', 'white', 'purple', 'yellow', 'orange', 'green', 'green']]

        self.assertEqual(expected_final_grid, final_grid)

