from datetime import datetime
import threading
import time
import sched
import webbrowser
import random
from threading import current_thread

class PieBreak(threading.Thread):
    """A timer class which accepts custom work times and lists of urls."""

    def __init__(
        self,
        periodic={50},
        one_off=set(),
        urls=["https://open.spotify.com/album/6H5fUQk4FkT9iR4SNHnK3D?si=N52exCBWSZW2ee4Pj8oTwg"]
        ):
        threading.Thread.__init__(self, group=None, target=self, name="pie_thread")
        self.start_time = time.time()
        self.periodic = periodic
        self.one_off = one_off
        if urls:
            self.urls = urls
        # Flag for thread survival
        self.timing = False

    def get_params(self):
        """Get the relative starting time in seconds, the total work
        time, and list of urls from which the timer will pick.
        """
        return self.start_time, self.urls, self.periodic, self.one_off, self.timing

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
                with open("urls.txt", "r") as links_file:
                    links = links_file.readlines()
                    links = [link.rstrip("\n") for link in links]
            except FileNotFoundError:
                # If no file is present return the default url
                return self.urls[0]
            else:
                # if the file could be found and parsed, return a url at random
                print("Reading urls from file..")
                if len(links) > 0:
                    return random.choice(links)

    def start_break(self):
        """The attention grabbing mechanism."""
        if self.timing:
            print(f"\nTime for a break.\nPieBreak: ", end="")
            url = self.get_random_url()
            print(url)
        # webbrowser.open(url)

    def set_timing(self, timing_toggle):
        self.timing = timing_toggle
        return self.timing

    def run(self):
        """Repeatedly open a url after a user-specified number of minutes."""

        s = sched.scheduler(time.time, time.sleep)

        # If there's anything in one_off, join it to periodic
        # Create and run a schedule with both
        # Loop over periodic thereafter
        self.timing = True
        if self.one_off:
            events = self.one_off | self.periodic
            for event_time in events:
                s.enter(event_time, 1, self.start_break)
            print(f"\r\n{time.strftime('%H:%M:%S', time.localtime())}: Starting timer..")
            s.run()
        if self.periodic:
            while self.periodic:
                if self.timing:
                    for event_time in self.periodic:
                        s.enter(event_time, 1, self.start_break)
                        s.run()
            print(f"\r\n{time.strftime('%H:%M:%S', time.localtime())}: Starting timer..")
            s.run()

