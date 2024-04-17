from abc import ABC, abstractmethod
from threading import Thread
import time as t


class Sensor(ABC, Thread):
    """
    Représente un capteur générique ayant un nom et une fréquence de rafraîchissement
    """
    def __init__(self, s_name: str, polling_interval=0.2) -> None:
        super().__init__()
        Thread.__init__(self) 
        self._s_name = s_name
        self._active = False
        self._value = None
        self._polling_interval = polling_interval

    @property
    def s_name(self) -> str:
        """
        Nom attribué au capteur pour l'identifier
        """
        return self._s_name
    
    @property
    def value(self):
        """
        Renvoie la valeur du capteur au temps T
        """
        return self._value

    def __str__(self):
        return f"{self.s_name}: {self.value}"
    
    @abstractmethod
    def get_value(self) -> None:
        raise NotImplementedError("You must implement this method in your class")
    
    def run(self):
        while self.active: # Boucle infinie pour mettre à jour la valeur du capteur
            self.get_value()
            t.sleep(self._polling_interval)

    def activate(self):
        """
        Lance la prise de mesure du capteur
        """
        self._active = True
        self.start()

    def deactivate(self):
        """
        Arrête la prise de mesure du capteur
        """
        self._active = False
