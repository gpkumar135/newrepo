class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print (f"{self.name} says hello!")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    # def speak(self):
    #     print(f"{self.name} says bow-bow")

dog =Dog("Charlie","hfuf")

dog.speak()

