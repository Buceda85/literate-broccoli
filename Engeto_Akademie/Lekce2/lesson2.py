#import knigovny "math", "datetime", "random"
import math, datetime, random, modul_engeto

#použití funkce z vlastního modulu, např. součet dvou čísel: 50 a 5
#print(modul_engeto.soucet(50,5))

print(modul_engeto.objem_koule(10))

#Tato funkce využívá matematickou operaci odmocniny ve float, viz. detail funkce "sqrt"
#Zde se vytiskne odmocnina z 16, což je 4
#print(math.sqrt(16))

#z modulu datetime použij funkci aktuální čas
#první datetime = volám import
#druhý datetime = funkce z knihovny datetime
#now = upřesnění, co přesně volám = aktuální čas
#aktualni_cas = datetime.datetime.now()
#print(aktualni_cas)

#z modulu random mohu vybírat náhodné volby
#print(random.choice(["Voda", "Káva", "Čaj"]))

#print("Ahojte z Python kurzu pokračování!")
#vaha_stromecku = 5.98
#print("Váha vánočního stromečku je: " + str(vaha_stromecku))

#vaha_stromecku = 6.01
#print("Nová váha stromečku je: " + str(vaha_stromecku))

#pojisteni_vozu = True
#print("Je vůz pojištěn? " + str(pojisteni_vozu))

#print(51!=51)

#Cyklus neboli iterace
#Na dálnici chceme vypsat uozornění: "Pozor nehoda!"
#print("Pozor nehoda!")

#Vypsat 5x pozor: 
#print("Pozor nehoda!")
#print("Pozor nehoda!")
#print("Pozor nehoda!")
#print("Pozor nehoda!")
#print("Pozor nehoda!")

#for i in range(55):
    #print("Pozor nehoda!")

#correct_password = "Test123!"
#user_input = input("Zadejte heslo: ")

#while user_input != "Test123!":
#    print("Nesprávné heslo! Prosím zkuste to znovu.") 
#    user_input = input("Zadejte heslo: ")

#print("Úspěšné přihlášení.")

#funkce
#def obvod_trojuhelnika(strana_a, strana_b, strana_c):
#    obvod = strana_a + strana_b + strana_c
#    return obvod

#zadaní pro výpoečet stran: a = 45, b = 56, c = 150
#print(obvod_trojuhelnika(45, 56, 150))

#funkce, která pozdraví Engeto studenty = definice nové vlastní funkce
#def pozdrav_engeto_studentu():
#    print("ahojte Engeti studneti! :)")
#volám funkci k pozdravu
#pozdrav_engeto_studentu()
