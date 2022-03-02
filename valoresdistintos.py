#n = int(input())
valores = set() # cria um conjunto vazio
for _ in range(n):
    valores.add(int(input())) # acrescenta o valor lido no conjunto, já eliminando as repetições
print(valores)
print(len(valores)) # imprime a cardinalidade do conjunto, ou seja a quantidade de valores distintos