n = int(input())
a = []
count = 0
somaRef = 0
for u in range(n):
    a.append([0] * n) # insere a linha i

for i in range(n):  # calcula os valores da linha i
    w = 0
    l = []
    l = [int(x) for x in input().split()]
    for j in range(n):
        a[i][j] = l[w]   
        w += 1

##############################


##calcula a diagonal 1  e seta o parametro de soma
soma = 0
for w in range(n):
    soma += a[w][w]
somaRef = soma     

##calcula a diagonal 2  
w = 0
soma = 0
for i in range(n-1, -1, -1):   
    soma += a[i][w]
    w += 1
    #print(soma)
if somaRef == soma:
    count +=1         
    #print("count diagonal2")



##Calcula as n linhas##        
j=0
for i in range(n):
    soma = 0
    for j in range(n):
        soma += a[i][j]
    if somaRef == soma:
        count +=1
        #print("count n linhas")
##Calcula as n lcolunas##  
for j in range(n):
    soma = 0
    for i in range(n):
        soma += a[i][j]
    if somaRef == soma:
        count +=1
        #print("count n colunas")

##verifica se as somas tem o resultado igual            
if count == (n * 2) + 1:
    status = True
else:
    status = False
print(status)
