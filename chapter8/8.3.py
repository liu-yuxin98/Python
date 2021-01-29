
def CheckCode(s):
    lenth=len(s)
    if(len(s))<8:
        flag=0
    else:
        countn=0 #number
        countc=0 #character
        counte=0 #other
        for i in range(0, lenth):
            if ord('0') <=ord(s[i]) and ord(s[i]) <= ord('9'):
                countn += 1
            elif ord('A') <= ord(s[i]) <= ord('Z') or ord('a') <= ord(s[i]) <= ord('z'):
                countc += 1
            else:
                counte += 1
        if counte>=1:
            flag=0
        elif countn<2:
            flag=0
        else:
            flag=1
        '''
        print(lenth)
        print(countn)
        print(countc)
        print(counte)
        '''
    if flag==1:
        print("valid")
        return True
    else:
        print("Invalid")
        return False
'''
s1=input("please enter first string").strip()
print(len(s1))
for i in range(0,len(s1)):
    print(s1[i],end=" ")
    print(ord(s1[i]))
CheckCode(s1)
'''


