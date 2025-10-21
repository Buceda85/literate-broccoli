soucet = 0

cislo = int(input("Zadejte číslo: "))

while cislo != 0:
    soucet += cislo
    cislo = int(input("Zadejte číslo: "))

print (f"Celkový součet vašich zadaných čísel je: {soucet}.")