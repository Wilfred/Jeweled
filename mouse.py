import autopy

import board


def move_to_jewel(x, y):
    """Move the cursor to the centre of a jewel on the Bejeweled grid.

    # e.g. put mouse in the centre of the top-left jewel:
    >>> move_to_jewel(0, 0)

    """
    
    board_x, board_y = board.get_position()

    target_x = int(board_x + (x + 0.5) * board.ELEMENT_WIDTH_PX)
    target_y = int(board_y + (y + 0.5) * board.ELEMENT_HEIGHT_PX)
    autopy.mouse.move(target_x, target_y)

