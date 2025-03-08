import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def pvi(t, y):
    return -(np.exp(t)*y + np.exp(t) - 1)/(np.exp(t)*y + 1)

# Condiciones iniciales
t_span = (1, 5)
y0 = [1]

# Resolver la ecuación diferencial
sol = solve_ivp(pvi, t_span, y0, t_eval=np.linspace(1, 5, 100))

# Graficar la solución
plt.plot(sol.t, sol.y[0], label='$y(x)$')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.title('Solución del P.V.I.')
plt.legend()
plt.grid(True)
plt.show()

# Segunda ecuación diferencial
x = np.linspace(-2, 2, 400)
y = np.linspace(-2, 2, 400)
X, Y = np.meshgrid(x, y)

# Campo vectorial de la ecuación diferencial original
U = Y**2 + 2*X*Y
V = -X**2

# Normalizar los vectores
N = np.sqrt(U**2 + V**2)
U /= N
V /= N

# Graficar el campo vectorial
plt.quiver(X, Y, U, V, color='C0', angles='xy')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.title('Campo vectorial de la ecuación diferencial')
plt.grid(True)
plt.show()
