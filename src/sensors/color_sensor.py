import board, adafruit_tcs34725, logging
from .sensor import Sensor


class ColorSensor(Sensor):
    """
    Capteur couleur (RGB) utilisant le capteur TCS34725 pour détecter si la couleur est verte
    """
    def __init__(self, s_name, gain=4):
        super().__init__(s_name)
        self.__sensor = adafruit_tcs34725.TCS34725(board.I2C())
        self.__sensor.gain = gain # can be 1, 4, 16, 60

    @property
    def sensor(self):
        return self.__sensor

    def get_value(self) -> tuple:
        """
        Renvoie un tuple des valeurs rgb (r, g, b) du capteur 
        """
        try:
            self._value = self.__sensor.color_rgb_bytes
            return self.value
        except Exception as e:
            logging.error(e)

    def is_green(self) -> bool:
        """
        Vérifie si la couleur est verte (renvoie True si c'est le cas)
        """
        red, green, blue = self.get_value()
        if (green > 2 * red and green > 2 * blue):
            return True
        else:
            return False
