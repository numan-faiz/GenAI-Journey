import json
import os

filename = "account.txt"

# --------- FILE CREATE IF NOT EXISTS ----------
if not os.path.exists(filename):
    default_data = {
        "username": "admin",
        "pin": "1234",
        "balance": 5000
    }
    with open(filename, "w") as file:
        json.dump(default_data, file)


# --------- LOGIN SYSTEM ----------
attempts = 0

while True:
    print("="*20 + " ATM LOGIN " + "="*20)
    username = input("Username: ").strip()
    pin = input("PIN: ").strip()

    with open(filename, "r") as file:
        data = json.load(file)

    if username == data["username"] and pin == data["pin"]:
        print("Login Successful!")
        break
    else:
        attempts += 1
        print("Invalid username or PIN")

    if attempts >= 3:
        print("Too many attempts. Account blocked.")
        exit()


# ---------NOW We GEN AI ENG NUMAN KHAN MAKE THE  ATM MENU ----------
while True:
    print("\n" + "="*20 + " ATM MENU " + "="*20)
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("0. Exit")

    choice = int(input("Enter choice: "))

    with open(filename, "r") as file:
        data = json.load(file)

    match choice:

        #Now WE GEN AI ENG NUMAN FAIZ CHECK BALANCE
        case 1:
            print("Your Balance is:", data["balance"])
            input()

        # DEPOSIT
        case 2:
            amount = int(input("Enter deposit amount: "))

            if amount > 0:
                data["balance"] += amount

                with open(filename, "w") as file:
                    json.dump(data, file)

                print("Money Deposited Successfully!")
            else:
                print("Invalid amount!")

            input()

        # WITHDRAW
        case 3:
            amount = int(input("Enter withdraw amount: "))

            if amount > 0:
                if amount <= data["balance"]:
                    data["balance"] -= amount

                    with open(filename, "w") as file:
                        json.dump(data, file)

                    print("Withdraw Successful!")
                else:
                    print("Insufficient Balance!")
            else:
                print("Invalid amount!")

            input()

        # OOPS THE LAST STEP IS FINALLY  EXIT
        case 0:
            print("Thank you for using ATM")
            break

        # DEFAULT
        case _:
            print("Invalid choice")
            input()