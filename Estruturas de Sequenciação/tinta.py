area = int(input())

galao = 64.8

numeroGaloes = area/galao
numeroGaloes = round(numeroGaloes)
numeroGaloes = min(1, numeroGaloes) 
valor = round(numeroGaloes) * 25

print("- área de cobertura:", area)
print("- número de galões:" ,numeroGaloes)
print("- valor a ser pago: R$", valor)
