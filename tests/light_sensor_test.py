import unittest, time
from src.lib import exit_handler
from src.sensors import LightSensor


class LightSensorTest(unittest.TestCase):
    def setUp(self) -> None:
        self.sensor = LightSensor("Light sensor", 20)

    def tearDown(self):
       del self.sensor

    def test_attributes(self):
        self.assertIsNotNone(self.sensor)
        self.assertIsInstance(self.sensor, LightSensor)
        self.assertEqual(self.sensor.pin, 20)
        self.assertEqual(self.sensor.s_name, "Light sensor")

    def test_get_value(self):
        print("--- Testing light sensor : get_value() method ---")
        for _ in range(10):
            value = self.sensor.get_value()
            print(f"Value: {value}")
            self.assertIn(value, [0, 1])
            time.sleep(1)

    def test_get_value_not_black(self):
        print("--- Testing light sensor : get_value() method (not black case) ---")
        time.sleep(5)
        for _ in range(10):
            value = self.sensor.get_value()
            print(f"Value: {value}")
            self.assertFalse(value)
            time.sleep(1)

    def test_get_value_black(self):
        print("--- Testing light sensor : get_value() method (black case) ---")
        time.sleep(5)
        for _ in range(10):
            value = self.sensor.get_value()
            print(f"Value: {value}")
            self.assertTrue(value)
            time.sleep(1)


if __name__ == "__main__":
    unittest.main()
