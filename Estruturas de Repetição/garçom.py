
numero_bandeijas = int(input())

n = 1
cd = 0
while n <= numero_bandeijas:  
    latas, copos = input().split()
    latas, copos = int(latas),int(copos)
    if latas > copos:
        cd = cd + copos
    n = n+1

print(cd)
