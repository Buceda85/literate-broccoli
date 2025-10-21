# funkce print, vytiskne na obrazovku text
# pro tento příklad to vytiskne "Ahoj Engeto studenti :)"
print("Ahoj Engeto studenti :)")
# pro tento příklad to vytiskne "40000"
print(40000)
# pro tento příklad to vytiskne "4.7"
print(4.7)
# pro tento příklad to vytiskne "Pozor, náledí"
print("Pozor, náledí")
# pro tento příklad to vytiskne "4 7"
print(4,7)
# pro tento příklad to vytiskne "Výsledek je: 100"
print("Výsledek je:", 100)
# pro tento příklad to vytiskne:
#"První řádek"
#"Druhý řádek"
#"Třetí řádek"
print("První řádek\nDruhý řádek\nTřetí řádek")

#Datový typ bool
print(True)

#Datový typ seznam
akciove_zbozi = ["Káva", "Banány", "Chléb", "Okurky"]
#Zde se vytiskne celý seznam
print(akciove_zbozi)

uzivatel = {
    "jméno:": "Daniel",
    "vek": 24
}
print(uzivatel)

#Proměnné
#Proměnná se nastaví na "17"
vek_uzivatele = 17
#Vytiskne se dosud uložená proměnná, tedy "17"
print(vek_uzivatele)

#Nastaví se nová proměnná na "18"
vek_uzivatele = 18
#Vytiskne se nová proměnná "18"
print(vek_uzivatele)
vek_uzivatele = 25
print(vek_uzivatele)
uzivatelske_jmeno = "Daniel Buček"
print(uzivatelske_jmeno)
pojisteni_uzivatele = True
print(pojisteni_uzivatele)
vek_uzivatele = 24
print(vek_uzivatele)
spotreba_paliva = 7.2
print(spotreba_paliva)

#funkce pro řetěžce
SMS = "Dobrou noc!"
print(len(SMS))
#Jaký je první znak v SMS?
#v tomto případě se zobrazí "D"
#index začíná od prvního místat jako "0", tedy v tomto případě se zobrazí "D"
print(SMS[0])
#v tomto případě se zobrazí "r"
print(SMS[3])
#v tomto případě se zobrazí poslední znak "!"
print(SMS[-1])

#v totmo případě se zobrazí chyba!
#print(SMS[20])

#Další funkce -> LowerCase
user_name = "DaNiElBuČeK007"
#Vypíše veškerý řetěžec v malých znacích
print(user_name.lower())
#Vypíše veškerý řetěžec ve velkých znacích
print(user_name.upper())

#arimetrické operace
#Toto vrácí přesnou hodnotu s desetinnými místy, v tomto případě "2.0"
print(10/5)
#Toto vrací jen celou část, zaokrouhluje se, v tomto případě "2"
print (10//4)
#Toto vrací zbytek z dělení, v tomto případě "1"
print (10%3)

#mocniny
print (2**3)

#Vstupy
print ("Vítejte\nKolik je Vám let?")
vek_navstevnika = input()
print("Váš věk je: " + vek_navstevnika)

#Funkce seznamů
#Došly banány = stáhnout produkt z nabídky
akciove_zbozi.remove("Banány")
print(akciove_zbozi)