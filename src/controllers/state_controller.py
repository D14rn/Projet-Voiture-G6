

class StateController:
    """
    Permet de contrôler l'état de la voiture dans la course (continuer ou arrêter)
    """
    def __init__(self, light, color, lap_count):
        self.__light = light
        self.__color = color
        self.__lap_count = lap_count
        self.__lap = 0

    def should_continue_race(self):
        """
        Vérifie si la voiture doit continuer la course : si le feux est vert et que le nombre de tour n'est pas atteint
        """
        if self.__color.is_green() and self.__lap_count>self.__lap:
            self.__lap_count -=1
            return True
        elif self.__lap_count==self.__lap:
                self.__lap_count = 0
                self.stop()

    def start(self):
        """
        Lance les threads des capteurs
        """
        self.__light.start()
        self.__color.start()

    def stop(self):
        """
        Arrête les threads des capteurs
        """
        self.__light.deactivate()
        self.__color.deactivate()

