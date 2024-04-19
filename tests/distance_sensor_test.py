import unittest, time
from src.lib import *
from src.sensors import DistanceSensor


class DistanceSensorTest(unittest.TestCase):
    def setUp(self) -> None:
        self.sensors = [*create_ds()]

    def tearDown(self):
       del self.sensors

    def test_attributes_front_sensor(self):
        for sensor in self.sensors:
            self.assertIsNotNone(sensor)
            self.assertIsInstance(sensor, DistanceSensor)

    def test_get_value(self):
        for sensor in self.sensors:
            print(f'--- Testing {sensor.s_name} ----')
            for _ in range(10):
                value = sensor.get_value()
                print(f"Distance: {round(value, 2)}cm")
                self.assertTrue(value > 0 and value < 300)
                time.sleep(1)

if __name__ == "__main__":
    unittest.main()
