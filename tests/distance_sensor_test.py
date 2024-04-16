from time import sleep
from src.sensors import DistanceSensor
from src.lib import exit_handler


if __name__ == "__main__":
    sleep_duration = 1
    front_sensor = DistanceSensor("front sensor", 6, 5)
    left_sensor = DistanceSensor("left sensor", 11, 9)
    right_sensor = DistanceSensor("right sensor", 26, 19)

    sensors = [front_sensor, left_sensor, right_sensor]
    distance_mesures = []
    tests_count = 5
    for sensor in sensors:
        print(f"Testing {sensor.s_name}")
        for _ in range(tests_count):
            current_value = sensor.get_value()
            print(current_value)
            distance_mesures.append(current_value)
            sleep(sleep_duration)
