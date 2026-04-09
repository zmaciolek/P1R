litery="abcdefghijklmnopqrstuvwxyz"
lista_liter=list(litery)
literyd=litery.upper()
lista_literd=list(literyd)

n1=3
slowo1="zyx1@"

def encrypt(slowo, n):
    szyfr=""
    for char in slowo:
        if char.isalpha():
            if char.islower():
                kod = ord("a")
            else:
                kod = ord("A")
            szyfr=szyfr+chr((ord(char) - kod + n ) % 26 + kod)
        else:
            szyfr=szyfr+char
    return szyfr
    
print(encrypt(slowo1, n1))

def decrypt(slowo, n):
    szyfr=""
    for char in slowo:
        if char.isalpha():
            if char.islower():
                kod = ord("a")
            else:
                kod = ord("A")
            szyfr=szyfr+chr((ord(char) - kod + n ) % 26 + kod)
        else:
            szyfr=szyfr+char
    return szyfr

print(decrypt(slowo1, n1))

