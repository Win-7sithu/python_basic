# class Stack():
#     def __init__(self):
#         print("Constructor run.")
        
# x = Stack()
# x 

class Stack:
    def __init__(self, max_length, lst = []):
        self.max_length = max_length
        self.lst = lst
        
    def push(self, ele):
        if len(self.lst) < self.max_length:
            self.lst.append(ele)
        else:
            print("Over max_length!")
            
    def pop(self):
        if not self.is_empty:
            return self.lst.pop()
        else:
            return None
    
    def is_empty(self):
        return len(self.lst) == 0
        
stack_1 = Stack(2)
stack_1.push(10)
stack_1.push(20)
# stack_1.push(30)
# stack_1.push(40)
print(stack_1)
print(stack_1.pop())
print(stack_1.pop())
        