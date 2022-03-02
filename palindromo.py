string = input()
stringlimpa = ''

for caracter in string.lower(): # percorre a frase caracter a caracter, já toda em letras minúsculas
    if caracter.isalpha():# se o caracter for uma letra, concatena na frase limpa
        stringlimpa += caracter 

print(stringlimpa == stringlimpa[::-1])  # compara a frase com ela invertida para ver se são iguais
