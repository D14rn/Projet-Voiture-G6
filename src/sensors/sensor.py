from threading import Thread
import time as t


class Sensor(Thread):
    """
    Représente un capteur générique ayant un nom et une fréquence de rafraîchissement
    """
    def __init__(self, s_name: str, polling_interval=0.1) -> None:
        super().__init__()
        Thread.__init__(self) 
        self.s_name = s_name
        self.active = False
        self.value = None
        self.polling_interval = polling_interval

    def __str__(self):
        return f"{self.s_name}: {self.value}"

    def get_value(self) -> None:
        raise NotImplementedError("You must implement this method in your class")
    
    def run(self):
        while self.active: # Boucle infinie pour mettre à jour la valeur du capteur
            self.get_value()
            t.sleep(self.polling_interval)

    def activate(self):
        """
        Lance la prise de mesure du capteur
        """
        self.active = True
        self.start()

    def deactivate(self):
        """
        Arrête la prise de mesure du capteur
        """
        self.active = False
