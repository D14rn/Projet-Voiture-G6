import board, adafruit_tcs34725, logging
from sensor import Sensor


class ColorSensor(Sensor):
    """
    Capteur couleur (RGB) utilisant le capteur TCS34725 pour détecter si la couleur est verte
    """
    def __init__(self, name, pin):
        super().__init__(name)
        self.__pin = pin
        self.__sensor = adafruit_tcs34725.TCS34725(board.I2C())

    def get_value(self) -> tuple:
        """
        Renvoie un tuple des valeurs rgb (r, g, b) du capteur 
        """
        try:
            self._value = self.__sensor.color_rgb_bytes()
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
