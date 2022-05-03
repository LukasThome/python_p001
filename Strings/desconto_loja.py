valor_inicial = float(input())
valor_desconto = valor_inicial*0.80

if valor_inicial >= 500:
    valor_desconto = valor_inicial*0.80 - valor_inicial*0.10
elif valor_inicial > 1000:
    valor_desconto = ((valor_inicial - 1000) *  0.85) + valor_desconto

print(valor_desconto)
