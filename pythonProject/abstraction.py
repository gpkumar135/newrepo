from abc import ABC,abstractmethod

class car(ABC):
    def milage(self):
        pass
class Tesla(car):
    def milage(self):
        print("the car milage is 30")
class breeza(car):
    def milage(self):
        print("the car get milage of 23")
class honda(car):
    def milage(self):
        print("the car get milage of 20")

t =Tesla ()
t.milage()

b = breeza()
b.milage()

h = honda ()
h.milage()

