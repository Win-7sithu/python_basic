class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        #print("Human Constructor.")
        
    def work(self):
        print("Human ", self.name.title(), "works.")
        
class Doctor(Human):
    def __init__(self, name, age, medical_field):
        super().__init__(name, age)
        self.medical_field = medical_field
        #print("Doctor class constructor.")
        
    def work(self):
        super().work()
        print(self.name.title(), " treats patients.")
    
class Engineer(Human):
    def __init__(self, name, age, field):
        super().__init__(name, age)
        self.field = field
        
class Robot:
    def __init__(self):
        pass
    
    def work(self):
        print("Robot works.")
        
h = Doctor("Tint Shwe", 40, 'Heart')
h.work()

h = Engineer("kyaw swar", 38, 'Construction')
h.work()

h = Robot()
h.work()