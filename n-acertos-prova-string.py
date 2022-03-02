respostas = input()
gabarito = input()
acertos = 0
for i in range (len(gabarito)):
    if(respostas[i] == gabarito[i]):
        acertos += 1

print(acertos)
