#estrutura de repetição até que a entrada seja '*'
status = True

while (status):
    #ler valores
    entrada = [str(x) for x in input().split()]
    
    intervalo = entrada[0][0].lower()
    c = 0
    if entrada[0] == '*':
        status = False
        break
    
    #verificar tautograma
    for i in range (len(entrada)):
        entrada[i] = entrada[i].lower()
        if intervalo == entrada[i][0]:
            c += 1
        
    if c == len(entrada):
        print("Y")
    else:
        print("N")
    