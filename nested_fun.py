def f1():
    x = 1
    print("f1: ", x)
    def f2():
        print("f2:", x + 1)
        def f3():
            nonlocal x
            x += 2
            print("f3: ", x)
        f3()
    f2()
    
    
f1()
