import RPi.GPIO as g, logging, time as t
from .sensor import Sensor


class LightSensor(Sensor):
    """
    Capteur de lumière -> utilisé pour détecter la ligne d'arrivée.

    lumière: 20 (in)
    """
    def __init__(self, name: str, pin: int) -> None:
        super().__init__(name, polling_interval=0.4) # 0.4 because thiccc line
        self.pin = pin
        g.setmode(g.BCM)
        g.setup(pin, g.IN) # We only need to receive input

    def get_value(self) -> bool:
        """
        Renvoie la valeur de lumière (0/False: RGB, 1/True: black)
        """
        try:
            self.value = g.input(self.pin)
            return self.value
        except Exception as e:
            logging.error(e)
