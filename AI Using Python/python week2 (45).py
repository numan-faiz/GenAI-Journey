# using try,except,else  and  finally blocks
# num=int(input("enter a number: "))
# print(10/num)
# try:
#     num=int(input("enter a number: "))
#     print(10/num)
# except ZeroDivisionError:
#     print("u cannot divide by zero")
# except ValueError:
#     print("that is not a number")
# except Exception as e:
#     print(f"unexpected error occur as ",{e})


try:
    print("running the code...")
except:
    print("error occured!")
else:
    print("no error found")
finally:
    print("done with!")