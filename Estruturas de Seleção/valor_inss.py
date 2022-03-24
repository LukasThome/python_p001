salario_bruto = float(input())

if salario_bruto <= 720:
    inss = salario_bruto*0.0765
elif salario_bruto <= 1200:
    inss = salario_bruto*0.09
elif salario_bruto <= 2400:
    inss = salario_bruto*0.11
else:
    inss = 2400*0.11
    
print(inss)