cont = 0
while True:
    try:
        def cria_matriz(n_linhas, n_colunas, valor_inicial=0):
            matriz = []
            for w in range(n_linhas):
                matriz.append([valor_inicial] * n_colunas)
            return matriz  
        n, m = [int(x) for x in input().split()] 
        a = cria_matriz(n, m)    
 
       
        ##Leitura de valores do usuario
        for i in range(n): 
            l = [int(x) for x in input().split()]   
            for j in range(m):
                a[i][j] = l[j]
        
        ##descobrir posicao do pokemon
        for i in range(n):
            for j in range(m):
                if a[i][j] == 2:
                    
                    linha_pokemon = i
                    coluna_pokemon = j
                    
                    
        
        ##descobrir posicao do player
        for i in range(n):
            for j in range(m):
                if a[i][j] == 1:
                    
                    linha_player = i
                    coluna_player = j
                    
        
        
        resultado  = abs(linha_player - linha_pokemon)  + abs(coluna_player - coluna_pokemon)
        print(resultado)
    except EOFError:
        break
print(cont)