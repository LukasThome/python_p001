p1 = input()
p2 = input()
p3 = input()
p4 = input()


def switch(p1):
    notas = {
        'a': 4,
        'b': 3,
        'c': 2,
        'e': 0,
    }
    return notas[p1]

p1 = switch(p1)
p2 = switch(p2)
p3 = switch(p3)
p4 = switch(p4)

if p1 < 2:
    resultdado = False
if p2 < 2:
    resultdado = False
if p3 < 2:
    resultdado = False
if p4 < 2:
    resultdado = False
    

media = (p1 + p2 + p3 + p4)/4

if media < 3:
    resultado = False
else:
    resultado = True
print(resultado)
    
