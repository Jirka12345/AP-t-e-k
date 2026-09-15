class Hero:
    def __init__(self, jmeno:str, lvl:int, lokace:str = "domov" ):
        self.jmeno = jmeno
        self.lvl = lvl
        self.lokace = lokace
        pass

    def pokrik(self):
        return "Co jeeeeeeeeeeeeee!"
    
    def predstav_se(self):
        return f"Jmenuji se {self.jmeno}."
    
    def kde_jsi(self):
        return f"Jsem v {self.lokace}."
    
    def presun_se(self, Nmisto:str):
        self.lokace = Nmisto
        return f"Přesunul jsem se na místo {Nmisto}."
    
hrdina = Hero("Ludva", 8)
print(hrdina.jmeno)
print(hrdina.lvl)
print(hrdina.lokace)
print(hrdina.pokrik())
print(hrdina.predstav_se())
print(hrdina.kde_jsi())
print(hrdina.presun_se("Kancelář"))
