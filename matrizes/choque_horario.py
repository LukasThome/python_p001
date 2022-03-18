n = int(input())
a = []
saida = []
horarios_ufsc= {'0730':0,'0820':1, '0910':2, '1010':3, '1100':4, '1330':5, '1420':6, '1510':7, '1620':8, '1710':9,'1830':10, '1920':11, '2020':12, '2110':13}


# Criar uma matriz
def cria_matriz(n_linhas, n_colunas, valor_inicial=0):
    matriz = []
    for i in range(n_linhas):
        matriz.append([valor_inicial] * n_colunas)
    return matriz

a = cria_matriz(14, 5, '*')
inconsistencia = ''        

for k in range(n):
    disciplina, *horarios= [x for x in input().split()]
  
    for r in range (len(horarios)):
     
        infos = horarios[r]
        coluna = int(infos[0]) -2
        key = infos[1:-1]
        linha = horarios_ufsc[key]
        n_aulas = int(infos[-1])
        
        w = 0
        for w in range(n_aulas):    
            if a[linha][coluna] == '*':
                a[linha][coluna] = disciplina
                linha +=1
            else:
                inconsistencia = a[linha][coluna] + ' ' + disciplina
                saida.append(inconsistencia)
                
print(saida[0])            

#for i in range(0,14):
    #for j in range(0,5):
        #print(a[i][j],end=' ')
    #print()