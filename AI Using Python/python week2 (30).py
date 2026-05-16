# defining a class and creating
class car():
    def drive(self):
        print("the car is moving")
car1=car()
car1.drive()

# program#
class car:
    color="red"
    def drive(self):
        print(f"{self.color} car is start on the road")
car2=car()
car2.drive()

#prgoram3
class car():
    color="green"
    def drive(self):
        print(f"{self.color} is moving in my house")
    def setcolor(self,new_color):
        self.color= new_color

car3=car()
car3.setcolor("purple")
car3.drive()

