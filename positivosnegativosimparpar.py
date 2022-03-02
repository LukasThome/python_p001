negativo = 0
positivo = 0
par = 0
impar = 0

for i in range(5):
    n= int(input())
    print(n%2)
    if n > 0:
        positivo = positivo + 1
    if n < 0:
        negativo = negativo + 1
    if (n%2) == 0:
        par = par +1
        print("par")
    else:
       impar = impar +1

print(par, "valor(es) par(es)")
print(impar, "valor(es) impar(es)")
print(positivo,"valor(es) positivo(s)")
print(negativo, "valor(es) negativo(s)")
