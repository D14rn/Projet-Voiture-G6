import atexit
import RPi.GPIO as g

# Register exit handler -> called when the program is terminated
@atexit.register
def exit_handler() -> None:
    """
    Perform all the necessary operations before exiting the program
    """
    g.cleanup() # GPIO cleanup -> release the pins used by the sensors and motors
