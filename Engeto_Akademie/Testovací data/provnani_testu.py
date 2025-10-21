expected_result = 10
actual_result = 8

if actual_result == expected_result:
    print("Test prošel.")
else:
    print("Test selhal.")

actual_result_dve = 8

if actual_result_dve < 10:
    print("Test selhal: Výsledek je příliš nízký.")
elif actual_result_dve > 10:
    print("Test selhal: Výsledek je příliš vysoký.")
else:
    print("Test prošel.")