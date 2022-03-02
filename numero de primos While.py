n1 = int(input())
n2 = int(input())
primos = 0

n2 += 1
for num in range(n1,n2):
    prime = True
    for i in range(2,num):
        if (num%i==0):
            prime = False
    if prime:
        primos += 1
print (primos)
