from ObjectClasses.Metal import Metal

class MetalList:
    def __init__(self, metal_list=[]):
        self._metal_list = metal_list

    @property
    def metal_list(self):
        return self._metal_list

    @metal_list.setter
    def metal_list(self, value):
        self._metal_list = value

    def update_metal_list(self, metal: Metal):
        """
        Update metal list with new metal
        :param metal: A new metal
        """
        self._metal_list.append(metal)

    def get_unit_price(self, metal_type):
        """
        Get the metal unit price
        :param metal_type: type of metal, e.g. Gold
        :return: metal unit price
        """
        for metal in self._metal_list:
            if metal.name == metal_type:
                return metal.unit_price
        return 0