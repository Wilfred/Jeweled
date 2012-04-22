"""Bejeweled: An automated bot for HTML 5 Bejeweled.

Scoring information: http://alexx-kay.livejournal.com/131629.html

"""

from __future__ import division

from time import sleep

import board
import mouse
from tactics import get_scoring_moves
from screen import get_current_grid


if __name__ == '__main__':
    # TODO: use xdg-open

    print "Searching for board..."

    while True:
        try:
            grid = get_current_grid()
            scoring_moves = list(get_scoring_moves(grid))
            
            # for now, we pick a scoring move arbitrarily
            move_a, move_b = scoring_moves[0]
            mouse.swap_jewels(move_a, move_b)

        except board.NotVisible:
            print "No board visible."

        sleep(1)
