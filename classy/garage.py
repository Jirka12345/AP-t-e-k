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
    
garage = Garage("Orange county Choppers")
print(garage.addCar(car1))
print(garage.addCar(car2))
print(garage.addCar(car3))