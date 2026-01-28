from errors import ValidationError

def validate_username(username: str)-> None:
    if not username or len(username) < 3:
        raise ValidationError("Username must be at least 3 characters")
    
def validate_password(password: str)-> None:
    if len(password)<6:
        raise ValidationError("Password must be at least 6 digits")

def validate_email(email: str)-> None:
    if "@" not in email or ".com" not in email:
        raise ValidationError("Invalid email address")