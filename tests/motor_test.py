import unittest, time
from src.lib import exit_handler
from src.motors import Motor


class MotorTest(unittest.TestCase):
    """
    bcm pins
    moteur gauche :
    A : 17 (out)
    B : 18 (out)
    channel : 4
    moteur droit :
    A : 27 (out)
    B : 22 (out)
    channel : 5
    """
    def setUp(self):
        self.motor = Motor(17,18,27,22,4,5)

    def tearDown(self):
       del self.motor
    
    def test_attributes(self):
        self.assertIsInstance(self.motor, Motor)
        self.assertIsNotNone(self.motor.pwm)
        self.assertEqual(self.motor.min, 0)
        self.assertEqual(self.motor.max, 4095)
        self.assertEqual(self.motor.left_motor_A, 17)
        self.assertEqual(self.motor.left_motor_B, 18)
        self.assertEqual(self.motor.left_motor_driver, 4)
        self.assertEqual(self.motor.right_motor_A, 27)
        self.assertEqual(self.motor.right_motor_B, 22)
        self.assertEqual(self.motor.right_motor_driver, 5)
    
    def test_move_forward(self):
        self.motor.move(30)
        time.sleep(2)
        self.motor.move(60)
        time.sleep(2)
        self.motor.stop()

    def test_move_backward(self):
        self.motor.move(30, True)
        time.sleep(2)
        self.motor.move(60, True)
        time.sleep(2)
        self.motor.stop()
    
    def test_stop(self):
        self.motor.stop()


if __name__ == "__main__":
     unittest.main()
