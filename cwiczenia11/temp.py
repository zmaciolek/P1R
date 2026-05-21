import numpy as np

T = np.full(50,50)

T1 = 50
T2 = 60
T3 = 70
T4 = 80
T0 = 20
alpha = 2


T = np.full((50,50), T0)

T[0, :] = T1
T[-1, :] = T2
T[:, -1] = T3
T[:, 0] = T4

def update():
    T_new = 0.25
