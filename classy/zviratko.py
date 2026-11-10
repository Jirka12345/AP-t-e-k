import random
from datetime import datetime

class Zvire:
    def __init__(self,druh:str,jmeno:str,rok_narozeni:int,rok_prohlidky:int,energie:int):
        self.druh = druh
        self.jmeno = jmeno
        self.rok_narozeni = rok_narozeni
        self.rok_prohlidky = rok_prohlidky
        self.energie = energie
        pass

    def __str__(self):
        return f"{self.druh} {self.jmeno} ({self.rok_narozeni}) - {self.energie}%."
    
    def play(self):
        spotreba_energie = (random.randint(5,20))
        if self.energie >=  spotreba_energie:
            self.energie -=  spotreba_energie
            return f"{self.druh} {self.jmeno} spotřeboval při hře {spotreba_energie}% energie a zbývá mu {self.energie}%"
        else:
            return f"{self.druh} {self.jmeno} je moc unavený. Potřebuje {spotreba_energie}% energie, ale má jen {self.energie}%"
        
    def feed(self):
        filled = 100 - self.energie
        self.energie = 100
        return f"{self.druh} {self.jmeno} byl nakrmen a doplnil {filled}% energie."
    
    def VetCheck(self):
        if self.rok_prohlidky < datetime.now().year:
            return f"{self.druh} {self.jmeno} musí k veterináři - plantost prohlídky skončila v roce {self.rok_prohlidky}"
        else:
            

LefHart = Zvire("lev", "Chabřík Bobřík", 2009, 2012, 85)
print(LefHart.play())