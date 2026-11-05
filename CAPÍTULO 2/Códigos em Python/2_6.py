import numpy as np

def fact(n):
    if n <= 0:
        return 1
    else:
        return n * fact(n - 1)

x = float(input("Entre com o valor de X: "))
n = int(input("Entre com o número de termos: "))

sinal = 1
fator = 2
inicio = 0
i = 0

if n == 1:
    cos = 1
else:
    while i < n:
        if i == 0:
            cos = 1
            sinal = -sinal
            inicio += fator

        else:
            cos = cos + sinal*(x ** inicio)/fact(inicio)

            sinal = -sinal
            inicio += fator

        i += 1

erro = (np.cos(x) - cos)/np.cos(x) * 100 
print(f"\nValor do Cos: {cos} x {np.cos(x)}|| erro = {erro}")