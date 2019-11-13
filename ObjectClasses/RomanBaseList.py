from ObjectClasses.RomanNum import RomanNum


class RomanBaseList:
    def __init__(self):
        self._base_roman = {}
        self._base_roman.update({'I': RomanNum('I', 1, True, True, ['V', 'X'])})
        self._base_roman.update({'V': RomanNum('V', 5)})
        self._base_roman.update({'X': RomanNum('X', 10, True, True, ['L', 'C'])})
        self._base_roman.update({'L': RomanNum('L', 50)})
        self._base_roman.update({'C': RomanNum('C', 100, True, True, ['D', 'M'])})
        self._base_roman.update({'D': RomanNum('D', 500)})
        self._base_roman.update({'M': RomanNum('M', 1000, True)})

    @property
    def base_roman(self):
        return self._base_roman

    @base_roman.setter
    def base_roman(self, value):
        self._base_roman = value

    def get_sorted_list_by_value(self):
        return [r.symbol for r in sorted(list({v for k, v in self._base_roman.items()}),
                                         key=lambda x: x.decimal_value, reverse=True)]

    def get_roman_by_galaxy_symbol(self, galaxy_symbol):
        """
        Get roman number from galaxy symbel
        :param galaxy_symbol: galaxy symbol
        :return: roman number
        """
        for k, v in self._base_roman.items():
            if v.galaxy_symbol == galaxy_symbol:
                return k
        return ''
