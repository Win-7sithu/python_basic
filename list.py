# lst = eval(input("Enter a list: "))
# print(lst)
# print(type(lst))

# lst = list(range(0, 11, 2))
# print(lst)

# x = "nyein"
# l = list(x)
# print(l)

# x = "Teaching is best job."
# l = x.split()
# print(l)

# lst = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# print(lst[2:6:3])
# print(lst[4::-1])
# print(lst[-1::-1])
# print(lst[-1:-5:-1])
# print(lst[5:1000])
# print()

# #print the list items sequentially
# #using while loop

# lst = [10, 20, 30, 40, 50]
# i = 0

# while i < len(lst):
#     print(lst[i])
#     i += 1

# #using for loop
# lst = [10, 20, 30, 40, 50]
# for i in lst:
#     print(i)
    
    
# lst = [10,11, 20, 30, 40, 50,60, 71]
# for i in lst:
#     if i % 2 == 0:
#         print(i)
        
        
# names = ['nyein', 'khaing', 'thae']
# total = len(names)
# for i in range(total):
#     print(f"{names[i]}==>Positive Index: {i}<<>>Negative Index:{i-total}")
    
# lst = [10, 11, 13, 10, 55, 0, 10, 11, -1, 'a', -1, 'A', 'a']
# print("10: ",lst.count(10))
# print("0: ",lst.count(0))
# print("a: ",lst.count("a"))
# print()

# print("10 INDEX: ", lst.index(10))
# print("A index:", lst.index('A'))

# lst = []
# for i in range(30):
#     if i % 5 == 0:
#         lst.append(i)
# print(lst)

# lst = [1,2,3,4,5]
# lst.insert(10, 700)
# lst.insert(6, 1000)
# lst.insert(-100, 'what!')
# print(lst)

#Matrix 

lst = [[1, 2, 3],[4, 5, 6], [7, 8, 9]]
print(lst)
for i in lst:
    print(i)
    
for i in range(len(lst)):
    for j in range(len(lst[i])):
        print(lst[i] [j],end=' ')
    print()
