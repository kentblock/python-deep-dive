

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
            if self.same_mod(other):
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
        return f"Mod object: value = {self.value}, modulus = {self.modulus}"

    def __add__(self, b):
        if isinstance(b, Mod):
            if self.same_mod(b):
                return Mod((self.value + b.value) % self.modulus, self.modulus)
            return NotImplemented
        if isinstance(b, int):
            return Mod((self.value + b) % self.modulus, self.modulus)  
        return NotImplemented

    def __sub__(self, b):
        if isinstance(b, Mod):
            if self.same_mod(b):
                return Mod((self.value - b.value) % self.modulus, self.modulus)
            return NotImplemented
        if isinstance(b, int):
            return Mod((self.value - b) % self.modulus, self.modulus)  
        return NotImplemented

    def __mul__(self, b):
        if isinstance(b, Mod):
            if self.same_mod(b):
                return Mod((self.value * b.value) % self.modulus, self.modulus)
            return NotImplemented
        if isinstance(b, int):
            return Mod((self.value * b) % self.modulus, self.modulus)  
        return NotImplemented

    def __pow__(self, p):
        if isinstance(b, int):
            return Mod((self.value ** p) % self.modulus, self.modulus)  
        return NotImplemented

    def __iadd__(self, b):
        return self + b

    def __isub__(self, b):
        return self - b

    def __imul__(self, b):
        return self * b

    def same_mod(self, other):
        return self.modulus == other.modulus
    #TODO implement ordering as well