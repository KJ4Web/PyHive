from abc import ABC, abstractmethod
class Vehicle(ABC):
    def __init__(self,brand):
        self.brand = brand
    @abstractmethod
    def startEngine(self):
        pass
    def description(self):
        print(self.brand)

class Car(Vehicle):
    def __init__(self, model, brand):
        super().__init__(brand)
        self.model = model
    def startEngine(self):
        print(f"{self.model} has a powerful engine.")
    def description(self):
        print(f"{self.model} is a powerful car and it is owned by the brand of {self.brand}.")

car1 = Car("S-MK4", "Supra")
car1.startEngine()
car1.description()