import math

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

#calculo do delta

delta = b**2 - 4*a*c

#calculo das raizes
x1 = (-b + math.sqrt(delta)) / (2*a)
x2 = (-b - math.sqrt(delta)) / (2*a)

print("As raizes reais sao:", x1, "e", x2)
