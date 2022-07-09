# Pie Break
#### An attention-grabbing break timer to keep you fresh.

pie_break optionally takes a number of minutes x and any number of urls as arguments. It alerts you every time x minutes have passed by opening a random url in your default web browser.

<br>

## Requires
 - Python 3.8.12
 - Optionally, a urls.txt file - containing space separated urls - placed in the same directory as pie_break.py

<br>

## Run
Run with:

`python3 pie/breaker.py`

<br>

You can also specify a time in minutes and url:

`python3 pie/breaker.py 90 https://bit.ly/1QVSIYb`

<br>

Or only a time and use the default array of distraction URLs:

`python3 pie/breaker.py 45`

<br>

If a urls.txt file is included in the same directory as pie_break.py, **it will automatically be read from** to get the next url at every cycle.

<br>

## Defaults
Array of default urls:
* Wikipedia Random article - https://en.wikipedia.org/wiki/Special:Random
* Cowboy Bebop OST on youtube - https://bit.ly/2KqqZ8r
* Girl Talk's "All Day" - https://vimeo.com/17194640

<br>


## TODO
* Better comments
* Tests
* Synchronize
* Read urls from a browser bookmark folder.
* A convenient way to specify the folder.