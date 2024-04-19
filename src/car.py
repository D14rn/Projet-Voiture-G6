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

    def _follow_right_wall_simple(self, target_distance, margin, correction_angle):
        distance = self.vivek.right_distance
        if (distance < target_distance - margin):
            self.samir.turn_left(correction_angle)
        elif (distance > target_distance + margin):
            self.samir.turn_right(correction_angle)
        else:
            self.samir.stay_center()

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

    def autonomous_mode(self):
        """
        Déplacement autonome : la voiture se déplace toute seule à l'aide des capteurs
        """
        self.vivek.start()
        self.jarvis.start()
        self.jarvis.waiting_for_greenlight()
        distance_margin = 2
        target_distance = 20
        correction_angle = 10
        while self.jarvis.should_continue_race():
            self.racing_strategy(distance_margin, target_distance)
        self.samir.reset()
        self.vivek.stop()
        self.jarvis.stop()

    def racing_strategy(self, 
                        distance_margin, 
                        target_distance, 
                        correction_angle,
                        max_front_distance
                        ) -> None:
        distance = self.vivek.right_distance
        if (distance < target_distance - distance_margin):
            self.samir.turn_left(correction_angle)
        elif (distance > target_distance + distance_margin):
            self.samir.turn_right(correction_angle)
        else:
            self.samir.stay_center()

    def back_it_up(self) -> None:
        """
        Fais reculer la voiture
        """
        self.samir.turn_left(45)
        self.samir.set_speed

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
