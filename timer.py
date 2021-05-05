import time


class TimerError(Exception):
    """TimerError"""


class Timer:
    def __init__(self):
        self._start_time = None

    def start(self):
        if self._start_time is not None:
            raise TimerError(f"Timer is running. Use .stop() to stop it")
        self._start_time = time.perf_counter()

    def stop(self):
        if self._start_time is None:
            raise TimerError(
                f"Timer is not running. Use .start() to start it")
        time_on_start = self._start_time
        self._start_time = None
        return time.perf_counter() - time_on_start
