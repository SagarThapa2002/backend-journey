class UserError(Exception):
    pass

class UserAlreadyExistsError(UserError):
    pass

class InvalidCredentialsError(UserError):
    pass

class ValidationError(UserError):
    pass