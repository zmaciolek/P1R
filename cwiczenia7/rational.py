import sys
import math

def simplify_fraction(p, q):
    if q <= 0:
        raise ValueError("q nie moze byc zero lub mniej")
    gcd = math.gcd(p, q)
    p = p / gcd
    q = q / gcd
    return int(p), int(q)


class RationalNumber:
    def __init__(self, p=int, q=int):
        p, q = simplify_fraction(p,q)
        self.p = p
        self.q = q

    def __str__(self):
        simplify_fraction(self.p,self.q)
        return f"{self.p}/{self.q}"
    def repr(self):
        simplify_fraction(self.p,self.q)
        return f"Liczba to {self.p}/{self.q}"
    def numerator(self):
        simplify_fraction(self.p,self.q)
        return (self.p)
    def denumerator(self):
        simplify_fraction(self.p,self.q)
        return (self.q)
    def __float__(self):
        return float(self.p/self.q)
    def przeciwny(self):
        simplify_fraction(self.p,self.q)
        self.p = -int(self.p)
        return f"Liczba to {self.p}/{self.q}"


numer = RationalNumber(2,4)
print(float(numer))
print(numer)
# print(numer.przeciwny())
# print(numer.denumerator())

