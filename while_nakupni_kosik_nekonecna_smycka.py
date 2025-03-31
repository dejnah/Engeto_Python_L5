#Vyzkoušej si práci s `řízenou nekonečnou while` smyčkou:

#1. Vytvoř prázdný nakupní košík `kosik` typu `list`,
#2. definuj smyčku WHILE, která bude *iterovat*, dokud uživatel nezadá slovo **hotovo**,
#3. nejprve vlož zboží do proměnné `produkt`,
#4. vypiš přidaný `produkt`,
#5. vypiš oddělovač `"---"`,
#6. jakmile uživatel zadá slovo **hotovo**, vypiš obsah proměnné `kosik`.

kosik_1 = list()

while True:
    produkt = (input("Vlož produkt do košíku: "))
    if produkt.lower() == "hotovo":
        break
    kosik_1.append(produkt)
    print(produkt)
    print("---")
    
print(f"Košík 1 obsahuje: {kosik_1}")

#nebo 
print()
print()

kosik_2 = list()
switch = True

while switch:
    produkt = (input("Vlož produkt do košíku: "))
    if produkt.lower() == "hotovo":
        switch = False.         # Ukončí cyklus
    else:
        kosik_2.append(produkt) # Přidá produkt do seznamu, ale ne "hotovo"
        print(produkt)
        print("---")
    
print(f"Košík 2 obsahuje: {kosik_2}")
