number = int(input())
binarynumber = ""
if (number!=0):
    while (number>=1):
        if (number %2==0):
            binarynumber=binarynumber+"0"
            number /=2
        else:
            binarynumber=binarynumber+"1"
            number=(number-1)/2

else:
    binarynumber="0"
print(binarynumber[::-1])
