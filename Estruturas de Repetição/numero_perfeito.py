num_casos = int(input())
for _ in range(num_casos):
    
    n = int(input())
    
    soma = 0
    for i in range(1, n):
        if n % i == 0:
            soma += i
    if n == soma:
        print("{} eh perfeito".format(n))
    else:
        print("{} nao eh perfeito".format(n))