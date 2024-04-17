import unittest
from src.controllers import DistanceController
from src.sensors import DistanceSensor

class DistanceControllerTest(unittest.TestCase):
    def setUp(self) -> None:
        self.front_sensor = DistanceSensor("front sensor", 6, 5)
        self.left_sensor = DistanceSensor("left sensor", 11, 9)
        self.right_sensor = DistanceSensor("right sensor", 26, 19)
        self.distController = DistanceController(self.front_sensor,self.left_sensor,self.right_sensor)

    def tearDown(self)-> None:
        del self.distController
    def test_start(self):
        self.distController.start()
        self.assertTrue(self.front_sensor._active,True)
        self.assertTrue(self.left_sensor._active,True)
        self.assertTrue(self.right_sensor._active,True)
        
    def test_front_distance(self):
        self.front_sensor.value = 30.123
        self.assertAlmostEqual(self.distController.front_distance(),30.123,2)

    def test_left_distance(self):
        self.left_sensor.value = 15.678
        self.assertAlmostEqual(self.distController.left_distance(),15.678,2)

    def test_right_distance(self):
        self.right_sensor.value = 40.987
        self.assertAlmostEqual(self.distController.right_distance(),40.987,2)

    def test_stop(self):
        self.assertIsNotNone(self.distController)
        self.assertIsInstance(self.distController, DistanceController)
        self.distController.stop()
        self.assertTrue(self.front_sensor._active,False)
        self.assertTrue(self.left_sensor._active,False)
        self.assertTrue(self.right_sensor._active,False)

if __name__ == "__main__":
    unittest.main()
