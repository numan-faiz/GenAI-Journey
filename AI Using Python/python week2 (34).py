# encapsulation in python---->public and private attributes
# means keeping all the data(attributes) and methods of an object
# inside that object
# private attributes data of class  cannot be accessible outside the class
# only access inside the class


# class student:
#     def __init__(self,name,grade):
#         #
#         private attritbute
#         self.__grade=grade
# student1=student("ali",90)
# print(student1.__grade)


class student:
    def __init__(self,name,grade):
        self.__grade=grade
    def get_grade(self):
        return self.__grade
student2=student("numan","a")
print(student2.get_grade())


class student:
    @property
    def grade(self):
        return self.__grade
    def __init__(self,name,grade):
        self.__grade=grade
    def get_grade(self):
        return self.__grade
    def set_grade(self,grade):
        if 0<=grade <=100:
            self.__grade=grade
        else:
            print("invalid input")

student5=student("ali",90)
student5.set_grade(95)
# student5.get_grade()
print(student5.get_grade())







