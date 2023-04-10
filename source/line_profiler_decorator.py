from line_profiler import LineProfiler
import time

profiler = LineProfiler()

def profile(func):
    def inner(*args, **kwargs):
        profiler.add_function(func)
        profiler.enable_by_count()
        return func(*args, **kwargs)
    return inner

def print_stats():
    profiler.print_stats()

@profile
def a():
    b=1
    for i in range(10):
        b+=i
        time.sleep(0.25)
    print_stats()
    return b

a()