import unittest
from unittest.mock import patch, Mock
from src.controllers import MovementController

class TestMovementController(unittest.TestCase):

    def setUp(self):
        self.mock_direction = Mock()
        self.mock_motor = Mock()
        self.controller = MovementController(self.mock_direction, self.mock_motor, 50)

    @patch.object(MovementController, 'go_forward')
    def test_go_forward(self, mock_go_forward):
        self.controller.go_forward()
        mock_go_forward.assert_called_once()

    @patch.object(MovementController, 'turn_left')
    def test_turn_left(self, mock_turn_left):
        self.controller.turn_left()
        mock_turn_left.assert_called_once()

    @patch.object(MovementController, 'turn_right')
    def test_turn_right(self, mock_turn_right):
        self.controller.turn_right()
        mock_turn_right.assert_called_once()

    @patch.object(MovementController, 'reset_direction')
    def test_reset_direction(self, mock_reset_direction):
        self.controller.reset_direction()
        mock_reset_direction.assert_called_once()

    @patch.object(MovementController, 'stop')
    def test_stop(self, mock_stop):
        self.controller.stop()
        mock_stop.assert_called_once()

    @patch.object(MovementController, 'accelerate')
    def test_accelerate(self, mock_accelerate):
        self.controller.accelerate()
        mock_accelerate.assert_called_once()

    @patch.object(MovementController, 'reset')
    def test_reset(self, mock_reset):
        self.controller.reset()
        mock_reset.assert_called_once()

if __name__ == '__main__':
    unittest.main()
