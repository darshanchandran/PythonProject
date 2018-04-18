#This program shows the use of compositions instead of inheritence

class Car(object):

    def shape(self):
        print("Car has tyres")

class Audi(object): #No class is being inherited

    def __init__(self):  # initializing self with other Car class
        self.car = Car()

    def shape(self):
        print("Audi has fat tyres")
        self.car.shape()

car = Car()
car.shape()
audi = Audi()
audi.shape()
