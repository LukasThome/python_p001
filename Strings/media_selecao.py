p1 = float(input())
p2 = float(input())
p3 = float(input())

media = (p1+p2+p3)/3

if media >= 9:
    print("Ótimo")
elif media < 9 and media >= 7.5:
    print("Bom")
elif media <7.5 and media >= 6:
    print("Satisfatório")
else:
    print("Insuficiente")
