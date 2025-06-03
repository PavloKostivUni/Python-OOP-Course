from enum import Enum, unique

@unique
class AppException(Enum):
    def __new__(cls, value, exception, message):
        member = object.__new__(cls)
        member._value_ = value
        member.exception = exception
        member.message = message
        return member
    
    def throw(self, message = None):
        if message is None:
            message = self.message
        raise self.exception(message)
    
    @property
    def code(self):
        return self.value

    NotAnInteger = (100, ValueError, 'Value is not an integer')
    NotAChar = (101, ValueError, 'Value is not a character')
    ExceedsMaxLimit = (201, ValueError, 'Value exceeds maximum limit')
    ExceedsMinLimit = (202, ValueError, 'Value exceeds minimum limit')


print(AppException.NotAnInteger.value)
print(AppException(201))
print(AppException['ExceedsMinLimit'])

try:
    AppException.NotAChar.throw("Custom message")
except ValueError as ex:
    print(ex)