import unittest
import time
from src.motors import Motor
from src.lib import exit_handler


class MotorTest(unittest.TestCase):
    '''
    bcm pins
    moteur gauche :
    A : 17 (out)
    B : 18 (out)
    channel : 4
    moteur droit :
    A : 27 (out)
    B : 22 (out)
    channel : 5
    '''
    def testMoveForward(self):
        motor = Motor(17,18,27,22,4,5)
        spdMotor = motor.move(40)
        if self.assertTrue(1<=spdMotor<100):
            print('Forward movement ok')
            for i in range(1,6):
                time.sleep(1)
                print(f'next test in {i} seconds')
        del motor

    def testMoveBackward(self):
        motor2 = Motor(17,18,27,22,4,5)
        spdMotor = motor2.move(40, backward=True)
        if self.assertTrue(1<=spdMotor<100):
            print('Backward movement ok')
            for i in range(1,6):
                time.sleep(1)
                print(f'next test in {i} seconds')
        del motor2

    def testShiftSpeed(self):
        '''
        pseudo-code test acceleration
        return speed dans move , est que cest ok ?
        '''
        motor3 = Motor(17,18,27,22,4,5)

        old_speed = motor3.move(40)
        time.sleep(5)
        new_speed = motor3.move(80)
        time.sleep(5)
        if self.assertGreater(new_speed,old_speed):
            print('acceleration ok')

        motor3.stop()       
        time.sleep(3)

        old_speed = motor3.move(80)
        time.sleep(5)
        new_speed = motor3.move(40)
        time.sleep(5)
        if self.assertLess(new_speed,old_speed):
            print('deceleration ok')

    def stop(self):
        motor4 = Motor(17,18,27,22,4,5)
        self.assertEqual(motor4.move(0),0)


if __name__ == "__main__":
     unittest.main()
