import csv


# with open('emp.csv', 'r') as file:
#     read_file = csv.reader(file)
#     lst_csv.append(read_file)



file = open('emp.csv', 'r')    
file_read = csv.reader(file)
lst_csv = list(file_read)

for items in lst_csv:
    for i in items:
        print(i, '\t', end='')
    print()
    
# print(lst_csv)