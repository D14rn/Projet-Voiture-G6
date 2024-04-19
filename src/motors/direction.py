from .pwm_driver import PWM


class Direction:
    """
    Représente le servo moteur qui permet de tourner les roues avant
    """
    def __init__(self):
        self.pwm = PWM() 
        self.pwm.frequency = 50 # Fréquence de 50 Hz
        self.min = 360 # borne gauche
        self.max = 550 # borne droite
    
    def _calc_angle(self, angle) -> int:
        angle = max(-45, min(45, angle))  # angle entre [-45, 45]
        angle = self.min + ((angle) / 90.0) * (self.max - self.min) # conversion de l'angle en signal PWM
        return int(angle)

    def turn(self, angle):
        """
        Donne un signal PWN au servo pour tourner
        """
        self.pwm.write(0, 0, self._calc_angle(angle))

    def home(self) -> None:
        """
        Donne un signal PWN au servo pour retourner à sa position de base (pour aller droit)
        """
        self.turn(0)

    def turn_left(self, angle) -> None:
        """
        Donne un signal PWN au servo pour tourner à gauche
        """
        self.turn(-angle)

    def turn_right(self, angle) -> None:
        """
        Donne un signal PWN au servo pour tourner à droite
        """
        self.turn(angle)
