def func(v):
    i = v + 3
    return i

class MyClass:
    def __init__(self, a=1, b=2):
        self.a = a
        self.b = b
    
    def sum(self):
        return self.a + self.b
        
    def show_attriburtes(self):
        print("a = {}, b = {}, sum: {}".format(self.a, self.b, self.sum())
    
