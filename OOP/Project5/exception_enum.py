from enum import Enum

class AppException(Enum):
    NotAnInteger = (100, ValueError, "Value is not an integer")

    def __new__(cls, code, exc_type, message):
        member = object.__new__(cls)
        member._value_ = code
        member._message = message
        member._exc_type = exc_type
        return member

    @property
    def code(self):
        return self.value

    @property
    def message(self):
        return self._message

    @property
    def exc_type(self):
        return self._exc_type

    def raises(self):
        raise self.exc_type(self.message)