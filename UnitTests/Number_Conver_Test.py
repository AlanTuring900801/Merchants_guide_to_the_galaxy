import unittest
from Main import Main
from ObjectClasses.RomanBaseList import RomanBaseList
from SemanticAnalysis.NumberConvert import NumberConvert

TEST_FILE_PATH = "UnitTests/TestInput/"


class UnitTest(unittest.TestCase):
    def test_number_convert_roman_to_num(self):
        number_convert = NumberConvert(RomanBaseList())
        num = number_convert.romanToNum("MCMXLIV")
        correct_result = 1944
        self.assertEqual(num, correct_result)

    def test_number_convert_num_to_roman(self):
        number_convert = NumberConvert(RomanBaseList())
        num = number_convert.numToRoman(1944)
        correct_result = "MCMXLIV"
        self.assertEqual(num, correct_result)


if __name__ == '__main__':
    unittest.main()

