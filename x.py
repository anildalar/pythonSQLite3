from this import d


class A():
    
    #pass

    def helloA(self):
        print("Hello from A")


class B(A):
    #pass
    def __init__(self):
        super().helloA()
        
    def helloA(self):
        print("Hello from A")



# Now lets create a class

bObject = B()



