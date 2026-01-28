from user import user
from storage import add_user, authenticate
from errors import UserError

def main():
    print("\n --- User Account System --- ")
    print("1. Create a account")
    print("2. Login")
    choice= input("choice option: ")

    try:
        if choice == "1":
            username = input("username: ")
            password = input("Password: ")
            email = input("Email: ")

            user = user(username, password, email)
            add_user(user.to_dict())
            print("User registered successfully")

        elif choice == "2":
            username = input("username: ")
            password = input("password: ")

            user= authenticate(username, password)
            print("\n login successful!")
            print(f"welcome {user['userna,e']}({user['email']})")
        else:
            print("Invalid option.")
        
    except UserError as error:
        print(f"Error: {error}")

if __name__ == "__main__":
    main()