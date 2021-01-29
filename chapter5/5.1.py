num = eval(input(" enter a number, except 0:"))
sum=num
count=0
while num!=0:
    num = eval(input(" enter a number, except 0:"))
    sum+=num
    count+=1
print("sum={}".format(sum/count,"5.2f"))
print(format(sum/count,"5.2f"))#