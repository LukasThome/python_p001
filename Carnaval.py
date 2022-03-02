notas = [float(x) for x in input().split()]
notas.sort()
print( "%.2f" % sum(notas[1:-1]))
