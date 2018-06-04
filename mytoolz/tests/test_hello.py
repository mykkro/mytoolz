from unittest import TestCase

from mytoolz import hello

class TestHello(TestCase):
    def test_is_string(self):
        s = hello()
        self.assertTrue(isinstance(s, str))
