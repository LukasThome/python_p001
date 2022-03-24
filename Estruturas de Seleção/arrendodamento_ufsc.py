import math

nota = float(input())

if nota*10%10 >= 2.5 and nota*10%10 < 7.5:
    final= (math.floor(nota)) + 0.5
elif nota*10%10 < 2.5:
    final= (math.floor(nota))
else:
    final= (math.ceil(nota))
    
print(final)