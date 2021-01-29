s=input("enter a string").strip()
low = 0
high = len(s) - 1
flag = 0
if len(s)%2!=0:  #odd
    while low<((len(s)-1)/2-1):
        if(s[low]==s[high]):
            low+=1
            high-=1
            flag=1
        else:
            print("is not palindrom and different from position "+low+" and different character is "+s[low])
            flag=0
            low=(len(s)-1)
else:  # even
    while low<len(s)/2-1:
        if(s[low]==s[high]):
            low+=1
            high-=1
            flag=1
        else:
            print(" is not palindrom and different from {}".format(low) + "different character is" + s[low])
            flag = 0
            low = (len(s)-1)
if flag==1:
    print("is palindrom")
else:
    print('',end="")








