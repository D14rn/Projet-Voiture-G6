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
state_controller = StateController(light_sensor, color_sensor, lap_count=3)

voiture = Car(movement_controller, distance_controller, state_controller)

menu = """ 
|------------------------------------------|
|----| Welcome to the car controller |-----|
|------------------------------------------|
|---------------[ menu ]-------------------|
|--------- 1. Follow right wall -----------|
|--------- 2. Follow left wall ------------|
|--------- 3. Control mode ----------------|
|--------- 4. Avoid object ----------------|
|--------- 5. Auto mode -------------------|
|------------------------------------------|
|--------| Press enter to exit |-----------|
|------------------------------------------|
"""

if __name__ == '__main__':
    print(menu)
    choice = input("Enter your choice: ")
    match choice:
        case "1":
            duration = int(input("Enter the duration of test: "))
            voiture.follow_right_wall(duration)
        case "2":
            duration = int(input("Enter the duration of test: "))
            voiture.follow_left_wall(duration)
        case "3":
            print(""" ________________________
                    |                        |
                    |        Controls        |
                    |------------------------|
                    |  z: go forward         |
                    |  s: go backward        |
                    |  q: turn left          |
                    |  d: turn right         |
                    |________________________|
                    """)
            voiture.controlled_mode()
        case "4":
            voiture.avoid_object()
        case "5":
            voiture.autonomous_mode()
