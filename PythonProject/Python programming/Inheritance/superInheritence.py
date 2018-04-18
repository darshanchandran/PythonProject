#This program shows the use of super in Inheritance

class Car(object):

    def shape(self):
        print("Car has tyres")

class Audi(Car):  # Inherit Car in Audi class

    def shape(self):
        print("Audi has Fat tyre")
        super(Audi, self).shape()    #super class to get the feature from the parent class

car = Car()
audi = Audi()

car.shape()
audi.shape()
