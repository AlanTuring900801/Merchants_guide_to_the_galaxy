class RomanNum:
    def __init__(self, symbol, decimal_value, repeatable=False, reducible=False, reduce_list=[], galaxy_symbol=None):
        self._symbol = symbol
        self._decimal_value = decimal_value
        self._repeatable = repeatable
        self._reducible = reducible
        self._reduce_list = reduce_list
        self._galaxy_symbol = galaxy_symbol

    @property
    def symbol(self):
        return self._symbol

    @symbol.setter
    def symbol(self, value):
        self._symbol = value

    @property
    def decimal_value(self):
        return self._decimal_value

    @decimal_value.setter
    def decimal_value(self, value):
        self._decimal_value = value

    @property
    def repeatable(self):
        return self._repeatable

    @repeatable.setter
    def repeatable(self, value):
        self._repeatable = value

    @property
    def reducible(self):
        return self._reducible

    @reducible.setter
    def reducible(self, value):
        self._reducible = value

    @property
    def reduce_list(self):
        return self._reduce_list

    @reduce_list.setter
    def reduce_list(self, value):
        self._reduce_list = value

    @property
    def galaxy_symbol(self):
        return self._galaxy_symbol

    @galaxy_symbol.setter
    def galaxy_symbol(self, value):
        self._galaxy_symbol = value