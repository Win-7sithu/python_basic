class Stack:
    def __init__(self, max_length):
        self.max_length = max_length
        self.lst = []
        print("Constructor Run!")
        
    def push(self, ele):
        if len(self.lst) < self.max_length:
            self.lst.append(ele)
        else:
            print("Error!")
            
    def is_empty(self):
        return len(self.lst) == 0
    
    def pop(self):
        if not self.is_empty():
            return self.lst.pop()
        else:
            return None 
        
s1 = Stack(3)
s1.push(10)
s1.push(10)
s1.push(10)
s1.push(10)
s1.push(10)
print(s1.is_empty())

print(s1.pop())
print(s1.pop())
print(s1.pop())
print(s1.pop())
print(s1.is_empty())