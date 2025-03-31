#Walrus operátor v kombinaci s whil smyčkou 
#1. vem kód z předchozího cvičení,
#2. nahraď standardní přiřazení proměnné produkt přiřazením s použitím walrus operátoru,
#3. opět vypiš obsah proměnné košík.

#původní zápis
kosik_1 = list()

while True:
    produkt = (input("Vlož produkt do košíku: "))
    if produkt.lower() == "hotovo":
        break
    kosik_1.append(produkt)
    print(produkt)
    print("---")
    
print(f"Košík 1 obsahuje: {kosik_1}")

#walrus operátor
kosik_2 = list()
TEXT = "Zadej typ zboží [nebo 'hotovo' pro ukončení]: "

while (produkt := input(TEXT)) != "hotovo":
    kosik.append(produkt)
    print(produkt)
    print("---")

print(kosik)
