"""Bejeweled: An automated bot for HTML 5 Bejeweled.

Bejeweled is at: http://bejeweled.popcap.com/html5/
Mode targeted: Classic

Scoring in first round:

3 in a row: 50
Each subsequent row scores 50 more: 50, 100, 150, and so on.

4 in a row: 100
Also gains a 'fire gem'.

Scores in subsequent rounds increase by 50 points per level.

"""

import autopy
from time import sleep

# TODO: dynamically calculate board position
BOARD_X = 1092
BOARD_Y = 253

GRID_WIDTH = GRID_HEIGHT = 80
GRID_SIZE = 8

if __name__ == '__main__':
    # TODO: use xdg-open
    print "Starting in 10 seconds, please switch to bejeweled"
    sleep(10)
    
    autopy.bitmap.capture_screen().save('screengrab.png')
