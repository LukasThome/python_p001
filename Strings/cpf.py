import re

cpf = input()

#limpa os pontos e ifens da string
cpf = re.sub(r'[^\w\s]','',cpf)

########################### Ultimo Digito ###########
def verificadorUD(numero):
    soma = 0
    peso = len(numero)   
    #aplica os pesos para o calculo do ultimo digito
    for i in range(len(numero)-1):
        soma += int(numero[i]) * peso
        peso -= 1
    dv = 11 - soma % 11

    #tratamento de casos
    if dv >= 10:
        dv = 0
    if(dv == int(numero[-1])):
        return True
    else:
        return False

################## Penúltimo dígito ##############
def verificadorPD(numero):
    soma = 0
    peso = len(numero) -1   
    #aplica os pesos para o calculo do ultimo digito
    for i in range(len(numero)-2):
        soma += int(numero[i]) * peso
        peso -= 1
        
    dv = 11 - soma % 11

    #tratamento de casos
    if dv >= 10:
        dv = 0
    if(dv == int(numero[-2])):
        return True
    else:
        return False

estadoUD = verificadorUD(cpf)

estadoPD = verificadorPD(cpf)

estado = estadoPD and estadoUD

#verifica se todos numeros são iguais
primeiroN = cpf[0]
if (estado == True):
    for i in range (len(cpf)):
        if(cpf[i] != primeiroN):
            estado = True
            break
        else:
             estado = False       

print(estado)
