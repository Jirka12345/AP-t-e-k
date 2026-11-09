class NPC:
    def __init__(self,jmeno:str, energie:int):
        self.jmeno = jmeno
        self.energie = energie
        pass

    def predstav_se(self):
        return f"Jmenuji se {self.jmeno}"
    
    def vyraz_na(self,vyraz_kam:str):
        if self.enerige >= 10:
            self.energie =- 10
            return f"Jdu na lokaci {vyraz_kam}. Zbývá mi {self.energie}"
        else:
            return f"{self.jmeno} Bratu ja němožem"
        
class Chodec(NPC):
    def __init__(self, jmeno, energie, domovska_ctvrt:str):
        super().__init__(jmeno, energie)
        self.domovska_ctvrt = domovska_ctvrt

    def predstav_se(self):
        return f"Zde chodec {self.jmeno}, rajón {self.domovska_ctvrt}."
    
    def vyraz_na(self, vyraz_kam):
        if self.energie >= 30:
            self.energie -= 30
            return f"Zahajuji náročný pěšný pochod k cíli {vyraz_kam}"
        else:
            return f"{self.jmeno} nema dostatek energie"

npc1 = Chodec("Big Smoke", 20, "Grove Street")
print(npc1.vyraz_na("Čtvrť Balas"))

class fizlik(NPC):
    def __init__(self, jmeno, energie, tasena_zbran:bool):
        self.tasena_zbran = tasena_zbran
        super().__init__(jmeno, energie)

    def predstav_se(self):
        return f"yo yo skid skid beng beng, tu {self.jmeno}"
    
    def tas_nebo_skryj_zbrab(self):
        self.tasena_zbran = not self.tasena_zbran
        if self.tasena_zbran:
            return f"{self.jmeno}: ZBRAŇ TASENA"
        else:
            return f"{self.jmeno}: ZBRAŇ skryta v pouzdře"
        
class RidicAutobusu(NPC):
    def __init__(self, jmeno, energie,jmeno_cestujiciho:str):
        super().__init__(jmeno, energie)
        self.jmeno_cestujiciho = jmeno_cestujiciho
    

    



npc = NPC("Hynek Židýn", 10)

npc2 = fizlik("Tenpenny", 100)

print(npc.predstav_se())
print(npc.vyraz_na("Praha"))
print(npc.vyraz_na("Brno"))
print(npc2.predstav_se())