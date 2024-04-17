from threading import Thread

class MovementController(Thread):
    """
    Permet de contrôler les mouvements de la voiture
    """
    def __init__(self, direction, motor, speed=50) -> None:
        Thread.__init__(self)
        self.__direction = direction
        self.__motor = motor
        self.__speed = speed

    def go_forward(self) -> None:
        self.__motor.move(self.__speed)
    
    def change_speed(self, new_speed):
        res = min(max(0, new_speed), 100)
        self.__speed = res

    def go_backward(self) -> None:
        self.__motor.move(-self.__speed, backward=True)

    def sharp_left(self) -> None:
        """
        Tourne à gauche fort
        """
        self.__direction.turn_left(45)

    def medium_left(self) -> None:
        """
        Tourne à gauche moyen
        """
        self.__direction.turn_left(30)

    def easy_left(self) -> None:
        """
        Tourne à gauche d'une miette
        """
        self.__direction.turn_left(15)

    def sharp_right(self) -> None:
        """
        Tourne à droite fort
        """
        self.__direction.turn_right(45)

    def medium_right(self) -> None:
        """
        Tourne à droite moyen
        """
        self.__direction.turn_left(30)

    def easy_right(self) -> None:
        """
        Tourne à droite d'une miette
        """
        self.__direction.turn_left(15)
    
    def stay_center(self):
        """
        Retourne au centre (duh)
        """
        self.__direction.home()

    def stop(self) -> None:
        self.__motor.stop()

    def accelerate(self):
        self.__speed += 10
        self.__motor.move()
    
    def reset(self):
        self.stop()
        self.reset_direction()

    def run(self) -> None:
        pass
