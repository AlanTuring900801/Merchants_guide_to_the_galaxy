class UnrecognizedRomanForm(SyntaxError):
    def __init__(self, galaxy_symbol=""):
        super().__init__(self)
        self._galaxy_symbol = galaxy_symbol

    def __str__(self):
        error_info = "The composition format of galaxy number '{}' is not correct," \
                     " please check it again.".format(self._galaxy_symbol)
        return error_info
