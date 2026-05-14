import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt


def f(t, vector, a,b,c,d):
    x, y = vector
    dxdt = (a-b*y)*x
    dydt = (-c+d*x)*y

    return [dxdt, dydt]


def solver(t_eval, vector0):
    a = 1
    b = 1
    c = 1
    d = 1
    sol = solve_ivp(f, (0, t_eval[-1]), vector0, t_eval=t_eval, args = (a,b,c,d))
    return sol.t, sol.y[0], sol.y[1]

t_max = 100
t_eval = np.linspace(0, t_max, 1000)
vector0 = np.array([1.5, 3])
t, x, y = solver(t_eval, vector0)

plt.plot(t, x, label='x(t)')
plt.plot(t, y, label='y(t)')
plt.legend()
plt.show()
