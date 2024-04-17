import unittest, time
from src.lib import exit_handler
from src.sensors import ColorSensor


class ColorSensorTest(unittest.TestCase):
    def setUp(self) -> None:
        self.sensor = ColorSensor("Color sensor", 4)
    
    def tearDown(self):
       del self.sensor

    def test_attributes(self):
        self.assertIsInstance(self.sensor, ColorSensor)
        self.assertIsNotNone(self.sensor)
        self.assertEqual(self.sensor.s_name, "Color sensor")
        self.assertIsNotNone(self.sensor.sensor)
        self.assertEqual(self.sensor.sensor.gain, 4)

    def test_get_value_types(self):
        rgb_value = self.sensor.get_value()
        self.assertIsInstance(rgb_value, tuple)
        self.assertEqual(len(rgb_value), 3)

    def test_is_green_types(self):
        res = self.sensor.is_green()
        self.assertIsInstance(res, bool)

    def test_get_value(self):
        values = [i for i in range(0,255)]
        print("--- Testing color sensor : get_value() method ---")
        for _ in range(10):
            r, g, b = self.sensor.get_value()
            print(f"R: {r}, G: {g}, B: {b}")
            self.assertIn(r, values)
            self.assertIn(g, values)
            self.assertIn(b, values)
            time.sleep(1)

    def test_is_green_not_green(self):
        print("--- Testing color sensor : is_green() method (not green case) ---")
        time.sleep(5)
        for _ in range(10):
            output = self.sensor.is_green()
            print(f"Is green: {output}")
            self.assertFalse(output)
            time.sleep(1)

    def test_is_green_green(self):
        print("--- Testing color sensor : is_green() method (green case) ---")
        time.sleep(5)
        for _ in range(10):
            output = self.sensor.is_green()
            print(f"Is green: {output}")
            self.assertTrue(output)
            time.sleep(1)


if __name__ == "__main__":
    unittest.main()
