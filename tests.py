from unittest import TestCase

import autopy

from board import get_position, NotVisible
from screen import get_current_grid
from tactics import get_scoring_moves, get_grid_after_move, count_scoring_lines


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

    def test_black_screen(self):
        """Just because we look for a black line, does not mean a
        screen with a lot of black should be detected as a board.

        """
        bitmap = autopy.bitmap.Bitmap.open("sample_images/terminal.png")
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

    def test_red_cross(self):
        bitmap = autopy.bitmap.Bitmap.open("sample_images/board_with_red_cross.png")
        grid = get_current_grid(bitmap)
        # todo: check it's special
        self.assertEqual(grid[6][6], 'red')

    def test_blue_cross(self):
        bitmap = autopy.bitmap.Bitmap.open("sample_images/board_with_blue_cross.png")
        grid = get_current_grid(bitmap)
        # todo: check it's special
        self.assertEqual(grid[6][3], 'blue')


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
        scoring_moves = list(get_scoring_moves(grid))

        expected_moves = [((6,2), (7,2)), ((6, 3), (7, 3))]

        # check we found all the expected moves
        for move in expected_moves:
            self.assertIn(move, scoring_moves)

        # check there are no other moves found
        self.assertEqual(len(scoring_moves), len(expected_moves))

    def test_move_outcome(self):
        bitmap = autopy.bitmap.Bitmap.open("sample_images/board2.png")
        grid = get_current_grid(bitmap)

        final_grid = get_grid_after_move(grid, ((6, 2), (7, 2)))

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

    def test_move_outcome_multiple_lines(self):
        """Test when lining up three jewels makes more line up, that
        we iterate until there are no more lines to remove.

        """
        grid = [
            ['green', 'yellow', 'purple', 'green', 'white', 'yellow', 'blue', 'yellow'],
            ['yellow', 'red', 'yellow', 'blue', 'orange', 'white', 'yellow', 'yellow'],
            ['blue', 'purple', 'orange', 'white', 'purple', 'blue', 'blue', 'red'],
            ['green', 'purple', 'red', 'yellow', 'green', 'white', 'yellow', 'yellow'],
            ['blue', 'green', 'red', 'white', 'purple', 'orange', 'white', 'yellow'],
            ['yellow', 'white', 'white', 'blue', 'orange', 'white', 'yellow', 'red'],
            ['purple', 'green', 'blue', 'red', 'yellow', 'blue', 'yellow', 'purple'],
            ['blue', 'green', 'yellow', 'orange', 'red', 'green', 'red', 'red']]

        final_grid = get_grid_after_move(grid, ((5, 4), (6, 4)))

        expected_final_grid = [
            ['green', 'yellow', 'purple', 'green', 'white', None, None, None],
            ['yellow', 'red', 'yellow', 'blue', 'orange', None, 'blue', 'yellow'],
            ['blue', 'purple', 'orange', 'white', 'purple', None, 'yellow', 'yellow'],
            ['green', 'purple', 'red', 'yellow', 'green', None, 'blue', 'red'],
            ['blue', 'green', 'red', 'white', 'purple', 'white', 'orange', 'yellow'],
            ['yellow', 'white', 'white', 'blue', 'orange', 'blue', 'yellow', 'red'],
            ['purple', 'green', 'blue', 'red', 'yellow', 'blue', 'yellow', 'purple'],
            ['blue', 'green', 'yellow', 'orange', 'red', 'green', 'red', 'red']]

        self.assertEqual(final_grid, expected_final_grid)

    def test_scoring_rows_sparse(self):
        """Empty grid positions are not scoring rows"""
        grid = [
            ['purple', 'green', 'green', 'yellow', 'white', 'blue', None, 'yellow'],
            ['white', 'blue', 'red', 'blue', 'purple', 'orange', None, 'white'],
            ['purple', 'purple', 'orange', 'yellow', 'white', 'blue', None, 'orange'],
            ['red', 'green', 'blue', 'purple', 'red', 'yellow', 'purple', 'blue'],
            ['blue', 'yellow', 'blue', 'yellow', 'orange', 'white', 'green', 'red'],
            ['orange', 'yellow', 'red', 'green', 'red', 'yellow', 'yellow', 'purple'],
            ['purple', 'green', 'white', 'blue', 'orange', 'orange', 'blue', 'purple'],
            ['blue', 'red', 'white', 'purple', 'yellow', 'orange', 'green', 'green']]

        self.assertEqual(count_scoring_lines(grid), 0)
