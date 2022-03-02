x1 = int(input())
x2 = int(input())
x3 = int(input())

pode_moverse = abs(x1-x2) + abs(y1-y2) == 3 and x1 != x2 and y1 != y2

print(pode_moverse)
