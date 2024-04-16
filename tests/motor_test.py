import unittest
import src.motors.motor
from src.lib import exit_handler

class MotorTest(unittest.TestCase):

#numerotation des pins mode board a voir pour le bcm
    def setUp(self,
            pin1_left_motor,
            pin2_left_motor,
            pin1_right_motor,
            pin2_right_motor,
            channel_motor1,
            channel_motor2):
        g.setmode(g.BOARD)
        # left motor
        self.__left_motor_A = pin1_left_motor
        self.__left_motor_B = pin2_left_motor
        self.__left_motor_driver = channel_motor1
        g.setup(self.__left_motor_A, g.OUT)
        g.setup(self.__left_motor_B, g.OUT)
        # right motor
        self.__right_motor_A = pin1_right_motor
        self.__right_motor_B = pin2_right_motor
        self.__right_motor_driver = channel_motor2
        g.setup(self.__right_motor_A, g.OUT)
        g.setup(self.__right_motor_B, g.OUT)
        # PWM (speed control)
        self.__pwm = PWM()
        self.__pwm.frequency = 50
        self.__min = 0 # min pwm (speed)
        self.__max = 4095 # max pwm (speed)
        

    def testMoveForward(self):
        self.move(400,backward=True)
        self.asserGreater(self.move(),0)
    def testMoveBackward(self):
        self.move(-100,backward=True)
        self.assertLessEqual(self.move(),0)

    def testStop(self):
        self.assertEqual(self.speed,0)

    exit_handler()

if __name__ == "__main__":
     unittest.main()
