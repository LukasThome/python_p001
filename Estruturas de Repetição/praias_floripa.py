n = int(input())
distancia_total = 0
distancia_anterior = 0
np = 0
distancia_totalf = 0
###################
##DISTANCIA MEDIA##
###################
for i in range(n):
    praia, distancia = input().split(';')
    distancia = int(distancia)
    
    distancia_total += distancia
    distancia_totalf = distancia_total/n
#####################
##PRAIA MAIS DISTANTE
#####################
    if distancia > distancia_anterior:
        praia_longe = praia
        distancia_anterior = distancia
######################
##CALCULA O RANGE     
    if 15 <= distancia <= 20:
        np +=1
#######################
        
string = (str(praia_longe) + ";" + str(np) + ";"+ str("%.1f" % distancia_totalf))
print(string)
