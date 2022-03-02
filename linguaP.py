string = input()
characters = "p"
lastCharacter = ''


#for i in range (len(string)):
        #if (lastCharacter == 'p'):
            #string = string.replace(characters,"")
       
       
       
string = ''.join( x for x in string if x not in characters)
print(string)
   
    
print(string)


