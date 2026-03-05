import sys
if __name__ == "__main_":
    print('hello')
lista=sys.argv[1:]
print(lista)
def bubble(lista):
	n = len(lista)
	for i in range(n):
		for j in range(0,n-i-1):
			if lista[j] > lista [j+1]:
				lista[j], lista[j+1] = lista[j+1], lista[j]
	print(lista)
	return lista

bubble(lista)
