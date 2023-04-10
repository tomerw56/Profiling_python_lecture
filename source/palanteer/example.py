#! /usr/bin/env python3
import sys
import random
from palanteer import *

globalMinValue, globalMaxValue =  0, 10

# Handler (=implementation) of the example CLI, which sets the range
def setBoundsCliHandler(minValue, maxValue):              # 2 parameters (both integer) as declared
    global globalMinValue, globalMaxValue
    if minValue>maxValue:                                 # Case where the CLI execution fails (non null status). The text answer contains some information about it
        return 1, "Minimum value (%d) shall be lower than the maximum value (%d)" % (minValue, maxValue)

    # Modify the state of the program
    globalMinValue, globalMaxValue = minValue, maxValue
    # CLI execution was successful (null status)
    return 0, ""


def main(argv):
    global globalMinValue, globalMaxValue

    plInitAndStart("example")                             # Start the instrumentation
    plDeclareThread("Main")                               # Declare the current thread as "Main", so that it can be identified more easily in the script
    plRegisterCli(setBoundsCliHandler, "config:setRange", "min=int max=int", "Sets the value bounds of the random generator")  # Declare the CLI
    plFreezePoint()                                       # Add a freeze point here to be able to configure the program at a controlled moment

    plBegin("Generate some random values")
    for i in range(100000):
        value = int(globalMinValue + random.random()*(globalMaxValue+1-globalMinValue))
        plData("random data", value)                      # Here are the "useful" values
    plEnd("")                                             # Shortcut for plEnd("Generate some random values")

    plStopAndUninit()                                     # Stop and uninitialize the instrumentation

# Bootstrap
if __name__ == "__main__":
    main(sys.argv)