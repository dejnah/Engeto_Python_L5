#1. Vytvoř prázdný nakupní košík `kosik` typu `list`,
#2. definuj smyčku WHILE, která bude *iterovat*, dokud **nemá `kosik` 3** hodnoty,
#3. nejprve vlož zboží do proměnné `produkt`,
#4. vypiš oddělovač `"---"`,
#5. jakmile podmínka v předpisu nebude pravdivá, vypiš obsah proměnné `kosik`.

kosik = list()

while len(kosik) < 3:
    produkt = input("Přidejte položku do košíku: ")
    kosik.append(produkt)
print("---")

print(f"Váš nákupní košík je plný. Obsahuje tyto položky: {kosik}")
