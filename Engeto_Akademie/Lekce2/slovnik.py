#příklad jednoduchého seznamu
uzivatel = {"Jméno" : "Daniel",
            "Příjmení":"Buček",
            "Věk":"24 let"
         }
uzivatel["Role"] = "Tester"
uzivatel["Věk"] = "25 let"

del uzivatel["Věk"]
role = uzivatel.pop("Role")
#uzivatel.clear()

uzivatel["Telefon"] = "+420704428244" 

#print("Role" in uzivatel)
#print("Jméno" in uzivatel)
#print(role)
#print(uzivatel)
