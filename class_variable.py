class Human:
    planet = 'Earth'
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display(self):
        print("Name: ",self.name, " Age: ",self.age, Human.planet)
        
    @classmethod
    def class_method(cls):
        print("Class method>>>", cls.planet)
        
    @staticmethod
    def static_method():
        print("Static method>>>", Human.planet)
        

h1 = Human("khaing", 24)
h2 = Human("nyein", 35)
h1.school = "Nursing"
h1.planet = "Yangon"
print("h1", h1.__dict__)

h1.display()
h2.display()

Human.planet = "Mars"        
# h1 = Human("khaing", 24)
# h2 = Human("nyein", 35)
h1.display()
h2.display()

h1.class_method()
h1.static_method()

Human.class_method()
Human.static_method()