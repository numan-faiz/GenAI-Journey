# method overriding:
# Jab child class apne parent class ke same method ko dobara likh kar change kar de,
# to usay method overriding kehte hain.

class animal():
    def bark(self):
        print("dark barked")
class dog(animal):
    def bark(self):
        print("woof,woof")
dog1=dog()
dog1.bark()