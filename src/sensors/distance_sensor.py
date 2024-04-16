import time as t, logging, RPi.GPIO as g
from .sensor import Sensor


class DistanceSensor(Sensor):
    """
    Capteur à ultrason HC-SR04 pour mesurer la distance avec les obstacles
    """
    def __init__(self, name, trigger_pin, echo_pin):
        super().__init__(name)
        self.__trigger_pin = trigger_pin
        self.__echo_pin = echo_pin
        self.__pulse_interval = 0.00001 # 10 µs
        g.setmode(g.BCM)
        g.setup(self.__trigger_pin, g.OUT)
        g.setup(self.__echo_pin, g.IN)

    def get_value(self) -> float:
        """
        Donne la distance (en cm) entre le capteur et l'objet le plus proche
        """
        try:
            g.output(self.__trigger_pin, True)  # Send signal
            t.sleep(self.__pulse_interval)      # Signal duration
            g.output(self.__trigger_pin, False) # Stop sending

            start_time = t.time()
            stop_time = t.time()

            # Save start_time
            while g.input(self.__echo_pin) == 0: # Wait until signal is received
                start_time = t.time()

            # Save time of arrival
            while g.input(self.__echo_pin) == 1: # Wait entire response
                stop_time = t.time()

            duration = stop_time - start_time 

            # Multiply by speed of sound (34300 cm/s)
            # Divide by 2 because it needs to travel back
            self._value = (duration * 34300) / 2 
            return self.value
        except Exception as e:
            logging.error(e)
            g.cleanup()
