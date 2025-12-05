# Q7. Create a class Person that allows the constructor to work with:

#  name only
#  name + age
#  name + age + address

# as direct costructor overloading (multiple constructors) are not allowed but we have to use default parameters to simulate constructor overloadning.

class Person:
    def __init__(self, name, age = None, address = None):
        self.name = name
        self.age = age
        self.address = address

p1 = Person("Amit")
p2 = Person("Amit", 20)
p3 = Person("Amit", 20, "Gujrat")

print(p1.name, p1.age, p1.address)
print(p2.name, p2.age, p2.address)
print(p3.name, p3.age, p3.address)