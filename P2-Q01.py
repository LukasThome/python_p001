i = 0
fraseC = input().split(' ')
novaFrase = ""
fraseC_range = len(fraseC) -2
#print(len(fraseC))
indice = i + 2
for i in range(fraseC_range):
    
    #print(fraseC[i].isdigit())
    #verifica se o digito atual eh um numero
    if (fraseC[i].isdigit()):
        print(fraseC[i], "elemento [i]")
        #novaFrase[i] = fraseC[i + 1]
    #se for um numero, ele verifica se o o digito i+2 tambem eh
    elif(fraseC[i + 2].isdigit()):
        print(fraseC[i+2], "elemento [i+2]")
        print(fraseC[i + 1], "elemento [i+1]")
        elemento = fraseC[i + 1]
        print(fraseC.index(elemento))
        
        #novaFrase[i] = fraseC[i]
  
print(novaFrase)