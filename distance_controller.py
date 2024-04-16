class DistanceController:
    """
    Permet de contrôler les capteurs de distance et de récupérer les distances
    """
    def __init__(self, front, left, right) -> None:
        self.__front = front
        self.__left = left
        self.__right = right
    
    def get_distance(self, side) -> float:
        return side.value
    
    def start(self) -> None:
        """
        Lance les threads des capteurs
        """
        self.__front.start()
        self.__left.start()
        self.__right.start()
    def stop(self) -> None:
        """
        Arrête les threads des capteurs
        """
        self.__front.deactivate()
        self.__left.deactivate()
        self.__right.deactivate()
