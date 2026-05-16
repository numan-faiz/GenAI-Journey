# instance variable and instance method
# 1. Instance Variables (Attributes)
# Ye wo variables hote hain jo har object ke liye alag (unique) hote hain.
# Inhein hamesha __init__ method ke andar self ke sath likha jata hai.
#
# Misaal: Agar 10 students hain, to har student ka "Roll Number" aur "Naam" alag hoga.
# Wo unke instance variables hain.
#
# 2. Instance Methods (Functions)
# Ye wo functions hote hain jo class ke andar banaye jate hain aur objects ke data
# (variables) par kaam karte hain. Inka pehla argument hamesha self hota hai.
#
# Misaal: Student ka result calculate karna ya uski details print karna.

class student():
    def __init__(self,name,age,grade):
        self.name="numan"
        self.age=22
        self.grade="A"

    def display(self):
        print(f"student name is: ",self.name)
        print(f"student age is:",self.age)
        print(f"student grade is:",self.grade)
    def is_eligible(self):
        if self.age>=15:
            print(self.name,"is eligible for admission.")
        else:
            print(self.name,"is not eligible for admission.")
s1=student("numan","12","A")
s1.display()
s1.is_eligible()