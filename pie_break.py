#!/usr/src/env python3.7
import time
import webbrowser
from sys import stdin, argv
import random

url_wikipedia_rand = 'https://en.wikipedia.org/wiki/Special:Random'
url_bebop = 'https://bit.ly/2KqqZ8r'
url_gt_allday = 'https://vimeo.com/17194640'
default_urls = [url_wikipedia_rand, url_bebop, url_gt_allday]

def random_url():
    '''Return a url at random from urls.txt in . or from the global defaults'''
    try:
        with open('urls.txt', 'r') as l:
            links = l.read()
    except FileNotFoundError as e:
        print('Using hardcoded urls.')
        return random.choice(default_urls)
    else:
        if len(links) > 0:
            links = links[:].split(' ')
            return random.choice(links)
        else:
            return random.choice(default_urls)


def break_timer(work_time=75, url='https://bit.ly/2KqqZ8r'):
    '''Open "url" approximately every "work_time" minutes forever.'''
    print(f'\r\nWorking for {work_time} minutes')
    count = 0
    while True:
        print(f'Distraction URL is: {url}\r\n')
        time.sleep(int(work_time)*60)
        print(f'{count}: {work_time} minutes have passed. Time for a break.')
        count += 1
        webbrowser.open(url)
        url = random_url()


if __name__ == '__main__':
    '''If two arguments are passed, parse the first as "working minutes"
        and the second as a url'''
    if len(argv) > 3:
        print('\r\nToo many arguments.')
        print('Specify time and url, only time, or none.\r\n')
    elif len(argv) == 3:
        break_timer(argv[1], argv[2])
    elif len(argv) == 2:
        break_timer(argv[1])
    else:
        print('How many minutes do you want to work for? ')
        work_time = int(stdin.readline())
        print('Any url preferences? ')
        url_today = stdin.readline()
