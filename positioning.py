import autopy


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


