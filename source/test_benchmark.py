import  time
def something(duration=0.0001):
    """
    Function that needs some serious benchmarking.
    """
    time.sleep(duration)
    # You may return anything you want, like the result of a computation
    return 123

def test_my_stuff(benchmark):
    # benchmark something

    result = benchmark(something)
    #the data is here benchmark.stats.stats
    assert result == 123