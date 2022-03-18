n = 12

metodo = input()
soma = 0


###METODO QUE MONTA A MATRIZ INFORMADA PELO USUARIO#####

matriz = []
for u in range(n):
        matriz.append([0] * n) # insere a linha i
for i in range(n):  # calcula os valores da linha i
    for j in range(n):
            matriz[i][j] = float(input())            
########################################################        

for i in range(n):  # calcula os valores acima da diagonal secundaria
    for j in range(n):
            if i + j >= (n-1):
                i+=1
            else:
                soma += matriz[i][j]  



n_elementos = ((n * n)/2) - n/2

media = soma/n_elementos

if metodo == 'S':
    print("{0:.1f}".format(soma))
else:
    print("{0:.1f}".format(media))