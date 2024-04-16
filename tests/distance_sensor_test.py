if __name__ == "__main__":
    from time import sleep
    from src.sensors import DistanceSensor
    from src.config import DISTANCE_SENSORS_BOARD_PINS as dsbp

    sleep_duration = 1
    front_sensor = DistanceSensor("front sensor", dsbp["FRONT"]["TRIGGER"], dsbp["FRONT"]["ECHO"])
    right_sensor = DistanceSensor("right sensor", dsbp["RIGHT"]["TRIGGER"], dsbp["RIGHT"]["ECHO"])
    left_sensor = DistanceSensor("left sensor", dsbp["LEFT"]["TRIGGER"], dsbp["LEFT"]["ECHO"])

    sensors = [left_sensor]

    for sensor in sensors:
        print(f"Testing sensor: {sensor.s_name}")
        for _ in range(5):
            print(sensor.get_value())
            sleep(sleep_duration)
