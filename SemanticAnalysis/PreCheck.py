from ObjectClasses.RomanBaseList import RomanBaseList

class Precheck:
    def __init__(self, roman_input):
        self._roman_input = roman_input
        self._roman_base_list = RomanBaseList()

    @property
    def roman_input(self):
        return self._roman_input

    @roman_input.setter
    def roman_input(self, value):
        self._roman_input = value

    @property
    def roman_base_list(self):
        return self._roman_base_list

    @roman_base_list.setter
    def roman_base_list(self, value):
        self._roman_base_list = value

    def precheck(self):
        res1 = self.repeatTimeCheck()
        res2 = self.subtractCheck()
        if res1 is True and res2 is True:
            return True
        else:
            return False

    def repeatTimeCheck(self):
        """
        Check max repeat time in a succession
        """
        cnt = 1
        for i in range(1, len(self._roman_input)):
            if self._roman_input[i] == self._roman_input[i-1]:
                cnt = cnt + 1
            else:
                cnt = 1
        if cnt > 3:
            return False
        else:
            return True

    def subtractCheck(self):
        """
        Check the subtract rules
        """
        roman_sorted_list = self._roman_base_list.get_sorted_list_by_value()
        for i in range(len(self._roman_input)-1):
            current_roman, next_roman = self._roman_input[i], self._roman_input[i+1]
            valid_roman = roman_sorted_list[roman_sorted_list.index(current_roman):]
            valid_roman.extend(self._roman_base_list.base_roman[current_roman].reduce_list)
            if next_roman not in valid_roman:
                return False
        return True

