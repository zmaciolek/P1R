import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt




def f(t, vector, g, l):
    theta, omega = vector
    dxdt = omega
    dydt = -(g/l)*np.sin(theta)

    return [dxdt, dydt]


def solver(t_eval, vector0):
    g = 9.81
    l = 1
    sol = solve_ivp(f, (0, t_eval[-1]), vector0, t_eval=t_eval, args = (g, l))
    return sol.t, sol.y[0], sol.y[1]

t_max = 10
t_eval = np.linspace(0, t_max, 100)
vector0 = np.array([1.5, 3])
t, x, y = solver(t_eval, vector0)

plt.plot(t, y, label='x(t)')
plt.show()
plt.plot(x, y, label="omega(teta)")
plt.show()