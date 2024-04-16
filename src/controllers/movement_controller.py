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
    
    def change_speed(self, new_speed):
        res = min(max(0, new_speed), 100)
        self.__speed = res

    def go_backward(self) -> None:
        self.__motor.move(-self.__speed, backward=True)

    def turn_left(self) -> None:
        self.__direction.turn_left(45)

    def turn_right(self) -> None:
        self.__direction.turn_right(45)
    
    def reset_direction(self):
        self.__direction.home()

    def stop(self) -> None:
        self.__motor.stop()

    def accelerate(self):
        self.__speed += 10
        self.__motor.move()
    
    def reset(self):
        self.stop()
        self.reset_direction()
