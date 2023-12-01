class information:
    def __init__(self,year,brand,model,fuel):
        self.year=year
        self.brand=brand
        self.model=model
        self.fuel=fuel

    def display(self):
        print("Year:",self.year)
        print("Brand:",self.brand)
        print("Model:",self.model)

class car(information):
    def printc(self):
        print("Car infomation:")
        self.display()
        print("Fuel Efficiency:", self.fuel, "mile/gallon")


class motor(information):


    def printm(self):
        print("Motor Cycle infomation:")
        self.display()
        print("Fuel Efficiency:", self.fuel,"mile/gallon")


class bicycle(information):

    def printb(self):
        print("Bicycle infomation:")
        self.display()



def main():
    Car=car(2023,"Toyoto","Camry",30.5)
    Motor=motor(2023,"Honda","CBR6009RR",40.2)
    Bicycle=bicycle(2023,"Trek","Mountain Bike",50)
    Car.printc()
    Motor.printm()
    Bicycle.printb()

if __name__ == '__main__':
    main()