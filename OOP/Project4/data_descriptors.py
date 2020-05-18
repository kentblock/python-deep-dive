from weakref import WeakKeyDictionary, ref
#TODO refactor and add BaseValidator class

class IntegerField:

    def __init__(self, min, max):
        self.min = min
        self.max = max
        self.values = {}

    def __get__(self, instance, owner_class):
        if instance:
            return self.values[id(instance)]
        return self
    
    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError("value must be of type str")
        if value > self.max or value < self.min:
            raise ValueError(f"Integer value must be greater than {self.min - 1} and less than {self.max + 1}")
        print(f"instance {instance}, value {value}")
        self.values[id(instance)] = (ref(instance, self._remove_object), value)

    def _remove_object(self, weak_ref):
        for key in self.values.keys():
            if self.values[key][0] is weak_ref:
                del self.values[key]
                
class CharField:

    def __init__(self, min_len, max_len):
        self.min_len = min_len
        self.max_len = max_len
        self.values = {}

    def __get__(self, instance, owner_class):
        if instance:
            return self.values[id(instance)]
        return self

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError("value must be of type str")
        value = value.strip()
        if len(value) > self.max_len or len(value) < self.min_len:
            raise ValueError(f"String length must be greater than {self.min_len - 1} and less than {self.max_len + 1}")
        self.values[id(instance)] = (ref(instance, self._remove_object), value)

    def _remove_object(self, weak_ref):
        for key in self.values.keys():
            if self.values[key][0] is weak_ref:
                del self.values[key]


class Tester:
    __slots__ = '__weakref__'
    integer = IntegerField(1, 10)
    char = CharField(0, 200)