inputDias = int(input())

ano = inputDias // 365

meses = (inputDias % 365) // 30

dias = ((inputDias % 365) % 30)

print(ano, "ano(s)")

print(meses, "mes(es)")

print(dias, "dia(s)")
