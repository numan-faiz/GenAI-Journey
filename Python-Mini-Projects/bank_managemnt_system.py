# ********************************* Bank management system ****************************

attempts = 0
while True:
    print("=" * 20 + " Login " + "=" * 20)
    username = input("username : ").strip()
    password = input("password : ").strip()

    if username == "admin" and password == "123456":
        print("Successfully login")
        break
    else:
        attempts += 1
        print("inavalid username or password")
    if attempts >= 3:
        print("Attempts Limit Range Completed!")
        exit()

print("=" * 20 + " Admin Panel " + "=" * 20)

import os

filename1 = "current_accounts.txt"
filename2 = "saving_accounts.txt"
choice = input("Press 1 to see Current Accounts & Press 2 to see Saving Accounts : ")

if choice.strip() == "1":
    attempts = 0
    while True:
        print("=" * 20 + " Current Account Login " + "=" * 20)
        username = input("username : ").strip()
        password = input("password : ").strip()

        if username == "banker" and password == "banker123":
            print("Successfully login")
            break
        else:
            attempts += 1
            print("inavalid username or password")
        if attempts >= 3:
            print("Attempts Limit Range Completed!")
            exit()

    print("=" * 20 + " Current Account Panel " + "=" * 20)

    while True:
        print("Press 1: View All Accounts.")
        print("Press 2: Open New Account (Add Record).")
        print("Press 3: Close Account (Remove Record).")
        print("Press 4: Deposit Money.")
        print("Press 5: Withdraw Money.")
        print("Press 0: exit")

        choice = int(input("choice : "))

        match choice:
            case 0:
                break
            case 1:
                print("View all records")
                try:
                    with open(filename1, "r") as file:
                        count = 0
                        for record in file:
                            count += 1
                            record = record.strip().split("||")
                            print("=" * 10, count, "=" * 10)
                            print("Acc Num :" + record[0])
                            print("Name :" + record[1])
                            print("Balance :" + record[2])

                except FileNotFoundError:
                    with open(filename1, "x"):
                        print("file created")
                except Exception as e:
                    print(e)
                input()
            case 2:
                print("Open New Account")
                with open(filename1, "a") as file:
                    acc_num = input("Acc Num : ").strip()
                    name = input("Name: ").strip()
                    balance = input("Initial Deposit: ").strip()
                    file.write(f"{acc_num}||{name}||{balance}\n")

                    print("added")
                    input()
            case 3:
                print("Close Account")
                acc_num = input("Acc Num : ").strip()

                is_Found = False
                new_list = []
                with open(filename1, "r") as file:
                    account_list = file.readlines()
                for account in account_list:
                    record = account.strip().split("||")

                    if record[0] == acc_num.strip():
                        is_Found = True
                        account_list.remove(account)
                        break
                    new_list.append(account)
                if is_Found:
                    with open(filename1, "w") as file:
                        file.writelines(account_list)
                        print("record deleted!")
                else:
                    print("Record Not Found.")
                input()
            case 4:
                print("Deposit Money")
                acc_num = input("Acc Num : ").strip()
                amount = float(input("Enter Amount to Deposit : "))

                is_found = False
                new_list = []
                with open(filename1, "r") as file:
                    account_list = file.readlines()
                for account in account_list:
                    record = account.strip().split("||")

                    if record[0] == acc_num:
                        is_found = True
                        current_balance = float(record[2])
                        new_balance = current_balance + amount
                        update_record = f"{record[0]}||{record[1]}||{new_balance}\n"
                        new_list.append(update_record)
                        print(f"Deposited successfully! New Balance: {new_balance}")
                    else:
                        new_list.append(account)
                if is_found:
                    with open(filename1, "w") as file:
                        file.writelines(new_list)
                else:
                    print("Record Not Found...")
                input()

            case 5:
                print("Withdraw Money")
                acc_num = input("Acc Num : ").strip()
                amount = float(input("Enter Amount to Withdraw : "))

                is_found = False
                new_list = []
                with open(filename1, "r") as file:
                    account_list = file.readlines()
                for account in account_list:
                    record = account.strip().split("||")

                    if record[0] == acc_num:
                        is_found = True
                        current_balance = float(record[2])
                        if current_balance >= amount:
                            new_balance = current_balance - amount
                            update_record = f"{record[0]}||{record[1]}||{new_balance}\n"
                            new_list.append(update_record)
                            print(f"Withdrawn successfully! Remaining Balance: {new_balance}")
                        else:
                            print("Insufficient Balance!")
                            new_list.append(account)
                    else:
                        new_list.append(account)
                if is_found:
                    with open(filename1, "w") as file:
                        file.writelines(new_list)
                else:
                    print("Record Not Found...")
                input()
            case _:
                print("invalid choice")

        os.system("cls")


# duplicate code sam as above just undertand the logic

elif choice.strip() == "2":
    attempts = 0
    while True:
        print("=" * 20 + " Saving Account Login " + "=" * 20)
        username = input("username : ").strip()
        password = input("password : ").strip()

        if username == "banker" and password == "banker123":
            print("Successfully login")
            break
        else:
            attempts += 1
            print("inavalid username or password")
        if attempts >= 3:
            print("Attempts Limit Range Completed!")


    print("=" * 20 + " Saving Account Panel " + "=" * 20)

    while True:
        print("Press 1: View All Accounts.")
        print("Press 2: Open New Account (Add Record).")
        print("Press 3: Close Account (Remove Record).")
        print("Press 4: Deposit Money.")
        print("Press 5: Withdraw Money.")
        print("Press 0: exit")

        choice = int(input("choice : "))

        match choice:
            case 0:
                break
            case 1:
                print("View all records")
                try:
                    with open(filename2, "r") as file:
                        count = 0
                        for record in file:
                            count += 1
                            record = record.strip().split("||")
                            print("=" * 10, count, "=" * 10)
                            print("Acc Num :" + record[0])
                            print("Name :" + record[1])
                            print("Balance :" + record[2])

                except FileNotFoundError:
                    with open(filename2, "x"):
                        print("file created")
                except Exception as e:
                    print(e)
                input()
            case 2:
                print("Open New Account")
                with open(filename2, "a") as file:
                    acc_num = input("Acc Num : ").strip()
                    name = input("Name: ").strip()
                    balance = input("Initial Deposit: ").strip()
                    file.write(f"{acc_num}||{name}||{balance}\n")

                    print("added")
                    input()
            case 3:
                print("Close Account")
                acc_num = input("Acc Num : ").strip()

                is_Found = False
                new_list = []
                with open(filename2, "r") as file:
                    account_list = file.readlines()
                for account in account_list:
                    record = account.strip().split("||")

                    if record[0] == acc_num.strip():
                        is_Found = True
                        account_list.remove(account)
                        break
                    new_list.append(account)
                if is_Found:
                    with open(filename2, "w") as file:
                        file.writelines(account_list)
                        print("record deleted!")
                else:
                    print("Record Not Found.")
                input()
            case 4:
                print("Deposit Money")
                acc_num = input("Acc Num : ").strip()
                amount = float(input("Enter Amount to Deposit : "))

                is_found = False
                new_list = []
                with open(filename2, "r") as file:
                    account_list = file.readlines()
                for account in account_list:
                    record = account.strip().split("||")

                    if record[0] == acc_num:
                        is_found = True
                        current_balance = float(record[2])
                        new_balance = current_balance + amount
                        update_record = f"{record[0]}||{record[1]}||{new_balance}\n"
                        new_list.append(update_record)
                        print(f"Deposited successfully! New Balance: {new_balance}")
                    else:
                        new_list.append(account)
                if is_found:
                    with open(filename2, "w") as file:
                        file.writelines(new_list)
                else:
                    print("Record Not Found...")
                input()

            case 5:
                print("Withdraw Money")
                acc_num = input("Acc Num : ").strip()
                amount = float(input("Enter Amount to Withdraw : "))

                is_found = False
                new_list = []
                with open(filename2, "r") as file:
                    account_list = file.readlines()
                for account in account_list:
                    record = account.strip().split("||")

                    if record[0] == acc_num:
                        is_found = True
                        current_balance = float(record[2])
                        if current_balance >= amount:
                            new_balance = current_balance - amount
                            update_record = f"{record[0]}||{record[1]}||{new_balance}\n"
                            new_list.append(update_record)
                            print(f"Withdrawn successfully! Remaining Balance: {new_balance}")
                        else:
                            print("Insufficient Balance!")
                            new_list.append(account)
                    else:
                        new_list.append(account)
                if is_found:
                    with open(filename2, "w") as file:
                        file.writelines(new_list)
                else:
                    print("Record Not Found...")
                input()
            case 6:
                print("invalid choice")
        os.system("cls")

else:
    print("Plz press 1 or 2...")