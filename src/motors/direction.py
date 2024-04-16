import time as t
from pwm_driver import PWM


class Direction:
    """
    Représente le servo moteur qui permet de tourner les roues avant
    """
    def __init__(self):
        self.__pwm = PWM() 
        self.__pwm.frequency = 50 # Fréquence de 50 Hz
        self.__wait_time = 0.5 # Temps d'attente pour que le servo ait le temps de tourner
        self.__min = 360 # borne gauche
        self.__max = 550 # borne droite
    
    def _calc_angle(self, angle) -> int:
        angle = max(-45, min(45, angle))  # angle entre [-45, 45]
        angle = self.__min + ((angle) / 90.0) * (self.__max - self.__min)
        print(angle)
        return int(angle)
    
    def turn_left(self, angle) -> None:
        """
        Donne un signal PWN au servo pour tourner à gauche
        """
        print('turning left')
        self.__pwm.write(0, 0, self._calc_angle(-angle))
        t.sleep(self.__wait_time)

    def turn_right(self, angle) -> None:
        """
        Donne un signal PWN au servo pour tourner à droite
        """
        print('turning right')
        self.__pwm.write(0, 0, self._calc_angle(angle))
        t.sleep(self.__wait_time)
    
    def home(self) -> None:
        """
        Donne un signal PWN au servo pour retourner à sa position de base (pour aller droit)
        """
        print('going home')
        self.__pwm.write(0, 0, self._calc_angle(0))
        t.sleep(self.__wait_time)
