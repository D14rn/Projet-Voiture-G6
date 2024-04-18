

class StateController:
    """
    Permet de contrôler l'état de la voiture dans la course (continuer ou arrêter)
    """
    def __init__(self, light, color, lap_count):
        self.__light = light
        self.__color = color
        self.__lap_count = lap_count

    @property
    def lap_count(self):
        return self.__lap_count
    
    @lap_count.setter
    def lap_count(self, value):
        if isinstance(value, int) and value >= 0:
            self.__lap_count = value
        else:
            raise ValueError("Le nombre de tours doit être un entier positif")
        
    def should_start_race(self):
        """
        Vérifie si la voiture doit démarrer la course : si le feux est vert
        """
        while not self.__color.is_green():
            pass

    def should_continue_race(self):
        """
        Vérifie si la voiture doit continuer la course : si le nombre de tour n'est pas atteind
        """
        if self.__light.value:
            print('counting lap')
            self.lap_count -= 1

        if self.lap_count > -1:
            return True
        else:
            return False

    def start(self):
        """
        Lance les threads des capteurs
        """
        self.__light.activate()
        self.__color.activate()

    def stop(self):
        """
        Arrête les threads des capteurs
        """
        self.__light.deactivate()
        self.__color.deactivate()

