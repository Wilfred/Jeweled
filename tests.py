from unittest import TestCase

import autopy
from board import get_position


class BoardDetectionTest(TestCase):
    def test_basic_detection(self):
        bitmap = autopy.bitmap.Bitmap.open("sample_images/board1.png")
        x, y = get_position(bitmap) # throws board.NotVisible if no position

        # since the board positioning is imprecise, we just assert a range
        self.assertGreater(x, 260)
        self.assertLess(x, 270)

        self.assertGreater(y, 100)
        self.assertLess(y, 110)

    def test_darker_board_detection(self):
        bitmap = autopy.bitmap.Bitmap.open("sample_images/board_dark_background.png")
        get_position(bitmap) # throws board.NotVisible if no position

