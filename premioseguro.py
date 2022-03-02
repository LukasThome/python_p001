valor = float(input())
tipo_desconto = input()
origem = input()
idade = int(input())

if origem == 'estrangeira':
    desconto_categoria = valor * 0.15
if origem == 'nacional':
    desconto_categoria = valor * 0.10

descontoIdade  = valor * 0.010

def classe_desconto(classe):
    if classe == 'A':
        desconto_classe = desconto_categoria * 0.70
    elif classe == 'B':
        desconto_classe = desconto_categoria * 0.80
    elif classe == 'C':
        desconto_classe = desconto_categoria * 0.90
    elif classe == 'D':
        desconto_classe = desconto_categoria * 0.95
    else:
        desconto_classe = desconto_categoria * 1
    return desconto_classe


desconto = classe_desconto(tipo_desconto)



if idade > 24:
    desconto = desconto - descontoIdade



print("{:.2f}".format(desconto))
