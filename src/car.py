'''
"Samir you're breaking the car!"
- Vivek Ponnusamy


https://www.youtube.com/watch?v=D9-voINFkCg
'''

import time as t
from .controllers import MovementController, DistanceController, StateController


class Car():
    """
    Objet voiture composé de contrôleurs et possédant des méthodes pour les modes : autonome et contrôlé
    """
    def __init__(self,
                 movement_controller: MovementController,
                 distance_controller: DistanceController,
                 state_controller: StateController,
                 speed: int = 30
        ):
        self.samir = movement_controller
        self.vivek = distance_controller
        self.jarvis = state_controller
        self.speed = speed
        self.back_it_up_treshold = 12
        self.min_front_dist = 6
        self.current_wall = "right"

    def avoid_object(self, duration: int = 10) -> None:
        """
        Fais avancer la voiture et évite les obstacles sur son chemin
        """
        self.vivek.start()
        self.samir.stay_center()
        self.samir.set_speed(self.speed)
        start_time = t.time()
        while (t.time() - start_time) < duration:
            if self.vivek.front_distance < 40:
                # Avoid obstacle
                self.samir.medium_left()
                t.sleep(0.6)
                self.samir.stay_center()
                t.sleep(3)

                # Get back on track
                self.samir.medium_right()
                t.sleep(1.2)
                self.samir.stay_center()
                t.sleep(3)
                self.samir.medium_left()
                t.sleep(0.6)

                # Keep going
                self.samir.stay_center()
                t.sleep(2)
                break
        self.samir.reset()
        self.vivek.stop()

    def emergency_mode(self):
        self.race_mode(wait_for_green=False)
    
    def programmable_autonomous_mode(self, wait_for_green=True):
        target_distance = int(input("Distance: "))
        distance_margin = int(input("Margin: "))
        correction_angle = int(input("Angle: "))
        speed = int(input("Speed: "))
        self.autonomous_mode(target_distance, distance_margin, correction_angle, speed, wait_for_green)

    def race_mode(self):
        target_distance = 20
        distance_margin = 1
        correction_angle = 20
        speed = 30
        self.autonomous_mode(target_distance, distance_margin, correction_angle, speed)
        if self.vivek.left_distance > self.vivek.right_distance:
            self.current_wall = "left"

    def autonomous_mode(self, target_distance, distance_margin, correction_angle, speed, wait_for_green=True):
        """
        Déplacement autonome : la voiture se déplace toute seule à l'aide des capteurs
        """
        self.samir.set_speed(speed)
        self.vivek.start()
        self.jarvis.start()
        self.samir.reset()
        if wait_for_green == True:
            self.jarvis.waiting_for_greenlight()
        while self.jarvis.should_continue_race():
            self.racing_strategy(distance_margin, target_distance, correction_angle)
        self.samir.reset()
        self.vivek.stop()
        self.jarvis.stop()

    def racing_strategy(self, 
                        distance_margin, 
                        target_distance, 
                        correction_angle,
                        ) -> None:
        max_distance = target_distance * 1.75
        stick_distance = target_distance * 1.25
        if (not self.current_wall == "left") and ((self.vivek.left_distance < stick_distance) and (self.vivek.right_distance > max_distance)):
            self.current_wall = "left"
            print("changing to left")
        elif (not self.current_wall == "right") and ((self.vivek.right_distance < stick_distance) and (self.vivek.left_distance > max_distance)):
            self.current_wall = "right"
            print("changing to right")
        if self.current_wall == "right":
            self.race_follow_right(target_distance, distance_margin, correction_angle)
        else:
            self.race_follow_left(target_distance, distance_margin, correction_angle)
        self.samir.go_forward()
    
    def race_follow_right(self, target_distance, margin, angle):
        distance = self.vivek.right_distance
        if (self.vivek.front_distance < self.min_front_dist):
            self.back_it_up()
        if (distance < target_distance * 0.5):
            self.samir.turn_left(40)
        elif (distance < target_distance - margin):
            self.samir.turn_left(angle)
        elif (distance > target_distance * 1.5):
            self.samir.turn_right(40)
        elif (distance > target_distance + margin):
            self.samir.turn_right(angle)
        else:
            self.samir.stay_center()
    
    def race_follow_left(self, target_distance, margin, angle):
        distance = self.vivek.left_distance
        if (self.vivek.front_distance < self.min_front_dist):
            self.back_it_up()
        if (distance < target_distance * 0.5):
            self.samir.turn_right(40)
        elif (distance < target_distance - margin):
            self.samir.turn_right(angle)
        elif (distance > target_distance * 1.5):
            self.samir.turn_left(40)
        elif (distance > target_distance + margin):
            self.samir.turn_left(angle)
        else:
            self.samir.stay_center()

    def back_it_up(self) -> None:
        """
        Essaie de remettre la voiture
        """
        turn = ""
        while self.vivek.front_distance < self.back_it_up_treshold:
            if self.vivek.left_distance > self.vivek.right_distance:
                self.samir.medium_right()
                turn = "right"
            else:
                self.samir.medium_left()
                turn = "left"
            self.samir.go_backward()
        t.sleep(0.3)
        if turn == "right":
           self.samir.sharp_left()
        else:
            self.samir.sharp_right()
        self.samir.go_forward()
        t.sleep(0.6)
        self.samir.stay_center()

    def controlled_mode(self):
        """
        Déplacement contrôlé : l'utilisateur contrôle la voiture
        Z/S => accelerate/decelerate
        Q/D => easy_left/easy_right
        SPACE/P => stay_center/stop motor
        """
        actions = {
            "z": self.samir.accelerate,
            "s": self.samir.decelerate,
            "q": self.samir.easy_left,
            "d": self.samir.easy_right,
            " ": self.samir.stay_center,
            "p": self.samir.stop
        }
        print("Enter action (Z/S | Q/D | SPACE/P)")
        while self.jarvis.should_continue_race():
            action = input().lower()
            try:
                actions[action]()
            except:
                pass
