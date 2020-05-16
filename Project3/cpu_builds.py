#TODOS, test, and refactor code

class Resource:

    def __init__(self, name, manufacturer, total, allocated): 
        self.name = name
        self.manufacturer = manufacturer
        check_pos_int(total)
        check_pos_int(allocated)
        self._total = total
        self._allocated = allocated

    @property
    def name(self):
        return self._name

    @property
    def manufacturer(self):
        return self._manufacturer

    @property
    def total(self):
        return self._total
    
    @property
    def allocated(self):
        return self._allocated

    @property
    def category(self):
        return self.name.lower()

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("name must be of type string.")

    @manufacturer.setter
    def manufacturer(self, manufacturer):
        if not isinstance(manufacturer, str):
            raise TypeError("name must be of type string.")

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"Resource(name = {self.name}, 
            manufacturer = {self.manufacturer}, 
            total = {self.total}, 
            allocated = {self.allocated})"
    
    def claim(self, n):
        check_pos_int(n)
        if n <= self.total:
            self._total -= n
            self._allocated += n
        elif self.total > 0:
            print(f"Insufficient resources to allocate {n}, allocating remaining {self.total}")
            self._allocated += self._total
            self._total = 0
        else:
            raise ValueError("No available resources to allocate.")

    def freeup(self, n):
        check_pos_int(n)
        if n <= self.allocated:
            self._total += n
            self._allocated -= n
        elif self.allocated > 0:
            print(f"Insufficient resources to allocate {n}, freeing up remaining {self.allocated}")
            self._total += self._allocated
            self._allocated = 0
        else:
            raise ValueError("No allocated resources to free up.")

    def died(self, n):
        check_pos_int(n)
        if n <= self.total:
            self.total -= n
        else:
            raise ValueError(f"Cannot remove {n} of this resource, only {self.total} remaining")

    def purchased(self, n):
        check_pos_int(n)
        self._total += n 
    
    @staticmethod
    def check_pos_int(n):
        if not isinstance(n, int):
            raise TypeError("The argument must be an integer.")
        if n < 0:
            raise ValueError("Argument must be greater than 0.")


class CPU(Resource):

    def __init__(self, cores, socket, power_watts, **args):
        check_pos_int(cores)
        check_pos_int(power_watts)
        if not isinstance(socket, str):
            raise TypeError("socket must be of type string.")
        self._cores = cores
        self._socket = socket
        self._power_watts = power_watts
        super(**args)

    @property
    def cores(self):
        return self._cores

    @property
    def socket(self):
        return self._socket

    @property
    def power_watts(self):
        return self._power_watts

class Storage(Resource):

    def __init__(self, capacity, **args):
        check_pos_int(capacity)
        self.capacity_gb = capacity
        self.super(**args)

    @property
    def capacity(self):
        return self._capacity_gb


class HDD(Storage):

    def __init__(self, size, rpm, **args):
        check_pos_int(size)
        check_pos_int(rpm)
        self._size = size
        self._rpm = rpm
        self.super(**args)

    @property
    def size(self):
        return self._size

    @property
    def rpm (self):
        return self._rpm

class SDD(Storage):

    def __init__(self, interface, **args):
        if not isinstance(interface, str):
            raise TypeError("interface must be of type string")
        self.interface = interface
        self.super(**args)

    @property
    def interface(self):
        return self._interface