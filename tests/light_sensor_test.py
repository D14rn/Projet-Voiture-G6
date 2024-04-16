import unittest
import time
from src.sensors import LightSensor


class LightSensorTest(unittest.TestCase):
    def test_get_value(self):
        test_sensor = LightSensor("test light sensor", 20)
        correct_values = (0, 1)
        test_value = test_sensor.get_value()
        self.assertTrue(test_value in correct_values)

def test_long_lightsensor_get_value():
    light_sensor = LightSensor("test light sensor", 20)
    for _ in range (10):
        print(light_sensor.get_value())
        time.sleep(0.5)


if __name__ == "__main__":
    unittest.main()
    test_long_lightsensor_get_value()
