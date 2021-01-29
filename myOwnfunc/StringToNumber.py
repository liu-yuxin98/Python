def StringToNumber(s):
    sum=0
    for i in range(0,len(s)):
        digit=0+ord(s[i])-ord('0') #get each digit
        sum=10*sum+digit
    return sum