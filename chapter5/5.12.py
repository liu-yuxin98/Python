def find(num):
    if num%5==0 and num%6==0:
        return 1
count=0
for i in range(0,1001):
    if find(i):
        print(format(i,"5.0f"),end=" ")
        count+=1
        if(count%10)==0:
            print(" ")