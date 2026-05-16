# conditional statement part 2

# elif condition
# score=95
# score=int(input("enter your score: "))
# if score>90:
#     print("A+")
# elif score>=80:
#     print("A")
# else:
#     print("try again")

# nested if statement

# age=18
# country="pakistan"
# # age=int(input("enter ur age"))
# if age>=18:
#       country=input("enter ur country")
#     if country=="pakistan":
#         print("you cant vote pakistan")
# else:
#     print("u cannot vote pakistan")
# else:
#      print("you cannot vote")
# combine condition
# age=18
# country="pakistan"
age=int(input("enter ur age"))
country=input("enter ur country") #.capitalize() use for first word capital automatically
if age>18 and country=="pakistan":
    print("eligible voter")
else:
    print("not eligible")

# # marks=90
# marks=int(input("enter ur marks: "))
# if marks>90:
#     print("A+")
# elif marks>80:
#     print("A")
# elif marks>70:
#     print("B+")
# elif marks>60:
#     print("B")
# else:
#     print("F")
