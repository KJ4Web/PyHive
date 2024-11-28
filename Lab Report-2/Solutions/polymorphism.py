class Transport:
    def calculate_cost(self, weight, distance):
        raise NotImplementedError("This method should be overridden by subclasses")

class Truck(Transport):
    def calculate_cost(self, weight, distance):
        return (weight * 0.5 + distance * 1.2)

class Ship(Transport):
    def calculate_cost(self, weight, distance):
        return (weight * 0.3 + distance * 0.8)

class Plane(Transport):
    def calculate_cost(self, weight, distance):
        return (weight * 0.8 + distance * 1.5)

def calculate_delivery_costs(transports, weight, distance):
    for transport in transports:
        cost = transport.calculate_cost(weight, distance)
        print(f"{transport.__class__.__name__} delivery cost: ${cost:.2f}")

transports = [Truck(), Ship(), Plane()]
weight = 50  
distance = 300 
calculate_delivery_costs(transports, weight, distance)