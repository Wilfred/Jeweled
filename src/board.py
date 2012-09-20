import autopy


class NotVisible(Exception): pass

ELEMENT_WIDTH_PX = ELEMENT_HEIGHT_PX = 51 # a single jewel on the grid
GRID_WIDTH = GRID_HEIGHT = 51 # size in px of one grid element

SIZE = 8 # number of row elements/column elements in grid


def get_position(screen_bitmap):
    """Find the co-ordinates of the top left corner of the board."""
    board_corner = autopy.bitmap.Bitmap.open('resources/board_corner.png')

    board_position = screen_bitmap.find_bitmap(board_corner)

    if board_position:
        raw_x, raw_y = board_position

        # the board position is not on the board, so the actual
        # top-left corner is slightly offset:
        return (raw_x + 1, raw_y + 9)
    else:
        # TODO: also check bottom right corner is visible
        raise NotVisible()


