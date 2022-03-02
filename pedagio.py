comprimento, distancia = input().split()
comprimento, distancia = float(comprimento),float(distancia)

custo_km, valor_pe = input().split()
custo_km, valor_pe = float(custo_km),float(valor_pe)

nPedagios = comprimento // distancia

resultado = custo_km * comprimento + nPedagios * valor_pe

print(resultado)
