#This program shows how compositions work with out inheriting the parent class

class Parent(object):
    def boss(self):
        print("I'm the boss")

class Child(object):
    def __init__(self):
        self.child = Parent()

    def boss(self):
        print("Child is the boss")
        self.child.boss()

son = Child()
son.boss()
