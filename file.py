file = open('note.txt', 'w')

print("Name", file.name)
print("Mode", file.mode)
print("Readable", file.readable())
print("Writeable", file.writable())
print("Is closed", file.closed)

word = "Hello"
for i in word:
    i += " World\n"
    file.write(i)
    
for i in range(0, 101, 2):
    file.write(f"Even Number: {str(i)}\n")
    
print("Out of loop.")
file.close()
print("Is closed", file.closed)