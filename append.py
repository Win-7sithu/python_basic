file = open('note.txt', 'a')

# word = "Hello"
# for i in word:
#     i += " World\n"
#     file.write(i)
    
# for i in range(0, 101, 2):
#     file.write(f"Even Number: {str(i)}\n")
    
names = ['nyein','khaing', 'thae']
for name in names:
    file.write(f"{name.title()}\t")
    
    
print("Out of loop.")
file.close()
print("Is closed", file.closed)