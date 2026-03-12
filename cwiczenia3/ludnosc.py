import json
import matplotlib.pyplot as plt
import numpy as np

plik = open("ludnosc.json")
dane = json.load(plik)
plik.close()

wojewodztwo = input("Podaj wojewodztwo: ")
rodzaj = input("Wybierz czego chcesz wykres: ludnosc, powierzchnia, gestosc:  ")
lista_ludnosc=[]
lista_powierzchnia=[]
lista_gestosc=[]
ludnosc_polski=[]
temp=0

for rok in range(2013,2026):
    lista_ludnosc.append(dane[str(rok)][wojewodztwo]["ludność"])
    lista_powierzchnia.append(dane[str(rok)][wojewodztwo]["powierzchnia km2"])

for rok2 in range(2013,2026):
    for woj in range(16):
        ludnosc_polski.append(dane[str(rok2)][woj])
   
   
   for i in range(13):
        temp=temp+lista_ludnosc[i]
    ludnosc_polski.append(temp)
    temp=0

print(ludnosc_polski)

print(dane["2013"]["Mazowieckie"]["ludność"])
print(lista_ludnosc)
print(lista_powierzchnia)

for i in range(13):
    lista_gestosc.append(lista_ludnosc[i]/lista_powierzchnia[i])
    
print(lista_gestosc)

xpoints = np.array([2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025])
y1points = np.array(lista_ludnosc)
y2points = np.array(lista_powierzchnia)
y3points = np.array(lista_gestosc)

print(xpoints)

if rodzaj == "ludnosc":
    plt.plot(xpoints, y1points)
    plt.show()
elif rodzaj == "powierzchnia":
    plt.plot(xpoints, y2points)
    plt.show()
elif rodzzaj == "gestosc":
    plt.plot(xpoints, y3points)
    plt.show()
    
    

