from abc import abstractmethod, ABC

class Animal(ABC):
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

    @abstractmethod
    def eat(self):
        pass

class Dog(Animal):

    def speak(self):
        print(f"{self.name} barks.")
    def eat(self):
        print(f"{self.name} eat meat.")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} meows.")

    def eat(self):
        print(f"{self.name} eat fish.")


try:
    dog = Dog("Rex")
    cat = Cat("Whiskers")

    dog.speak()
    cat.speak()
    dog.eat()
    cat.eat()
except TypeError as e:
    print(f"Error: {e}")