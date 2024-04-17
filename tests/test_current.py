from src.lib import exit_handler
from src.sensors import CurrentSensor
from src.motors import Direction


if __name__ == '__main__':
    current_sensor = CurrentSensor("current_sensor")
    direction = Direction()
    for i in range(0, 40, 10):
        direction.turn_left(i)
        print("Current: ", current_sensor.get_value())
    direction.home()
    for i in range(0, 40, 10):
        direction.turn_right(i)
        print("Current: ", current_sensor.get_value())
