from copy import deepcopy

import board

def count_scoring_lines(rows):
    """Count the number of rows and columns that are three of the same
    color.

    """
    return len(list(get_scoring_lines(rows)))


def get_scoring_lines(rows):
    """List all the rows and columns that are three of the same
    color. This 'cheats' for t-shapes, l-shapes and rows of four or
    more, since we just consider them to be multiple rows of three.

    """

    # horizontal lines of 3
    for y, row in enumerate(rows):
        for x in range(len(row) - 2):

            if row[x] == row[x+1] == row[x+2]:
                yield [(x, y), (x+1, y), (x+2, y)]

    # vertical lines of 3
    for y in range(len(rows) - 2):
        for x in range(len(rows[0])):

            if rows[y][x] == rows[y+1][x] == rows[y+2][x]:
                yield [(x, y), (x, y+1), (x, y+2)]


def get_all_moves():
    """Return a list of possible moves on a Bejeweled grid.

    >>> get_all_moves()
    [((0, 0), (0, 1)), ((0, 1), (0, 2)) ... etc]

    """
    # horizontal moves
    for x in range(board.SIZE - 1):
        for y in range(board.SIZE):

            # swap a jewel with the jewel to the right
            yield (x, y), (x + 1, y)

    for x in range(board.SIZE):
        for y in range(board.SIZE - 1):

            # swap a jewel with the jewel underneath
            yield (x, y), (x, y + 1)


# we only need to calculate the possible moves once
MOVES = list(get_all_moves())


def get_swapped_position(grid, a, b):
    """Return a new grid showing the layout if the jewel at A is
    swapped with B.

    """
    a_x, a_y = a
    b_x, b_y = b
    
    new_grid = deepcopy(grid)

    temp = new_grid[a_y][a_x]
    new_grid[a_y][a_x] = new_grid[b_y][b_x]
    new_grid[b_y][b_x] = temp

    return new_grid


def get_scoring_moves(grid):
    """Given a grid of jewels, find the moves that will put three or
    more jewels in a line.

    """
    scoring_moves = []
    
    for move in MOVES:
        move_a, move_b = move
        grid_after_move = get_swapped_position(grid, move_a, move_b)

        scoring_lines = count_scoring_lines(grid_after_move)
        if scoring_lines > 0:
            scoring_moves.append(move)

    # sort the moves so the highest on the board comes first. Ideally
    # we'd find the rows that are highest rather than the moves.
    scoring_moves.sort(key=lambda ((from_x, from_y), (to_x, to_y)): (from_y, to_y))
    return scoring_moves


def get_grid_after_move(grid, move):
    """Given a grid where some jewels are lined up, remove those lines
    and move jewels down to fill the gaps. Note we just put None where
    we don't know what will fill the gap.

    """
    move_a, move_b = move
    grid = get_swapped_position(grid, move_a, move_b)
    
    # find the jewels that will disappear
    removed_jewels = set()
    for line in get_scoring_lines(grid):
        for jewel in line: # of the form (x, y)
            removed_jewels.add(jewel)

    # remove them
    for x, y in removed_jewels:
        grid[y][x] = None

    # move all the jewels down if there's a space below
    # repeating until we can't move anything down any further
    changed = True
    while changed:
        changed = False

        for y in range(board.SIZE - 1):
            for x in range(board.SIZE):

                current_jewel = grid[y][x]
                jewel_below = grid[y + 1][x]
                if current_jewel is not None and jewel_below is None:
                    # empty position below, move this one down
                    grid[y + 1][x] = grid[y][x]
                    grid[y][x] = None

                    changed = True

    return grid
