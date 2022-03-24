n = int(input())
melhorSalto = 0
melhorSalto_anterior = 0
melhor_saltador = ""

for i in range(n):
    infos = input().split()
    infos.sort()
    
   
    melhorSalto = float(infos[2])
    

 
  
    if melhorSalto > melhorSalto_anterior:
        melhor_saltador = infos[-1]
        melhorSalto_anterior = melhorSalto
print(melhor_saltador)