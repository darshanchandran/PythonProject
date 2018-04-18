# This program shows the use of __init__ method

class CarModel(object):
    """docstring for CarModel."""
    def __init__(self, model, year):

        self.model = model
        self.year = year

    def cost(self):
        if self.model == 'suzuki':
            print(self.model)
            print(Cost.suzuki())
        else:
            Cost.mahindra()

class Cost(object):
    def suzuki():
        cost = 10000
        return cost
    def mahindra():
        cost = 15000
        return cost

car = CarModel("szuki","1999")
print(car.cost())
