n = int(input())

for i in range(n):
    var = 0
    aproximado = 0
    varAnterior = 0
    
    qt,valorEscolhido = [int(x) for x in input().split()] 
    valores = [int(x) for x in input().split()] 
    
        
        #Se o usuario acertou o valor exato
    if valorEscolhido in valores:
        #print("Entrou no if errado")
        indice = valores.index(valorEscolhido) + 1
        print(indice)
        #Se nao calcula o valor aproximado
    else:
        for v in range (len(valores)):
            var = valores[v] - valorEscolhido
            if var < varAnterior:
                aproximado = valores[v]
                indiceAproximado = valores.index(aproximado) + 1
                print(type(indiceAproximado))
                primeiroIndice = append()      
                    #print("Entrou no if var < varAnterior")
            varAnterior = var
                
                 
        print(indiceAproximado)