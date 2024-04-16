import unittest
import time
from src.sensors import ColorSensor
from src.lib import exit_handler


class ColorSensorTest(unittest.TestCase):
    def test_getValue(self):
        color_sensor = ColorSensor("Color sensor", 4)
        rgb_value = color_sensor.get_value()
        self.assertIsInstance(rgb_value, tuple)
        self.assertEqual(len(rgb_value), 3)

    def test_isGreen(self):
        color_sensor = ColorSensor("Color sensor", 4)
        res = color_sensor.is_green()
        self.assertIsInstance(res, bool)

def test_long_get_value():
    color_sensor = ColorSensor("Color sensor", 16)
    print("Testing the color sensor value: rgb tuple")
    for _ in range(10):
        print(color_sensor.get_value())
        time.sleep(0.5)

def test_long_is_green():
    color_sensor = ColorSensor("Color sensor", 16)
    print("Testing green color, try putting some green stuff in front!")
    for _ in range(10):
        print(color_sensor.is_green())
        time.sleep(0.5)


if __name__ == "__main__":
    test_long_get_value()
    test_long_is_green()
    unittest.main()
