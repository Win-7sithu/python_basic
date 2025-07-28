class Student():
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        self._name = new_name
        
    @property
    def age(self):
        return self._age    
    
    @age.setter
    def age(self, new_age):
        print("Setter Run!")
        if 0 < new_age < 100:
            self._age = new_age
        else:
            print("Invalid input!")
        
    def display(self):
        print("Name: ", self._name, "Age: ", self._age)


class School:
    def __init__(self):
        self._student_list = []
    
    def enroll(self, student):
        print("Student:", student.name, " have been enrolled.")
        self._student_list.append(student)
        
mgMg = Student("Mg Mg", 18)
mgMg.display()
# mgMg.name = "Change form outside"
# mgMg.display()
print("Name Changed: ", mgMg.name)

mgMg.age = 40
print("Above changed Age: ",mgMg.age)
print()

school_1 = School()
school_1.enroll(mgMg)