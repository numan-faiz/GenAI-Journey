# polymorphism--->overriding and overloading
class dog:
    def speak(self):
        print("woof")
class cat:
    def speak(self):
        print("meo!")
for pet in [dog(),cat()]:
    pet.speak()

# metthod overriding
class vehicle:
    def move(self):
        print("car is moving")
class car(vehicle):
    def move(self):
        print("car is driving")
car1=car()
car1.move()

# method overloading---in this we use mutliple form of single function but
# diffrentiate the arguments
# Jab ek hi class me same naam ka method ho lekin different number ya type of
# parameters ke sath use kiya jaye, to usay method overloading kehte hain.

class calculator:
    # b = 0, c = 0 its adefualt argument
    def add(self,a,b=0,c=0):
        return a+b+c
calc1=calculator()
print(calc1.add(5))
print(calc1.add(5,10))
print(calc1.add(5,6,7))
