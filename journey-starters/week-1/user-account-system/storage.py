import json
from errors import UserAlreadyExistsError, InvalidCredentialsError

FILE_PATH ="users.json"

def load_users()-> list:
    try:
        with open(FILE_PATH, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return[]
    
def save_users(users: list)-> None:
    with open(FILE_PATH, "w") as file:
        json.dump(users, file, indent=2)

def add_user(user: dict)-> None:
    users = load_users()
    for existing in users:
        if existing["username"] == user["username"]:
            raise UserAlreadyExistsError("user already exists")
    
    users.append(user)
    save_users(users)

def authenticate(username: str, password: str)-> dict:
    users= load_users()
    for user in users:
        if user["username"]== username and user["password"] == password:
            return user
    
    raise InvalidCredentialsError("Invalid username or password")


