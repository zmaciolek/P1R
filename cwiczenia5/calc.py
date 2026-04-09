import sys

plik1 = sys.argv[1]
plik2 = sys.argv[2]

slownik = {"+": lambda a, b: a + b, "-": lambda a, b: a-b, "*": lambda a, b: a*b, "/": lambda a, b: a/b, "^": lambda a, b: a**b, "%": lambda a, b: a % b, }



def calc(plik1,plik2):
    with ( open(plik1, "r") as input_file,
         open(plik2, "w") as output_file, ):
            for line in input_file:
                liczba1 = line.split()[0]
                znak = line.split()[1]
                liczba2 = line.split()[2]
                wynik = slownik[znak](float(liczba1), float(liczba2))
                print(wynik)
                output_file.write(line+" = "+str(wynik))
                
calc(plik1,plik2)
            
            

