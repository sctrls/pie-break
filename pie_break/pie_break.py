from datetime import datetime
import threading
import time
import sched
import webbrowser
import random
from threading import current_thread

class PieBreak(threading.Thread):
    """A timer class which accepts custom work times and lists of urls."""

    s = sched.scheduler(time.time, time.sleep)

    def __init__(
        self,
        start_time=time.time(),
        work_minutes=50,
        urls=["https://www.youtube.com/watch?v=6VB4bgiB0yA&ab_channel=Fireplace4K"],
        event_queue=[],
        ):
        threading.Thread.__init__(self, group=None, target=self, name='pie_thread')
        self.start_time = start_time
        self.work_minutes = work_minutes
        if urls:
            self.urls = urls
        # self.daemon = True
        self.event_queue = event_queue

    def get_params(self):
        """Get the relative starting time in seconds, the total work
        time, and list of urls from which the timer will pick.
        """
        return self.start_time, self.work_minutes, self.urls, self.event_queue

    # def pause(self):
    #     # Time with asynchio
    #     pass

    # def restart_timer(self, new_work_time):
    #     self.work_time = new_work_time
    #     self.run()

    # def set_break_length(self, break_length):
    #     # Implement a break length. How to time it?
    #     pass

    # # def get_url_file_location(self):
    #     # System agnostic open text file cmd
    #     pass

    def get_random_url(self):
        """Return a url at random from urls.txt or default."""
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

    def start_break(self):
        """The attention grabbing mechanism."""
        print(f"\n{self.work_minutes} minutes have passed. Time for a break.\nPieBreak: ", end='')
        url = self.get_random_url()
        print(url)
        # webbrowser.open(url)

    def add_scheduled_action(self, delay, priority, action, argument=(), kwargs={}):
        """Update the schedule on the fly."""
        # for event in self.s.queue:
        #     self.s.enterabs(event[0], event[1], event[2], event[3], event[4])
        self.s.enter(delay, priority, action, argument, kwargs)
        print(self.s.queue)
        self.s.run()

    def run(self):
        """Repeatedly open a url after a user-specified number of minutes."""
        print(f'\r\n{time.strftime("%H:%M:%S", time.localtime())}: Working for {self.work_minutes} minutes')

        # Start an event queue, checking for a queue carried over.
        if not self.event_queue:
            self.event_queue.append((self.work_minutes, 1, self.start_break))
            print(f"1: {self.event_queue}")
        # Read the latest queue and run it
        for i in range(10):
            print(f"Before for loop: {self.s.queue}")
            for event in self.event_queue:
                print(f"Event in queue: {event}")
                self.s.enter(event[0], event[1], self.start_break)
            print(f"After for loop: {self.s.queue}")
            self.s.run()

        # x = threading.Thread(target=self.schedule, args=(2, 1, self.start_break), name="pie_scheduler", daemon=True)
