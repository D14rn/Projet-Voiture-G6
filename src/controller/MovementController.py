class MovementController:
    """
    Permet de contrôler les mouvements de la voiture
    """

    def __init__(self, direction, motor) -> None:
        self.__direction = direction
        self.__motor = motor

    def go_forward(self) -> None:
        self.__motor.move(50)

    def go_backward(self) -> None:
        self.__motor.move(-50, backward=True)

    def turn_left(self) -> None:
        self.__direction.turn_left(45)
        self.go_forward()

    def turn_right(self) -> None:
        self.__direction.turn_right(45)
        self.go_forward()

    def stop(self) -> None:
        self.__motor.stop()
        self.__direction.home()
