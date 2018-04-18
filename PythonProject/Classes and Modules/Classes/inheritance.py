# This program shows how inheritance works

#Create a parent/base class

class Parent(object):
    def boss(self):
        print("i'm the boss")

# Create a child/sub class inheriting from Parent class

class Child(Parent):
    pass

#calling the parent and the child/subclass

boss1 = Parent()
boss2 = Child()
boss1.boss()
boss2.boss()

#Overriding the parent class(do this by creating the same function in the subclass)

class ChildOne(Parent):
    def boss(self):
        print("Child one is the boss")

boss3=ChildOne()
boss3.boss()

#Overriding with a super class (call the function of base class )

class ChildTwo(Parent):
    def boss(self):
        print("This is Overriding , before calling the super parent")
        super(Parent,self).boss()
        print("This is after calling the super class")
