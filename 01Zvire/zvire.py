import random

class Zvire:
    def __init__(self, jmeno:str, vek:int, misto:str = "bouda"):
        self.jmeno = jmeno
        self.vek = vek
        self.misto = misto
        pass

    def zvuk(self):
        return "???"
   
    def predstav_se(self):
        return f"jmenuji se {self.jmeno}, a je mi {self.vek} let."
    
    def kde_jsi(self):
        return f"Jsem v {self.misto}"
    
    def jdi_na(self, Nmisto:str):
        self.misto = Nmisto
        return f"Přesunul jsem se na {Nmisto}. {self.kde_jsi}"


class Pes(Zvire):
    def __init__(self, jmeno, vek, plemeno, misto = "bouda"):
        super().__init__(jmeno, vek, misto)
        self.plemeno = plemeno

    def zvuk(self):
        return "Haf, haf!"
    
    def aport(self):
        return f"{self.jmeno} přinesl míček."
    
    def vycesat(self):
        if(random.randint(0,1) > 0):
            return f"{self.jmeno} utekl před tvým kartáčem!"
        else:
            return f"{self.jmeno} se nechal vyčesat"
    
    def predstav_se(self):
        return f"{super().predstav_se()} jsem {self.plemeno}"

class Kocka(Pes):
    def __init__(self, jmeno, vek, barva:str, misto="bouda"):
        super().__init__(jmeno, vek, misto)

    def zvuk(self):
        return "Mňau, mňau"
    
    def utok(self):
        return f"{self.jmeno} škrábe"
    
    def pohladit(self):
        if (random.randint(0,1) > 0):
            return f"{self.jmeno} se nechal/a pohladit."
        else:
            return f"Vrní a {self.utok}."

micka = Kocka("Micka", 4, "zrzavá")

print("-" * 20)

class Papousek(Zvire):
    def __init__(self, jmeno, vek, BarvaPeri, misto = "klec"):
        super().__init__(jmeno, vek, misto)
        self.BarvaPeri = BarvaPeri
    
    def zvuk(self):
        return "Píp, píp!"
    
    def opakuj(self, slovo:str):
        return f"{self.jmeno} opakuje: {slovo}! {slovo}!"

class Had(Zvire):
    def __init__(self, jmeno, vek, delkavcm:int, jedovaty:bool, misto = "bouda"):
        super().__init__(jmeno, vek, misto)
        self.delkavcm = delkavcm
        self.jedovaty = jedovaty

    def zvuk(self):
        return "SsssSSss"
    
    def ustknuti(self):
        if self.jedovaty:
            return f"POZOR! {self.jmeno} tě uštknul a je jedovatý!"
        else:
            return f"{self.jmeno} tě kousnul, ale naštěstí není jedovatý!"
        
    def predstav_se(self):
        if self.jedovaty:
            typ = "jedovatý"
        else:
            typ = "škrtič"
        
        return f"Sssss... já jsem {self.jmeno}, měřím {self.delkavcm} a jsem {typ}"
    
hadice = Had("Hadice", 6, 23, True)
print(hadice.ustknuti())
print(hadice.predstav_se())

print("-" * 20)

Papuch = Papousek("Papuch", 3,"červená")
print(Papuch.zvuk())
print(Papuch.opakuj("test"))

print("-" * 20)

radegast = Pes("Radegast",2,"Ovčák","V boudě")
print(radegast.jmeno)
print(radegast.plemeno)
print(radegast.zvuk())
print(radegast.predstav_se())
print(radegast.aport())
print(radegast.vycesat())
print(radegast.kde_jsi())
print(radegast.predstav_se())

print("-" * 20)

zvire = Zvire("Luděk", 22)
print(zvire.jmeno)
print(zvire.vek)
print(zvire.zvuk())

print("-" * 20)

zvire2 = Zvire("Amálka", 5, "na zahradě")
print(zvire2.jmeno)
print(zvire2.vek)
print(zvire2.misto)
print(zvire2.zvuk())
print(zvire2.predstav_se())
print(zvire2.kde_jsi)
print(zvire.jdi_na("Škola"))
print(zvire2.jdi_na("oběd"))

print("-" * 20)

zoo = [micka, hadice, Papuch, radegast]

for obyvatel in zoo:
    print(obyvatel.zvuk())
    print(obyvatel.predstav_se())
    print("-" * 20)