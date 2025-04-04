#Fibonacci

#1. Pomocí smyčky WHILE získej prvních 15 čísel Fibonacciho posloupnosti.
#2. Doplň do řešení samotnou smyčku WHILE.
#3. Definuj smyčku while,...., 
#4. kdy iterace bude trvat tak dlouho, 
#5. pokud vysledky nebudou obsahovat 15 hodnot,
#6. nezapomeň zapsat proces, který ti v každém kroce přepočítá číselné hodnoty,
#7. tedy každé nové číslo je součástí Fibonacciho posloupnosti – součet dvou předchozích čísel (kde x a y jsou počáteční hodnoty posloupnosti).
#8. Naformátuj výstup jako: Fibonacci: [<VYSLEDKY>]


#0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610
#x = 0
#y = 1



x = 0
y = 1
vysledky = [0, 1]
delka_rady = 15
delka_aktualni = len(vysledky)

while delka_aktualni < delka_rady:  
    #cislo = x + y
    #vysledky.append(cislo)  
    #y = vysledky[-1]
    #x = vysledky[-2]

    cislo = vysledky[-1] + vysledky[-2]
    vysledky.append(cislo)
    delka_aktualni += 1         #i = i + 1

print(f"Fibonacci: {vysledky}")

#nebo verze jiná:
x = 0
y = 1
vysledky = []  # Seznam pro uložení výsledků
delka_rady = 15

while len(vysledky) < delka_rady:
    vysledky.append(x)  # Přidání aktuálního čísla do seznamu
    nove_cislo = x + y  # Vypočítání dalšího čísla
    x = y  # Posun hodnot
    y = nove_cislo

print(f"Fibonacci: {vysledky}")  # Formátovaný výstup  # Výpis výsledků
