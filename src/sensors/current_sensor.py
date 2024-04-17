from .sensor import Sensor
import board, logging
from adafruit_ina219 import ADCResolution, BusVoltageRange, INA219


class CurrentSensor(Sensor):
    """
    Capteur de courant -> utilisé pour mesurer la consommation électrique du robot
    """

    def __init__(self, name):
        super().__init__(name)
        self.__ina = INA219(board.I2C())


    def get_value(self):
        """
        Renvoie la valeur de courant (en mA) consommée par le robot
        """
        try:
            self._value = self.__ina.current
            return self.value
        except Exception as e:
            logging.error(e)
