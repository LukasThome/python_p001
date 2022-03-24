escalaO = input()
valor = float(input())
escalaS = input()

if escalaO == 'c' and escalaS == 'f':
    resultado = (valor * 9/5) + 32
elif escalaO == 'c' and escalaS == 'k':
    resultado = valor + 273.15
elif escalaO == 'c' and escalaS == 'r':
    resultado = (valor + 273.15) * 9/5

if escalaO == 'f' and escalaS == 'c':
    resultado =  (valor - 32) * 5/9 
elif escalaO == 'f' and escalaS == 'k':
    resultado = (valor - 32) * 5/9 + 273.15 
elif escalaO == 'f' and escalaS == 'r':
    resultado = valor + 459.67 

if escalaO == 'k' and escalaS == 'c':
    resultado =  valor - 273.15 
elif escalaO == 'k' and escalaS == 'f':
    resultado = (valor - 273.15) * 9/5 + 32 
elif escalaO == 'k' and escalaS == 'r':
    resultado = valor *1.8


if escalaO == 'r' and escalaS == 'c':
    resultado =  (valor - 491.67) * 5/9 
elif escalaO == 'r' and escalaS == 'f':
    resultado = valor - 459.67 
elif escalaO == 'r' and escalaS == 'k':
    resultado = valor * 5/9

print(resultado)

