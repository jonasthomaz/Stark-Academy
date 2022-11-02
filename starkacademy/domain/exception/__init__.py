class InternalException(Exception):
    def __init__(self, message, code=500):
        self.code = code
        self.message = message
        super().__init__(self, message)


class NotFoundException(InternalException):
    def __init__(self, message):
        super().__init__(message=message, code=404)
