import sys

plik = sys.argv[1]


suma=0
with open(plik, "r") as input_file:
    for line in input_file:
        suma = suma + float(line.split()[-1])
        
        

print(suma)
