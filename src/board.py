import autopy


class NotVisible(Exception): pass

ELEMENT_WIDTH_PX = ELEMENT_HEIGHT_PX = 51 # a single jewel on the grid
GRID_WIDTH = GRID_HEIGHT = 51 # size in px of one grid element

SIZE = 8 # number of row elements/column elements in grid

WIDTH_IN_PX = 644
HEIGHT_IN_PX = 485


def get_position(screen_bitmap):
    """Find the co-ordinates of the top left corner of the board."""
    board_left_edge = autopy.bitmap.Bitmap.open('resources/board_edge.png')

    # we search for the left edge of the board. Since autopy searches
    # left to right, find_bitmap returns the correct co-ordinates
    board_edge_positions = screen_bitmap.find_every_bitmap(board_left_edge)

    if len(board_edge_positions) != 1:
        raise NotVisible()
    
    board_position = board_edge_positions[0]
    raw_x, raw_y = board_position
        
    # check the diagonally opposite corner is on screen
    bottom_right_x = raw_x + WIDTH_IN_PX
    bottom_right_y = raw_y + HEIGHT_IN_PX
    if not screen_bitmap.point_in_bounds(bottom_right_x, bottom_right_y):
        raise NotVisible()

    # the board itself is offset from the left edge
    x = raw_x + 199
    y = raw_y + 32

    return (x, y)
