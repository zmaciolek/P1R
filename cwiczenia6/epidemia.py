import sys

class Person:
    def __init__(self, x: float, y: float, status: str, MaxDistance: float = 1, MaxIllDistance: float = 0.1):
        self.x = x
        self.y = y
        self.status = status
    def Move():
        pass
    def Info():
        pass
    def __str__(self):
        pass
        
class Population:
    def __init__(self, people: "Person", h: float = 100, w: float = 100, InfectionProbability: float = 0.2, InfectionDistance: float = 1):
        pass
    def Move():
        pass
    def Paint():
        pass