import time
from src.motors import Motor
from src.motors import Direction
from src.controllers import MovementController
from src.lib import exit_handler


def forward_procedure(movement_controller: MovementController, start_speed, end_speed, speed_increment, acceleration_delay):
    for speed in range(start_speed, end_speed, speed_increment):
        movement_controller.go_forward(speed)
        time.sleep(acceleration_delay)
    
    for speed in range(end_speed, start_speed, -speed_increment):
        movement_controller.go_forward(speed)
        time.sleep(acceleration_delay)

    movement_controller.stop()


def backward_procedure(movement_controller: MovementController, start_speed, end_speed, speed_increment, acceleration_delay):
    for speed in range(start_speed, end_speed, speed_increment):
        movement_controller.go_backward(speed)
        time.sleep(acceleration_delay)
    
    for speed in range(end_speed, start_speed, -speed_increment):
        movement_controller.go_backward(speed)
        time.sleep(acceleration_delay)

    movement_controller.stop()


def run_forest_run(movement_controller: MovementController):
    start_speed = 10
    max_speed = 100
    speed_increment = 20
    acceleration_delay = 0.25
    movement_controller.reset_direction()

    forward_procedure(movement_controller, start_speed, max_speed, speed_increment, acceleration_delay)
    backward_procedure(movement_controller, start_speed, max_speed, speed_increment, acceleration_delay)
    movement_controller.reset()


if __name__ == "__main__":
    test_motor = Motor(
        17, 18,
        27, 22,
        4, 5
    )

    test_direction = Direction()
    test_movement_controller = MovementController(motor=test_motor, direction=test_direction)
    run_forest_run(test_motor, test_direction)
