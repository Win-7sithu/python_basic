class Animal:
    def __init__(self, name, age, sound):
        self.name = name
        self.age = age
        self.sound = sound
        #print("This is Parent Constructor.")
        
    def display(self):
        print(f"{self.name} is {self.age} years old.\n{self.name} says {self.sound}.")
        
class Dog(Animal):
    def __init__(self, name, age, sound):
        super().__init__(name, age, sound)
        #print("This is Dog Constrctor.")
        
        
class Cat(Animal):
    def __init__(self, name, age, sound):
        super().__init__(name, age, sound)
        #print("This is Cat Constructor.")
        
        
dog1 = Dog('Blacky', 4, 'Garrr')
cat1 = Cat('Kitty', 3, 'Meow')

dog1.display()
cat1.display()
        