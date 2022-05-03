import math

n = int(input())
valores = [float(input()) for _ in range(n)] # lê os valores um a um em linhas subsequentes e monta a lista de valores
    
media = sum(valores) / len(valores)
soma = sum([(x - media) ** 2 for x in valores]) # somatório dos quadrados das diferenças
desvio_padrao = math.sqrt(soma / (len(valores) -1))

print(desvio_padrao)
