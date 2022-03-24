n = int(input())
list = []
for i in range(n):
    x = int(input())
    list.append(x)
list_modified = list.copy()
list_modified.sort()
last = list_modified[-1] 



print(list_modified[-1], list.index(last)+1)