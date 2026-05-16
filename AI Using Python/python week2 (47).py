# creating custom exception in python
class InvalidError(Exception):
    pass
# -------------------------->age=int(input("enter age: "))
# if age<0:
#     raise InvalidError("age cannot be negative") ye code extra hy ye error show
# agar age negative hva or try except tak nahi jaega ok
age=int(input("enter age: "))
if age<0:
    raise InvalidError("age cannot be negative")
try:
    age=int(input("enter age: "))
    if age<0:
        raise InvalidError(f"age cannot be negative",{age})
except InvalidError as e:
    print(e)