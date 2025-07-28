# user_input = input("Enter some string: ")
# i = 0
# for u1 in user_input:
#     print(i, "index", u1)
#     i += 1
    
# print()

# l = eval(input("Enter some list: "))
# total = 0

# for i in l:
#     total += i
# print("Addition", total)

#while loop

# a = 1

# while a <= 4:
#     print(a)
#     a += 1
    
# print()

#Addition of  the first n numbers

# num = int(input("Enter a number: "))
# total = 0
# index = 1

# while index <= num:
#     total += index
#     index += 1
# print(f"Addition of first {num} number: ", total)
    
# name = ""
# while name != 'khaing':
#     name = input("Enter your name: ")
# print("Done!")

# name = input("Enter your name: ") ဒီလို input ကို while loop ထဲထည့်မရေးတာက infinity loop ဖြစ်သွားတယ်။ 
# while name != 'nyein':
#     name = name
#     print("Enter again")
# print("Done.")

#nested loop

# for i in range(3):
#     for j in range(3):
#         print("i", i, "j", j)

# lst = [15, 18, 22, 25]
# for i in lst:
#     if i > 18:
#         print("The location is here.")
#     print(i)
    
# for i in range(len(lst)):
#     print(f"Index {i}: {lst[i]}")
    
# for i in range(8):
#     if i == 6:
#         print("Stop at", i)
#         break
#     print(i)

lst = [12, 4, 34, 19, 0, 3, 18, 32, 50]

# for i in lst:
#     if i >= 18:
#         continue
#     print(i)
    
# lst_1 = lst
# lst_1.insert(2, 0)
# for i in lst_1:
#     if i == 0:
#         continue
#     print(f"30 / {i} = {30/i}")
    
# print(lst_1)

# lst = [11, 24, 61, 43, 60, 59]
# for i in lst:
#     if i >= 60:
#         break
#     print(i)
# else:
#     print("Done.")

for i in range(101):
    if i % 2 != 0:
        continue
    print(i)