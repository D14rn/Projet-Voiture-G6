import unittest, time
from src.lib import exit_handler
from src.sensors import DistanceSensor


class DistanceSensorTest(unittest.TestCase):
    def setUp(self) -> None:
        front_sensor = DistanceSensor("front sensor", 6, 5)
        left_sensor = DistanceSensor("left sensor", 11, 9)
        right_sensor = DistanceSensor("right sensor", 26, 19)
        self.sensors = [front_sensor, left_sensor, right_sensor]

    def tearDown(self):
       del self.sensors

    def test_attributes_front_sensor(self):
        for sensor in self.sensors:
            self.assertIsNotNone(sensor)
            self.assertIsInstance(self.sensor, DistanceSensor)

    def test_get_value(self):
        correct_values = [i for i in range(0, 100)]
        for sensor in self.sensors:
            print(f'--- Testing {sensor.s_name} ----')
            for _ in range(10):
                value = sensor.get_value()
                self.assertIn(value, correct_values)
                time.sleep(1)

if __name__ == "__main__":
    unittest.main()
