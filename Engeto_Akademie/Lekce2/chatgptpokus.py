while True:
    vek_uzivatele = input("Zadejte váš věk: ")

    # kontrola, jestli jsou zadána čísla
    if not vek_uzivatele.isdigit():
        print("Prosím, věk zadejte jen jako kladná čísla.")
        continue  # vrátí se na začátek smyčky

    vek_uzivatele = int(vek_uzivatele)

    # kontrola rozsahu věku
    if vek_uzivatele <= 0 or vek_uzivatele >= 125:
        print("Prosím, zadejte reálnou hodnotu věku.")
        continue  # znovu se zeptá

    # pokud je všechno v pořádku -> ukončí smyčku
    break


# po úspěšném zadání vypíše odpovídající text
if vek_uzivatele < 18:
    print("Kofola")
elif vek_uzivatele < 64:
    print("Nazdraví!")
else:
    print("Pozor! Pijte s rozumem!")

plnoletost = vek_uzivatele >= 18
if plnoletost is True:
    print("Jste plnoletý")
else:
    print("Ještě nejste plnoletý")
