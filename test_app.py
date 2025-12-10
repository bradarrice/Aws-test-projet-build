import unittest
from app import say_hello 

class TestSayHello(unittest.TestCase):
      def test_say_hello(self):
            self.assertEqual(say_hello("bradarrice"), "hello, bradarrice")
        