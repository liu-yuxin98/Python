def IsstringInside(s1,s2):#s2<s1
    if len(s2)>len(s1):
        return False
    else:
        lenth2=len(s2)
        lenth1=len(s1)
        count=0
        for i in range(0,lenth1):
            if(s2[0]==s1[i]):
                t=i
                j=0
                while j<lenth2-2:
                    if(s2[j]!=s1[t]):
                        j=lenth2
                    else:
                        j+=1
                        t+=1
                if(j==lenth2-2):
                    count+=1
        if(count>0):
            print("appear {} times".format(count,".0f"))
            return True
        else:
            return False

s1=input("please enter first string").strip()
s2=input("please enter second string").strip()
print(IsstringInside(s1,s2))