# Q9. Create the following classes: Herbivore, Carnivore, Omnivore with some attributes and methods. Then Create a class Bear that inherits from all the above classes to showcase how multiple inheritance works.


class Herbivore:
    def __init__(self,):
        self.type = "Herbivore"

    def eat_plants(self):
        print("Eats plants")

class Carnivore:
    def __init__(self):
        self.type = "Carnivore"

    def eat_meat(self):
        print("Eats meat")

class Omnivore:
    def __init__(self):
        self.type = "Omnivore"

    def eat_both(self):
        print("Eat Plants and meat both")

class Bear(Herbivore, Carnivore, Omnivore):
    def __init__(self):
        Herbivore.__init__(self)
        Carnivore.__init__(self)
        Omnivore.__init__(self)

b1 = Bear()
b1.eat_plants()
b1.eat_meat()
b1.eat_both()