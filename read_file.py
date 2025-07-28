# with open('note.txt', 'r') as file:
#     content = file.read()
#     print(content)

# with open('note.txt', 'r') as file:
#     for line in file:
#         print(line, end='')

# def file_read(filename):
#     with open(filename, 'r') as file:
#         return file.read()
    
# x = file_read('note.txt')
# #print(x)
    
#Create the generator

def file_readline(filename):
    with open(filename, 'r') as file:
        for line in file:
            yield line.strip()
            
reader = file_readline('note.txt')
    
def get_next_line():
    try:
        return next(reader)
    except StopIteration:
        return "No more line!"

# x = get_next_line()
print(list(get_next_line()))
print(get_next_line().split(','))
print(get_next_line())


# def file_readlines(filename):
#     with open(filename, 'r') as file:
#         for line in file:
#             return file.readlines()

# x = file_readlines('note.txt')
# print(x)
# print(x)
# print(x)