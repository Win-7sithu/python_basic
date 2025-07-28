def stack(max_length):
    lst = []
    def push(ele):
        if len(lst) < max_length:
            lst.append(ele)
        else:
            print("Over Maximum Length!")
            
    def pop():
        if not is_empty():
            return lst.pop()
        else:
            return None 
          
    def is_empty():
        return len(lst) == 0
    return (push, pop, is_empty)
        
push, pop, is_empty = stack(3)

print(stack(5))
# push(10)
# push(20)
# push(30)
# push(40)
# push(50)

# print(pop())
# print(pop())
# print(pop())
# print(pop())
# print(is_empty())




