#This program shows how to use setter and delete propery decorator

class CarModel(object):

    def __init__(self,name,year):
        self.name = name
        self.year = year

    @property   #setting the class as a property decorator
    def model(self):
        print("The Model is : ")
        model = '{} {}'.format(self.name,self.year)
        return model

    @property
    def price(self):
        return '{} {}'.format(self.name)

    @price.setter
    def price(self,name):
        self.name = name
        #self.cost = cost

car = CarModel("suzuki","2018")

car.name = 'bmw'
car.price = 'Audi'
print(car.model)  # Calling the model function like an attribute
