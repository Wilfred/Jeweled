# Jeweled

Jeweled is a Python bot that plays the Flash/HTML 5 version of
Bejeweled.

GPLv3 license.

## Bejeweled target

Bejeweled is at http://bejeweled.popcap.com/html5/ and this bot
assumes the SD mode since its maximum resolution is lower.

We are targetting the 'classic' mode, so there are no time
constraints. Make sure you disable animated backgrounds.

## Usage

### Installation

Python 2.X, Pip and virtualenv are required.

    $ virtualenv ~/.virtualenvs/jeweled
    $ . ~/.virtualenvs/jeweled/bin/activate
    (jeweled) $ pip install -r requirements.txt
    (jeweled) $ src/play_bejeweled
     
There are also convenience tools:

    (jeweled) $ src/take_board_screenshot
    Saved board.png.

    (jeweled) $ src/find_board_in_image sample_images/board1.png
    Found a board at position (267, 104)

    (jeweled) $ src/cut_jewel_from_board sample_images/board_with_glowing_yellow.png 7 7
    Saved jewel.png.

    (jeweled) $ src/show_jewels_on_board sample_images/board1.png
    green	blue	blue	orange	purple	yellow	red	red
    blue	red	blue	blue	white	blue	blue	green
    green	purple	orange	purple	orange	white	blue	red
    yellow	yellow	orange	yellow	red	green	red	orange
    red	purple	purple	yellow	purple	green	orange	blue
    green	yellow	blue	green	white	red	purple	green
    purple	blue	white	purple	yellow	yellow	red	purple
    purple	yellow	red	white	green	red	green	yellow
    
Running the tests:

    $ nosetests

## Scores

Highest score achieved: 1,298,550

How scores are calculated: http://support.popcap.com/bejeweled-html5

Basic summary of Bejeweled strategy: http://alexx-kay.livejournal.com/131629.html


