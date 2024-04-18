import unittest
from unittest.mock import MagicMock
from src.controllers.state_controller import StateController


class TestStateController(unittest.TestCase):
    def setUp(self):
        self.mock_light = MagicMock()
        self.mock_color = MagicMock()
        self.state_controller = StateController(self.mock_light, self.mock_color, lap_count=3)

    def test_should_continue_race_green(self):
        self.mock_color.is_green.return_value = True
        result = self.state_controller.should_continue_race()
        self.assertTrue(result)

    def test_should_continue_race_red(self):
        self.mock_color.is_green.return_value = False
        result = self.state_controller.should_continue_race()
        self.assertFalse(result)

    def test_should_continue_race_full_lap(self):
        self.mock_color.is_green.return_value = True
        self.state_controller._StateController__lap = 2
        result = self.state_controller.should_continue_race()
        self.assertTrue(result)

    def test_stop(self):
        result = self.state_controller.stop()
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()
