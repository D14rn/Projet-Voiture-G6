"""
'Samir you're breaking the car!'
- Vivek Ponnusamy

https://www.youtube.com/watch?v=D9-voINFkCg
"""
import time as t
from .controllers import MovementController, DistanceController, StateController
from .lib import exit_handler
from random import uniform


class Car():
    """
    Objet voiture composé de contrôleurs et possédant des méthodes pour les modes : autonome et contrôlé
    """
    def __init__(self,
                 movement_controller: MovementController,
                 distance_controller: DistanceController,
                 state_controller: StateController
        ):

        self.__movement_controller = movement_controller
        self.__distance_controller = distance_controller
        self.__state_controller = state_controller
        self.last_back = 10
        self.back_cooldown = 7
        self.last_turn = ""

    @property
    def samir(self): # Appelle le pilote
        """
        Contrôleur de mouvement de la voiture
        """
        return self.__movement_controller
    
    @property
    def vivek(self): # Appelle le co-pilote
        """
        Contrôleur de distance de la voiture
        """
        return self.__distance_controller

    @property
    def state_controller(self):
        """
        Contrôleur d'état de la voiture dans la course
        """
        return self.__state_controller

    def __str__(self) -> str:
        return str(self.__dict__)

    def follow_right_wall(self, duration):
        try:
            self.vivek.start()
            self.samir.stay_center()
            self.samir.speed = 20
            start_time = t.time()
            while t.time() - start_time < duration:
                if self.vivek.right_distance < 17:
                    print("ahaha")
                    self.turn_left_and_reset()
                elif self.vivek.right_distance > 23:
                    print("huhuhu")
                    self.turn_right_and_reset()
                else:
                    self.samir.stay_center()
        except:
           pass
        finally: 
            self.samir.reset()
            self.vivek.stop()

    def follow_left_wall(self, duration):
        try:
            self.vivek.start()
            self.samir.stay_center()
            self.samir.speed = 50
            start_time = t.time()
            while t.time() - start_time < duration:
                if self.vivek.right_distance < 25:
                    self.turn_left_and_reset()
                elif self.vivek.left_distance > 31:
                    self.turn_right_and_reset()
                else:
                    self.samir.stay_center()
        except:
           pass
        finally: 
            self.samir.reset()
            self.vivek.stop()

    # def follow_right_wall(self, duration: float|int) -> None:
        # """
        # Fais avancer la voiture à une distance fixe d'un mur à droite durant durée déterminée
        # """
        # try:
            # self.vivek.start()
            # self.samir.stay_center()
            # self.samir.speed = 20
            # start_time = t.time()
            # while t.time() - start_time < duration:
                # if self.vivek.front_distance < 55:
                    # self.samir.turn_left(10)
                # elif self.vivek.right_distance < 8:
                    # self.samir.turn_left(25)
                # elif self.vivek.right_distance < 14:
                    # self.samir.turn_left(10)
                # elif self.vivek.right_distance > 24:
                    # self.samir.turn_right(20)
                # elif self.vivek.right_distance > 26:
                    # self.samir.turn_right(30)
                # else:
                    # self.samir.stay_center()
        # except:
        #    pass
        # finally: 
            # self.samir.reset()
            # self.vivek.stop()
# 
    # def follow_left_wall(self, duration: float|int) -> None:
        # """
        # Fais avancer la voiture à une distance fixe d'un mur durant durée déterminée
        # """
        # try:
            # self.vivek.start()
            # self.samir.stay_center()
            # self.samir.speed = 30
            # start_time = t.time()
            # while t.time() - start_time < duration:
                # if self.vivek.front_distance < 55:
                    # self.samir.turn_right(10)
                # elif self.vivek.left_distance < 8:
                    # self.samir.turn_right(25)
                # elif self.vivek.left_distance < 14:
                    # self.samir.turn_right(10)
                # elif self.vivek.left_distance > 24:
                    # self.samir.turn_left(20)
                # elif self.vivek.right_distance > 26:
                    # self.samir.turn_left(30)
                # else:
                    # self.samir.stay_center()
        # except:
        #    pass
        # finally: 
            # self.samir.reset()
            # self.vivek.stop()

    def avoid_object(self, duration: int = 10) -> None:
        """
        Fais avancer la voiture et évite les obstacles sur son chemin
        """
        self.vivek.start()
        self.samir.stay_center()
        self.samir.speed = 20
        start_time = t.time()
        while (t.time() - start_time) < duration:
            if self.vivek.front_distance < 40:
                self.samir.medium_left()
                print("turning left")
                t.sleep(0.5)
                print("continuing forward")
                self.samir.stay_center()
                t.sleep(3)
                print("turning right")
                self.samir.sharp_right()
                t.sleep(1)
                print("going forward")
                self.samir.stay_center()
                t.sleep(3)
                self.samir.medium_left()
                t.sleep(0.5)
                self.samir.stay_center()
                t.sleep(3)
                break
        self.samir.reset()
        self.vivek.stop()

    def racing_strategy(self) -> None:
        ok_offset = 3
        delta = self.vivek.left_distance - self.vivek.right_distance # negative delta = more space on right
        print(delta)
        print("speed", self.samir.speed)
        print("front dist", self.vivek.front_distance)
        if t.time() - self.last_back > self.back_cooldown:
            self.samir.stop()
            self.samir.speed = -30
            t.sleep(0.5)
            if self.last_turn == "center":
                self.samir.stay_center()
            else:
                if self.last_turn == "right":
                    t.sleep(0.4)
                    self.samir.easy_left()
                    t.sleep(0.2)
                    self.samir.easy_right()
                elif self.last_turn == "left":
                    t.sleep(0.4)
                    self.samir.easy_right()
                    t.sleep(0.2)
                    self.samir.easy_left()
            self.samir.stay_center()
            t.sleep(0.2)
            self.last_back = t.time()
            self.samir.speed = 30
            return
        else:
            self.samir.speed = 30
        # if self.vivek.front_distance < 10:
            # print("backing it up")
            # self.back_it_up(delta)
        #elif delta > ok_offset:
            #self.turn_right_and_reset()
            #self.turn_left_and_reset()
        if delta < - ok_offset: # more space on right
            self.samir.medium_right()
            self.last_turn = "right"
            print("turning right")
        elif delta > ok_offset:
            self.samir.medium_left()
            self.last_turn = "left"
            print("turning left")
        else:
            self.samir.stay_center()
            self.last_turn = "center"

    def turn_right_and_reset(self):
        self.samir.easy_right()
        t.sleep(0.2)
        self.samir.easy_left()
        t.sleep(0.1)
        self.samir.stay_center()
        t.sleep(0.1)
    
    def turn_left_and_reset(self):
        self.samir.easy_left()
        t.sleep(0.2)
        self.samir.easy_right()
        t.sleep(0.1)
        self.samir.stay_center()
        t.sleep(0.1)

    def back_it_up(self, delta) -> None:
        """
        Fais reculer la voiture
        """
        #self.samir.reset()
        back_time = uniform(0.5, 0.8)
        #t.sleep(1.5)
        #l = self.vivek.left_distance
        #r = self.vivek.right_distance
        self.samir.speed = -30
        print(self.samir.speed)
        #self.samir.stay_center()
        t.sleep(0.3)
        self.samir.stay_center()
        #if delta < 0:
        #    self.samir.medium_left()
        #else:
        #    self.samir.medium_right()
        #t.sleep(back_time)
        t.sleep(back_time)

    def autonomous_mode(self) -> None:
        """
        Déplacement autonome : la voiture se déplace toute seule à l'aide des capteurs
        """
        self.vivek.start()
        self.state_controller.start()
        self.state_controller.should_start_race()
        while self.state_controller.should_continue_race():
            print("hahaha")
            self.racing_strategy()
        self.samir.reset()
        self.vivek.stop()
        self.state_controller.stop()

    def controlled_mode(self):
        """
        Déplacement contrôlé : l'utilisateur contrôle la voiture
        """
        pass
