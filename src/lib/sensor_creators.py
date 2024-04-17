from ..sensors import *


def front_distance_sensor():
    return DistanceSensor("front sensor", 6, 5)

def left_distance_sensor():
    return DistanceSensor("left sensor", 11, 9)
        
def right_distance_sensor():
    return DistanceSensor("right sensor", 26, 19)
