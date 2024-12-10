class UnfoundException(Exception):
    "Raised when item is not found in persistance layer"
    pass


class AlreadyCompletedException(Exception):
    "Raised when item is already completed"
    pass


class BadDataException(Exception):
    "Raised when given data is wrong"
    pass


class UnknownException(Exception):
    "Raised when an unkown error happens"
    pass
