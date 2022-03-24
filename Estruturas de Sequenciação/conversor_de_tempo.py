segundos = int(input())

minutos = segundos//60
horas  = minutos//60

segundosR = segundos % 3600

minutos = segundosR // 60

segundosR = segundosR % 60

print(horas,":",minutos,":",segundosR)


