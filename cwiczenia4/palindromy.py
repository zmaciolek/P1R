
slowo=input("Podaj slowo do sprawdzenia: ")


def is_palindrome(x):
    slowo_male=x.lower()
    lista1=list(slowo_male)
    print(lista1)
    lista2 = list(filter(str.isalpha,lista1))
    lista3 = lista2[::-1]
    print(lista2)
    print(lista3)
    if lista2 == lista3:
        return(True)
    else:
        return(False)

print(is_palindrome(slowo))


