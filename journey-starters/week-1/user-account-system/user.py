from validators import validate_username, validate_password, validate_email

class user:
    def __init__(self, username: str, password: str, email: str):
        validate_username(username)
        validate_password(password)
        validate_email(email)

        self.username = username
        self.password = password
        self.email = email

    def to_dict(self) -> dict:
        return {
            "username": self.username,
            "password": self.password,
            "email": self.email
        }