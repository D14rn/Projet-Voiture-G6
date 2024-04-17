import unittest, time
from src.lib import exit_handler
from src.motors import Direction


class DirectionTest(unittest.TestCase):
    def setUp(self) -> None:
        self.direction = Direction()

    def tearDown(self) -> None:
        del self.direction

    def test_attributes(self) -> None:
        self.assertIsInstance(self.direction, Direction)
        self.assertIsNotNone(self.direction.pwm)
        self.assertEqual(self.direction.min, 360)
        self.assertEqual(self.direction.max, 550)
        self.assertEqual(self.direction.wait_time, 0.025)
        self.assertEqual(self.direction.pwm.frequency, 50)

    def test_calc_angle(self) -> None:
        self.assertEqual(self.direction._calc_angle(-45), 265)
        self.assertEqual(self.direction._calc_angle(-100), 265)
        self.assertEqual(self.direction._calc_angle(0), 360)
        self.assertEqual(self.direction._calc_angle(45), 455)
        self.assertEqual(self.direction._calc_angle(100), 455)

    def test_home(self):
        self.direction.home()

    def test_turn_left(self):
        self.direction.home()
        self.direction.turn_left(45)
        time.sleep(1)
        self.direction.home()
        time.sleep(1)

    def test_turn_right(self):
        self.direction.home()
        self.direction.turn_right(45)
        time.sleep(1)
        self.direction.home()
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
