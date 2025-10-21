#cykly While
count = 0
while count < 5:
    print(count + 1)
    count += 1



loading = True
time_elapsed = 0

while loading and time_elapsed < 10:
    print("Načítání stránky...")
    time_elapsed += 1
    # Simulace načtení stránky po 5 sekundách
    loading = time_elapsed != 10

print("Test dokončen: stránka načtena" if not loading else "Test selhal: stránka se nenačetla včas.")