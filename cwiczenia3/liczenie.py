from collections import Counter

lista1=[4,6,3,2,4,5,66,4,5,3,3,3]

def most_frequent(lista):
    print(lista)
    temp = Counter(lista)
    print(temp)

most_frequent(lista1)
