class Money:
    def __init__(self, value):
        self.value = value
        
    def __add__(self, other):
        #return self.value + self.other
        return Money(self.value + other.value)
    

    
m1 = Money(10)
m2 = Money(20)
m3 = m1 + m2
print(m3.value)
        