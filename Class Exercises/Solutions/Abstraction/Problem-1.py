from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass
class Car(Vehicle):
    def __init__(self, name, model):
        self.name = name
        self.model = model
    def start(self):
        print(f"The Car called {self.name} starts the engine.")
    def stop(self):
        print(f"The brand of {self.model} is {self.name},stops the engine.")

class MotorCycle(Vehicle):
    def __init__(self, name, brand):
        self.name = name
        self.brand = brand
    def start(self):
        print(f"The Bike called {self.name} starts the engine.")
    def stop(self):
        print(f"The brand of {self.name} is {self.brand},stops the engine.")

car1 = Car("Supra", "S-MK4")
car1.start()
car1.stop()

moto1 = MotorCycle("Ninja H2", "Kawasaki")
moto1.start()
moto1.stop()