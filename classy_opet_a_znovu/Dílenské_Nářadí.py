class Naradi:
    def __init__(self,znacka:str, model:str):
        self.znacka = znacka
        self.model = model
        pass

    def identifikace(self):
        return f"Značka:{self.znacka}\n Model: {self.model}"
    
    def pracuj(self):
        return "Pracuju šefiku"
    
class AkuVrtacka(Naradi):
    def __init__(self, znacka, model, baterie:int):
        super().__init__(znacka, model)
        self.baterie = baterie

    def pracuj(self):
        if self.baterie > 0:
            self.baterie -= self.baterie * 0.10
            return f"Vrtačka vrtá."
        else:
            return ""
    