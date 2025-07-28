# class Parent:
#     def __init__(self):
#         print("Parent Constructor.")
        
#     def method1(self):
#         print("Method 1 Call.")
        
#     @classmethod
#     def method2(cls):
#         print("Method 2 ClassMethod Call.")
        
#     @staticmethod
#     def method3():
#         print("Method 3 StaticMethod Call.")
        
# class Child(Parent):
#     def __init__(self):
#         super().__init__()
#         super().method1()
#         super().method2()
#         super().method3()
        
# c1 = Child()
# c1.method1()
# # c1.method2()
# # c1.method3()

class User:
    user_created = 0
    
    def __init__(self, name, age):
        self.name = name
        self.age = int(age)
        User.user_created += 1
        
    @classmethod
    def from_string(cls, user_info):
        name, age = user_info.split(",")
        return cls(name.strip(), age.strip())
    
    def show(self):
        print(f"Name: {self.name}, Age: {self.age}")
    
    @classmethod
    def how_many_users(cls):
        print(f"{cls.user_created} users created.")
        

raw_users = ["aung aung, 22", "khaing, 25", 'thae, 27', 'nyein, 36'] 
users = []

for raw in raw_users:
    user = User.from_string(raw)
    users.append(user)
    
# for u in users:
#     u.show()
print(users)
        
# u1 = User('mg mg')
# u2 = User('khaing')
# u3 = User('nyein')
# u1.how_many_users()
# User.how_many_users()
