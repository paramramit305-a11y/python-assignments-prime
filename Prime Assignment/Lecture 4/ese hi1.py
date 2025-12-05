class student:
    def __init__(self, name, cgpa):
        self.name = name
        self.cgpa = cgpa

    def get_cgpa(self):
        return self.cgpa
    
stu1 = student("Rahul", 8.1)
stu2 = student("Amit", 9.8)
stu3 = student("Shradhha", 9.2)

print(f"{stu1.name} hsa cgpa = {stu1.get_cgpa()}")
print(f"{stu2.name} hsa cgpa = {stu2.get_cgpa()}")
print(f"{stu3.name} hsa cgpa = {stu3.get_cgpa()}")