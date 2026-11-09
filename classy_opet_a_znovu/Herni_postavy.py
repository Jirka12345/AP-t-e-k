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
        else:
            return "Nemam manu, utočim holí - udělené poškození 5 bodů"
        
class Zloděj(Postava):
    def __init__(self, jmeno, zdravi, uspesnost_loupeze:bool = True):
        super().__init__(jmeno, zdravi)
        self.uspesnost_loupeze = uspesnost_loupeze
    
    def utok(self):
        return "Zloděj útočí zezadu a bodá za 20 bodů poškození."

Velkej_Tony = Rytir("Velkej Tony", 50, 100)

Ďurda = Zloděj("Ďurda", 100,)

Čadomír_Čaromír = Mag("Čadomír Čaromír", 65, 100)

druzina = [Velkej_Tony,Ďurda,Čadomír_Čaromír]

for clovek in druzina:
   print(clovek.predstav_se())
   print(clovek.utok())
   print("-" * 20)
