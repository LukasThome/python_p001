nSequencia = int(input())
soma = 0
n = 0
while n < nSequencia:
    value = float(input())

    soma = value + soma
    n = n + 1

media = soma/nSequencia
print(media)
