#This program shows object instatiation (constructor)

class Addition(object):
    def add(self,a,b):
        self.a = a
        self.b = b
        c = a + b
        print(c)
        return c

addnum = Addition()

addnum.add(5,3)
addnum.add(6,9)
