import unittest
import keep
class TestHello(unittest.TestCase):

    def test_hello(self):
        # make a new keep object
        obj = keep.Keep()
        self.assertEqual(obj.say_hello(), "Hello World", "Should return hello world.")