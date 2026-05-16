# using getters and setters
# getters-->getters are the function to get data attributes  of class
# setters--> use for set data attributes in classs

class student:
    def grade(self):
        return self.__grade
    def __init__(self,name,grade):
        self.__grade=grade
    def get__grade(self):
        return self.__grade
    def set__grade(self,grade):
        if 0<= grade <=100:
            self.__grade=grade
        else:
            print("invalid input")
student=student("arsal",89)
student.set__grade(67)
print(student.get__grade())
