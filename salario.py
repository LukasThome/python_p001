horas = float(input())
horasE = float(input())


salarioBase = 2500

valorHora = salarioBase/200
valorHoraE = valorHora*1.2

salarioBruto = (horas*valorHora) + (horasE*valorHoraE)

ir = salarioBruto * 0.13
inss = salarioBruto *0.09

salarioLiquido = salarioBruto - ir - inss


print(" - Salário Bruto : R$", salarioBruto)
print(" - IR (13%) : R$ ", ir)
print(" - INSS (9%) : R$" ,inss)
print(" - Salário Líquido : R$",salarioLiquido)
