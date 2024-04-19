from src.controllers import DistanceController, MovementController, StateController
from src import Car
from src.lib import *


voiture = Car(create_movement_controller(), create_distance_controller(), create_state_controller(), speed=30)

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
            voiture.follow_right_wall()
        case "2":
            voiture.follow_left_wall()
        case "3":
            voiture.controlled_mode()
        case "4":
            voiture.avoid_object()
        case "5":
            voiture.autonomous_mode()
