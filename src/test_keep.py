"""Simple unittest test case to test the basic keep file."""
import unittest

import keep


class TestHello(unittest.TestCase):
    """Tests the keep module"""

    def test_hello(self):
        """Test the hello message function

        Returns:
            None: Returns nothing.
        """
        # make a new keep object
        obj = keep.Keep()
        self.assertEqual(
            obj.say_hello(" World"), "Hello World", "Should return hello world."
        )

    def test_add(self):
        """Tests the add two numbers function"""
        obj = keep.Keep()
        self.assertEqual(
            obj.add_numbers(first_number=1, second_number=2), 3, msg="1 + 2 should be 3"
        )

    def test_ema(self):
        ema_list = keep.Keep().exponential_moving_average(
            [2, 4, 6, 8, 12, 14, 16, 18, 20], 2 / 3, 2
        )
        exp_result = [2, 3.333, 5.111, 7.037, 10.346, 12.782, 14.927, 16.976, 18.992]
        for i in range(0, len(exp_result)):
            self.assertAlmostEqual(ema_list[i], exp_result[i], 3)


t = TestHello()
t.test_ema()
