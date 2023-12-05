class AB:
    
    def show(self):
        try:
            a = "11"+12
            print(a)
        except Exception as e:
            print(e)
        else:
            print("Code Successfully exicuted")
        finally:
            print("I am always exicute...")
            
obj = AB()
obj.show()