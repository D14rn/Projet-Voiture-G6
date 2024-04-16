if __name__ == "__main__":
    from src.sensors import LightSensor
    from time import sleep


    light_sensor = LightSensor("light sensor", 20)
    for i in range (15):
        print(light_sensor.get_value())
        sleep(0.5)