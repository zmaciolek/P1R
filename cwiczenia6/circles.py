from math import inf, pi, sqrt, fabs
import sys

if __name__ == '__main__':

    class circles:
        def __init__(self, x: float, y: float, r: float):
            self.x = x
            self.y = y
            self.r = r

        def Circumference(self):
            obwod = 2*pi*self.r
            return obwod
    
        def Intersection(self, drugie_kolo: "circles"):
            d = sqrt((drugie_kolo.x-self.x)**2+(drugie_kolo.y-self.y)**2)
            if d == 0 and self.r == drugie_kolo.r:
                przeciecia = inf
            elif d > (self.r+drugie_kolo.r):
                przeciecia = 0
            elif d == (self.r+drugie_kolo.r):
                przeciecia = 1
            elif d == fabs(self.r-drugie_kolo.r):
                przeciecia = 1
            elif d != 0 and d < fabs(self.r-drugie_kolo.r):
                przeciecia = 0
            elif fabs(self.r-drugie_kolo.r) < d < (self.r+drugie_kolo.r):
                przeciecia = 2
            return przeciecia
        
            print(self.x, self.y, self.r)
            print(drugie_kolo.x, drugie_kolo.y, drugie_kolo.r)

    x1 = float(sys.argv[1])
    y1 = float(sys.argv[2])
    r1 = float(sys.argv[3])
    x2 = float(sys.argv[4])
    y2 = float(sys.argv[5])
    r2 = float(sys.argv[6])

    kolo1 = circles(x1,y1,r1)
    kolo2 = circles(x2,y2,r2)
    
    print(kolo1.Intersection(kolo2))
    print(kolo2.Intersection(kolo1))

    









