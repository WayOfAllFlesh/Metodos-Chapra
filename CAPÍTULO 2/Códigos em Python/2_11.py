import pandas as pd
import numpy as np

def verifica(variavel):
    if variavel < 0:
        while variavel < 0:
            variavel = int(input("O valor da entrada não pode ser negativo. Tente novamente: "))

    return variavel

p = int(input("Entre com o valor do investimento inicial: "))
p = verifica(p)

j = int(input("Entre com o valor da taxa de juros: "))
j = verifica(j)

n = int(input("Entre com o prazo do investimento inicial: "))
n = verifica(n)

anos = [0] * (n + 1)
valores = [0] * (n + 1)
for i in range(0, n + 1):
    anos[i] = i
    valores[i] = p*((1 + j/100) ** i)

data = {
    "Anos": anos,
    "Retorno": valores
}

df = pd.DataFrame(data)
print(df)