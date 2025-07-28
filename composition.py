class Engine:
    def __init__(self):
        print("Engine Constructor.")
        
    def start(self):
        print("Engine Starts.")
        
class Car:
    def __init__(self):
        print("Car Constructor.")
        self.engine = Engine()
    
    def start(self):
        print("Car Starts.")
        self.engine.start()
        
c = Car()
c.start()
        