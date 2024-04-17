"""
'Samir you're breaking the car!'
- Vivek Ponnusamy

https://www.youtube.com/watch?v=D9-voINFkCg
"""
import time as t


class Car():
    """
    Objet voiture composé de contrôleurs et possédant des méthodes pour les modes : autonome et contrôlé
    """
    def __init__(self, movement_controller, distance_controller, state_controller):
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

    def __str__(self) -> str:
        return str(self.__dict__)

    def follow_right_wall(self, duration: int = 10) -> None:
        """
        Fais avancer la voiture à une distance fixe d'un mur durant durée déterminée
        """
        self.vivek.start()
        self.samir.go_forward()
        start_time = t.time()
        while (t.time() - start_time) < duration:
            if self.vivek.right_distance > 22:
                self.samir.easy_right()
            elif self.vivek.right_distance < 17:
                self.samir.easy_left()
            else:
                self.samir.stay_center()
        self.samir.stop()
        self.vivek.stop()

    def avoid_object(self):
        self.__distance_controller.start()
        while True:
            if self.__distance_controller.front_distance() < 50:
                start_time = t.time()
                while (t.time() - start_time) < 4:
                    gauche = self.__distance_controller.left_distance()
                    droite = self.__distance_controller.right_distance()
                    if gauche > droite:
                        self.samir.turn_left()
                        t.sleep(0.4)
                        self.samir.reset_direction()
                    else:
                        self.samir.turn_right()
                        t.sleep(0.4)
                        self.samir.reset_direction()

    def autonomous_mode(self) -> None:
        """
        Déplacement autonome : la voiture se déplace toute seule à l'aide des capteurs
        """
        # Implement the autonomous mode here
        pass

    def controlled_mode(self) -> None:
        """
        Déplacement contrôlé : l'utilisateur contrôle la voiture
        """
        # Implement here the controlled mode
        pass
