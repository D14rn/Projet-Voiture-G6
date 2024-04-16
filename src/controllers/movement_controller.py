class MovementController:
    """
    Permet de contrôler les mouvements de la voiture
    """
    def __init__(self, direction, motor, speed=50) -> None:
        self.__direction = direction
        self.__motor = motor
        self.__speed = speed

    def go_forward(self) -> None:
        self.__motor.move(self.__speed)

    def go_backward(self) -> None:
        self.__motor.move(-self.__speed, backward=True)

    def turn_left(self) -> None:
        self.__direction.turn_left(45)

    def turn_right(self) -> None:
        self.__direction.turn_right(45)

    def stop(self) -> None:
        self.__motor.stop()
        self.__direction.home()
