class Nemoc:
    # poradi argumentu v radku nize si klidne preskladejte
    def __init__(self, jmeno, inkubacni_doba, pocet_obeti, sireni):
        self.jmeno = jmeno
        self.inkubacni_doba = inkubacni_doba
        self.pocet_obeti = pocet_obeti
        self.sireni = sireni

    def __str__(self):
        return f'Jmeno: {self.jmeno}'

    def zmen_pocet_obeti(self, pocet_obeti):
        self.pocet_obeti = pocet_obeti
        return self.pocet_obeti

class Koronavirus(Nemoc):
    def __init__(self, jmeno, varianty):
        super().__init__(jmeno, 12, 1000, "vzduchem")
        self.varianty = []
         
    def pridej_variantu(self, varianta):
        self.varianty.append(varianta)
        return self.varianty

    def __str__(self):
        if len(self.varianty) == 0:
            return super().__str__() + f" (zadne nalezene varianty)."
        return super().__str__() + f" (varianty: {', '.join(self.varianty)})."

corona = Koronavirus('Coronavirus', ['omikron'])
print(corona)
print(corona.pocet_obeti) # nejake cislo ktere se da menit pomoci metody zmen_pocet_obeti() - muze byt nacatku nula nebo cislo ktere si zvolite pri vytvoreni objektu
print(corona.sireni) # 'vzduchem' -- muzete reprezentovat i cislem
print(corona.inkubacni_doba) # 12 -- je mi jedno jake cislo - pevne dane ve volani super().__init__(...)
corona.pridej_variantu('omikron')
corona.pridej_variantu('delta')
print(corona) # 'Jmeno: Coronavirus (varianty: omikron, delta)'
corona.pridej_variantu('alpha')
print(corona) # 'Jmeno: Coronavirus (varianty: omikron, delta, alpha)'
print(corona.zmen_pocet_obeti(6000))