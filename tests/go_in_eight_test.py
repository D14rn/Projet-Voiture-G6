import time
from src.motors import Motor
from src.motors import Direction
from src.lib import exit_handler


_SPEED = 60
_MOVEMENT_DURATION = 4.5

def circle_right(motor: Motor, direction: Direction):
    direction.turn_right(45)
    motor.move(_SPEED)
    time.sleep(_MOVEMENT_DURATION)
    motor.stop()
    direction.home()

def circle_left(motor: Motor, direction: Direction):
    direction.turn_left(45)
    motor.move(_SPEED)
    time.sleep(_MOVEMENT_DURATION)
    motor.stop()
    direction.home()

def continue_a_bit(motor: Motor, direction: Direction):
    direction.home()
    motor.move(_SPEED)
    motor.stop()

def go_in_a_eight(motor: Motor, direction: Direction):
    circle_right(motor, direction)
    continue_a_bit(motor, direction)
    circle_left(motor, direction)


if __name__ == "__main__":
    test_motor = Motor(
        17, 18,
        27, 22,
        4, 5
    )

    test_direction = Direction()

    go_in_a_eight(test_motor, test_direction)
