class Destructor:
    def __init__(self):
        print("Destructor.")
        self.lst = [x for x in range(100000)]
        
    def dele(self):
        self.lst = None
        
test = Destructor()
#print(test.lst)

test.dele()
print(test.lst)