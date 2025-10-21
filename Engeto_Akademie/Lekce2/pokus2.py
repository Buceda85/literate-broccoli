vek_uzivatele = input("Zadejte váš věk: ")

while not vek_uzivatele.isdigit():
    print("Prosím, věk zadejte jen jako celá čísla.")
    vek_uzivatele = input("Zadejte váš věk: ")

vek_uzivatele = int(vek_uzivatele)

if vek_uzivatele > 0 and vek_uzivatele < 18:
    print("Kofola")
elif vek_uzivatele >= 18 and vek_uzivatele < 64:
    print("Nazdraví!")
elif vek_uzivatele >= 64 and vek_uzivatele < 125:
    print("Pozor! Pijte s rozumem!")
else:
    print("Prosím, zadajte reálnou hodnotu věku.")
    vek_uzivatele = int(input("Zadejte váš věk: "))
