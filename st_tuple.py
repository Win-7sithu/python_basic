def push(st, ele):
    if len(st[0]) < st[1]:
        st[0].append(ele)
    else:
        print("Error!")
        

def pop(st):
    if len(st[0] > 0):
        return st[0].pop()
    else:
        return None
    
    
def is_empty(st):
    return len(st[0])  == 0

        
my_stack = []
max_length = 5
st = (my_stack, max_length)

push(st, 100)
push(st, 200)
push(st, 300)
push(st, 400)
push(st, 500)
push(st, 600)
print(my_stack)
        