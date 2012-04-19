"""Bejeweled: An automated bot for HTML 5 Bejeweled.

Scoring in first round:

3 in a row: 50
Each subsequent row scores 50 more: 50, 100, 150, and so on.

4 in a row: 100
Also gains a 'fire gem'.

Scores in subsequent rounds increase by 50 points per level.

"""

from __future__ import division

from time import sleep
from math import sqrt


import autopy

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


def get_jewel_names(jewel_colors):
    """Given a grid of jewel colors, get their names."""
    rows = []

    for color_row in jewel_colors:
        row = []

        for color in color_row:
            row.append(get_closest_jewel(color))

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


# TODO: wildcard jewel
JEWELS = {
    "orange": (126, 81, 47),
    "green": (34, 125, 56),
    "purple": (92, 40, 104),
    "white": (114, 118, 122),
    "yellow": (112, 108, 53),
    "red": (145, 38, 54),
}


def get_closest_jewel(color):
    """Given a color from the screen, find the closest jewel color."""
    first_color = JEWELS.keys()[0]

    # initialise
    closest_color = first_color
    shortest_distance = get_distance(color, JEWELS[first_color])

    # find the closest color
    for jewel_name, jewel_color in JEWELS.items():
        distance = get_distance(color, jewel_color)

        if distance < shortest_distance:
            shortest_distance = distance
            closest_color = jewel_name

    return closest_color


def get_distance(x, y):
    """Find the Euclidean distance between two 3-dimensional points."""
    p1, p2, p3 = x
    q1, q2, q3 = y

    distance = sqrt((p1 - q1) ** 2 + (p2 - q2) ** 2 + (p3 - q3) ** 2)
    return distance


if __name__ == '__main__':
    # TODO: use xdg-open

    print "Searching for board..."

    while True:
        try:
            bitmaps = get_jewel_bitmaps()
            colors = get_jewel_colors(bitmaps)

            for row in get_jewel_names(colors):
                print row
                
        except BoardNotVisible:
            print "No board visible."

        sleep(1)
