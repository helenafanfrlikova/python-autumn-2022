baliky = {
    "B541X": True,
    "B547X": False,
    "B251X": False,
    "B501X": True,
    "B947X": False,
}
kod = input('Zadejte kód balíku: ')
if kod in baliky:
    if baliky[kod] == True:
        print("Balík byl předán kurýrovi.")
    if baliky[kod] == False:
        print("Balík nebyl předán kurýrovi.")
else:
    print("Nesprávné číslo balíku.")