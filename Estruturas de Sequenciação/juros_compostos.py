import math

c = float(input("Insira o aporte inicial: "))

n = float(input("Insira a quantidade de anos que o dinheiro ira render: "))

i = float(input("Insira o valor da taxa de juros: "))


m = c * ((1 + i)**n)

print(m)
