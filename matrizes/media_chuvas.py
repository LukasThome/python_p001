m = 12
new = []
media = 0
for i in range(m): 
    soma = 0
    media = 0
    w = 0
    l = []
    l = [int(x) for x in input().split()]
    for j in l:
        #a[i][j] = l[w]  
        soma += l[w]
        w += 1
    
    media = soma/int(len(l))
    media = round(media, 2)
    new.append(media) 
     
print(new)