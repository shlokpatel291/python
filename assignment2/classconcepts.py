class vehicle:
    def __init__(self):
        print("constructor")

    def __del__(self):
        print("destructor called")

car= vehicle()
print("hello")

        
