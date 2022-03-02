import math

n = int(input())
# lê os valores um a um em linhas subsequentes e monta a lista de valores
valores = [float(input()) for _ in range(n)] 


#geometric media function

def MediaGeometrica(numero, lista):
    produto = 1 
    for numero in lista:
        produto *= numero
        
    
    mediaG = produto ** (1/n)
   
    return mediaG

mediaGeo = MediaGeometrica(n, valores)
print("mediaGeo", mediaGeo)
