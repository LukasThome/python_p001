salario_bruto = float(input())
dependentes = int(input())

if salario_bruto <= 720:
    inss = salario_bruto*0.0765
elif salario_bruto <= 1200:
    inss = salario_bruto*0.09
elif salario_bruto <= 2400:
    inss = salario_bruto*0.11
else:
    inss = 2400*0.11
    
if 1372.82 < salario_bruto <= 2743.25:
    aliquota = 0.15
    deducao = 205.92
elif salario_bruto > 2743.25:
    aliquota = 0.275
    deducao = 548.82
else:
    aliquota = 0
    deducao = 0
    
irrf = (salario_bruto - dependentes*137.99 - inss) * aliquota - deducao
    
print(irrf)