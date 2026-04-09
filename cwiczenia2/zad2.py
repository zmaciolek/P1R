import sys

lista1=sys.argv[1:]

def bubble(lista):
   
    for i in range(len(lista)-1):
        for j in range(len(lista)-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista


a = [5, 7, 8, 6 , 2, 2.444, 2.11]
print(a)
print(bubble(a))
print(bubble(lista1))
