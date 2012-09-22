from unittest import TestCase

import autopy
from board import get_position


class BoardDetectionTest(TestCase):
    def test_basic_detection(self):
        bitmap = autopy.bitmap.Bitmap.open("sample_images/board1.png")
        get_position(bitmap) # throws board.NotVisible if no position

    def test_darker_board_detection(self):
        bitmap = autopy.bitmap.Bitmap.open("sample_images/board_dark_background.png")
        get_position(bitmap) # throws board.NotVisible if no position

