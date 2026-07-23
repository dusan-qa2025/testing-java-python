from unittest import TestCase
import example

class TestHello(TestCase):

    def test_hello(self):
        self.assertEqual(example.hello("Ben"), "Hello Ben")
        self.assertEqual(example.hello("Tom"), "Hello Tom")
        