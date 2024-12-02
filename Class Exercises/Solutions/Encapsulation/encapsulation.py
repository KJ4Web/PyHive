class Vehicle:
    def __init__(self, color):
        self.color = color

    def vehicle_info(self):
        print(f"Vehicle Color: {self.color}")

class Taxi(Vehicle):
    def __init__(self, color, model, capacity, variant):
        super().__init__(color)
        self.__model = model
        self.__capacity = capacity
        self.__variant = variant

    def get_model(self):
        return self.__model

    def get_capacity(self):
        return self.__capacity

    def get_variant(self):
        return self.__variant

    def set_model(self, model):
        self.__model = model

    def set_capacity(self, capacity):
        self.__capacity = capacity

    def set_variant(self, variant):
        self.__variant = variant

    def vehicle_info(self):
        super().vehicle_info()
        print(f"Model: {self.__model}, Capacity: {self.__capacity}, Variant: {self.__variant}")

t1 = Taxi("Red", "Toyota Prius", 4, "Hybrid")
t2 = Taxi("Blue", "Honda Civic", 5, "Petrol")

t1.vehicle_info()
t2.vehicle_info()