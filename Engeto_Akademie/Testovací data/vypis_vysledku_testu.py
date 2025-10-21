#Příklad výpisu neúspěšných výsledků testu
test_results = ["PASS", "PASS", "FAIL", "PASS"]
index = 0

while index < len(test_results) and test_results[index] != "FAIL":
    index += 1

print(f"Chyba nalezena v testu č. {index + 1}." if index < len(test_results) else "Všechny testy prošly.")