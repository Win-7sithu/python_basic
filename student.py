class Student():
    def __init__(self, name, age):
        self._name = name
        self._age = age
        
    def display(self):
        print("Name: ", self._name, "Age: ", self._age)
        
    def set_age(self, new_age):
        if 0 < new_age < 100:
            self._age = new_age
        
        
    def get_age(self):
        return self._age
    
mgMg = Student("Mg Mg", 18)
mgMg.display()
mgMg.name = "Change form outside"
mgMg.display()

mgMg.set_age(40)
print("Above changed Age: ",mgMg.get_age())