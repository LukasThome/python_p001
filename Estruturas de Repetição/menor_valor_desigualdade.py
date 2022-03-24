import math

n = 1000

def qual_valor():
    for i in range(1, n):
        if math.factorial(i) > i**10:
            print(i)
            break
            
qual_valor()
