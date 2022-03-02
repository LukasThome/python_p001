# function to check if two strings are
# anagram or not
def check(s1, s2):
     
    if (s1 == s2):
        print("False")

    else:
        print((sorted(s1) == sorted(s2)))
       
   
         
# driver code 
s1 = input()
s2 = input()
check(s1, s2)
