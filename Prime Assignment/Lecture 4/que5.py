# Q5. Create a base class Vehicle with attributes like brand and model.
# Create two subclasses Car and Bike that add extra attributes - seats (in Car) & engine_cc (in Bike).

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class Car(Vehicle):
    def __init__(self, brand, model, seats):
        super().__init__(brand, model)
        self.seats = seats

class Bike(Vehicle):
    def __init__(self, brand, model, engine_cc):
        super().__init__(brand, model)
        self.engine_cc = engine_cc

c1 = Car("Toyota", "Fortuner", 7)
print(c1.brand, c1.model, c1.seats)