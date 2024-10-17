# Parent class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

# Child class (inherits from Person)
class Student(Person):
    def __init__(self, name, age, student_id):
        # Initialize the parent class using super()
        super().__init__(name, age)
        self.student_id = student_id

    # Method specific to Student
    def display_student_info(self):
        self.display_info()  # Call method from parent class
        print(f"Student ID: {self.student_id}")

# Create an object of the Student class
student1 = Student("John", 22, "S12345")

# Access the methods
student1.display_student_info()
