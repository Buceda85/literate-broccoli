kilometry_ujete = int(input("Zdajte počet ujetých kilometrů: "))
litry_paliva = int(input("zadjete množství spotřebovaného paliva (v litrech): "))
prumerna_spotreba = float((litry_paliva / kilometry_ujete)*100)
print("Vaše průměrná spotřeba je ", str(round(prumerna_spotreba, 2)), " litrů na 100 km.")