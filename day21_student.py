from day21_person import person
class student(person):
    def __init__(self, name, age, school):
        self.name = name
        self.age = age
        self.school = school
    
    def print_school(self):
        print(self.school)

    def print_age(self):
        return super().print_age()
    
    def print_age(slef):
        print(slef.school)

stu1 = student('k', 15, 'nthu')
stu1.print_age()