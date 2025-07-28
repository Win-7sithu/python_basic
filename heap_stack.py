import sys

lst = [100, 200]
lst = None
lst1 = lst
print(lst1)
print("Reference Count: ", sys.getrefcount(lst))
lst = None
print(lst1)
print("Reference Count: ", sys.getrefcount(lst1))