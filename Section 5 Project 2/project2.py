import operator
from functools import total_ordering

@total_ordering
class Mod:
    def __init__(self, value, modulus):
        self.init_check(value, modulus)
        self._modulus = modulus
        self._value = value % self.modulus
    
    def init_check(self, value, modulus):
        if not isinstance(modulus, int):
            raise TypeError("Modulus must be an integer")
        if not isinstance(value, int):
            raise TypeError("Value must be an integer")
    
    def __eq__(self, other):
        if isinstance(other, int):
            return self.value == other % self.modulus
        if isinstance(other, Mod):
            return self.value == other.value and self.modulus == other.modulus
        raise TypeError("Modulus can be only compared to an integer and other modulus")
    
    def __hash__(self):
        return hash((self.modulus, self.value))
    
    def __neg__(self):
        return Mod(-self.value, self.modulus)
    
    def __int__(self):
        return self.value
    
    def __repr__(self):
        return f"Mod(value = {self.value}, modulus = {self.modulus})"
    
    def __add__(self, other):
        return self._perform_operation(other, operator.add, "Addition")
    
    def __iadd__(self, other):
        return self._perform_operation(other, operator.add, "In-place addition", in_place=True)
    
    def __sub__(self, other):
        return self._perform_operation(other, operator.sub, "Subtraction")
    
    def __isub__(self, other):
        return self._perform_operation(other, operator.sub, "In-place subtraction", in_place=True)
    
    def __mul__(self, other):
        return self._perform_operation(other, operator.mul, "Multiplication")
    
    def __imul__(self, other):
        return self._perform_operation(other, operator.mul, "In-place multiplication", in_place=True)
    
    def __pow__(self, other):
        return self._perform_operation(other, operator.pow, "To the power")
    
    def __ipow__(self, other):
        return self._perform_operation(other, operator.pow, "In-place power", in_place=True)
    
    def __lt__(self, other):
        other_value = self._get_value(other, "Less than")
        return self.value < other_value
    
    # def __gt__(self, other):
    #     other_value = self._get_value(other, "Greater than")
    #     return self.value > other_value
    
    # def __le__(self, other):
    #     other_value = self._get_value(other, "Less equal than")
    #     return self == other and self.value < other_value
    
    # def __ge__(self, other):
    #     other_value = self._get_value(other, "Greater equal than")
    #     return self == other and self.value > other_value
    
    def _get_value(self, other, operation_name):
        if isinstance(other, int):
            return other % self.modulus
        if isinstance(other, Mod):
            if self.modulus == other.modulus:
                return other.value
            raise TypeError(f"{operation_name} operation can only be performed on Mod with the same modulus")
        raise TypeError(f"{operation_name} operation can only be performed with integer or other Mod ")
    
    def _perform_operation(self, other, op, op_name, in_place = False):
        other_value = self._get_value(other, op_name)
        new_value = op(self.value, other_value)
        if in_place:
            self._value = new_value % self.modulus
            return self
        else:
            return Mod(new_value, self.modulus)

    @property
    def value(self):
        return self._value
    
    @property
    def modulus(self):
        return self._modulus


m1 = Mod(15, 5)
m2 = Mod(3, 5)
m3 = Mod(15, 5)

print(m1)
print(m1 == m3)
print(f"Hash: {hash(m1)}")

m_sum = m1+m2
print(m_sum)

print(m1 > m2)
print(m1 < m2)
print(m1 >= m3)

print(Mod(3, 12) + Mod(5, 12))

print(m2 * m2)

