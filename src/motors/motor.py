import RPi.GPIO as g
from .pwm_driver import PWM


class Motor:
    """
    Représente la force motrice : les moteurs DC arrières
    moteur gauche :
    A : 17 (out)
    B : 18 (out)
    channel : 4
    moteur droit :
    A : 27 (out)
    B : 22 (out)
    channel : 5
    """
    def __init__(self,
            pin1_left_motor,
            pin2_left_motor,
            pin1_right_motor,
            pin2_right_motor,
            channel_motor1,
            channel_motor2):
        g.setmode(g.BCM)

        # Left motor
        self.left_motor_A = pin1_left_motor
        self.left_motor_B = pin2_left_motor
        self.left_motor_driver = channel_motor1
        g.setup(self.left_motor_A, g.OUT)
        g.setup(self.left_motor_B, g.OUT)

        # Right motor
        self.right_motor_A = pin1_right_motor
        self.right_motor_B = pin2_right_motor
        self.right_motor_driver = channel_motor2
        g.setup(self.right_motor_A, g.OUT)
        g.setup(self.right_motor_B, g.OUT)

        # PWM (speed control)
        self.pwm = PWM()
        self.pwm.frequency = 50
        self.min = 0 # min pwm (speed)
        self.max = 4095 # max pwm (speed)

    def move(self, speed, backward=False):
        """
        Actionne les moteurs arrières pour faire avancer ou reculer la voiture à une vitesse donnée (en %)
        """
        if speed <= 0: # We stop the motors if negative value
            self.pwm.write(self.left_motor_driver, self.min, 0)
            self.pwm.write(self.right_motor_driver, self.min, 0)
            return 0
        else:
            speed = int(min(self.max, (self.max * speed / 100)))

        if not backward:
            g.output(self.left_motor_A, g.HIGH)
            g.output(self.left_motor_B, g.LOW)
            g.output(self.right_motor_A, g.HIGH)
            g.output(self.right_motor_B, g.LOW)
        else:
            g.output(self.left_motor_A, g.LOW)
            g.output(self.left_motor_B, g.HIGH)
            g.output(self.right_motor_A, g.LOW)
            g.output(self.right_motor_B, g.HIGH)

        self.pwm.write(self.left_motor_driver, self.min, speed)
        self.pwm.write(self.right_motor_driver, self.min, speed)
        return speed # Recuperation de la valeur envoyée aux moteurs

    def stop(self):
        """
        Arrête les moteurs arrières
        """
        self.move(0)
