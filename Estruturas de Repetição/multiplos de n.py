n = int(input())
m = int(input())
intervalo = abs(m - n) +n
print(intervalo)
rep = 1
while (rep <= intervalo):
    if rep%n==0:
        print (rep)
    rep=rep+1
        


    
    
    
