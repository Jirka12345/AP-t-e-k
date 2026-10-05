import random

class Postava:
    def __init__(self, jmeno:str, zdravi:int):
        self.jmeno = jmeno
        self.zdravi = zdravi
        pass

    def predstav_se(self):
        return f"Jmenuji se {self.jmeno} a mam {self.zdravi} hp"
    
    def utok(self):
        return "0"
    
class Rytir(Postava):
    def __init__(self, jmeno, brneni:int, zdravi):
        super().__init__(jmeno, zdravi)
        self.brneni = brneni
    
    def utok(self):
        return f"Sek mečem udělil poškozeni {(random.randint(10,20))} bodů."
    
    def zablokuj(self):
        return "Vyblokoval jsi utok."
    
class Mag(Postava):
    def __init__(self, jmeno, mana:int, zdravi):
        super().__init__(jmeno, zdravi)
        self.mana = mana
    
    def utok(self):
        if self.mana >= 10:
            self.mana -= 10
            return f"{(random.randint(25,40))}"