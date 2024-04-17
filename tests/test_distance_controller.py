import unittest, time
from src.controllers import DistanceController

class DistanceControllerTest(unittest.TestCase):
    def setUp(self) -> None:
        self.front_sensor = DistanceSensor("front sensor", 6, 5)
        self.left_sensor = DistanceSensor("left sensor", 11, 9)
        self.right_sensor = DistanceSensor("right sensor", 26, 19)
        
        self.distController = DistanceController(self.front_sensor, self.left_sensor, self.right_sensor)
        
    def test_start(self):
        self.assertIsNotNone(self.distController)
        self.assertIsInstance(self.distController, DistanceController)
        self.distController.start()
        self.assertTrue(self.front_sensor.activate())
        self.assertTrue(self.left_sensor.activate())
        self.assertTrue(self.right_sensor.activate())
        
    def test_front_distance(self):
        # Simulation d'une valeur de capteur
        self.front_sensor.value = 50
        self.assertEqual(self.distController.front_distance(),30)

    def test_left_distance(self):
        self.front_sensor.value = 15
        self.assertEqual(self.distController.front_distance(),15)
        
    def test_right_distance(self):
        self.front_sensor.value = 40
        self.assertEqual(self.distController.front_distance(),40)

    def test_stop(self):
        self.distController.stop()
        self.assertTrue(self.front_sensor.deactivate())
        self.assertTrue(self.left_sensor.deactivate())
        self.assertTrue(self.right_sensor.deactivate())

if __name__ == "__main__":
    unittest.main()
