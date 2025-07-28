#Write a program the sum of every tenth number from 0 to 100, using a while loop.


# for i in range(0, 110, 10):
#     print(i)
    
# print(sum(range(0, 110, 10)))

# lst =[0,10,20,30,40,50,60,70,80,90,100]
# print(sum(lst))

counter = 0
total = 0

while counter <= 100:
    if counter % 10 == 0:
        total += counter
    counter += 1
print("Total", total)