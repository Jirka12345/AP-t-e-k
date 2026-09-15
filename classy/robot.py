class Robot:
    def __init__(self, oznaceni:str, baterie:int, ukol:str = "nerozbít se" ):
        self.oznaceni = oznaceni
        self.baterie = baterie
        self.ukol = ukol
        pass

    def zvuk(self):
        return f"pípuppiripípup"
    
    def diagonstika(self):
        return f"Jsem model {self.oznaceni} a mam {self.baterie}% baterie."
    
    def aktualni_ukol(self):
        return f"Aktualné pracuji na úkolu: {self.ukol}."
    
    def zadej_ukol(self,Nukol:str):
        self.ukol = Nukol
        return f"Byl mi zadán nový úkol: {Nukol}."
    
droid = Robot("C3P0", 84)
print(droid.oznaceni)
print(droid.baterie)
print(droid.ukol)
print(droid.zvuk())
print(droid.diagonstika())
print(droid.aktualni_ukol())
print(droid.zadej_ukol("vypni se"))