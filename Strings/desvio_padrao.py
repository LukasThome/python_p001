import math

n = int(input())
valores = [float(input()) for _ in range(n)] # l� os valores um a um em linhas subsequentes e monta a lista de valores
    
media = sum(valores) / len(valores)
soma = sum([(x - media) ** 2 for x in valores]) # somat�rio dos quadrados das diferen�as
desvio_padrao = math.sqrt(soma / (len(valores) -1))

print(desvio_padrao)
