import unittest
from src.motors import Motor
from src.lib import exit_handler
import time 

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
            print('''Actual speed : {spdMotor}
                  next test in 5 sec''')
        time.sleep(5)
        del motor

    def testMoveBackward(self):
        motor2 = Motor(17,18,27,22,4,5)
        spdMotor = motor2.move(40)
        self.assertLessEqual(spdMotor,0)
        time.sleep(5)
        del motor2

    def testShiftSpeed(self):
        '''
        pseudo-code test acceleration
        return speed dans move , est que cest ok ?
        '''
        motor3 = Motor(17,18,27,22,4,5)

        oldSpeed=motor3.move(40)
        time.sleep(5)
        newSpeed=motor3.move(80)
        time.sleep(5)
        if self.assertLess(newSpeed,oldSpeed):
            print('acceleration ok')
        #else: 

        motor3.stop()       
        time.sleep(3)

        oldSpeed=self.move(80)
        time.sleep(5)
        newSpeed=self.move(40)
        time.sleep(5)
        if self.assertLess(newSpeed,oldSpeed):
            print('deceleration ok')
        #else:
        
        


    def stop(self):
        self.assertEqual(self.move(0),0)

    exit_handler()

if __name__ == "__main__":
     unittest.main()
