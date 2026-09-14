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

zvire = Zvire("Luděk", 22)
print(zvire.jmeno)
print(zvire.vek)
print(zvire.zvuk())

zvire2 = Zvire("Amálka", 5, "na zahradě")
print(zvire2.jmeno)
print(zvire2.vek)
print(zvire2.misto)
print(zvire2.zvuk())
print(zvire2.predstav_se)
print(zvire2.kde_jsi)
print(zvire.jdi_na("Škola"))
print(zvire2.jdi_na("oběd"))