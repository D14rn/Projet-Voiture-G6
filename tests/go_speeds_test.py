import time
from src.motors import Motor
from src.motors import Direction
from src.lib import exit_handler


speed = 30

def go_speeds(motor: Motor, direction: Direction):
    direction.home()
    
    for _ in range(1, 3):
        motor.move(speed)
        speed += 30
        time.sleep(1.5)

    for _ in range(1, 3):
        motor.move(speed)
        speed -= 30
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
