import yappi

def a():
    for _ in range(10000000):  # do something CPU heavy
        pass

yappi.set_clock_type("cpu") # Use set_clock_type("wall") for wall time
yappi.start()
a()

yappi.get_func_stats().print_all()
yappi.get_thread_stats().print_all()