#!/usr/bin/env python

import threading
import time
import webbrowser
import random


class PieBreak(threading.Thread):
    """A timer class which accepts custom work times and lists of urls."""

    def __init__(
        self, work_time=1,
        urls=["https://www.youtube.com/watch?v=6VB4bgiB0yA&ab_channel=Fireplace4K"]
        ):
        threading.Thread.__init__(self, group=None, target=self, name='pie_thread')
        self.start_time = time.time()
        self.work_time = work_time
        if urls:
            self.urls = urls
        self.daemon = True

    def get_params(self):
        """Get the relative starting time in seconds, the total work
        time, and list of urls from which the timer will pick.
        """
        return self.start_time, self.work_time, self.urls

    def pause(self):
        # time with asynchio
        pass

    def restart_timer(self, new_work_time):
        self.work_time = new_work_time
        self.run()

    def set_break_length(self, break_length):
        # Implement a break length. How to time it?
        pass

    def get_url_file_location(self):
        # system agnostic open text file cmd
        pass


    def get_random_url(self):
        """Return a random url at random from urls.txt or default."""
        if len(self.urls) > 1:
            return random.choice(self.urls)
        else:
            try:
                with open('urls.txt', 'r') as links_file:
                    links = links_file.readlines()
                    links = [link.rstrip("\n") for link in links]
            except FileNotFoundError:
                # If no file is present return the default url
                return self.urls[0]
            else:
                # if the file could be found and parsed, return a url at random
                print('Reading urls from file..')
                if len(links) > 0:
                    return random.choice(links)

    def run(self):
        """Repeatedly open a url after a user-specified number of minutes."""
        print(f'\r\n{time.strftime("%H:%M:%S", time.localtime())}: Working for {self.work_time} minutes')
        while True:
            url = self.get_random_url()
            time.sleep(int(self.work_time) * 60)
            # TODO print "5 minutes left"
            # TODO time with asyncio instead
            print(
                f'''{self.work_time} minutes have passed. Time for a break.'''
            )
            webbrowser.open(url)

    # async def get_user_input(self):
    #     while True:
    #         new_in = input("Add info while loop runs: ")
    #         print(new_in)
