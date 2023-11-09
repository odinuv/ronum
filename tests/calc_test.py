import unittest

from src.calc import calculate, validate


class CalcTest(unittest.TestCase):
    def test_calculate(self) -> None:
        self.assertEqual(1, calculate("+", 0, 1))

        self.assertEqual(0, calculate("-", 1, 1))

        self.assertEqual(1, calculate("*", 1, 1))
        self.assertEqual(2, calculate("*", 1, 2))

        self.assertEqual(1, calculate("/", 1, 1))
        self.assertEqual(0, calculate("/", 1, 2))
        self.assertEqual(1, calculate("/", 3, 2))

    def test_validate(self) -> None:
        self.assertEqual(0, validate(0))
        self.assertEqual(0, validate(4000))
        self.assertEqual(1, validate(4001))
        self.assertEqual(1, validate(-1001))
        self.assertEqual(2, validate(40001))
        self.assertEqual(2, validate(-10001))
