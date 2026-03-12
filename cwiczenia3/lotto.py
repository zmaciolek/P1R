from random import randint

lista=[]

while len(lista) < 6:
    a = randint(1, 49)
    if a not in lista:
        lista.append(a)

print(lista)
