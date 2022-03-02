txt = input().split(' ')
n_txt = ''
for p in txt:
    for i in range(1,len(p),2):
        n_txt += p[i]
    n_txt += ' ' 

print(n_txt)