import csv

with open('emp.csv', 'w', newline='') as file:
    w = csv.writer(file)
    w.writerow(["ENO", 'ENAME', 'ESAL', 'EADDR'])
    total = int(input("Enter employee number: "))
    
    for i in range(total):
        eno = int(input("Enter number: "))
        ename = input("Enter name: ")
        esal = int(input("Enter Salary: "))
        eaddr = input("Enter address: ")
        w.writerow([eno, ename, esal, eaddr])
        
print("Work Done.")
        