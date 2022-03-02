n = int(input())
var = 0
for i in range(n):
    
    qt,valorEscolhido = [int(x) for x in input().split()] 
    
    for i in qt:
        valores = input().split()
        
        if valorEscolhido in valores:
            indice = valores.index(valorEscolhido) + 1
            print(indice)
        else:
            for i in valores:
                var = abs(int(valores[i]) - valoresEscolhido)
                varAnterior = var
                if var < varAnterior:
                    aproximado = var
                print(aproximado)