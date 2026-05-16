# constructor method
class dog:
    def __init__(self):
        self.name="buddy"
    def bark(self):
        print(f"{self.name} says woops")
dog1=dog()
dog1.bark()



class car:
    def __init__(self,brand,color):
        self.brand=brand
        self.color=color
car2=car("toyota","pink")
print(car2.brand)
print(car2.color)
car2.color="green"
print(car2.color)
car3=car("honda","white")
print(car3.brand)
print(car3.color)