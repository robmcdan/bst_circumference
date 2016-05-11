from unittest import TestCase
from state import State


class TestState(TestCase):
    def test_LEFT(self):
        s = State()
        original_left = s.LEFT
        s.LEFT = not original_left
        self.assertIsNot(s.LEFT, original_left, "LEFT value did not change from setter.")

    def test_RIGHT(self):
        s = State()
        original_right = s.RIGHT
        s.RIGHT = not original_right
        self.assertIsNot(s.RIGHT, original_right, "RIGHT value did not change from setter.")
