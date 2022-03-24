valor_inicial = float(input())
valor_desconto = valor_inicial*0.80

if valor_inicial >= 500:
    valor_desconto = valor_desconto - valor_inicial*0.10
   

if valor_inicial > 1000:
    descontoMil =  (valor_inicial - 1000)    -    ((valor_inicial - 1000) *  0.85)  
    valor_desconto = valor_desconto - descontoMil
    

print("%.2f" %valor_desconto)
