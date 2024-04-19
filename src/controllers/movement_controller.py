class MovementController:
    """
    Permet de contrôler les mouvements de la voiture
    """
    def __init__(self, direction, motor, max_speed=70) -> None:
        self.__direction = direction
        self.__motor = motor
        self.__max_speed = max_speed
        self.__speed = 0
        self.__acceleration = 5

    @property
    def max_speed(self) -> int:
        return self.__max_speed

    @property
    def speed(self) -> int:
        return self.__speed

    @speed.setter
    def speed(self, new_speed: int) -> None:
        res = min(max(-100, new_speed), 100)
        self.__speed = res
        if res >= 0:
            self.go_forward()
        else:
            self.go_backward()

    def go_forward(self) -> None:
        self.__motor.move(self.__speed)

    def go_backward(self) -> None:
        print("going backward")
        self.__motor.move(-self.__speed, backward=True)

    def turn_left(self, angle: int) -> None:
        self.__direction.turn_left(angle)

    def turn_right(self, angle: int) -> None:
        self.__direction.turn_right(angle)

    def sharp_left(self) -> None:
        """
        Tourne à gauche fort
        """
        self.turn_left(45)

    def medium_left(self) -> None:
        """
        Tourne à gauche moyen
        """
        self.turn_left(30)

    def easy_left(self) -> None:
        """
        Tourne à gauche d'une miette
        """
        self.turn_left(15)

    def sharp_right(self) -> None:
        """
        Tourne à droite fort
        """
        self.turn_right(45)

    def medium_right(self) -> None:
        """
        Tourne à droite moyen
        """
        self.turn_right(30)

    def easy_right(self) -> None:
        """
        Tourne à droite d'une miette
        """
        self.turn_right(15)
    
    def stay_center(self) -> None:
        """
        Retourne au centre (duh)
        """
        self.__direction.home()

    def stop(self) -> None:
        self.__motor.stop()

    def accelerate(self) -> None:
        self.__speed += self.__acceleration
    
    def decelerate(self) -> None:
        self.__speed -= self.__acceleration
    
    def reset(self) -> None:
        self.stop()
        self.stay_center()
