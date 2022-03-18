def cria_matriz(n_linhas, n_colunas, valor_inicial=0):
    matriz = []
    for w in range(n_linhas):
        matriz.append([valor_inicial] * n_colunas)
    return matriz


numero_instancia = 0
ref = [1,2,3,4,5,6,7,8,9]
lista_analise = []
count = 0

n  = int(input())
linhas_total = n *9
linhas = 9
a = cria_matriz(linhas_total, 9)       

##Leitura de valores do usuario
for i in range(linhas_total): 
    l = [int(x) for x in input().split()]   
    for j in range(9):
        a[i][j] = l[j]

###########################################
j = 0        
for i in range(n):
    #analisar somente uma instancia
    #analisa  a primeira linha
    for j in range(len(ref)):
        item = a[i][j]
        lista_analise.append(item)
    if(set(ref) == set(lista_analise)):
        count += 1
    #######################
        
    #linhas
    lista_analise = []
    for i in range(linhas):
        if(set(ref) == set(lista_analise)):
            count += 1
        lista_analise = []
        for j in range(len(ref)):
            item = a[i][j]
            lista_analise.append(item)

    #colunas
    for j in range (linhas):
        if(set(ref) == set(lista_analise)):
            count += 1
        lista_analise = []
        for i in range(len(ref)):
            item = a[i][j]
            lista_analise.append(item)

    numero_instancia += 1
    print("Instancia", numero_instancia)
    
    if count == 18:
   
        print("SIM")
    else:
         print("NÃO")
    