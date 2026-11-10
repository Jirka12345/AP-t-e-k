import random
from datetime import datetime

class Car:
    def __init__(self, brand:str, model:str, year:int, stkYear:int, fuel:int = 100):
        self.brand = brand
        self.model = model
        self.year = year
        self.stkYear = stkYear
        self.fuel = fuel
        pass

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year}) - palivo: {self.fuel}"
    
    def move(self):
        usage = random.randint(5,20)
        if self.fuel >= usage:
            self.fuel -= usage
            return f"{self.brand} {self.model} spotřeboval {usage} % paliva a zbývá mu {self.fuel} %."
        else:
            return f"{self.brand} {self.model} by do cíle nedoje. Potřebuje {usage} % paliva, ale má jen {self.fuel} %."
        
    def fullfill(self):
        filled = 100 - self.fuel
        self.fuel = 100
        return f"{self.brand} {self.model} natankoval {filled}"
    
    def STK(self):
        if self.stkYear < datetime.now().year:
            return f"Nemaš STK zařiď si to woe."
        else:
            return f"Na STK musíš až za {self.stkYear - datetime.now().year}"


car1 = Car("Škoda", "Octavia 3", 2016,2026,85)
car2 = Car("Dai", "Grc", 2018, 2022,3)
car3 = Car("ToToja", "Hilux", 2014, 2028, 34)

#testovací výpis
print(40 * "-")
print(car1)
print(car2)
print(car3)
print(40 * "-")

#testovaci jízdy
print(40 * "-")
print(car1.move())
print(car1.move())
print(40 * "-")
print(car2.move())
print(car2.move())
print(40 * "-")
print(car3.move())
print(car3.move())
print(40 * "-")

#testování STK
print(car1.STK())
print(car2.STK())
print(car3.STK())

class Garage:
    def __init__(self, name:str):
        self.name = name
        self.cars = []
        pass

    def addCar(self, car:Car):
        self.cars.append(car)
        return f"Do garaže {self.name} bylo přidano auto: {car.model}"
    
    def showCars(self):
        if len(self.cars) == 0:
            print(f"V garáži {self.name}")
        else:
            print(f"Auta v garáži: {self.name}")
        print(f"Auta v garáži: {self.name}")
        for car in self.cars:
            print("-->", car)

    def oldestCar(self):
        if len(self.cars) == 0:
            return None
        theOldest = min(self.cars, key = lambda a: a.year)
    
    def avgFuel(self):
        if len(self.cars) == 0:
            return 0
        return sum(car.fuel for car in self.cars)

garage = Garage("Orange county Choppers")
garage.showCars()
print(40 * "=")
print(garage.addCar(car1))
print(garage.addCar(car2))
print(garage.addCar(car3))
print(40 * "=")
print(garage.showCars())

print("---Nejstarší auto---")
oldest = garage.oldestCar()
if oldest:
    print(f"Nejstarší auto v garáži je {oldest.brand} {oldest.model} ({oldest.year})")

print("---Průměrná hodnota paliva---")
print(f"{garage.avgFuel():.1f}%")

print("---Jízda specifického auta v garáži---")
print(garage.cars[2].move())
for bramborák in garage.cars:
    print(bramborák.move())

print("---Hromadná kontrola STK---")
for HadakKadak in garage.cars:
    print(HadakKadak.STK())