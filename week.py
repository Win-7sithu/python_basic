week_list = ['Sunday', 'Monday', 'Tuesday', 'Wednesday','Thursday', 'Friday', 'Saturday']

try:
    day = int(input("Enter 0 to 6: "))
    print(f"Today is {week_list[day]}.")
except ValueError and IndexError:
    print("Enter only number: 0 to 6")