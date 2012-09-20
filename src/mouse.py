import autopy

import board


def move_to_jewel(bitmap, x, y):
    """Move the cursor to the centre of a jewel on the Bejeweled grid.

    # e.g. put mouse in the centre of the top-left jewel:
    >>> move_to_jewel(0, 0)

    """
    
    board_x, board_y = board.get_position(bitmap)

    target_x = int(board_x + (x + 0.5) * board.ELEMENT_WIDTH_PX)
    target_y = int(board_y + (y + 0.5) * board.ELEMENT_HEIGHT_PX)
    autopy.mouse.move(target_x, target_y)


def swap_jewels(bitmap, a, b):
    """Swap the jewels A and B according to their positions on the
    Bejeweled grid.


    >>> swap_jewels((0, 0), (0, 1))

    """
    a_x, a_y = a
    move_to_jewel(bitmap, a_x, a_y)
    autopy.mouse.click()

    b_x, b_y = b
    move_to_jewel(bitmap, b_x, b_y)
    autopy.mouse.click()
