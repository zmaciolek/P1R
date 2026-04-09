
import sys

znak = sys.argv[1]
plik1 = sys.argv[2]
plik2 = sys.argv[3]
#znak, plik1, plik2 = sys.argv[1:]

def comments(znak,plik1,plik2):
    with ( open(plik1, "r") as input_file,
         open(plik2, "w") as output_file, ):
        
            for line in input_file:
                if not line.strip().startswith(znak):
                    output_file.write(line)
    

comments(znak,plik1,plik2)
