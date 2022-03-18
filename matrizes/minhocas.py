def cria_matriz(n_linhas, n_colunas, valor_inicial=0):
    matriz = []
    for w in range(n_linhas):
        matriz.append([valor_inicial] * n_colunas)
    return matriz

n, m = [int(x) for x in input().split()] 

a = cria_matriz(n,m)

soma = 0
soma_anterior = []

l = []

##Leitura de valores do usuario
for i in range(n): 
    l = [int(x) for x in input().split()]   
    for j in range(m):
        a[i][j] = l[j]


#############LINHAS#############
for i in range(n): 
    soma_anterior.append(soma)
    soma = 0  
    for j in range(m):
        
        soma += a[i][j]   


        
        
#############COLUNAS#############
for j in range(m): 
    soma_anterior.append(soma)
    soma = 0
    for i in range(n):
        soma += a[i][j]   

soma_anterior.append(soma)
soma_anterior = sorted(soma_anterior)
print(soma_anterior[-1])