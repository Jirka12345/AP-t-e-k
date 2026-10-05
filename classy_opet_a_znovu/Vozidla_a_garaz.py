class Vozidlo:
    def __init__(self, znacka:str, rok_vyroby:int, stav_nadrze:int = 100):
        self.znacka = znacka
        self.rok_vyroby = rok_vyroby
        self.stav_nadrze = stav_nadrze
        pass

    def zvuk_motoru(self):
        return "Hututuutu Vrmmmmmmm"
    
    def info(self):
        return f"Vozidlo {self.znacka}, rok vyroby {self.rok_vyroby}"
    
    def startuj(self):
        if self.stav_nadrze > 0:
            return f"{self.zvuk_motoru()}. Vozidlo se nastartovalo"
        else:
            return f"Vehikel nefakčí, došla štáva :("

class Auto(Vozidlo):
    def __init__(self, znacka, rok_vyroby, typ_prevodovky:str, stav_nadrze = 100):
        super().__init__(znacka, rok_vyroby, stav_nadrze)
        self.typ_prevodovky = typ_prevodovky
    
    def zvuk_motoru(self):
        return "Vrum vrum!"
    
    def zatrub(self):
        return "Túúúút túúút"

class Moped(Vozidlo):
    def __init__(self, znacka, rok_vyroby, ma_slapadla:bool, stav_nadrze = 100):
        super().__init__(znacka, rok_vyroby, stav_nadrze)
        self.ma_slapadla = ma_slapadla
    
    def zvuk_motoru(self):
        return "Trrrrr!"
    
    def slapej(self):
        return f"Šlapej nebo nedojedem"
    
Rychla_strela = Auto("Škoda", 1995, "manuál")

Peklostroj = Moped("Babbeta", 1991, True, 53)

Garaz = [Rychla_strela, Peklostroj]

for Vehikel in Garaz:
    print(Vehikel.info())
    print(Vehikel.startuj())
    print("-" *20)