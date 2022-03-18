n = 12

linha = int(input())

metodo = input()




###METODO QUE LE A MATRIZ INFORMADA PELO USUARIO#####

matriz = []
for u in range(n):
        matriz.append([0] * n) # insere a linha i
for i in range(n):  # calcula os valores da linha i
    for j in range(n):
        matriz[i][j] = float(input())
########################################################        


soma = 0
media = 0
for x in range (n):
    soma += matriz[linha][x]
soma = 0

for y in range (n):
    soma += matriz[linha][y]
media = soma/n 

if metodo == 'S':
    print("{0:.1f}".format(soma))
else:
    print("{0:.1f}".format(media))