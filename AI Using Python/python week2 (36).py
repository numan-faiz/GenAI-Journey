# inheritance mean parents to child
# inheritance allow a new class to reuse the properties and method
# of existing class

class animal:
    def speak(self):
        print("some sound")
class dog(animal):
    pass
dog1=dog()
dog1.speak()


class dog(animal):
    def bark(self):
        print("wooof")
childog=dog()
childog.speak()
childog.bark()