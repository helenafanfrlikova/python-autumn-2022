import csv
        
def zmen_znamku(text, slovnik_znamek={"1":"A", "2":"B", "3":"C", "4":"D", "5":"F"}):
    for k,v in slovnik_znamek.items():
        text = [item.replace(k, v) for item in text]
    return text

with open('znamky-List1.csv', 'r', encoding='utf-8') as vstup:
    radky = list(csv.reader(vstup))
    prvni_radek = [radky[0]]
    ostatni_radky = radky[1:]
    nove_ostatni_radky = [zmen_znamku(radek) for radek in ostatni_radky] 
    cely_seznam = prvni_radek + nove_ostatni_radky
                
with open('znamky-List2.csv', 'w', encoding='utf-8', newline='') as vystup:
    vystup = csv.writer(vystup)
    vystup.writerows(cely_seznam)