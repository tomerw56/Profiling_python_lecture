import atexit
# Using cProfile.Profile example
import random
import signal

def print_msg():
    for i in range(10):
        print("Program completed")

def generate():
    data = [random.randint(0, 99) for p in range(0, 1000)]
    return data

def search_function(data):
    for i in data:
        if i in [100,200,300,400,500]:
            print("success")

def main():
  while(True):
    data=generate()
    search_function(data)
    print_msg()


def exit_handler(profiler):
  print("!!!!!!!!")
  profiler.disable()
  stats = pstats.Stats(profiler).sort_stats('tottime')
  stats.print_stats()


if __name__ == '__main__':
    import cProfile, pstats
    try:
      profiler = cProfile.Profile()
      atexit.register(exit_handler,profiler)
      profiler.enable()
      main()
      exit_handler(profiler)
    except KeyboardInterrupt:
      exit_handler(profiler)