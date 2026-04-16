import sys
from argparse import ArgumentParser

class Stack:
    def __init__(self):
        self.stos = []

    def pusty(self):
        return self.stos == []
    
    def push(self, element):
        return self.stos.append(element)
    
    def pop(self):
        return self.stos.pop()
    

 

#x1 = float(sys.argv[1])
#x2 = float(sys.argv[2])

#stos1 = Stack()

#stos1.push(x1)
#stos1.push(x2)


def main():
    parser = ArgumentParser()
    parser.add_argument( 
        "numbers",
        nargs="+",
        type=float,
    )   
    args = parser.parse_args()
    stos1 = Stack()
    for number in args.numbers:
        stos1.push(number)
    while not stos1.pusty():
            print(stos1.pop())




main()
