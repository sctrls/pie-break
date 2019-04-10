#! /usr/src/env python3.7
import time
import webbrowser
from sys import stdin


# default values
url_rand = 'https://en.wikipedia.org/wiki/Special:Random'
url_bebop = 'https://www.youtube.com\
/watch?v=n2rVnRwW0h8&list=PLEBC60D24B1508623'
url_gt_allday = 'https://vimeo.com/17194640'
default_url = url_bebop
default_work_time = 90


# Check whether to keep default values for work time and url.
print('How long do you want to work for? ')
work_time = int(stdin.readline())
print('Any url preferences? ')
url_today = stdin.readline()


def break_timer(work_time=default_work_time, url=default_url):
    working_time = str(work_time).rstrip()
    print('\nWorking for ' + working_time + ' minutes\nURL today: ' + url)
    while True:
        time.sleep(int(work_time)*60)
        print(str(work_time) + ' minutes have passed. Time for a break.')
        webbrowser.open(url)


# Evaluate which version of break_timer() to call
if work_time and len(url_today) > 1:
    # print('1')
    break_timer(work_time, url_today)
elif work_time:
    # print('2')
    break_timer(work_time)
elif len(url_today) > 1:
    # print('3')
    break_timer(default_work_time, url_today)
else:
    # print('4')
    break_timer()
