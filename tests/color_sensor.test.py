import unittest
from src.color_sensor import ColorSensor
import time


class ColorSensorTest(unittest.TestCase):

    @staticmethod
    def test_getValue():
        color_sensor = ColorSensor("Color sensor", 5)
        for i in range(30):
            print(color_sensor.get_value())
            time.sleep(0.5)

    @staticmethod
    def test_isGreen():
        color_sensor = ColorSensor("Color sensor", 5)
        for i in range(30):
            print(color_sensor.is_green())
            time.sleep(0.5)


if __name__ == "__main__":
    unittest.main()
