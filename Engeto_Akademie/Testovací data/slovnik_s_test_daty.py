#Slovník pro testovací data - test zadaného inputu a reálného outputu
test_data = {
    "scénář_1": {"vstup": "abc", "očekávaný_výstup": "ABC", "reálný_výstup": "abc"},
    "scénář_2": {"vstup": 123, "očekávaný_výstup": "123"}
}
print(test_data["scénář_1"]["reálný_výstup"]) 
print("očekávaný_výstup" == "reálný_výstup")

vysledky_testovani = {}
vysledky_testovani["Test_1"] = "Prošel"
vysledky_testovani["Test_2"] = "Selhal"
print(vysledky_testovani)

očekávané = {"status": 200, "data": "OK"}
skutečné = {"status": 200, "data": "OK"}
if očekávané == skutečné:
    print("Test proběhl v pořádku.")

print(očekávané == skutečné) 