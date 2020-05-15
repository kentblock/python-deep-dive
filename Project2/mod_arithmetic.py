

class Mod:

    def __init__(self, value, modulus):
        
        if not isinstance(modulus, int):
            raise TypeError("modulus must be an integer.")
        if modulus < 1: 
            raise ValueError("modulus must be a positive integer")
        self._modulus = modulus 
        if not isinstance(value, int):
            raise TypeError("value must be an integer.")
        self._value = value % self._modulus

    @property
    def value(self):
        return self._value

    @property
    def modulus(self):
        return self._modulus

    def __eq__(self, other):
        """Equal if they have same modulus and value, 
        allow comparison between Mod and residue of an int as well"""
        if isinstance(other, Mod):
            if other.modulus != self.modulus:
                return NotImplemented
            else: 
                if self.value == other.value:
                    return True
                return False
        if isinstance(other, int):
            if other % self.modulus == self.value:
                return True
            return False
        return NotImplemented

    def __hash__(self):
        return hash((self.value, self.modulus))

    def __int__(self):
        return self.value

    def __repr__(self):
        pass

    def __add__(self, b):
        pass

    def __sub__(self, b):
        pass

    def __mul__(self, b):
        pass

    def __pow__(self, p):
        pass

    def __iadd__(self, b):
        pass

    def __isub__(self, b):
        pass

    def __imul__(self, b):
        pass

    #TODO implement ordering as well