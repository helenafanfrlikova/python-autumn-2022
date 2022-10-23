class Recept:
    def __init__(self, nazev, narocnost, url_adresa):
        self.nazev = nazev
        self.narocnost = narocnost
        self.url_adresa = url_adresa
        self.vyzkouseno = False

    def __str__(self):
        vypis = f"Recept na {self.nazev} má stupeň náročnosti {self.narocnost}. Recept najdete na adrese {self.url_adresa}. "
        if self.vyzkouseno:
            return vypis + 'Vyzkoušen.'
        return vypis + 'Ještě nevyzkoušen.'

    def zmen_narocnost(self, nova_hodnota):
        self.narocnost = nova_hodnota
        return self.narocnost

    def zkusit(self):
        self.vyzkouseno = True
        return self.vyzkouseno
    
    def __repr__(self):
        return self.__str__()
                    
tiramisu = Recept('tiramisu', 5, 'www.tiramisu.cz')
print(tiramisu)     
muffiny = Recept('muffiny', 3, 'www.muffiny.cz')
muffiny.zkusit()
muffiny.zmen_narocnost(2)
print(muffiny)


class Kucharka:
    def __init__(self, nazev, autor):
        self.nazev = nazev
        self.autor = autor
        self.recepty = []

    def __str__(self):
        return f"Kuchařka {self.nazev}, jejímž autorem je {self.autor}, má {self.pocet_receptu()} receptů."
        
    def pocet_receptu(self):
        self.pocet = len(self.recepty)
        return self.pocet
                         
    def pridej_recept(self, novy_recept):
        self.recepty.append(novy_recept)
        print("Přidán nový recept.")

    def vyzkousene_recepty(self):
        seznam_vyzkousenych = []
        for recept in self.recepty:
            if recept.vyzkouseno == True:
                seznam_vyzkousenych.append(recept)
        return f"Tyto recepty byly vyzkoušeny: {seznam_vyzkousenych}."

moje_kucharka = Kucharka('Vypečená kuchařka', 'Linda')
print(moje_kucharka)
moje_kucharka.pridej_recept(tiramisu)
moje_kucharka.pridej_recept(muffiny)
print(moje_kucharka)
print(moje_kucharka.vyzkousene_recepty())