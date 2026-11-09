class Robot:
    def __init__(self, oznaceni:str, baterie:int):
        self.oznaceni = oznaceni
        self.baterie = baterie
        pass

    def hlaseni_stavu(self):
        return f"Mám {self.baterie}% baterie."
    
    def proved_misi(self):
        return "Čekám na zadání souřadnic."
    
    def nabij_baterii(self):
        self.baterie = 100

class Kvadrokoptera(Robot):
    def __init__(self, oznaceni, baterie, max_vyska:int):
        super().__init__(oznaceni, baterie)
        self.max_vyska = max_vyska

    def proved_misi(self):
        if self.baterie >= 25:
            self.baterie -= 25
            return f"Letím do výšky {self.max_vyska} metrů a pořizuji snímky terénu"
        else:
            return "Nemam dost baterie na vzlet."
    
class Pruzkumny_pasak(Robot):
    def __init__(self, oznaceni, baterie, ma_termokameru:bool):
        super().__init__(oznaceni, baterie)
        self.ma_termokameru = ma_termokameru
    
    def proved_misi(self):
        if self.ma_termokameru == True:
            self.baterie -= 15
            return f"Jedu těžkým terénem a skenuji teplotu"
        else:
            return "Jedu těžkým terénem"

dron = Kvadrokoptera("Dron", 67, 128)

pasac = Pruzkumny_pasak("Pásáč", 50, True)

stroje = [dron, pasac]

for objekt in stroje:
    print(objekt.proved_misi())
    print(objekt.hlaseni_stavu())
    print(objekt.nabij_baterii())
    print("-" * 20)