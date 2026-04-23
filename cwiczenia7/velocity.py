import sys
from math import sqrt

class Velocity:
    def __init__(self, velocity=float):
        self.velocity = velocity

    def __str__(self):
        return f"Predkosc to {self.velocity}"
    
    def __repr__(self):
        return f"Predkosc('{self.velocity})"
    
    def gamma(self):
        return (1 / (sqrt(1 - (self.velocity)**2)))
    
    def _adding(self, other="Velocity"):
        return ((self.velocity - other.velocity) / (1 + (self.velocity * other.velocity)) )
    
    def __add__(self, other="Velocity"):
        return self._adding(other)

    def __iadd__(self, other="Velocity"):
        self.velocity = (self.velocity - other.velocity) / (1 + (self.velocity * other.velocity)) 
        return self
    


vel1 = Velocity(0.4)
vel2 = Velocity(0.2)
print(vel1.gamma())
print(vel2)
print(repr(vel1))
print(vel1 + vel2)

vel1 += vel2
print(vel1)


vel1 += vel2
print(vel1)
