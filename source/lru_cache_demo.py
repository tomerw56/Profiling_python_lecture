import random
import time
from functools import lru_cache


@lru_cache(maxsize=None)
def heavy_processing(n):
    sleep_time = n + random.random()
    print(f"sleeping ? {sleep_time}")
    time.sleep(sleep_time)

def run_heavy_processing():
    start_time = time.perf_counter()
    heavy_processing(0)
    end_time = time.perf_counter()
    total_time = end_time - start_time
    print(f' took {total_time:.4f} seconds')


run_heavy_processing()
run_heavy_processing()
run_heavy_processing()




