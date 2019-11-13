from ObjectClasses.RomanBaseList import RomanBaseList
from ObjectClasses.MetalList import MetalList
from ObjectClasses.Metal import Metal
from SemanticAnalysis.NumberConvert import NumberConvert
import re


class InfoCollection:
    def __init__(self, roman_base_list: RomanBaseList, metal_list: MetalList):
        self._roman_base_list = roman_base_list
        self._metal_list = metal_list
        self._number_convert = NumberConvert(self._roman_base_list)

    def assignment_syntax_handle(self, sentence):
        """
        Explain sentence like: 'prok is V'
        :param sentence:
        :return:
        """
        galaxy_symbol, roman_symbol = sentence.split(' is ')
        self._roman_base_list.base_roman[roman_symbol].galaxy_symbol = galaxy_symbol

    def metal_syntax_handle(self, sentence):
        """
        Explain sentence like: 'glob glob Silver is 34 Credits'
        :param sentence:
        :return:
        """
        sen_info = re.match(r'([a-z ]+[a-z]) ([A-Z][a-z]+) is (\d+) Credits', sentence)
        galaxy_part, metal_part, credits_part = sen_info.group(1), sen_info.group(2), sen_info.group(3)
        metal_unit_price = int(credits_part) / int(self._number_convert.galaxy_to_num(galaxy_part))
        self._metal_list.update_metal_list(Metal(metal_part, metal_unit_price))