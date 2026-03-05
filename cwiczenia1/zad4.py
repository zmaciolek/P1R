import math
import numpy as np

def sum_a(x, n):
    suma1 = 0
    for i in range(n+1):
        suma1 = suma1+(x**i)/(math.factorial(i))
    return(suma1)
    
print(sum_a(3,20))
print(np.exp(3))
        

