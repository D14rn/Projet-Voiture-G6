class DistanceController:
    """
    Permet de contrôler le démarrage et l'arrêt des capteurs de distance et de récupérer les distances
    """

    def __init__(self, front, left, right) -> None:
        self.__front = front
        self.__left = left
        self.__right = right

    @property
    def front_distance(self):
        """
        Retourne la distance récupérée par le capteur de devant
        """
        return self.__front.value

    @property
    def right_distance(self):
        """
        Retourne la distance récupérée par le capteur de droite
        """
        return self.__right.value

    @property
    def left_distance(self):
        """
        Retourne la distance récupérée par le capteur de gauche
        """
        return self.__left.value
    
    def start(self) -> None:
        """
        Lance les threads des capteurs
        """
        self.__front.get_value()
        self.__left.get_value()
        self.__right.get_value()
        self.__front.activate()
        self.__left.activate()
        self.__right.activate()
        print("capteurs distance lancés")

    def stop(self) -> None:
        """
        Arrête les threads des capteurs
        """
        self.__front.deactivate()
        self.__left.deactivate()
        self.__right.deactivate()
