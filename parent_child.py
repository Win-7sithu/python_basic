class Parent:
    var_one = "var one of parent"
    def __init__(self):
        self.ver_two = "instance of parent"
        print("Parent Constructor.")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child constructor.")
    
    def methodOne(self):
        print("Child method.", super().var_one.title())
        print("Instance of Parent: ", super().ver_two)
        
c = Child()
c.methodOne()