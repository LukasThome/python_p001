numero = input()

soma = 0
peso = len(numero)
#print(peso)

#aplica os pesos para o calculo
for i in range(len(numero)-1):
    soma += int(numero[i]) * peso
    peso -= 1


dv = 11 - soma % 11

#tratamento de casos
if dv >= 10:
    dv = 0

#resultado
print(dv == int(numero[-1]))
#print (dv)
