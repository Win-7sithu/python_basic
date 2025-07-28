#Saya Thet Khine Python Free Course

'''
num_subjects = int(input("Enter number of subjects: "))
marks = []

for i in range(num_subjects):
    mark = int(input("Enter marks of each subject: "))
    marks.append(mark)
    
print(marks)

'''
# subjects = ['myan', 'eng', 'math', 'science', 'history', 'geo']
# marks = []

# for i in range(len(subjects)):
#     print(subjects[i].title())
#     mark = int(input("Enter marks for each subjects: "))
#     marks.append(mark)
        
# # print(marks)
# flag = True
# pass_mark = 40
# extinction_mark = 80

# for mark in marks:
#     flag = flag and mark >= pass_mark
    
# if flag:
#     print("Pass")
# else:
#     print("Fail")

# subjects = ['myan', 'eng', 'math', 'science', 'history', 'geo']
# Pass = True
# pass_mark = 40

# for i in range(len(subjects)):
#     mark = int(input(f"Enter marks for {subjects[i].title()}: "))
#     Pass = Pass and mark >= pass_mark
    
# if Pass:
#     print("Pass")
# else:
#     print("Fail")

            
# lst = [1, 2, 3, 4]
# for i in lst:
#     i * 2 #In for loop, i value can't be accessed from outer.
#     print(i)
# print(lst)

# double= []
# for i in lst:
#     doub = i * 2
#     double.append(doub)
# print(double)

# for i in range(len(lst)):
#     lst[i] = lst[i] * 2
# print(lst)


my_list = [10, 20, 30, 40, 50]
user_num = int(input("Enter the number to find in the list: "))
found = False
index = 0

while not found and index < len(my_list):
    if my_list[index] == user_num:
        print("Found the number at index: ", index)
        found = True
    else:
        index += 1
        
print("End of the loop.")