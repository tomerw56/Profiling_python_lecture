import time
from functools import wraps
last_time_called=0.0


def rate_limited(maxPerSecond:int=1):
    """
        Decorator for rate limiting a function
    """
    minInterval = 1.0 / float(maxPerSecond)

    def decorate(func):
        lastTimeCalled = [0.0]

        def rateLimitedFunction(*args, **kargs):
            elapsed = time.perf_counter() - lastTimeCalled[0]
            leftToWait = minInterval - elapsed
            if leftToWait > 0:
                time.sleep(leftToWait)
            ret = func(*args, **kargs)
            lastTimeCalled[0] = time.perf_counter()
            return ret

        return rateLimitedFunction

    return decorate


@rate_limited(maxPerSecond=4)
def frequantly_called_function():
    print(f"called on {time.perf_counter()}")


for i in range(8):
    frequantly_called_function()