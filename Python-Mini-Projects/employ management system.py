# ********************************* Employee Management System ****************************

import os

attempts = 0
while True:
    print("=" * 20 + " Login " + "=" * 20)
    username = input("username : ").strip()
    password = input("password : ").strip()

    if username == "admin" and password == "admin123":
        print("Successfully login")
        break
    else:
        attempts += 1
        print("invalid username or password")
    if attempts >= 3:
        print("Attempts Limit Range Completed!")
        exit()

print("=" * 20 + " Admin Panel " + "=" * 20)

filename1 = "managers.txt"
filename2 = "staff.txt"
choice = input("Press 1 to see Managers record & Press 2 to see Staff record : ")

if choice.strip() == "1":
    attempts = 0
    while True:
        print("=" * 20 + " Manager Login " + "=" * 20)
        username = input("username : ").strip()
        password = input("password : ").strip()

        if username == "manager" and password == "manager123":
            print("Successfully login")
            break
        else:
            attempts += 1
            print("invalid username or password")
        if attempts >= 3:
            print("Attempts Limit Range Completed!")
            exit()

    print("=" * 20 + " Manager Panel " + "=" * 20)

    while True:
        print("Press 1: View Data.")
        print("Press 2: Add Data.")
        print("Press 3: Remove Data.")
        print("Press 4: Update a record.")
        print("Press 5: Search a record.")
        print("Press 0: exit")

        try:
            choice = int(input("choice : "))
        except ValueError:
            print("Please enter a number!")
            continue

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
                            print("Name :" + record[0])
                            print("Email :" + record[1])
                            print("Age :" + record[2])

                except FileNotFoundError:
                    with open(filename1, "x"):
                        print("file created")
                except Exception as e:
                    print(e)
                input()
            case 2:
                print("Add Record")
                with open(filename1, "a") as file:
                    name = input("Name : ").strip()
                    email = input("Email: ").strip()
                    age = input("Age: ").strip()
                    file.write(f"{name}||{email}||{age}\n")

                    print("added")
                    input()
            case 3:
                print("remove a record")
                email = input("email : ").strip()

                is_Found = False
                with open(filename1, "r") as file:
                    employee_list = file.readlines()

                new_list = []
                for employee in employee_list:
                    record = employee.strip().split("||")
                    if record[1] == email.strip():
                        is_Found = True
                        continue  # Skip this record to "delete" it
                    new_list.append(employee)

                if is_Found:
                    with open(filename1, "w") as file:
                        file.writelines(new_list)
                        print("record deleted!")
                else:
                    print("Record Not Found.")
                input()
            case 4:
                print("update a record")
                email = input("Email to update : ").strip()
                name = input("New Name : ").strip()
                age = input("New Age : ").strip()

                is_found = False
                new_list = []
                with open(filename1, "r") as file:
                    employee_list = file.readlines()
                for employee in employee_list:
                    record = employee.strip().split("||")

                    if record[1] == email:
                        is_found = True
                        update_record = f"{name}||{email}||{age}\n"
                        new_list.append(update_record)
                    else:
                        new_list.append(employee)
                if is_found:
                    with open(filename1, "w") as file:
                        file.writelines(new_list)
                    print("record updated successfully...")
                else:
                    print("Record Not Found...")
                input()

            case 5:
                print("Find a record.")
                search_name = input("Search Name... : ").strip()
                found = False

                with open(filename1, "r") as file:
                    employee_list = file.readlines()

                for employee in employee_list:
                    record = employee.strip().split("||")
                    name = record[0].lower()

                    if search_name.lower() in name:
                        found = True
                        print("=" * 10)
                        print("Name : ", record[0])
                        print("Email : ", record[1])
                        print("Age : ", record[2])

                if not found:
                    print("Name Not Found! ")
                input()
            case _:
                print("invalid choice")

        os.system("cls" if os.name == "nt" else "clear")

elif choice.strip() == "2":
    attempts = 0
    while True:
        print("=" * 20 + " Staff Login " + "=" * 20)
        username = input("username : ").strip()
        password = input("password : ").strip()

        if username == "staff" and password == "staff123":
            print("Successfully login")
            break
        else:
            attempts += 1
            print("invalid username or password")
        if attempts >= 3:
            print("Attempts Limit Range Completed!")
            exit()

    print("=" * 20 + " Staff Panel " + "=" * 20)

    while True:
        print("Press 1: view data.")
        print("Press 2: add data.")
        print("Press 3: remove data.")
        print("Press 4: update a record.")
        print("Press 5: Search a record.")
        print("Press 0: exit")

        try:
            choice = int(input("choice : "))
        except ValueError:
            print("Please enter a number!")
            continue

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
                            print("Name :" + record[0])
                            print("Email :" + record[1])
                            print("Age :" + record[2])

                except FileNotFoundError:
                    with open(filename2, "x"):
                        print("file created")
                except Exception as e:
                    print(e)
                input()
            case 2:
                print("Add Record")
                with open(filename2, "a") as file:
                    name = input("Name : ").strip()
                    email = input("Email: ").strip()
                    age = input("Age: ").strip()
                    file.write(f"{name}||{email}||{age}\n")

                    print("added")
                    input()
            case 3:
                print("remove a record")
                email = input("email : ").strip()

                is_Found = False
                new_list = []
                with open(filename2, "r") as file:
                    staff_list = file.readlines()
                for staff in staff_list:
                    record = staff.strip().split("||")

                    if record[1] == email.strip():
                        is_Found = True
                        continue
                    new_list.append(staff)
                if is_Found:
                    with open(filename2, "w") as file:
                        file.writelines(new_list)
                        print("record deleted!")
                else:
                    print("Record Not Found.")
                input()
            case 4:
                print("update a record")
                email = input("Email : ").strip()
                name = input("Name : ").strip()
                age = input("Age : ").strip()

                is_found = False
                new_list = []
                with open(filename2, "r") as file:
                    staff_list = file.readlines()
                for staff in staff_list:
                    record = staff.strip().split("||")

                    if record[1] == email:
                        is_found = True
                        update_record = f"{name}||{email}||{age}\n"
                        new_list.append(update_record)
                    else:
                        new_list.append(staff)
                if is_found:
                    with open(filename2, "w") as file:
                        file.writelines(new_list)
                    print("record updated successfully...")
                else:
                    print("Record Not Found...")
                input()

            case 5:
                print("Find a record.")
                search_name = input("Search... : ").strip()
                found = False

                with open(filename2, "r") as file:
                    staff_list = file.readlines()

                for staff in staff_list:
                    record = staff.strip().split("||")
                    name = record[0].lower()

                    if search_name.lower() in name:
                        found = True
                        print("=" * 10)
                        print("Name : ", record[0])
                        print("Email : ", record[1])
                        print("Age : ", record[2])

                if not found:
                    print("Name Not Found! ")
                input()
            case _:
                print("invalid choice")
        os.system("cls" if os.name == "nt" else "clear")

else:
    print("Plz press 1 or 2...")