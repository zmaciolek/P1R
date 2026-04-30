class Polynomial:
    def __init__(self, c):
        self.c = list(c)
    def __str__(self):
        return (f"Wielomian ma współczynniki: {self.c}")
    def degree(self):
        return len(self.c)-1
    def __getitem__(self, index):
        return self.c[index]
    def __setitem__(self, index, new_coeff):
        self.c[index]=new_coeff
    def evaluate(self, x):
        value = 0
        power = 0
        for i in range(len(self.c)):
            value = value+(self.c[i]*(x**power))
            power = power+1
        return value
    def __add__(self, other="Polynomial"):
        if self.degree() >= other.degree():
            referencja = other.c
            suma = self.c.copy()
        else:
            referencja = self.c
            suma = other.c.copy()
        for i, wspolczynnik in enumerate(referencja):
            suma[i] = suma[i] + wspolczynnik
        return Polynomial(suma)
    def __mul__(self, k=float):
        new_coeffs = [k*self.c[i] for i in range(len(self.c))]
        return Polynomial(new_coeffs)
    
    def __rmul__(self, k = float):
        return self.__mul__(k)
    def D(self):
        new_coeffs = []
        for i in range(self.degree()):
            new_coeffs.append(self.c[i+1]*(i+1))
        return Polynomial(new_coeffs)
        
p1 = Polynomial([1,2,1])
p2 = Polynomial([2,1,1])
print(p1.D())
# print(2*p1)



    
