import math

def f(x):
    return x**3-2*x**2+2*x-5


x0 = 1
x1 = 1.5
x2 = 2


h0 = x1 - x0
h1 = x2 - x1
d0 = (f(x1) - f(x0)) / h0  
d1 = (f(x2) - f(x1)) / h1  

a = (d1 - d0) / (h1 + h0)

# Parámetros del método
i = 3  # Empezamos desde la tercera iteración
N = 100  # Número máximo de iteraciones
tol = 0.0000001  # Tolerancia

# Iteraciones
while i < N:
    b = d1 + a * h1
    D = (b**2 - 4 * f(x2) * a)**0.5
    if abs(b - D) < abs(b + D):
        E = b + D
    else:
        E = b - D

    h = -2 * f(x2) / E
    x = x2 + h

    # Imprimir el valor de x en cada iteración
    print(f"Iteración {i}: x = {x}")

    # Comprobar si la diferencia es menor que la tolerancia
    if abs(h) < tol:
        print(f"Raíz aproximada encontrada: {x}")
        break

    # Actualizar los valores para la siguiente iteración
    x0 = x1
    x1 = x2
    x2 = x

    h0 = x1 - x0
    h1 = x2 - x1
    d0 = (f(x1) - f(x0)) / h0
    d1 = (f(x2) - f(x1)) / h1

    a = (d1 - d0) / (h1 + h0)

    i += 1