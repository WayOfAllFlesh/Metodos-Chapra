def maximo(valores, idx):
    tamanho = idx
    idx = 0

    maior = valores[idx]
    while idx < tamanho:
        if valores[idx] > maior:
            maior = valores[idx]

        idx += 1

    return maior

def media(valores, idx):
    tamanho = idx

    soma = 0
    idx = 0

    while idx < tamanho:
        soma += valores[idx]
        idx += 1

    return soma/(tamanho)

def soma(valores, idx):
    tamanho = idx

    soma = 0
    idx = 0

    while idx < tamanho:
        soma += valores[idx]
        idx += 1

    return soma

idx = 0
cartoes_valores = []
cartoes_status = []

while True:
    valor = int(input("Entre com o valor do cartão: "))
    status = int(input("É o cartão de saída? (1 - Sim | 0 - Não): "))
    if status != 0 and status != 1:
        while status != 0 and status != 1:
            print("Opção inválida! ")
            status = int(input("É o cartão de saída? (1 - Sim | 0 - Não): "))

    cartoes_valores.append(valor)
    cartoes_status.append(status)
    idx += 1

    if status != 0:
        break

valor_max = maximo(cartoes_valores, idx)
valores_media = media(cartoes_valores, idx)
valores_soma = soma(cartoes_valores, idx)

print(f"\nA soma dos valores é: {valores_soma}")
print(f"\nA média dos valores é: {valores_media}")
print(f"\nO valor máximo é: {valor_max}")