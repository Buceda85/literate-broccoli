seznam_cisel = [1, 2, 3, 4, 5]
seznam_slov = ["Auto", "Brambora", "Citrón"]
seznam_kombinace = [1, "Auto", 3.14, True]

#Změní první pozici seznamu na požadovaný výsledek "2"
seznam_kombinace[0] = 2

#Přidá na konec seznamu nový prvek seznamu
seznam_slov.append("Delli")

#Přidá na přesnou pozici
seznam_cisel.insert(0, 0)

#Odebere první zadanou hodnotu ze seznamu
seznam_cisel.remove(5)

#Odebere prvek z dané pozice
seznam_cisel.pop(1)

print(seznam_cisel)
print(seznam_slov)
print(seznam_kombinace)

test_cases = ["Přihlášení", "Registrace", "Zapomenuté heslo"]
for case in test_cases:
    print(f"Spouštím tetovací scénář: {case}")

for i in range(5):
    print(f"Test číslo:", i + 1)

text = "Test"
for char in text:
    print(f"Písmeno: ", {char})