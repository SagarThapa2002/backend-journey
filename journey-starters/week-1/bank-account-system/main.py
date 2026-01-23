from account import BankAccount
from exceptions import InvalidAmountError, InsufficientFundsError

def main()-> None:
    try:
        name = input("Enter account holder name: ").strip()
        account = BankAccount(name, balance =1000.00)

        while True:
            print("\n---  Bank Menu  ---")
            print("1. Show Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")

            choice = input("choose an option: ").strip()
            try:
                if choice == "1":
                    print(f"Current Balance: £{account.get_balance():.2f}")

                elif choice == "2":
                    amount = float(input("Enter deposit amount: "))
                    account.deposit(amount)
                    print("Deposit succesful.")

                elif choice == "3":
                    try:
                       amount = float(input("Enter withdrawal amount: "))
                       account.withdraw(amount)
                       print("withdrawal succesful.")
                    except ValueError:
                        print("please enter a valid number. ")
                    except InvalidAmountError as e:
                        print(f"Error: {e}")
                    except InsufficientFundsError as e:
                        print(f"Error: {e}")

                elif choice == "4":
                    print(f"Thank you, {account.holder_name} for using our Bank system.")
                    break

                else:
                    print("Invalid option. please choose 1-4.")

            except (InvalidAmountError, InsufficientFundsError, ValueError) as error:
                print(f"Error: {error}")

    except ValueError as error:
        print(f"Error: {error}")

if __name__ == "__main__":
    main()