# *********************************School management system****************************
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
        print("invalid username or password")
    if attempts >= 3:
        print("Attempts Limit Range Completed!")
        exit()

print("=" * 20 + " Admin Panel " + "=" * 20)

import os

filename1 = "students.txt"
filename2 = "teachers.txt"
choice = input("Press 1 to see Students record & Press 2 to see Teachers record : ")

if choice.strip() == "1":
    attempts = 0
    while True:
        print("=" * 20 + " Student Login " + "=" * 20)
        username = input("username : ").strip()
        password = input("password : ").strip()

        if username == "student" and password == "student123":
            print("Successfully login")
            break
        else:
            attempts += 1
            print("inavalid username or password")
        if attempts >= 3:
            print("Attempts Limit Range Completed!")
            exit()

    print("=" * 20 + " Student Panel " + "=" * 20)

    while True:
        print("Press 1: View Data.")
        print("Press 2: Add Data.")
        print("Press 3: Remove Data.")
        print("Press 4: Update a record.")
        print("Press 5: Search a record.")
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
                new_list = []
                with open(filename1, "r") as file:
                    student_list = file.readlines()
                for student in student_list:
                    record = student.strip().split("||")

                    if record[1] == email.strip():
                        is_Found = True
                        student_list.remove(student)
                        break
                    new_list.append(student)
                if is_Found:
                    with open(filename1, "w") as file:
                        file.writelines(student_list)
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
                with open(filename1, "r") as file:
                    student_list = file.readlines()
                for student in student_list:
                    record = student.strip().split("||")

                    if record[1] == email:
                        is_found = True
                        update_record = f"{name}||{email}||{age}\n"
                        new_list.append(update_record)
                    else:
                        new_list.append(student)
                if is_found:
                    with open(filename1, "w") as file:
                        file.writelines(new_list)
                    print("record updated successfully...")
                else:
                    print("Record Not Found...")
                input()

            case 5:
                print("Find a record.")
                search_name = input("Search... : ").strip()
                found = False

                with open(filename1, "r") as file:
                    student_list = file.readlines()

                for student in student_list:
                    record = student.strip().split("||")
                    name = record[0].lower()

                    if search_name.lower() in name.lower():
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

        os.system("cls")


# duplicate code sam as above just undertand the logi

elif choice.strip() == "2":
    attempts = 0
    while True:
        print("=" * 20 + " Teacher Login " + "=" * 20)
        username = input("username : ").strip()
        password = input("password : ").strip()

        if username == "teacher" and password == "teacher123":
            print("Successfully login")
            break
        else:
            attempts += 1
            print("invalid username or password")
        if attempts >= 3:
            print("Attempts Limit Range Completed!")


    print("=" * 20 + " Teacher Panel " + "=" * 20)

    while True:
        print("Press 1: view data.")
        print("Press 2: add data.")
        print("Press 3: remove data.")
        print("Press 4: update a record.")
        print("Press 5: Search a record.")
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
                    teacher_list = file.readlines()
                for teacher in teacher_list:
                    record = teacher.strip().split("||")

                    if record[1] == email.strip():
                        is_Found = True
                        teacher_list.remove(teacher)
                        break
                    new_list.append(teacher)
                if is_Found:
                    with open(filename2, "w") as file:
                        file.writelines(teacher_list)
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
                    teacher_list = file.readlines()
                for teacher in teacher_list:
                    record = teacher.strip().split("||")

                    if record[1] == email:
                        is_found = True
                        update_record = f"{name}||{email}||{age}\n"
                        new_list.append(update_record)
                    else:
                        new_list.append(teacher)
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
                    teacher_list = file.readlines()

                for teacher in teacher_list:
                    record = teacher.strip().split("||")
                    name = record[0].lower()

                    if search_name.lower() in name.lower():
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
        os.system("cls")

else:
    print("Plz press 1 or 2...")