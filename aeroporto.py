


aeroporto = []
maior = 0 
num = 0
num2 = 0
entrada = True
n = 0




#Lendo os valores de A e V - aeroportos e voos
a,v = [int(x) for x in input().split()]  

while (entrada):
    
   #verificando os valores para interromper o loop quando a e v == 0
    if a and v == 0:
        entrada = False
        continue
    
    
    
    
    #lendo os valores de x e y, numero do aeroporto e voos
    for i in range(v):
        x = [int(x) for x in input().split()]
        aeroporto.append(x)
        print(aeroporto)
       


    n += 1   
    
    print("Teste ", n)
    
    
    
    #encontrando o aeroporto com mais incidencias
    for i in aeroporto:
        c= aeroporto.count(i)
        #d = aeroporto.count(i)
        #print(c)
        if c >= maior:
            maior = c
            num = i

    #se existirem dois aeroportos com o mesmo numero de voos ele deve apresentar os dois
    print(num)
    print()
    
    a,v = [int(x) for x in input().split()] 
    