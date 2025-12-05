# Q.6 Create an abstract class Employee with an abstract method
# calculate_salary().
# Create subclasses Intern, FullTimeEmployee, and ContractEmployee that implement the method differently.\

from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def calc_salary(self):
        pass

class Intern(Employee):
    def __init__(self, stipend):
        self.stipend = stipend

    def calc_salary(self):
        return self.stipend
    
class FullTimeEmployee(Employee):
    def __init__(self, base, hra, bonus):
        self.base = base
        self.hra = hra
        self.bonus = bonus

    def calc_salary(self):
        return self.base + self.hra + self.bonus
    
class ContractEmployee(Employee):
    def __init__(self, rate, hours):
        self.rate = rate
        self.hours = hours

    def calc_salary(self):
        return self.rate * self.hours
    
I1 = Intern(40000)
print(I1.calc_salary())