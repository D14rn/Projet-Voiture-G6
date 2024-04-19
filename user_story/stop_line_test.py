import time as t

from src.sensors import ColorSensor, DistanceSensor, LightSensor
from src.motors import Motor, Direction
from src.controllers import DistanceController, MovementController, StateController
from src.lib import exit_handler

# Instantiate the distance sensors
front_sensor = DistanceSensor("front sensor", 6, 5)
left_sensor = DistanceSensor("left sensor", 11, 9)
right_sensor = DistanceSensor("right sensor", 26, 19)
distance_controller = DistanceController(front_sensor, left_sensor, right_sensor)

# Instantiate the motors
motor = Motor(17, 18, 27, 22, 4, 5)
direction = Direction()
movement_controller = MovementController(direction, motor, 50)

# Instantiate the state sensors
color_sensor = ColorSensor("color sensor")
light_sensor = LightSensor("light sensor", 20)
state_controller = StateController(light_sensor, color_sensor, lap_count=0)


def stop_line() -> None:
    state_controller.start()
    movement_controller.stay_center()
    movement_controller.speed = 50
    while state_controller.should_continue_race():
        pass
    t.sleep(0.65)
    movement_controller.reset()
    state_controller.stop()


if __name__ == '__main__':
    stop_line()
