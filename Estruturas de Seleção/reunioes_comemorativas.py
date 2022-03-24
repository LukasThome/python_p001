list = []
def remove_repetidos(lista):
    l = []
    for i in lista:
        if i not in l:
            l.append(i)
    l.sort()
    return l


for i in range (3):
    data = input()
    list.append(data)
    
list = remove_repetidos(list)
print(len(list))