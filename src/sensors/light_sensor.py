import RPi.GPIO as g, logging, time as t
from sensor import Sensor


class LightSensor(Sensor):
    """
    Capteur de lumière -> utilisé pour détecter la ligne d'arrivée.
    """
    def __init__(self, name, pin):
        super().__init__(name)
        self.__pin = pin
        g.setmode(g.BOARD) # Set pin numbering to BOARD numbering (could also be g.BCM but doesnt work with the diagram)
        g.setup(pin, g.IN) # Set pin in receiving mode

    def get_value(self) -> bool:
        """
        Renvoie la valeur de lumière (0/False: RGB, 1/True: black)
        """
        try:
            self._value =  g.input(self.__pin)
            return self.value
        except Exception as e:
            logging.error(e)
