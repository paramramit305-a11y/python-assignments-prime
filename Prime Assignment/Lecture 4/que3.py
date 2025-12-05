# Q3. Create a class student with private attributes _name, _roll_no, and _marks.
# provide getter and setter methods with validation (e.g., marks cannot be negative, roll no has to between 1 & 100 name cannot be empty).

class Student:
    def __init__(self, _name, _roll_no, _marks):
        self._name = _name
        self._roll_no = _roll_no
        self._marks = _marks

#     GETTERS:

    def get_name(self):
        return self._name
    
    
    def get_roll_no(self):
        return self._roll_no
    
    def get_marks(self):
        return self._marks
    
    
#     SETTERS:

    def set_name(self, name):
        if name == "":
          print("error")

        else:
            self._name = name

    def set_roll_no(self, roll_no):
        if roll_no <= 100 and roll_no >= 1:
           self._roll_no = roll_no

        else:
            print("error..")
    
    def set_marks(self, marks):
        if marks < 0:
            print("error")

        else:
            self._marks = marks

            
s1 = Student("Amit", 34, 100)
s1.set_name("Amit")
s1.set_roll_no(34)
s1.set_marks(100)

print(s1.get_name())
print(s1.get_roll_no())
print(s1.get_marks())