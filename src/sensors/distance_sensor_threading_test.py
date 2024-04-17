from src.lib import exit_handler, front_distance_sensor, left_distance_sensor, right_distance_sensor
from src.controllers import DistanceController
import time
import threading


def print_sensor_values(distance_controller: DistanceController):
        print(f"Left sensor: {distance_controller.left_distance}")
        print(f"Front sensor: {distance_controller.front_distance}")
        print(f"Right sensor: {distance_controller.right_distance}")

def test_sensors(distance_controller: DistanceController):
    distance_controller.start()
    for thread in threading.enumerate():
         print(f"Fuck you: {thread.name}")
    time.sleep(1)
    print("hah")
    for _ in range(10):
        print_sensor_values(distance_controller)
        time.sleep(0.5)
    distance_controller.stop()


if __name__ == "__main__":
    for thread in threading.enumerate():
         print(f"Fuck you: {thread.name}")
    front_sensor = front_distance_sensor()
    right_sensor = right_distance_sensor()
    left_sensor = left_distance_sensor()

    test_sensors(DistanceController(front_sensor, left_sensor, right_sensor))
    print("wtf")
    print("when the party dont stop")
    for thread in threading.enumerate():
         print(f"Fuck you: {thread.name}")
