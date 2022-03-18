n_matriz = int(input())

p, q, r, s, x, y = [int(w) for w in input().split()]

ci, cj= [int(w) for w in input().split()]

v = 0
a = []
b = []

for u in range(n_matriz):
        a.append([0] * n_matriz) # insere a linha i
        b.append([0] * n_matriz) # insere a linha i

###############################
###inicio da logica maluca#####
###############################
i = ci - 1
j = 1

for k in range(0, n_matriz): 
    a[i][k] = ((p * ci) + (q * j)) % x
    j += 1

j = cj - 1
i = 1

for k in range(0, n_matriz):    
    b[k][j] = (r * i + s * cj) % y
    i += 1

i = ci-1
j = cj-1
for k in range (0, n_matriz):
    v += a[i][k] * b[k][j]

print(v)