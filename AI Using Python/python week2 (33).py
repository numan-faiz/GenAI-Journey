# accessing objects  attributes and methods
class student():
    def __init__(self,name,age,course):
        self.name=name
        self.age=age
        self.course=course
    def display(self):
        print(f"student name is : ",{self.name})
        print(f"student age is : ",{self.age})
        print(f"student course is : ",{self.course})
    def is_eligilbe(self):
        if self.age>=15:
            print("u can eligilbe for admission")
        else:
            print("u cannot eligible")
student1=student("numan",34,"gen ai")
student2=student("ali",72,"loka chuppi")

# accessing attributes now
print(student1.name)
print(student2.age)

# calling methods
student1.display()
student1.is_eligilbe()
student2.display()
student2.is_eligilbe()