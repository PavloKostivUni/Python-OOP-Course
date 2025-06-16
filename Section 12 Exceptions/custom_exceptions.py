import json


class TimeoutError(Exception):
    """Timeout exception"""

try:
    raise TimeoutError('timeout occured')
except Exception as ex:
    print(repr(ex))

class ReadOnlyError(AttributeError):
    """Indicates an attribute is read-only"""

try:
    raise ReadOnlyError('Account number is read-only', 'BA10001')
except ReadOnlyError as ex:
    print(repr(ex))


class WebScraperException(Exception):
    """Base exception for WebScraper"""

class HTTPException(WebScraperException):
    """General HTTP exception for WS"""

class InvalidUrlException(HTTPException):
    """Indicates the url is invalid (dns lookup fail)"""

class TimeoutException(HTTPException):
    """Indicates a general timeout exception in http connectivity"""

class PingTimeoutException(TimeoutException):
    """Ping time out"""

class LoadTimeoutException(TimeoutException):
    """Page load time out"""

class ParserException(WebScraperException):
    """General page parsing exception"""

try:
    raise PingTimeoutException('Ping to www timed out....')
except WebScraperException as ex:
    print(repr(ex))



from http import HTTPStatus
from datetime import datetime

class APIException(Exception):
    """Base API exception"""

    http_status = HTTPStatus.INTERNAL_SERVER_ERROR
    internal_err_msg = 'API exception occurred'
    user_err_msg = 'We are sorry! An unexpected error occurred on our end'

    def __init__(self, *args, user_err_msg=None):
        if args:
            self.internal_err_msg = args[0]
            super().__init__(*args)
        else:
            super().__init__(self.internal_err_msg) 
        
        if user_err_msg is not None:
            self.user_err_msg = user_err_msg
        
    def to_json(self):
        err_object = {'status': self.http_status, 'message': self.user_err_msg}
        return json.dumps(err_object)
    
    def log_exception(self):
        exception = {
            'type': type(self).__name__,
            'http_status': self.http_status,
            'message': self.args[0] if self.args else self.internal_err_msg,
            'args': self.args[1:]
        }
        print(f'Exception: {datetime.now().isoformat()}: {exception}')


try:
    raise APIException('custom message', 10, 20, user_err_msg='custom user message')
except APIException as ex:
    print(repr(ex))
    print(ex.user_err_msg)
    print(ex.to_json())
    ex.log_exception()


class ApplicationException(APIException):
    """Indicates an application error (not user caused) - 5xx HTTP type errors"""
    http_status = HTTPStatus.INTERNAL_SERVER_ERROR
    internal_err_msg = 'Generic server side exception'
    user_err_msg = 'We are sorry, unexpected error occured'

class DBException(ApplicationException):
    """General database exception"""
    http_status = HTTPStatus.INTERNAL_SERVER_ERROR
    internal_err_msg = 'Database error'
    user_err_msg = 'We are sorry, unexpected error occured'
    
class DBConnectionError(DBException):
    """Indicates an error connecting to database"""
    http_status = HTTPStatus.INTERNAL_SERVER_ERROR
    internal_err_msg = 'Database connection error'
    user_err_msg = 'We are sorry, unexpected error occured'
    
class ClientException(APIException):
    """Indicates exception that was caused by user, not an internal error"""
    http_status = HTTPStatus.BAD_REQUEST
    internal_err_msg = 'Client submitted bad request'
    user_err_msg = 'A bad request was received'
    
class NotFoundError(ClientException):
    """Indicates resource was not found"""
    http_status = HTTPStatus.NOT_FOUND
    internal_err_msg = 'Resource not found'
    user_err_msg = 'Requested object does not exist'

class NotAuthorizedError(ClientException):
    """User is not authorized to perform requested action on resource"""
    http_status = HTTPStatus.UNAUTHORIZED
    internal_err_msg = 'Client not authorized to perform operation'
    user_err_msg = 'You are not authorized to perform this request'


class Account:
    def __init__(self, account_id, account_type):
        self.account_id = account_id
        self.account_type = account_type

def lookup_account_by_id(account_id):
    if not isinstance(account_id, int) or account_id <= 0:
        raise ClientException(f'Account number {account_id} is invalid',
                              f'account_id = {account_id}',
                              'type error - account number not an integer')

    if account_id < 100:
        raise DBConnectionError('Permanent failure connecting to database', 'db=db01')
    elif account_id < 200:
        raise NotAuthorizedError('User does not have permissions to read this account', f'account_id={account_id}')
    elif account_id < 300:
        raise NotFoundError('Account not found', f'account_id={account_id}')
    else:
        return Account(account_id, 'Savings')


def get_account(account_id):
    try:
        account = lookup_account_by_id(account_id)
    except APIException as ex:
        ex.log_exception()
        return ex.to_json()
    else:
        return HTTPStatus.OK, {'id': account.account_id, 'type': account.account_type}

print(get_account('abc'))
print(get_account(50))
print(get_account(150))
print(get_account(250))
print(get_account(350))


class AppException(Exception):
    """generic application exception"""

class NegativeIntegerError(AppException, ValueError):
    """Used to indicate an error when an integer is negative"""

def set_age(age):
    if age < 0:
        raise NegativeIntegerError('age cannot be negative')

try:
    set_age(-10)
except ValueError as ex:
    print(repr(ex))

ex = NegativeIntegerError()
print(isinstance(ex, AppException), isinstance(ex, ValueError))