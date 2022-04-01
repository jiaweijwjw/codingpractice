class Person:
    def __init__(self, name, age, hobby):
        self._name = name
        self._age = age
        self. _hobby = hobby

    def greet(self):
        print(f"Hi, my name is {self._name}, I am {self._age} years old and my hobby is {self._hobby}.")

class Student(Person):
    def __init__(self, name, age, hobby):
        super().__init__(name, age, hobby)

    def greet(self):
        print(f"Hi, I am a student and my name is {self._name}. I am {self._age} years old and my hobby is {self._hobby}.")

john = Person("john", 25, "singing")
jack = Student("jack", 24, "swimming")
john.greet()
jack.greet()
print(jack._age)