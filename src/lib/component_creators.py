from ..sensors import *
from ..motors import *
from ..controllers import *


def create_fds():
    return DistanceSensor("FDS", 6, 5)

def create_lds():
    return DistanceSensor("LDS", 11, 9)
        
def create_rds():
    return DistanceSensor("RDS", 26, 19)

def create_ds():
    return (create_fds(), create_lds(), create_rds())

def create_ls():
    return LightSensor("LS", 20)

def create_cs():
    return ColorSensor("CS")

def create_motor():
    return Motor(17, 18, 27, 22, 4, 5)

def create_direction():
    return Direction()

def create_dm():
    return (create_direction(), create_motor())

def create_distance_controller():
    return DistanceController(*create_ds())

def create_movement_controller():
    return MovementController(*create_dm())

def create_state_controller(lap_count):
    return StateController(create_ls(), create_cs(), lap_count)
