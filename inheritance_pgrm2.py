class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)

class teacher(Person):
    def __init__(self,name,age,subject):
        super().__init__(name,age)
        self.subject=subject
    def display(self):
        super().display()
        print("subject:",self.subject)

class student(Person):
    def __init__(self,name,age,rollno):
        super().__init__(name,age)
        self.rollno=rollno
    def display(self):
        super().display()
        print("Rollno:",self.rollno)

t=teacher("Raj",30,"Python")
t.display()
s=student("Ravi",20,101)
s.display()