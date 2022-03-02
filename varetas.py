qtTotal = 0
exit = False

while exit == False:  
       
        nEntradas = int(input())

        if nEntradas == 0:
                exit = True
                break
        n = 1
        qtTotal = 0
        while n <= nEntradas:
                tamanho, quantidade = input().split()
                tamanho, quantidade = float(tamanho),float(quantidade)
                #print(tamanho, quantidade)
                qtTotal = qtTotal + quantidade//4
                #print(qtTotal)
                n +=1
                #print("n entradas = ",nEntradas)


                if (quantidade // 2 == 1):
                        qtTotal += 1/2

        print(int(qtTotal))
       
