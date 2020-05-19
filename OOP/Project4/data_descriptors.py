from weakref import WeakKeyDictionary, ref


class BaseValidator:

    def __init__(self, min, max):
        self.min = min
        self.max = max
        self.values = {}

    def __get__(self, instance, owner_class):
        if instance:
            return self.values[id(instance)]
        return self
    
    def __set__(self, instance, value):
        self.validate(value)
        self.values[id(instance)] = (ref(instance, self._remove_object), value)

    def validate(self, value):
        pass

    def _remove_object(self, weak_ref):
        for key in self.values.keys():
            if self.values[key][0] is weak_ref:
                del self.values[key]
    

class IntegerField(BaseValidator):

    def __init__(self, min=None, max=None):
        super().__init__(min, max)

    def validate(self, value):
        if not isinstance(value, int):
            raise TypeError("value must be of type int")
        if self.max: 
            if value > self.max:
                raise ValueError(f"Integer value must be less than {self.max + 1}")
        if self.min:
            if value < self.min:
                raise ValueError(f"Integer value must be greater than {self.min - 1}")          

class CharField(BaseValidator):

    def __init__(self, min_len=0, max_len=None):
        super().__init__(min_len, max_len)

    def validate(self, value):
        if not isinstance(value, str):
            raise TypeError("value must be of type string")
        if self.max: 
            if len(value) > self.max:
                raise ValueError(f"String length must be less than {self.max + 1}")
        if self.min:
            if len(value) < self.min:
                raise ValueError(f"String length must be greater than {self.min - 1}") 

class Tester:

    __slots__ = '__weakref__'
    integer = IntegerField(1, 10)
    char = CharField(0, 200)