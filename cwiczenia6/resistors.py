import sys

class Resistor:
    def __init__(self, resistance: float = 0):
        self.__R = resistance
    
    def get_resistance(self):
        return self.__R
    def set_resistance(self, resistance):
        self.__R = resistance
    
    @staticmethod
    def series(r1: "Resistor", r2: "Resistor"):
        return Resistor(r1.get_resistance()+r2.get_resistance())
def parallel(r1: "Resistor", r2: "Resistor"):
    return Resistor(1 / (1 / r1.get_resistance() + 1 / r2.get_resistance()))
    
res1 = float(sys.argv[1])
res2 = float(sys.argv[2])

opornik1 = Resistor(res1)
opornik2 = Resistor(res2)

print(Resistor.series(opornik1, opornik2).get_resistance()) #wywołanie metody statycznej
print(parallel(opornik1, opornik2).get_resistance())
    

