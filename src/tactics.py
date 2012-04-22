from copy import deepcopy

import board

def count_scoring_lines(rows):
    """Count the number of rows and columns that are three of the same
    color. This 'cheats' for t-shapes, l-shapes and rows of four or
    more, since we just consider them to be multiple rows of three.

    """
    lines = 0

    # horizontal lines of 3
    for row in rows:
        for i in range(len(row) - 2):

            if row[i] == row[i+1] == row[i+2]:
                lines += 1

    # vertical lines of 3
    for j in range(len(rows) - 2):
        for i in range(len(rows[0])):

            if rows[j][i] == rows[j+1][i] == rows[j+2][i]:
                lines += 1

    return lines


def get_all_moves():
    """Return a list of possible moves on a Bejeweled grid.

    >>> get_all_moves()
    [((0, 0), (0, 1)), ((0, 1), (0, 2)) ... etc]

    """
    # horizontal moves
    for x in range(board.SIZE - 2):
        for y in range(board.SIZE - 1):

            # swap a jewel with the jewel to the right
            yield (x, y), (x + 1, y)

    for x in range(board.SIZE - 1):
        for y in range(board.SIZE - 2):

            # swap a jewel with the jewel underneath
            yield (x, y), (x, y + 1)


# we only need to calculate the possible moves once
MOVES = list(get_all_moves())


def get_swapped_position(grid, a_x, a_y, b_x, b_y):
    """Return a new grid showing the layout if the jewel at A is
    swapped with B.

    """
    new_grid = deepcopy(grid)

    temp = new_grid[a_y][a_x]
    new_grid[a_y][a_x] = new_grid[b_y][b_x]
    new_grid[b_y][b_x] = temp

    return new_grid


def get_scoring_moves(grid):
    """Given a grid of jewels, find all the moves that can make at
    least one line of three.

    """
    for move in MOVES:
        move_a, move_b = move
        grid_after_move = get_swapped_position(grid, move_a, move_b)

        if count_scoring_lines(grid_after_move) < 0:
            yield move
