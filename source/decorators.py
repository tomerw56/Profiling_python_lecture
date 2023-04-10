from functools import wraps
import time
import sys
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s',
                              '%m-%d-%Y %H:%M:%S')

stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setLevel(logging.DEBUG)
stdout_handler.setFormatter(formatter)



def timeit(file_name=""):
    logger.addHandler(stdout_handler)
    if (file_name!=""):
        file_handler = logging.FileHandler(file_name)
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            start_time = time.perf_counter()
            result = function(*args, **kwargs)
            end_time = time.perf_counter()
            total_time = end_time - start_time
            logger.info(f'Function {function.__name__}{args} {kwargs} Took {total_time:.4f} seconds')
            return result
        return wrapper
    return decorator



class Calculator:
    @timeit(file_name="1.log")
    def calculate_something(self, num):
        """
        an example function that returns sum of all numbers up to the square of num
        """
        total = sum((x for x in range(0, num**2)))
        return total

    def __repr__(self):
        return f'calc_object:{id(self)}'


if __name__ == '__main__':
    calc = Calculator()
    calc.calculate_something(10)
    calc.calculate_something(100)
    calc.calculate_something(1000)
    calc.calculate_something(5000)
    calc.calculate_something(10000)