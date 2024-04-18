import time
from src.motors import Motor
from src.motors import Direction
from src.lib import exit_handler


_SPEED = 30

def go_30_cm(motor: Motor, direction: Direction):
    direction.home()
    motor.move(_SPEED)
    time.sleep(1.5)
    motor.stop()


if __name__ == "__main__":
    test_motor = Motor(
        17, 18,
        27, 22,
        4, 5
    )

    test_direction = Direction()
    go_30_cm(test_motor, test_direction)
