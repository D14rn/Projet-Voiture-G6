import time as t, RPi.GPIO as g
from .pwm_driver import PWM


class Motor:
    """
    Représente la force motrice : les moteurs DC arrières
    """
    def __init__(self,
            pin1_left_motor,
            pin2_left_motor,
            pin1_right_motor,
            pin2_right_motor,
            channel_motor1,
            channel_motor2):
        g.setmode(g.BCM)
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

    @property
    def pwm(self):
        return self.__pwm
    
    @property
    def min(self):
        return self.__min
    
    @property
    def max(self):
        return self.__max
    
    @property
    def left_motor_A(self):
        return self.__left_motor_A
    
    @property
    def left_motor_B(self):
        return self.__left_motor_B
    
    @property
    def left_motor_driver(self):
        return self.__left_motor_driver
    
    @property
    def right_motor_A(self):
        return self.__right_motor_A
    
    @property
    def right_motor_B(self):
        return self.__right_motor_B
    
    @property
    def right_motor_driver(self):
        return self.__right_motor_driver
    
    def move(self, speed, backward=False):
        """
        Actionne les moteurs arrières pour faire avancer ou reculer la voiture à une vitesse donnée (en %)
        """
        if speed <= 0:
            self.__pwm.write(self.__left_motor_driver, self.__min, 0)
            self.__pwm.write(self.__right_motor_driver, self.__min, 0)
        else:
            speed = int(min(self.__max, (self.__max * speed / 100)))

        if not backward:
            g.output(self.__left_motor_A, g.HIGH)
            g.output(self.__left_motor_B, g.LOW)
            g.output(self.__right_motor_A, g.HIGH)
            g.output(self.__right_motor_B, g.LOW)
        else:
            g.output(self.__left_motor_A, g.LOW)
            g.output(self.__left_motor_B, g.HIGH)
            g.output(self.__right_motor_A, g.LOW)
            g.output(self.__right_motor_B, g.HIGH)
        self.__pwm.write(self.__left_motor_driver, self.__min, speed)
        self.__pwm.write(self.__right_motor_driver, self.__min, speed)
        return speed #recuperation de l' actuel valeur de la vitesse qui est set.

    def stop(self):
        """
        Arrête les moteurs arrières
        """
        self.move(0)
