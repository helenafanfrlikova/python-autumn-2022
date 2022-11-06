def zmen_znamku(text, slovnik_znamek={"1":"A", "2":"B", "3":"C", "4":"D", "5":"F"}):
    for k,v in slovnik_znamek.items():
        text = text.replace(k, v)
    return text
    
with open('Znamky-List1.txt', encoding='utf-8') as vstup:
    radky = vstup.readlines()
    prvni_radek = [radky[0]]
    ostatni_radky = radky[1:]
    nove_ostatni_radky = [zmen_znamku(radek) for radek in ostatni_radky] 
    cely_seznam = prvni_radek + nove_ostatni_radky
            
with open('Znamky-List2.txt', mode='w', encoding='utf-8') as vystup:
    vystup.writelines(cely_seznam)