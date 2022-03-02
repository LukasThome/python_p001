
i = 0
txt = input()
#txt = input().replace(" ", "")
txt = ''.join(reversed(txt))
#txt = input().split(' ')
n_txt = ''
print(txt)
indice = i+1
print(len(txt))
for i in range (len(txt)-2):
        
    if (txt[i].isdigit() and txt[i + 1].isalpha()):
        if txt[i+2].isdigit() == False:
            print(txt[i+2])
            n_txt += txt[i+2]
    if txt[i] == " ":
        i += 1
        print()
        if txt[i].isalpha() and txt[i + 1].isdigit():
            n_txt += txt[i+2]
            print(txt[i+2])
    #elif txt[i].isalpha() and txt[i + 1].isdigit():
        #n_txt += txt[i+2]
        #print(txt[i+2])
    
    #elif txt[indice].isdigit():
        #print("boa")
        #n_txt += txt[i+2]
    
    #n_txt += ' ' 

print(n_txt)