dias = int(input())
km = float(input())

custo_dias = dias*45

if km > 60*dias:
    custo_km = 0.50*(km-(60*dias))
else:
    custo_km = 0

valor_locacao = custo_km + custo_dias

print(valor_locacao)
    