nomeCompleto = input().split()
primeiroNome = nomeCompleto[0]
ultimoNome = nomeCompleto[-1]
meio = " "
nomeMeio = ""
named = ""
for i in range (1, len(nomeCompleto) -1):  
    meio += nomeCompleto[i] + " "
    

meio = meio.split()

#print(len(meio[0]))
for i in range (len(meio)):
    
    if len(str(meio[i])) > 3:
        
        named = meio[i]
        named  = named[0:1] + "."
        
        nomeMeio += named + " "
    else:
        nomeMeio += meio[i]
        
primeiroNome = str(primeiroNome)
ultimoNome = str(ultimoNome)


print(primeiroNome + " " + nomeMeio + " " + ultimoNome)