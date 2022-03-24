consumo = int(input())

contador = 0
tarifa_4 = 0
tarifa_3 = 0
tarifa_2 = 0
tarifa_1 = 0

while consumo >= contador:
    contador += 1
    if contador <= 30:
        tarifa_1 = contador*0.09556
    elif 31 <= contador <= 100:
        tarifa_2 = (consumo-30)*0.16698
    elif 101 <= contador <= 200:
        tarifa_3 = (consumo-100)*0.25052
    else:
        tarifa_4 = (consumo-200)*0.27836

custo_total = tarifa_1 + tarifa_2 + tarifa_3 + tarifa_4

print(round(custo_total,2))
