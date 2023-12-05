class A:
    def __show(self):
        print("I am private method")
        
    def show1(self):
        print("Show1 Called...")
        self.__show()
        
obj = A()
obj.show1()