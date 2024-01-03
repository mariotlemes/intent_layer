import time


class Timer:
    def __init__(self):
        self.start_time = None
        self.paused_time = None
        self.paused = False

    def start(self):
        self.start_time = time.time()

    def pause(self):
        if not self.paused:
            self.paused_time = time.time()
            self.paused = True
            # print("Timer paused.")

    def resume(self):
        if self.paused:
            elapsed_paused_time = time.time() - self.paused_time
            self.start_time += elapsed_paused_time
            self.paused = False
            # print("Timer resumed.")

    def elapsed_time(self):
        if self.start_time:
            if self.paused:
                return self.paused_time - self.start_time
            else:
                return time.time() - self.start_time
        return 0
