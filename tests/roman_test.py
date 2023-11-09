import unittest

from src.roman import convert_decimal_to_roman, convert_to_confusing_roman, get_number


class RomanTest(unittest.TestCase):
    def test_convert_decimal_to_roman(self) -> None:
        self.assertEqual("N", convert_decimal_to_roman(0))
        self.assertEqual("I", convert_decimal_to_roman(1))
        self.assertEqual("II", convert_decimal_to_roman(2))
        self.assertEqual("III", convert_decimal_to_roman(3))
        self.assertEqual("IV", convert_decimal_to_roman(4))
        self.assertEqual("V", convert_decimal_to_roman(5))
        self.assertEqual("VI", convert_decimal_to_roman(6))
        self.assertEqual("VII", convert_decimal_to_roman(7))
        self.assertEqual("VIII", convert_decimal_to_roman(8))
        self.assertEqual("IX", convert_decimal_to_roman(9))
        self.assertEqual("X", convert_decimal_to_roman(10))
        self.assertEqual("XI", convert_decimal_to_roman(11))
        self.assertEqual("XLIX", convert_decimal_to_roman(49))
        self.assertEqual("L", convert_decimal_to_roman(50))

        self.assertEqual("LI", convert_decimal_to_roman(51))
        self.assertEqual("XCIX", convert_decimal_to_roman(99))
        self.assertEqual("C", convert_decimal_to_roman(100))
        self.assertEqual("CI", convert_decimal_to_roman(101))
        self.assertEqual("CDXCIX", convert_decimal_to_roman(499))
        self.assertEqual("D", convert_decimal_to_roman(500))
        self.assertEqual("DI", convert_decimal_to_roman(501))
        self.assertEqual("CMXCIX", convert_decimal_to_roman(999))
        self.assertEqual("M", convert_decimal_to_roman(1000))
        self.assertEqual("MI", convert_decimal_to_roman(1001))
        self.assertEqual("MMMCMXCIX", convert_decimal_to_roman(3999))

        # This is not a valid roman number, but we will accept it
        self.assertEqual("MMMM", convert_decimal_to_roman(4000))
        self.assertEqual("XL", convert_decimal_to_roman(-40))

    def test_convert_to_confusing_roman(self) -> None:
        self.assertEqual("1", convert_to_confusing_roman("I"))
        self.assertEqual("11", convert_to_confusing_roman("II"))
        self.assertEqual("111", convert_to_confusing_roman("III"))
        self.assertEqual("15", convert_to_confusing_roman("IV"))
        self.assertEqual("5", convert_to_confusing_roman("V"))
        self.assertEqual("51", convert_to_confusing_roman("VI"))
        self.assertEqual("5111", convert_to_confusing_roman("VIII"))
        self.assertEqual("110", convert_to_confusing_roman("IX"))
        self.assertEqual("10", convert_to_confusing_roman("X"))
        self.assertEqual("101", convert_to_confusing_roman("XI"))
        self.assertEqual("50", convert_to_confusing_roman("L"))
        self.assertEqual("100", convert_to_confusing_roman("C"))
        self.assertEqual("500", convert_to_confusing_roman("D"))
        self.assertEqual("1000", convert_to_confusing_roman("M"))

    def test_get_number(self) -> None:
        self.assertEqual("N", get_number(0, True))
        self.assertEqual("I", get_number(1, True))
        self.assertEqual("0", get_number(0, False))
        self.assertEqual("1", get_number(1, False))
