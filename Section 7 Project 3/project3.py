from numbers import Real
import pytest

class Resource:
    def __init__(self, name, manufacturer, total, allocated):
        self.name = name
        self.manufacturer = manufacturer
        self.check_real_pos(total, "Total")
        self._total = total
        self.check_allocated(allocated)
        self._allocated = allocated
    
    def check_real_pos(self, value, name):
        if not isinstance(value, Real) or value <= 0:
            raise ValueError(f"{name} must be a real positive number")
    
    def check_allocated(self, value):
        if not isinstance(value, Real) or value <= 0:
            raise ValueError("Allocated must be a real positive number")
        if(value > self.total):
            raise ValueError("Allocated can't be bigger than the total number")
    
    @property
    def total(self):
        return self._total
        
    @property
    def allocated(self):
        return self._allocated
    
    def __str__(self):
        return f"Resource name: {self.name}"

    def __repr__(self):
        return f"Resource name: {self.name}; manufacturer: {self.manufacturer};" \
                f" total amount: {self.total}; allocated: {self.allocated}"
    
    def claim(self, amnt):
        self.check_real_pos(amnt, "Claimed amount")
        self.check_allocated(self.allocated + amnt)
        self._allocated += amnt
    
    def freeup(self, amnt):
        self.check_real_pos(amnt, "Freed amount")
        self.check_allocated(self.allocated - amnt)
        self._allocated -= amnt
    
    def died(self, amnt):
        self.check_real_pos(amnt, "Dead resources")
        if self.allocated < amnt:
            raise ValueError("Amount of dead resources cannot exceed the allocated")
        self._allocated -= amnt
        self._total -= amnt
    
    def purchased(self, amnt):
        self.check_real_pos(amnt, "Purchased resources")
        self._total += amnt
    
    @property
    def category(self):
        return f"Name: {self.__class__.__name__}".lower()
    

class CPU(Resource):
    def __init__(self, name, manufacturer, total, allocated, cores, socket, power_watts):
        super().__init__(name, manufacturer, total, allocated)
        self.cores = cores
        self.socket = socket
        self.power_watts = power_watts
    
    def __repr__(self):
        return f"Resource name: {self.name}; manufacturer: {self.manufacturer};" \
                f" total amount: {self.total}; allocated: {self.allocated}" \
                f" cores amount: {self.cores}; socket: {self.socket}; power: {self.power_watts} Watts."
    
    @property
    def cores(self):
        return self._cores
    
    @cores.setter
    def cores(self, num):
        self.check_real_pos(num, "Number of cores")
        self._cores = num
    
    @property
    def power_watts(self):
        return self._power_watts
    
    @power_watts.setter
    def power_watts(self, num):
        self.check_real_pos(num, "Power watts")
        self._power_watts = num


class Storage(Resource):
    def __init__(self, name, manufacturer, total, allocated, capacity_GB):
        super().__init__(name, manufacturer, total, allocated)
        self.capacity_GB = capacity_GB
    
    def __repr__(self):
        return f"Resource name: {self.name}; manufacturer: {self.manufacturer};" \
                f" total amount: {self.total}; allocated: {self.allocated}; capacity: {self.capacity_GB} GB."
    
    @property
    def capacity_GB(self):
        return self._capacity_GB
    
    @capacity_GB.setter
    def capacity_GB(self, GB):
        self.check_real_pos(GB, "Capacity in GB")
        self._capacity_GB = GB


class HDD(Storage):
    def __init__(self, name, manufacturer, total, allocated, capacity_GB, size, rpm):
        super().__init__(name, manufacturer, total, allocated, capacity_GB)
        self.size = size
        self.rpm = rpm
    
    def __repr__(self):
        return f"Resource name: {self.name}; manufacturer: {self.manufacturer};" \
                f" total amount: {self.total}; allocated: {self.allocated}; capacity: {self.capacity_GB} GB;" \
                f" size: {self.size}; RPM: {self.rpm}."
    
    @property
    def rpm(self):
        return self._rpm
    
    @rpm.setter
    def rpm(self, rpm):
        self.check_real_pos(rpm, "RPM")
        self._rpm = rpm


class SSD(Storage):
    def __init__(self, name, manufacturer, total, allocated, capacity_GB, interface):
        super().__init__(name, manufacturer, total, allocated, capacity_GB)
        self.interface = interface
    
    def __repr__(self):
        return f"Resource name: {self.name}; manufacturer: {self.manufacturer};" \
                f" total amount: {self.total}; allocated: {self.allocated}; capacity: {self.capacity_GB} GB;" \
                f" interface: {self.interface}."


r1 = Resource("Rtx 3060 Ti", "Nvidia", 25, 15)

print(r1.allocated)
r1.claim(4)
print(r1.allocated)
try:
    r1.claim(7)
except:
    pass
print(r1.allocated)

r1.freeup(10)
print(r1.allocated)
try:
    r1.freeup(10)
except:
    pass
print(r1.allocated)

r1.died(5)
print(r1.allocated)
print(r1.total)
try:
    r1.died(5)
except:
    pass
print(r1.allocated)
print(r1.total)

r1.purchased(50)
print(r1.total)

print(r1.category)

s1 = SSD("Hyper", "Kingston", 10, 5, 512, "ipc15")
print(s1.__repr__())