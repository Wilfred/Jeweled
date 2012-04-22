import board
from jewels import get_closest_jewel

import autopy

def get_jewel_bitmaps(screen_bitmap):
    x, y = board.get_position()

    rows = []

    # every row
    for i in range(board.SIZE):
        row = []

        # every jewel in that row
        for j in range(board.SIZE):
            jewel_position = (x + board.ELEMENT_WIDTH_PX * j,
                              y + board.ELEMENT_HEIGHT_PX * i)
            jewel_bitmap = screen_bitmap.get_portion(
                jewel_position, (board.ELEMENT_WIDTH_PX, board.ELEMENT_HEIGHT_PX))
            
            row.append(jewel_bitmap)

        rows.append(row)

    return rows


CENTRE_SIZE = 30

def get_jewel_colors(jewel_bitmaps):
    """We get the average color of the centre of the bitmap of each jewel."""

    rows = []

    for bitmap_row in jewel_bitmaps:
        row = []

        for bitmap in bitmap_row:

            # get the centre of the bitmap
            centre = bitmap.get_portion((board.ELEMENT_WIDTH_PX // 2 - CENTRE_SIZE // 2, board.ELEMENT_HEIGHT_PX // 2 - CENTRE_SIZE // 2),
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


def get_current_grid():
    screen_bitmap = autopy.bitmap.capture_screen()

    jewel_bitmaps = get_jewel_bitmaps(screen_bitmap)
    colors = get_jewel_colors(jewel_bitmaps)
    grid = get_jewel_names(colors)

    return grid


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


