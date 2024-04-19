class MovementController:
    """
    Permet de contrôler les mouvements de la voiture
    """
    def __init__(self, direction, motor) -> None:
        self.direction = direction
        self.motor = motor
        self.speed = 0
        self.acceleration = 5

    def reset(self) -> None:
        """
        Redresse les roues et arrête le moteur
        """
        self.stop()
        self.stay_center()

    # Motor stuff
    def set_speed(self, new_speed: int) -> None:
        """
        Change la vitesse
        """
        res = min(max(0, new_speed), 100)
        self.speed = res

    def go_forward(self) -> None:
        """
        Change moteur pour aller vers avant
        """
        self.motor.move(self.speed)

    def go_backward(self) -> None:
        """
        Change moteur pour aller vers arrière
        """
        self.motor.move(self.speed, backward=True)

    def stop(self) -> None:
        """
        Arrête le moteur
        """
        self.motor.stop()

    def accelerate(self) -> None:
        """
        Augmente la vitesse
        """
        self.set_speed(self.speed - self.acceleration)

    def decelerate(self) -> None:
        """
        Réduis la vitesse
        """
        self.set_speed(self.speed - self.acceleration)

    # Direction stuff
    def stay_center(self) -> None:
        """
        Retourne au centre (duh)
        """
        self.direction.home()

    def turn_left(self, angle: int) -> None:
        """
        Tourne avec un angle vers la gauche
        """
        self.direction.turn_left(angle)

    def turn_right(self, angle: int) -> None:
        """
        Tourne avec un angle vers la droite
        """
        self.direction.turn_right(angle)

    def sharp_left(self) -> None:
        """
        Tourne à gauche fort
        """
        self.turn_left(45)

    def sharp_right(self) -> None:
        """
        Tourne à droite fort
        """
        self.turn_right(45)

    def medium_left(self) -> None:
        """
        Tourne à gauche moyen
        """
        self.turn_left(30)

    def medium_right(self) -> None:
        """
        Tourne à droite moyen
        """
        self.turn_right(30)

    def easy_left(self) -> None:
        """
        Tourne à gauche d'une miette
        """
        self.turn_left(15)

    def easy_right(self) -> None:
        """
        Tourne à droite d'une miette
        """
        self.turn_right(15)
