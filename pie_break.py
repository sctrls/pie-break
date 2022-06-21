#!/usr/bin/env python3

import time
import webbrowser
from sys import argv, exit
import random


class PieBreak():
    """Working time is in minutes"""

    def __init__(self, working_time = 70, urls = ['https://en.wikipedia.org/wiki/Special:Random']):
        self.working_time = working_time
        if urls:
            self.urls = urls


    def get_params(self):
        return self.working_time, self.urls

    def get_random_url(self, *urls):
        '''Return a random url at random from urls.txt or default'''

        if urls[0]:
            print(urls[0])
            return random.choice(urls)

        try:
            with open('urls.txt', 'r') as links_file:
                links = links_file.readlines()
                links = [link.rstrip('\n') for link in links]
        except FileNotFoundError as e:
            print('urls.txt file not found. Using defaults...')
            return self.default_url
        else:
            print('Reading urls from file..')
            if len(links) > 0:
                return random.choice(links)


    def run(self, *urls, work_time = 75):
            #url = 'https://en.wikipedia.org/wiki/Special:Random'):
        '''Repeatedly open a url after a user-specified number of minutes'''

        print(f'\r\nWorking for {work_time} minutes')
        count = 0
        while True:
            url = self.get_random_url(urls)
            print(f'Distraction URL is: {url}\r\n')
            time.sleep(int(work_time)*60)
            print(f'Break number {count}: {work_time} minutes have \
                  passed. Time for a break.')
            count += 1
            webbrowser.open(url)


if __name__ == '__main__':
    '''If multiple arguments are passed, parse the first as "working minutes"
        and the rest as urls'''

    # take input parameters: either nothing, a worktime, or a worktime and a series of urls
    # create class accordingly
    # call run()

    timer = None

    # If a time and several urls are passed
    if len(argv) >= 3:
        try:
            timer = PieBreak(working_time = int(argv[1]), urls = argv[2:])
        except ValueError:
            working_time = input('Try again. For how many minutes do you want to work? ')
            try:
                working_time = int(working_time)
            except ValueError:
                exit('You use numbers like elon musk names children.. Exiting.')
            else:
                urls = []
                while True:
                    if urls:
                        new_url = input('Another?: ')
                    else:
                        new_url = input('If you want, enter a url by which to be interrupted: ')
                    if not new_url:
                        break
                    urls.append(new_url)
            # urls = input('Pass the urls you want to use (if any), separated by commas.. ')
            # urls = urls.split(', ')
            # print(urls)
                timer = PieBreak(working_time = working_time, urls = urls)
        timer.get_params()

    # If only a working time is passed
    elif len(argv) == 2:
        try:
            timer = PieBreak(working_time = int(argv[1]))
        except ValueError:
            working_time = input("Try again. For how many minutes do you want to work?")

    # If no parameters are passed
    else:
        timer = PieBreak()

    print(timer.get_params())