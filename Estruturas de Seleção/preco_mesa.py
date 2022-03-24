comprimento = float(input())
largura = float(input())
gaveta = int(input())
madeira = str(input())

tamanho = largura * comprimento
custo = (tamanho * 100) + (gaveta * 30)

if tamanho > 2:
    custo_tamanho = custo + 50
else:
    custo_tamanho = custo
    
if madeira == "mogno":
    custo_tipo = custo_tamanho + 150
elif madeira == "carvalho":
    custo_tipo = custo_tamanho + 125
else:
    custo_tipo = custo_tamanho

if custo_tipo < 200:
    custo_final = 200
else:
    custo_final = custo_tipo
    
print(f'{custo_final:.2f}')

