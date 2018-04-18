#This program shows impicit Inheritance

class Car(object):
    def feature(self):
        print("Car has tyres")

class Audi(Car):  #Audi Inherits Car features
    pass

bmw = Car()
audi = Audi()

bmw.feature()
audi.feature()
