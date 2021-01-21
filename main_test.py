import main
import unittest


class MyTest(unittest.TestCase):
    def test_method1(self):
        assert 15, main.a + main.b
