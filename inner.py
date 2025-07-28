class External:
    def __init__(self):
        print("External constructor.")
    
    def external_method(self):
        print("External Method.")
    
    class Internal:
        def __init__(self):
            print("Internal Constructor.")
            
        def internal_method(self):
            print("Internal Method.")
            
            
test = External()
#print(test.external_method())
#print(test.Internal.internal_method)