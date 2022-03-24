salario_atual = float(input())
salario_minimo = float(input())

#ajusta para 20%
if salario_atual <= salario_minimo * 3:
    reajustado = (salario_atual * 1.2)
#ajusta para 15%
elif 3*salario_minimo < salario_atual <= 5*salario_minimo:
    reajustado = (salario_atual * 1.15)
#ajusta para 10#
else:
    reajustado = salario_atual * 1.1
    
if salario_minimo*20 >= reajustado >= 1.5 * salario_minimo:
    salario_final = reajustado
else:
    salario_final = salario_atual * 1.10
    
#print(salario_final)
print(f'{salario_final:.2f}')