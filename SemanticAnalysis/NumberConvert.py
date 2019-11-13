from SemanticAnalysis.PreCheck import Precheck
from Except.UnrecognizedRomanForm import UnrecognizedRomanForm
from ObjectClasses.RomanBaseList import RomanBaseList

ROMA_NUMS_DICT = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
ROMA_INT_DICT = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC',
                 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}


class NumberConvert:
    def __init__(self, roman_base_list: RomanBaseList):
        self._roman_base_list = roman_base_list

    def romanToNum(self, s: str) -> int:
        """
        Change a roman number to arabic number
        :param s: input the roman value
        :return: return the same value, but in arabic number
        """
        if Precheck(s).precheck():
            num = 0
            for i in range(len(s) - 1):
                if ROMA_NUMS_DICT[s[i]] >= ROMA_NUMS_DICT[s[i+1]]:
                    num += ROMA_NUMS_DICT[s[i]]
                else:
                    num -= ROMA_NUMS_DICT[s[i]]
            last_num = s[len(s)-1]
            num += ROMA_NUMS_DICT[last_num]
            return num
        else:
            raise UnrecognizedRomanForm()

    def numToRoman(self, num: int) -> str:
        """
        Change arabic number to roman number
        :param num: arabic number
        :return: roman number
        """
        roman_symbol = ""
        for key in sorted(ROMA_INT_DICT.keys())[::-1]:
            a = num // key
            if a == 0:
                continue
            roman_symbol += (ROMA_INT_DICT[key] * a)
            num -= a * key
            if num == 0:
                break
        return roman_symbol

    def galaxy_to_num(self, galaxy_symbol):
        """
        Change galaxy symbol to arabic number
        :param galaxy_symbol:
        :return:
        """
        try:
            return self.romanToNum(self.galaxy_to_roman(galaxy_symbol))
        except UnrecognizedRomanForm as e:
            raise UnrecognizedRomanForm(galaxy_symbol)

    def galaxy_to_roman(self, galaxy_symbol):
        """
        Change galaxy symbol to roman symbol
        :param galaxy_symbol:
        :return:
        """
        romanstr = ''
        for galaxy in galaxy_symbol.split(' '):
            romanstr += self._roman_base_list.get_roman_by_galaxy_symbol(galaxy)
        return romanstr