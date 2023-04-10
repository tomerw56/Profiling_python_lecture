#! /usr/bin/env python3
import sys
import palanteer_scripting as ps

def main(argv):
    if len(sys.argv)<2:
        print("Error: missing parameters (the program to launch)")
        sys.exit(1)

    # Initialize the scripting module
    ps.initialize_scripting()

    # Enable the freeze mode so that we can safely configure the program once stopped on its freeze point
    ps.program_set_freeze_mode(True)

    # Launch the program under test
    ps.process_launch(sys.argv[1], args=sys.argv[2:])
    # From here, we are connected to the remote program

    # Configure the selection of events to receive
    my_selection = ps.EvtSpec(thread="Main", events=["random data"]) # Thread "Main", only the event "random data"
    ps.data_configure_events(my_selection)

    # Configure the program
    status, response = ps.program_cli("config:setRange min=300 max=500")
    if status!=0:
        print("Error when configuring: %s\nKeeping original settings." % response)

    # Disable the freeze mode so that the program resumes its execution
    ps.program_set_freeze_mode(False)

    # Collect the events as long as the program is alive or we got some events in the last round
    qty, sum_values, min_value, max_value, has_worked = 0, 0, 1e9, 0, True
    while ps.process_is_running() or has_worked:
        has_worked = False
        for e in ps.data_collect_events(timeout_sec=1.):  # Loop on received events, per batch
            has_worked, qty, sum_values, min_value, max_value = True, qty+1, sum_values+e.value, min(min_value, e.value), max(max_value, e.value)

    # Display the result of the processed collection of data
    print("Quantity: %d\nMinimum : %d\nAverage : %d\nMaximum : %d" % (qty, min_value, sum_values/max(qty,1), max_value))

    # Cleaning
    ps.process_stop()            # Kills the launched process, if still running
    ps.uninitialize_scripting()  # Uninitialize the scripting module


# Bootstrap
if __name__ == "__main__":
    main(sys.argv)