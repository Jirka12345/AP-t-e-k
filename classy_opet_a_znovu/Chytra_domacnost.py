class Chytre_Zarizeni:
    def __init__(self, nazev:str, mistnost:str, zapnuto:bool = False):
        self.nazev = nazev
        self.mistnost = mistnost
        self.zapnuto = zapnuto
        pass

    def prepni_stav(self):
        if self.zapnuto == False:
            self.zapnuto = True
            return "Zařízení se zaplo."
        else:
            self.zapnuto = False
            return "Zařízení se vyplo."
        
    def proved_akci(self):
        return "Zařízení čeká na příkaz."
    
class Chytra_Zarovka(Chytre_Zarizeni):
    def __init__(self, nazev, barva:str, mistnost, zapnuto = False):
        super().__init__(nazev, mistnost, zapnuto)
        self.barva = barva
    
    def proved_akci(self):
        if self.zapnuto == True:
            return f"Svítí barvou {self.barva}"
        else:
            return "Je zhasnuto."
        
    def zmen_barvu(self,nova_barva):
        self.barva = nova_barva
    
class Chytra_Zasuvka(Chytre_Zarizeni):
    def __init__(self, nazev, mistnost, aktualni_odber_w:int, zapnuto = False):
        super().__init__(nazev, mistnost, zapnuto)
        self.aktualni_odber_w = aktualni_odber_w
    
    def proved_akci(self):
        if self.zapnuto == True:
            return f"Propouštím proud a odbíram {self.aktualni_odber_w} watů."
        else:
            return "Zarizeni vypnuto, to nepude šefiku."

Zasuvka1 = Chytra_Zasuvka("Zasuvka1", "obývák", 60, True)

Žárovka1 = Chytra_Zarovka("Žárovka1", "červená", "záchod", True)

domácnost = [Zasuvka1,Žárovka1]

for zarizeni in domácnost:
    print(zarizeni.prepni_stav())
    print(zarizeni.proved_akci())
    print("-" * 20)