from src.sensors import ColorSensor, DistanceSensor, LightSensor
from src.motors import Motor, Direction
from src.controllers import DistanceController, MovementController, StateController
from src import Car
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
state_controller = StateController(color_sensor, light_sensor, lap_count=3)

voiture = Car(movement_controller, distance_controller, state_controller)


if __name__ == '__main__':
    voiture.follow_right_wall(6)
