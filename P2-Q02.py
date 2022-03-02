from collections import OrderedDict

lista = []
listaTratada = []
while True:
    
    email = input()
    
    if 'fim' in email:
        break
    else:
        lista.append(email)
    
    #print(lista)
    #for i in range (len(lista)):
        #if lista[i] not in listaTratada:
            #
            #listaTratada.append(str(lista[i]))
    listaTratada = list(OrderedDict.fromkeys(lista))
    listaTratada.sort()

for v in range (len(listaTratada)):
    print(str(listaTratada[v]))