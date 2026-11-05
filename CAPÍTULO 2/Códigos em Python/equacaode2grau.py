import matplotlib.pyplot as plt
import numpy as np

def raizSegundoGrau(a, b, c):
    delta = b**2 - 4*a*c

    if delta > 0:
        x1 = -b/(2 * a) + (np.sqrt(delta))/(2*a)
        x2 = -b/(2 * a) - (np.sqrt(delta))/(2*a)
        condition = 0

        return x1, x2, condition
    
    elif delta == 0:
        x = -b/(2 * a)
        condition = 1

        return x, 0, condition

    else:
        parte_real = -b/(2 * a)
        parte_imaginaria = (np.sqrt(-delta))/(2 * a)
        condition = 2

        return parte_real, parte_imaginaria, condition

print("Entre com os três coeficientes da equação de segundo grau: ")
a = int(input("Entre com o coeficiente A: "))
b = int(input("Entre com o coeficiente B: "))
c = int(input("Entre com o coeficiente C: "))

x1, x2, condition = raizSegundoGrau(a, b, c)

if condition == 0:
    print(f"As raizes da equação são: {x1} e {x2}")
    
elif condition == 1:
    print(f"As raiz da equação é: {x1}")

else:
    print(f"As raizes da equação são: {x1} +- {x2}i")
