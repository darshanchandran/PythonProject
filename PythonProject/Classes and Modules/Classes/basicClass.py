# This is a simple python class file
# A class named Employee has been created
class Employee(object):

    hike_percent = 10   # this is a class / global variable

    def __init__(self,name,age,pay):  # init will self initialize when the class object is created
        self.name = name
        self.age = age
        self.pay = pay

    def display(self):
        print(f"Name is {self.name} , age is {self.age} , pay is {self.pay}")

    def hike(self):
        self.pay1 = (int(self.pay) * int(self.hike_percent)) / int(100)
        self.pay = int(self.pay) + int (self.pay1)
        print(self.hike_percent)
        print(self.pay)

    @classmethod
    def set_hike_percent(cls,amount):
        cls.hike_percent = amount
        return cls.hike_percent


    #pass      # pass keyword is like skip for now

emp1 = Employee('a','22','300000')       #emp1 and emp2 are the new instances or object of the class Employee
emp2 = Employee('b','44','150000')

emp1.display()
emp1.hike()

Employee.set_hike_percent(9)

emp1.display()
emp1.hike()
