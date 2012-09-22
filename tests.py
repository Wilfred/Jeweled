from unittest import TestCase

import autopy
from board import get_position, NotVisible


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
