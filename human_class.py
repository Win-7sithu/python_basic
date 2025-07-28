class Human:
    def __init__(self, name, age, location):
        self.name = name
        self.age = age
        self.location = location
        
    def get_pronoun(self):
        female_name = ('a','e','i', 'j', 'l', 'm', 's')
        return "She" if self.name.lower().startswith(female_name) else "He"
        
    def work(self):
        pronoun = self.get_pronoun()
        print(f"{self.name.title()} is {self.age} years old.\n{pronoun} works at {self.location.title()}.")
        
class Doctor(Human):
    def __init__(self, name, age, location):
        super().__init__(name, age, location)
        
class Teacher(Human):
    def __init__(self, name, age, location):
        super().__init__(name, age, location)
        

        
        
h = Doctor("david", 25, "new york")
h.work()

h = Teacher("jenny", 27, 'london')
h.work()
        