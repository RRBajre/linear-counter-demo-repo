import unittest

from app.counter import decrement, increment


class CounterTest(unittest.TestCase):
    def test_increment(self):
        self.assertEqual(increment(2), 3)

    def test_decrement(self):
        self.assertEqual(decrement(3), 2)

    def test_decrement_clamps_at_zero(self):
        self.assertEqual(decrement(0), 0)

    def test_decrement_does_not_go_negative(self):
        self.assertEqual(decrement(-5), 0)


if __name__ == "__main__":
    unittest.main()
