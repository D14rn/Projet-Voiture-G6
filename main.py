from src.sensors import ColorSensor, DistanceSensor, LightSensor
from src.motors import Motor, Direction
from src.controllers import DistanceController, MovementController, StateController
from src import Car

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
colorSensor = ColorSensor("color sensor")
lightSensor = LightSensor("light sensor", 20)
state_controller = StateController(colorSensor, lightSensor, 2)

voiture = Car(movement_controller, distance_controller, state_controller)

menu = """ 
|------------------------------------------|
|----| Welcome to the car controller |-----|
|------------------------------------------|
|---------------[ menu ]-------------------|
|--&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&--|
|----- 1. Follow right wall ---------------|
|----- 2. Follow left wall ----------------|
|----- 3. Avoid object --------------------|
|----- 4. Get light sensor value ----------|
|------------------------------------------|
|--------| Press enter to exit |-----------|
|------------------------------------------|
"""

print(menu)
choice = input("Enter your choice: ")
if choice == "1":
    voiture.follow_right_wall(True)
if choice == "2":
    voiture.follow_left_wall(True)
if choice == "3":
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
if choice == "4":
    voiture.avoid_object()
if choice == "5":
    lightSensor.get_value()
