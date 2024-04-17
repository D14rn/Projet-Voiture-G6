import time
from src.motors import Motor
from src.motors import Direction
from src.lib import exit_handler


_SPEED = 30

def go_speeds(motor: Motor, direction: Direction):
    if input("press f for forward, b for backward: ") == 'f':
        _BACKWARD = False
    else:
        _BACKWARD = True
    direction.home()
    
    for i in range(1, 6):
        motor.move(_SPEED, _BACKWARD)
        _SPEED += 10
        time.sleep(1.5)

    for i in range(1, 6):
        motor.move(_SPEED, _BACKWARD)
        _SPEED -= 10
        time.sleep(1.5)
    
    motor.stop()


if __name__ == "__main__":
    test_motor = Motor(
        17, 18,
        27, 22,
        4, 5
    )

    test_direction = Direction()
    go_speeds(test_motor, test_direction)
