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
        """Tests the add two numbers function
        """
        obj = keep.Keep()
        self.assertEqual(
            obj.add_numbers(first_number=1, second_number=2), 3, msg="1 + 2 should be 3"
        )
