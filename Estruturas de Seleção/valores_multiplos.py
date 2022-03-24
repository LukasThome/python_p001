a, b = [int(w) for w in input().split()]

if a%b  == 0 or b%a == 0:
    resultado = 'Sao Multiplos'
else:
    resultado = 'Nao sao Multiplos'
print(resultado)
