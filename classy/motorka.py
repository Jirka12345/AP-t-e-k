class Motorka:
    def __init__(self, znacka:str, kategorie:str, stav_nadrze:int = 20, stav_stojanku:str = "vyklopen"):
        self.znacka = znacka
        self.kategorie = kategorie
        self.stav_nadrze = stav_nadrze
        self.stav_stojanku = stav_stojanku
        pass

    def zatoc_plyn(self):
        return f"VRRRUUUM"
    
    def popis_moto(self):
        return f"znacka: {self.znacka}, kategorie: {self.kategorie}, stav výdrže: {self.stav_nadrze}, stav stojánku: {self.stav_stojanku}"
    
    def vypis_stav_stojanku(self, ):
        return f"Stojánek je {self.stav_stojanku}."
    
    def zmen_stojanek(self, NSstojanku:str):
        self.stav_stojanku = NSstojanku
        return f"Stav stojanku se změnil a je nyní {NSstojanku}."
    
    def popojed(self, kolikjet:int):
        return f"Motorka popojela, zbylo jí {self.stav_nadrze - {kolikjet}} litrů v nádrži."
    
    def vypis_palivo(self):
        return f"Motorka má {self.stav_nadrze} litrů v nádži."
    
    def natankuj(self, koliktankovat:int):
        self.stav_nadrze = koliktankovat
        return f"Po natankování je v nádrži {koliktankovat}."
    
motorka = Motorka("Honda", "silnička", 20)
print(motorka.znacka)
print(motorka.kategorie)
print(motorka.stav_nadrze)
print(motorka.stav_stojanku)
print(motorka.zatoc_plyn())
print(motorka.popis_moto())
print(motorka.vypis_stav_stojanku())
print(motorka.zmen_stojanek("zaklopen"))
print(motorka.popojed(5))
print(motorka.vypis_palivo())
print(motorka.natankuj())    