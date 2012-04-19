"""Bejeweled: An automated bot for HTML 5 Bejeweled.

Scoring in first round:

3 in a row: 50
Each subsequent row scores 50 more: 50, 100, 150, and so on.

4 in a row: 100
Also gains a 'fire gem'.

Scores in subsequent rounds increase by 50 points per level.

"""

from __future__ import division
import autopy
from time import sleep

GRID_WIDTH = GRID_HEIGHT = 51 # size in px of one grid element
GRID_SIZE = 8 # number of rows/columns in grid

class BoardNotVisible(Exception): pass

def get_board_position():
    """Find the co-ordinates of the top left corner of the board."""
    screen = autopy.bitmap.capture_screen()
    board_corner = autopy.bitmap.Bitmap.open('board_corner.png')

    board_position = screen.find_bitmap(board_corner)

    if board_position:
        raw_x, raw_y = board_position

        # the board position is not on the board, so the actual
        # top-left corner is slightly offset:
        return (raw_x + 1, raw_y + 9)
    else:
        # TODO: also check bottom right corner is visible
        raise BoardNotVisible()


def get_jewel_bitmaps():
    x, y = get_board_position()

    screen = autopy.bitmap.capture_screen()

    rows = []

    # every row
    for i in range(GRID_SIZE):
        row = []

        # every jewel in that row
        for j in range(GRID_SIZE):
            jewel_position = (x + GRID_WIDTH * j, y + GRID_HEIGHT * i)
            jewel_bitmap = screen.get_portion(jewel_position, (GRID_WIDTH, GRID_HEIGHT))
            row.append(jewel_bitmap)

        rows.append(row)

    return rows


CENTRE_SIZE = 50

def get_jewel_colors(jewel_bitmaps):
    """We get the average color of the centre of the bitmap of each jewel."""

    rows = []

    for bitmap_row in jewel_bitmaps:
        row = []

        for bitmap in bitmap_row:

            # get the centre of the bitmap
            centre = bitmap.get_portion((GRID_WIDTH // 2 - CENTRE_SIZE // 2, GRID_HEIGHT // 2 - CENTRE_SIZE // 2),
                                        (CENTRE_SIZE, CENTRE_SIZE))

            row.append(get_average_color(centre))

        rows.append(row)

    return rows


def get_average_color(bitmap):
    """Return an RGB tuple of the average color of this bitmap."""
    red_total, green_total, blue_total = 0, 0, 0

    for x in range(bitmap.width):
        for y in range(bitmap.height):
            hex_color = bitmap.get_color(x, y)
            r, g, b = autopy.color.hex_to_rgb(hex_color)

            red_total += r
            green_total += g
            blue_total += b

    total_pixels = bitmap.width * bitmap.height

    average_red = red_total / total_pixels
    average_green = green_total / total_pixels
    average_blue = blue_total / total_pixels

    return (average_red, average_green, average_blue)

    

if __name__ == '__main__':
    # TODO: use xdg-open

    print "Searching for board..."

    while True:
        try:
            bitmaps = get_jewel_bitmaps()
            print get_jewel_colors(bitmaps)
        except BoardNotVisible:
            print "No board visible."

        sleep(1)
