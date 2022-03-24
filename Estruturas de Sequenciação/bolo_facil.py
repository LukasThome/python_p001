farinha, ovo, leite = [int(w) for w in input().split()]

farinha = farinha//2
ovo = ovo//3
leite = leite//5

if farinha <= ovo and farinha <= leite:
    print("{:.0f}".format(farinha))
if ovo <= farinha and ovo <= leite:
    print("{:.0f}".format(ovo))
else:
    print("{:.0f}".format(leite))
