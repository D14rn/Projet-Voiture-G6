import time


class Car():
    """
    Objet voiture composé de contrôleurs et possédant des méthodes pour les modes : autonome et contrôlé
    """

    def __init__(self, movement_controller, distance_controller, state_controller):
        super().__init__()
        self.__movement_controller = movement_controller
        self.__distance_controller = distance_controller
        self.__state_controller = state_controller

    def __str__(self) -> str:
        return str(self.__dict__)

    def follow_wall(self):
        self.__distance_controller.start()
        while self.__distance_controller.front_distance < 10:
            if self.__distance_controller.front_distance < 15:
                self.__movement_controller.go_backward()
                time.sleep(0.5)
                self.__movement_controller.stop()
                break

            if self.__distance_controller.right_distance > 20:
                self.__movement_controller.turn_right()
                time.sleep(0.3)
                self.__movement_controller.reset_direction()

            if self.__distance_controller.right_distance < 15:
                self.__movement_controller.turn_left()
                time.sleep(0.3)
                self.__movement_controller.reset_direction()

    def avoid_object(self):
        self.__distance_controller.start()
        while True:
            if self.__distance_controller.front_distance() < 50:
                start_time = time.time()
                while (time.time() - start_time) < 4:
                    gauche = self.__distance_controller.left_distance()
                    droite = self.__distance_controller.right_distance()
                    if gauche > droite:
                        self.__movement_controller.turn_left()
                        time.sleep(0.4)
                        self.__movement_controller.reset_direction()
                    else:
                        self.__movement_controller.turn_right()
                        time.sleep(0.4)
                        self.__movement_controller.reset_direction()

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
