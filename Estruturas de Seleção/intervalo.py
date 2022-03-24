t = 1
while True:
    aero = input().split(' ')

    #se for 0 
    if aero == ['0', '0']:
        break
    else:
        voos = []
        maior = {'voos' : [], 'vezes' : 0}

        #add tds os voos
        for _ in range(int(aero[1])):
            for v in input().split(' '):
                voos.append(int(v))

        #acho o maior
        for v in range(1, int(aero[0])+1):
            vezes = voos.count(v)
            if vezes > maior['vezes']:
                maior['voos'] = [v]
                maior['vezes'] = vezes
            elif vezes == maior['vezes']:
                maior['voos'].append(v)

        #print resultado        
        print(f'Teste {t}')
        maior['voos'].sort()
        for a in maior['voos']:
            print(a, end= ' ')
        print()
        print()
        t += 1