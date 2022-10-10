def spravne_cislo(cislo):

    cislo = str(cislo)

    navratova_hodnota = False
      
    if len(cislo) == 9:
        navratova_hodnota = True
    
    elif len(cislo) == 13:
        if cislo[0:4] == "+420":
            navratova_hodnota = True
        else:
            navratova_hodnota = False
                
    return navratova_hodnota

cislo = input("Zadejte telefonní číslo, na které chcete zaslat SMS zprávu: ")
    
cislo = cislo.replace(" ", "")

if spravne_cislo(cislo):
    
    zprava = input("Zadejte text SMS zprávy: ")
 
    def cena_zpravy(zprava):
        import math
 
        return math.ceil(len(zprava) / 180) * 3         
       
    print(f"Cena Vaší SMS zprávy je {cena_zpravy(zprava)} Kč.")

else:
    print("Nesprávné telefonní číslo.")