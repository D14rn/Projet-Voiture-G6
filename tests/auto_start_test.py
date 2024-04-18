import time as t

from src.sensors import ColorSensor, DistanceSensor, LightSensor
from src.motors import Motor, Direction
from src.controllers import DistanceController, MovementController, StateController

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
state_controller = StateController(light_sensor, color_sensor, lap_count=3)


def auto_start() -> None:
    state_controller.start()
    state_controller.should_start_race()
    movement_controller.stay_center()
    movement_controller.speed = 50
    t.sleep(3)
    movement_controller.reset()
    state_controller.stop()


if __name__ == '__main__':
    auto_start()
