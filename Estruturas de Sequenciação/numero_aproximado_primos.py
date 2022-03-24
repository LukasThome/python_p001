import math

numero = int(input())
pi = math.pi

minimo = numero / math.log(numero)
maximo = 1.25506 * (numero / math.log(numero))

print(f'{minimo:.1f} {maximo:.1f}')