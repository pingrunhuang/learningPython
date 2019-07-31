class Scope(object):
    def func1(self, obj1, obj2):
        obj1 = 100
        obj2['bbb'] = 123
    
    def run(self):
        # this won't change because this is primitive type
        obj1 = 123421
        # this will change 
        obj2 = {'aaa':111}
        self.func1(obj1,obj2)
        print(obj1)
        print(obj2)

if __name__ == "__main__":
    s = Scope()
    s.run()