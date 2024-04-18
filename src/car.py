"""
'Samir you're breaking the car!'
- Vivek Ponnusamy

https://www.youtube.com/watch?v=D9-voINFkCg
"""
import time as t
from .controllers import MovementController, DistanceController, StateController
from .lib import exit_handler


class Car():
    """
    Objet voiture composé de contrôleurs et possédant des méthodes pour les modes : autonome et contrôlé
    """
    def __init__(self,
                 movement_controller: MovementController,
                 distance_controller: DistanceController,
                 state_controller: StateController
        ):

        self.__movement_controller = movement_controller
        self.__distance_controller = distance_controller
        self.__state_controller = state_controller

    @property
    def samir(self): # Appelle le pilote
        """
        Contrôleur de mouvement de la voiture
        """
        return self.__movement_controller
    
    @property
    def vivek(self): # Appelle le co-pilote
        """
        Contrôleur de distance de la voiture
        """
        return self.__distance_controller

    @property
    def state_controller(self):
        """
        Contrôleur d'état de la voiture dans la course
        """
        return self.__state_controller

    def __str__(self) -> str:
        return str(self.__dict__)

    def follow_right_wall(self, duration: float|int) -> None:
        """
        Fais avancer la voiture à une distance fixe d'un mur à droite durant durée déterminée
        """
        try:
            self.vivek.start()
            self.samir.stay_center()
            self.samir.speed = 30
            start_time = t.time()
            while t.time() - start_time < duration:
                if self.vivek.front_distance < 55:
                    self.samir.turn_left(10)
                elif self.vivek.right_distance < 8:
                    self.samir.turn_left(25)
                elif self.vivek.right_distance < 14:
                    self.samir.turn_left(10)
                elif self.vivek.right_distance > 24:
                    self.samir.turn_right(20)
                elif self.vivek.right_distance > 26:
                    self.samir.turn_right(30)
                else:
                    self.samir.stay_center()
        except:
           pass
        finally: 
            self.samir.reset()
            self.vivek.stop()

    def follow_left_wall(self, duration: float|int) -> None:
        """
        Fais avancer la voiture à une distance fixe d'un mur durant durée déterminée
        """
        try:
            self.vivek.start()
            self.samir.stay_center()
            self.samir.speed = 30
            start_time = t.time()
            while t.time() - start_time < duration:
                if self.vivek.front_distance < 55:
                    self.samir.turn_right(10)
                elif self.vivek.left_distance < 8:
                    self.samir.turn_right(25)
                elif self.vivek.left_distance < 14:
                    self.samir.turn_right(10)
                elif self.vivek.left_distance > 24:
                    self.samir.turn_left(20)
                elif self.vivek.right_distance > 26:
                    self.samir.turn_left(30)
                else:
                    self.samir.stay_center()
        except:
           pass
        finally: 
            self.samir.reset()
            self.vivek.stop()

    def avoid_object(self, duration: int = 10) -> None:
        """
        Fais avancer la voiture et évite les obstacles sur son chemin
        """
        self.vivek.start()
        self.samir.go_forward()
        start_time = t.time()
        while (t.time() - start_time) < duration:
            if self.vivek.front_distance < 15:
                self.samir.sharp_right()
            if self.vivek.left_distance < 15:
                a = True
                self.follow_left_wall(a)
            elif self.vivek.left_distance > 30:
                pass
            else:
                a = False
                self.samir.sharp_left()
        self.samir.stop()
        self.vivek.stop()

    def autonomous_mode(self) -> None:
        """
        Déplacement autonome : la voiture se déplace toute seule à l'aide des capteurs
        """
        self.vivek.start()
        self.state_controller.should_start_race()
        self.samir.speed = 50
        while self.state_controller.should_continue_race():
            self.samir.stay_center()
        self.samir.reset()

    def controlled_mode(self):
        """
        Déplacement contrôlé : l'utilisateur contrôle la voiture
        """
