class Sitove_zarizeni:
    def __init__(self, nazev:str, ip_adresa:str, online:bool = False):
        self.nazev = nazev
        self.ip_adresa = ip_adresa
        self.online = online
        pass

    def Zmen_stav(self):
        if self.online == False:
            self.online = True
            return f"Síťové zařízení bylo zapnuto"
        elif self.online == True:
            self.online = False
            return f"Síťové zařízení bylo vypnuto"
    
    def diagnostika(self):
        return f"Spouštím obecnou diagnostiku zařízení..."
    
class Router(Sitove_zarizeni):
    def __init__(self, nazev, ip_adresa, pocet_portu:int, online = False):
        super().__init__(nazev, ip_adresa, online)
        self.pocet_portu = pocet_portu

    def diagnostika(self):
        return f"{super().diagnostika()} Kontroluji LAN Porty"

    def restartuj_wifi(self):
        return f"Restartovávám Wifi..."
    
class Server(Sitove_zarizeni):
    def __init__(self, nazev, ip_adresa, operacni_system:str = "Ubuntu", online = False):
        super().__init__(nazev, ip_adresa, online)
    
    def diagnostika(self):
        return f"{super().diagnostika()} Kontroluji vytížení CPU a stav disků."
    
routros_jednos = Router("routroš bengroš", 19216810, 4)

severos_jednos = Server("první serveros", 19216821, "Windows")

Sítě = [routros_jednos, severos_jednos]

for Zarizeni in Sítě:
    print(Zarizeni.Zmen_stav())
    print(Zarizeni.diagnostika())
    print("-" *20)