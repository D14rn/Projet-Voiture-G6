import time as t


class StateController:
    """
    Permet de contrôler l'état de la voiture dans la course (continuer ou arrêter)
    """
    def __init__(self, light, color, lap_count):
        self.light = light
        self.color = color
        self.last_update = 0
        self.wait = 2
        self.lap_count = lap_count + 1

    def waiting_for_greenlight(self):
        """
        Vérifie si la voiture doit démarrer la course : si le feux est vert
        """
        while not self.color.is_green():
            continue
        self.color.deactivate()

    def should_continue_race(self):
        """
        Vérifie si la voiture doit continuer la course : si le nombre de tour n'est pas atteind
        """
        if ((self.light.value == 1) and ((t.time() - self.last_update) > self.wait)):
            self.last_update = t.time()
            self.lap_count -= 1
            print(f"Tours restants: {self.lap_count}")

        if self.lap_count > 0:
            return True
        else:
            return False

    def start(self):
        """
        Lance les threads des capteurs
        """
        self.light.activate()
        self.color.activate()

    def stop(self):
        """
        Arrête les threads des capteurs
        """
        self.light.deactivate()
        self.color.deactivate()
