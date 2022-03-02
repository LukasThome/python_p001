x,y = [int(x) for x in input().split()]

l = [int(x) for x in input().split()]
comprimentoLeitura = len(l) - 1

for i in range (comprimentoLeitura):
    if ((l[i] - l[i+1])) > (-x):
        resultado = "YOU WIN"
        #print(l[i] - l[i+1])
        #print(resultado)
    else:
        resultado = "GAME OVER"
        #print(l[i] - l[i+1])
        #print(resultado)
print(resultado)
