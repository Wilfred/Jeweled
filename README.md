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
     (jeweled) $ python src/bejeweled.py

## Scores

Highest score achieved: 363,760

How scores are calculated: http://support.popcap.com/bejeweled-html5

Basic summary of Bejeweled strategy: http://alexx-kay.livejournal.com/131629.html


