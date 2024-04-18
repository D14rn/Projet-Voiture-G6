from sensors import ColorSensor, DistanceSensor, LightSensor
from motors import Motor,Direction
from controllers import DistanceController, MovementController, StateController
from car import Car

front_sensor = DistanceSensor("front sensor", 6, 5)
left_sensor = DistanceSensor("left sensor", 11, 9)
right_sensor = DistanceSensor("right sensor", 26, 19)
distance_controller = DistanceController(front_sensor, left_sensor, right_sensor)

motor = Motor(17,18,27,22,4,5)
direction = Direction()
movement_controller = MovementController(motor, direction)

colorSensor = ColorSensor("color sensor")
lightSensor = LightSensor("light sensor")
state_controller = StateController(colorSensor, lightSensor,2)

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
while True:
    print(menu)
    choice = input("Enter your choice: ")
    if choice == "1":
        voiture.follow_right_wall(True)
    if choice == "2":
        voiture.follow_left_wall(True)
    if choice == "3":
        voiture.avoid_object()
    if choice == "4":
        lightSensor.get_value()
    else:
        break

