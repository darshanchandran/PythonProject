#This program shows override Explicitly Inheritance

class Car(object):
    def feature(self):
        print("Car has tyres")

class Audi(Car):  #Audi Inherits Car features
    def feature(self): # Define same function name in the child
        print("Audi has Fat tyres")

bmw = Car()
audi = Audi()

bmw.feature()
audi.feature()
