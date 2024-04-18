import RPi.GPIO as g, logging, time as t
from .sensor import Sensor


class LightSensor(Sensor):
    """
    Capteur de lumière -> utilisé pour détecter la ligne d'arrivée.

    lumière: 20 (in)
    """
    def __init__(self, name, pin):
        super().__init__(name)
        self.__pin = pin
        g.setmode(g.BCM)
        g.setup(pin, g.IN) # We only need to receive input

    @property
    def pin(self):
        return self.__pin

    def get_value(self) -> bool:
        """
        Renvoie la valeur de lumière (0/False: RGB, 1/True: black)
        """
        try:
            self._value = g.input(self.__pin)
            return self.value
        except Exception as e:
            logging.error(e)
