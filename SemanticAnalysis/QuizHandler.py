from SemanticAnalysis.NumberConvert import NumberConvert
from ObjectClasses.RomanBaseList import RomanBaseList
from ObjectClasses.MetalList import MetalList
import re


class QuizHandler:
    def __init__(self, roman_base_list: RomanBaseList, metal_list: MetalList):
        self._roman_base_list = roman_base_list
        self._metal_list = metal_list
        self._number_convert = NumberConvert(self._roman_base_list)

    def how_much_quiz_handle(self, sentence):
        """
        Explain sentence like: 'how much is pish tegj glob glob ?'
        :param sentence:
        :return:
        """
        sen_info = re.match(r'how much is ([a-z ]+[a-z]) ?', sentence)
        galaxy_symbol = sen_info.group(1)
        num = self._number_convert.galaxy_to_num(galaxy_symbol)
        return ' '.join([galaxy_symbol, 'is', str(num)])

    def how_many_quiz_handle(self, sentence):
        """
        Explain sentence like: how many Credits is glob prok Silver ?
        :param sentence:
        :return:
        """
        sen_info = re.match(r'how many Credits is (([a-z ]+[a-z]) ([A-Z][a-z]+)) ?', sentence)
        galaxy_symbol, metal_type = sen_info.group(2), sen_info.group(3)
        credit = self._number_convert.galaxy_to_num(galaxy_symbol) * self._metal_list.get_unit_price(metal_type)
        return ' '.join([galaxy_symbol, metal_type, 'is', '{:g}'.format(credit), 'Credits'])