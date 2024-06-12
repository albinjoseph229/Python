class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        print("Dog barks")

# Creating instances of the classes
animal = Animal("Generic Animal")
dog = Dog("Buddy", "Labrador")

# Calling methods on the instances
animal.speak()  # Output: Animal speaks
dog.speak()     # Output: Dog barks